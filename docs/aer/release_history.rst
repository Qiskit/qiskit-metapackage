Qiskit Aer Release Notes
========================

`Issues <https://github.com/Qiskit/qiskit-aer/issues>`_

Qiskit Aer 0.1.0
----------------

Aer provides three simulator backends:
  * ``QasmSimulator``: simulate experiments and return measurement outcomes.
  * ``StatevectorSimulator``: return the final statevector for a quantum circuit acting on the all zero state
  * ``UnitarySimulator``: return the unitary matrix for a quantum circuit

``noise`` module: contains advanced noise modeling features for the ``QasmSimulator``
  * ``NoiseModel``, ``QuantumError``, ``ReadoutError`` classes for simulating a Qiskit quantum circuit in the presence of errors
  * ``errors`` submodule including functions for generating ``QuantumError`` objects for the following types of quantum errors: Kraus, mixed unitary, coherent unitary, Pauli, depolarizing, thermal relaxation, amplitude damping, phase damping, combined phase and amplitude damping.
  * ``device`` submodule for automatically generating a noise model based on the ``BackendProperties`` of a device

``utils`` module:
  * ``qobj_utils`` provides functions for directly modifying a ``qobj`` to insert special simulator instructions not yet supported through the Qiskit Terra API
