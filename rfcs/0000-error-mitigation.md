# RFC Title

| **Status**        | **Proposed/Accepted/Deprecated** |
|:------------------|:---------------------------------------------|
| **RFC #**         | ####                                         |
| **Authors**       | Daniel Egger (deg@zurich.ibm.com)            |
| **Deprecates**    | RFC that this RFC deprecates                 |
| **Submitted**     | YYYY-MM-DD                                   |
| **Updated**       | YYYY-MM-DD                                   |

RFC markdown filename should be of the form `####-rfc-title.md`. Where #### will be set as `max(rfc_####) + 1` after the acceptance of the RFC, but before its merger. If the RFC requires supporting files, a folder may be created with the same name as the RFC, `####-rfc-title`, in which the RFC should reside.

## Summary
Error mitigation can greatly improve results on noisy quantum hardware.
This is done by running a given quantum circuit several times.
In run i of the circuit the duration of all the gates is stretched by a factor c_i to increase the noise in the gates.
An improved result is then obtained by extrapolating to the zero-order noise limit c->0.
The purpose of this RFC is to discuss how to implement error mitigation in Qiskit such that it is usable in applications.

## Motivation
Error mitigation allows users to significantly improve their results.
It is expected that partners and members of the IBM Q network will benefit from this by being able to easily improve the quality of their results.

## User Benefit
The target users of this work are those who run quantum circuits for applications of quantum computing.

## Design Proposal
There are several ways to implement error mitigation.

### Simple error mitigation
The simplest way to implement error mitigation is to run the quantum circuit several times. 
In each run the entangling two-qubit gate is replaced several entangling two-qubit gates such that the additional gates have no effect.
For instance, replacing each CNOT gate in a quantum circuit by an odd number of CNOT gates results in the same quantum circuit in the ideal case.
This has, for example, been implemented in https://arxiv.org/abs/1905.02666.
This approach is also valid for other types of two-qubit gates such as the CZ gate.

See https://github.com/Qiskit/qiskit-aqua/pull/683 which aims to implement this error mitigation method.

**The advantage of this method is:**
- Simplicity, it is easy to implement and understand.

**The limitations of this method are**:
- Quantum circuits that are already very deep may not see any gain since replacing each CNOT gate with three CNOT gates may produce circuits which, when executed, result in noise only.
- It does not include single-qubit gates.
- The effective stretch factors to chose from are very limited.
- Some two-qubit gates, such as root-SWAP, need to be applied more than twice to compose to the identity.

### Backend constrained error mitigation
When implementing error mitigation using stretch factors, as is done in https://arxiv.org/abs/1805.04492, new pulses must be defined and calibrated for the different stretch factors c_i.
To implement error mitigation in the manner the backend could have a set of pre-defined calibrated pulses with different stretch factors.
For instance, following Kandala et al., the backend could store calibrated pulses for c=1 (i.e. the pulses used in regular operations), c=1.1, c=1.25, and c=1.5.
At execute time, the user would specify that he wants to run a quantum circuit using error mitigation.
The pulse scheduler would then create four copies of the quantum circuit, each with a different stretch factor supported by the backend.
Alternatively, the user could elect to use only a subset of the calibrate stretch factors.

**The advantages of this method are:**
- The user does not need to know much about error mitigation, a simple flag at execute time would most likely suffice.
- This allows error mitigation to be applied on single-qubit and two-qubit gates.
- Circuits that have many gates may still benefit from error mitigation as stetch factors such as c=1.1, c=1.25, and c=1.5 do not emphasis the noise as much as replacing each two-qubit gate by three two-qubit gates.
- It is fast in that the user does not need to run many quantum circuits.

**The limitations of this method are**:
- The user cannot specify his own stretch factors.
- It increases the amount of gates that the backend needs to calibrate.

### User specified error mitigation
In a more complex implementation the user specifies which stretch factors to use.
This will, therefore, require the user to run calibration procedures to calibrate the gates for each individual stretch factor before the intended quantum circuit can be run with error mitigation.
This solution may be overly complex as the user has to calibrate himself the stretched gates.
The calibration of stretched gates, could be automated to simplify the task for the user, but this would not decrease the run time.
Qiskit-ignis would most likely need to be involved ontop of qiskit-aqua and qiskit-terra.

**The advantages of this method are:**
- It is very flexible.
- This allows error mitigation to be applied on single-qubit and two-qubit gates.
- The stretch factors may be chosen as a function of the depth of the quantum circuit.

**The limitations of this method are**:
- It requires a lot of knowledge from the user.
- It requires that the user run many calibration jobs in addition to his quantum circuit.

## Detailed Design
Here we focus on the implementation details of the Backend constrained error mitigation.
The backend will have a set of calibrated gates with different stretch factors that will be made available to Qiskit through the config file.
For example, a backend that calibrated its default set of gates with four different stretch factors would have

