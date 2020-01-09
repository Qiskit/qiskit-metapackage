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
This will, thereofre, require the user to run calibration procedures to calibrate the gates for each individual stretch factor before the intended quantum circuit can be run with error mitigation.
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

```
 in: config = backend.configuration().to_dict()
 in: print(config['stretch_factors'])
out: [1.0, 1.1, 1.25, 1.5]
```

To execute a quantum circuit, the user would do
```
 in: execute(cirq, backend, ..., error_mitigation=True)
```
to use all the stretch factors or 
```
 in: execute(cirq, backend, ..., error_mitigation=True, stretch_factors=[1.0, 1.25, 1.5])
```
to use only a subset of the stretch factors.
The changes needed in Qiskit to implement error mitigation would require a pre-prossessing step in assemble to convert the quantum circuit (or list of quantum circuits) into a list of schedules, using the scheduler, that include the stretched pulses.
This also implies that error mitigation will only be a meaningful option for quantum circuits and not for schedules.
For instance, following code would be required in `assemble` 
```
if error_mitigation and all(isinstance(exp, QuantumCircuit) for exp in experiments):
    error_mitigation_schedules = schedule_circuit_error_mitigation(experiments, schedul_config, method)
    
    return assemble_schedules(schedules=error_mitigation_schedules, qobj_id=qobj_id,
                              qobj_header=qobj_header, run_config=run_config)
```
The parameters needed for the error mitigation would then be included in the `schedule_config`.

Technical reference level design. Elaborate on details such as:
- Implementation procedure
  - If spans multiple projects cover these parts individually
- Interaction with other features
- Dissecting corner cases
- Reference definition, eg., formal definitions.

## Alternative Approaches
Discuss other approaches to solving this problem and why these were not selected.

## Questions
Open questions for discussion and an opening for feedback.

## Future Extensions
Consider what extensions might spawn from this RFC. Discuss the roadmap of related projects and how these might interact. This section is also an opening for discussions and a great place to dump ideas.

If you do not have any future extensions in mind, state that you cannot think of anything. This section should not be left blank.
