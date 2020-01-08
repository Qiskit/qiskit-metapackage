# RFC Title

| **Status**        | **Proposed/Accepted/Deprecated** |
|:------------------|:---------------------------------------------|
| **RFC #**         | ####                                         |
| **Authors**       | First Author (first.author@ibm.com),  ...    |
| **Deprecates**    | RFC that this RFC deprecates                 |
| **Submitted**     | YYYY-MM-DD                                   |
| **Updated**       | YYYY-MM-DD                                   |

RFC markdown filename should be of the form `####-rfc-title.md`. Where #### will be set as `max(rfc_####) + 1` after the acceptance of the RFC, but before its merger. If the RFC requires supporting files, a folder may be created with the same name as the RFC, `####-rfc-title`, in which the RFC should reside.

## Summary
Error mitigation can greatly improve results on noisy quantum hardware.
This is done by running a given quantum circuit several times.
In run i of the circuit the duration of all the gates is stretched by a factor c_i to increase the noise in the gates.
The ideal result is then obtained by extrapolating to the zero-order noise limit.
The purpose of this RFC is to discuss implementations of error mitigation usable in applications.

## Motivation
Error mitigation allows users to significantly improve their results.
It is expected that partners and members of the IBM Q network will benefit from this by being able to easily improve the quality of their results.

## User Benefit
The target users of this work are those who run quantum circuits for applications of quantum computing.

## Design Proposal
There are several ways to implement error mitigation.

### Simple error mitigation
The simplest way to implement error mitigation is to run the quantum circuit several times. 
In each run the entangling two-qubit gate is replaced several entangling gates to have the same effect.
For instance, quantum circuits in which each CNOT is replaced by an odd number of CNOT gates has the same effect.
This has, for example, been implemented in https://arxiv.org/abs/1905.02666.
This approach is also valid for other types of two-qubit gates such as the CZ gate.

See https://github.com/Qiskit/qiskit-aqua/pull/683 which aims to implement this error mitigation method.

The advantages of this method are:
- Simplicity, it is easy to implement and understand.

This method has several limitations:
- Quantum circuits that are already very deep may not see any gain since replacing each CNOT with three CNOTs may produce in ciquits that result in only noise.
- It does not include single qubit gates.
- The effect stretch factors to chose from are very limited.

### Backend constrained error mitigation
When implementing error mitigation using stretch factors, as is done in https://arxiv.org/abs/1805.04492, new pulses must be defined and calibrated for the different stretch factors c_i.
The backend could have a set of pre-defined calibrated pulses with different stretch factors.
For instance, following Kandala et al., the backend could store calibrated pulses for c=1 (i.e. the pulses used in regular operations), c=1.1, c=1.25, and c=1.5.
At execute time, the user would specify that he wants to run a quantum circuit using error mitigation.
The pulse scheduler would then create four copies of the quantum circuit, each with a different stretch factor supported by the backend.
Alternatively, the user could elect to use only a subset of the calibrate stretch factors.

This method has several advantages:
- The user does not need to know much about error mitigation, a simple flag at execute time would most likely suffice.
- This allows error mitigation to be applied on single and two-qubit gates.
- Circuits that have many gates may still benefit from error mitigation as stetch factors such as c=1.1, c=1.25, and c=1.5 do not emphasis the noise as much as replacing each two-qubit gate by three two-qubit gates.
- It is fast in that the user does not need to run many quantum circuits.

This method has the following disadvantages:
- The user cannot specify his own stretch factors.
- Increases the amount of gates that the backend needs to calibrate.

### User specified error mitigation
The user specifies which stretch factors to use.
This will require calibration procedures to calibrate the gates for each individual stretch factor before the intended quantum circuit can be run.
This solution may be overly complex as the user has to calibrate himself the stretched gates.
The calibration of stretched gates, could be automated, however this would increase the run time.
Qiskit-ignis would most likely need to be involved ontop of qiskit-aqua and qiskit-terra.

This methods has the following advantage:
- It is very flexible.

This method has several disadvantages:
- It requires a lot of knowledge from the user.
- It requires that the user run many jobs.

## Detailed Design
Here we focus on the Backend constrained error mitigation.

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
