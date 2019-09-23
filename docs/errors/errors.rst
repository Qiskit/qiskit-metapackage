.. _errors:

#############################
IBM Quantum Cloud Error Codes
#############################

.. contents:: Error Codes
   :local:

6XXX
====
.. _6xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**6000**          :Error message: Too many shots given ({} > {}).
                  :Solution: Reduce the requested number of shots.

**6001**          :Error message: Too few shots given ({} < {}).
                  :Solution: Increase the number of shots.

**6002**          :Error message: Too many experiments given ({} > {}).
                  :Solution: Reduce the number of experiments given at once.

**6003**          :Error message: Too few experiments given ({} < {}).
                  :Solution: Increase number of experiments.
================  ============================================================


7XXX
====
.. _7xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**7000**          :Error message: Instruction not in basis gates:
                                  instruction: {}, qubits: {}, params: {}
                  :Solution: Circuits must be constructed from backend
                             basis gates.

**7001**          :Error message: Instruction {} is not supported.
                  :Solution: Remove unsupported instruction, or run on a
                             simulator that supports it.

**7002**          :Error message: Memory output is disabled.
                  :Solution: Select a different backend or set
                             `memory=False` in transpile / execute.

**7003**          :Error message: qubits: {} and classical bits: {} do not
                                  have equal lengths.
                  :Solution: Qubit and Clbits must be correctly mapped.

**7004**          :Error message: Qubit measured multiple times in circuit.
                  :Solution: Remove multiple measurements on qubits.
================  ============================================================


8XXX
====
.. _8xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**8000**          :Error message: Channel {}{} lo setting: {} is not within
                                  acceptable range of {}.
                  :Solution: Set channel LO within specified range.

**8001**          :Error message: qubits {} in measurement are not mapped.
                  :Solution: Assign qubits to a classical memory slot.

**8002**          :Error message: Total samples exceeds the maximum number of
                                  samples for channel {}. ({} > {}).
                  :Solution: Reduce number of samples below specified limit.

**8003**          :Error message: Total pulses exceeds the maximum number of
                                  pulses for channel: {}, ({} > {}).
                  :Solution: Reduce number of pulses below specified limit.
================  ============================================================


-1
==
.. _minus1:

================  ============================================================
Error codes       Messages
================  ============================================================
**-1**            :Error message: Internal error.
                  :Solution: Contact IBM Quantum via email or slack for help.
================  ============================================================