```
 in: config = backend.configuration()
 in: print(config.stretch_factors)
out: [1.0, 1.1, 1.25, 1.5]
```
A backend may implement as many stretch factors as is deemed reasonable by those who maintain the backend.
A backend may also have the choice to not implement error mitigation at all.
The `gateconfig` schema (see `qiskit/schemas/backend_configuration_schema.json`) will be updated to support the stretch factor as follows
```
"gateconfig": {
    "type": "object",
    "required": ["name", "parameters", "qasm_def"],
    "properties": {
        ...
        "stretch_factor": {
            "type": "string"
            "description": "The stretch factor of the gate for error mitigation (if supported)."
        }
    }
}
```

To execute a quantum circuit, the user would do
```
execute(circ, backend, ..., error_mitigation='richardson')
```
to use all the stretch factors or 
```
execute(circ, backend, ..., error_mitigation='richardson', stretch_factors=[1.0, 1.25, 1.5])
```
to use only a subset of the stretch factors.
Here, `error_mitigation` specifies the error mitigation method to use.
This value would be default be `None` when error mitigation is not used.
The changes needed in Qiskit to implement error mitigation would require a pre-prossessing step in assemble to convert the quantum circuit (or list of quantum circuits) into a list of schedules, using the scheduler, that include the stretched pulses.
This also implies that error mitigation will only be a meaningful option for quantum circuits and not for schedules.
For instance, code like the following would be required in `assemble` 
```
if error_mitigation and all(isinstance(exp, QuantumCircuit) for exp in experiments):
    schedule_config['stretch_factors'] = stretch_factors
    error_mitigation_schedules = schedule(experiments, schedule_config, method='stretch_factor_error_mitigation')
    
    return assemble_schedules(schedules=error_mitigation_schedules, qobj_id=qobj_id,
                              qobj_header=qobj_header, run_config=run_config)
```
The parameters needed for the error mitigation, such as the stretch factors, are included in the `schedule_config`.
The function `schedule_circuit_error_mitigation` creates, for each quantum circuit in `experiments`, several schedules corresponding to different stretch factors in `schedule_config`. 
For example
```
schedules = []
stretch_factors = schedule_config['stretch_factors']

for circuit in experiments:
    for c in stretch_factors:
        schedule_config['stretch_factor'] = c
        schedules.append(schedule_circuit(circuit, schedule_config, method))
```
In `schedule_circuit` the translation between gates and pulses is done by the function
```
translate_gates_to_pulse_defs(circuit: QuantumCircuit,
                              schedule_config: ScheduleConfig) -> List[CircuitPulseDef]
```
located in `scheduler.methods.basic.py`.
This method currently uses the `CmdDef` to relate gates to pulses.
Therefore, the pulses in the `CmdDef` should contain information on the stretch factor they correspond to.
Consider, for example, a CNOT gate 
```
Command(name='cx', qubits=[0, 1], sequence=[
    PulseQobjInstruction(ch='d0', name='fc', phase=1.5707963267948966, t0=0), 
    PulseQobjInstruction(ch='u1', name='fc', phase=1.5707963267948966, t0=0), 
    PulseQobjInstruction(ch='d0', name='Ym_d0_4b7a', t0=0), 
    PulseQobjInstruction(ch='d1', name='X90p_d1_cfee', t0=0), 
    PulseQobjInstruction(ch='d1', name='CR90p_d1_4334', t0=160), 
    PulseQobjInstruction(ch='u0', name='CR90p_u0_0e7b', t0=160), 
    PulseQobjInstruction(ch='d0', name='Xp_d0_e1b0', t0=672), 
    PulseQobjInstruction(ch='d1', name='CR90m_d1_f19b', t0=832), 
    PulseQobjInstruction(ch='u0', name='CR90m_u0_0cdb', t0=832)
])
```
The definition of this gate could be extended to
```
Command(name='cx', qubits=[0, 1], stretch_factor=1.1, sequence=[
    PulseQobjInstruction(ch='d0', name='fc', phase=1.5707963267948966, t0=0),
    ...
])
```
to include information on the stretch factor which can be used by `translate_gates_to_pulse_defs` to select the gates with a stretch factor corresponding to `schedule_config['stretch_factor']` (this is a float and not a list).
This would then allow the creation of schedules for error mitigation that can be assembled using `assemble_schedule` and run on the backend.

Here are some additional considerations:
- Currently, the name of a scheduled circuit is the same as the circuit. We will also need to distinguish the schedules with different stretch factors, for instance, by including the stretch factor in the name of the circuit. E.g. `sched = Schedule(name=circuit.name + 'c=%d'.format(schedule_config['stretch_factor']))`.

## Alternative Approaches
See section Simple error mitigation and section User specified error mitigation.

## Questions
- The Backend constrained error mitigation requires extra effort from the backend to calibrate gates with different stretch factors. We need to check that the resulting overhead is acceptable.

## Future Extensions
See section User specified error mitigation.
