.. _errors:

#############################
IBM Quantum Cloud Error Codes
#############################

.. contents:: Error Codes
   :local:

5XXX
====
.. _5xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**5201**          :Error message: Job timed out after {} seconds.
                  :Solution: Reduce the complexity of the job, or number of
                             shots

**5202**          :Error message: Job was canceled
                  :Solution: None. Job was canceled.
================  ============================================================


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
                  :Solution: Instruction not supported by backend. Please
                             remove the instruction shown in the error message.

**7001**          :Error message: Instruction {} is not supported.
                  :Solution: Remove unsupported instruction, or run on a
                             simulator that supports it.

**7002**          :Error message: Memory output is disabled.
                  :Solution: Select a different backend or set
                             `memory=False` in transpile / execute.

**7003**          :Error message: qubits: {} and classical bits: {} do not
                                  have equal lengths.
                  :Solution: Length of memory slots must be same as number of
                              qubits used

**7004**          :Error message: Qubit measured multiple times in circuit.
                  :Solution: Remove multiple measurements on qubits.

**7005**          :Error message: Error in supplied instruction.
                  :Solution: Please refer to IQX gate overview and make sure
                             the instructions are correct.

**7006**          :Error message: Qubit measurement is followed by instructions.
                  :Solution: Cannot perform any instruction on a measured qubit.
                             Please remove all instructions following a measurement.
   
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

**8004**	  :Error message: Channel {}{} is not available.
		  :Solution: Must use available drive channels.

**8006**	  :Gate {}in line {}s not understood ({}).
		  :Solution: This instruction is not supported. Please make 
                              sure that the gate name is correct and it is within 
                              the gate overview section of IQX website.

**8007**	  :Error message: Qasm gate not understood: {}.
                  :Solution: The instruction is not understood. Please refer to IQX
                             website and make sure the instruction is within the gate
                             overview section.

**8008**	  :Error message: Unconnected Qubits.
		  :Solution: Please refer to the qubit mapping for this backend in 
                             IQX website and make sure the qubits are connected.

**8009**          :Error message: Measurement level is not supported..
		  :Solution: The given measurement level is not supported on this backend.
                             Please change it to 0-2 except the measurement level specified.

**8011**	  :Error message: Pulse experiments are not supported on this system..
		  :Solution: Pulse experiment is not supported on this backend.
                             Please use a backend that support pulse to run this experiment.

**8013**	  :Error message: This backend does not support conditional pulses.
		  :Solution: Conditionals are not supported on this backend.
                             Please remove the conditional instruction in your program.

**8014**	  :Error message: reset instructions are not supported.
                  :Solution: Reset instructions are not supported at this time for this
                             backend. Please remove the reset instruction.

**8016**          :Error message: Pulse {} has too few samples ({} > {}).
                  :Solution: Please add more samples.

**8017**          :Error message: Pulse not a multiple of {} samples.
                  :Solution: Due to hardware limitations pulses must be a multiple of a
                             given number of samples.

================  ============================================================


9XXX
==
.. _9XXX:

================  ============================================================
Error codes       Messages
================  ============================================================
**9999**          :Error message: Internal error.
                  :Solution: Contact IBM Quantum via email or slack for help.
================  ============================================================
