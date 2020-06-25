%%%%%%%%%%%%%
Release Notes
%%%%%%%%%%%%%


###############
Version History
###############

This table tracks the meta-package versions and the version of each Qiskit element installed:

.. version-history:: **Version History**

.. note::

   For the ``0.7.0``, ``0.7.1``, and ``0.7.2`` meta-package releases the
   :ref:`versioning_strategy` policy was not formalized yet.


###############
Notable Changes
###############

*************
Qiskit 0.19.6
*************

Terra 0.14.2
============

No Change

Aer 0.5.2
=========

No Change

Ignis 0.3.3
===========

.. _Release Notes_0.3.3_Upgrade Notes:

Upgrade Notes
-------------

- A new requirement `scikit-learn <https://scikit-learn.org/stable/>`__ has
  been added to the requirements list. This dependency was added in the 0.3.0
  release but wasn't properly exposed as a dependency in that release. This
  would lead to an ``ImportError`` if the
  :mod:`qiskit.ignis.measurement.discriminator.iq_discriminators` module was
  imported. This is now correctly listed as a dependency so that
  ``scikit-learn`` will be installed with qiskit-ignis.


.. _Release Notes_0.3.3_Bug Fixes:

Bug Fixes
---------

- Fixes an issue in qiskit-ignis 0.3.2 which would raise an ``ImportError``
  when :mod:`qiskit.ignis.verification.tomography.fitters.process_fitter` was
  imported without ``cvxpy`` being installed.

Aqua 0.7.3
==========

No Change

IBM Q Provider 0.7.2
====================

No Change


*************
Qiskit 0.19.5
*************

Terra 0.14.2
============

No Change

Aer 0.5.2
=========

No Change

Ignis 0.3.2
===========

Bug Fixes
---------

- The :meth:`qiskit.ignis.verification.TomographyFitter.fit` method has improved
  detection logic for the default fitter. Previously, the ``cvx`` fitter method
  was used whenever `cvxpy <https://www.cvxpy.org/>`__ was installed. However,
  it was possible to install cvxpy without an SDP solver that would work for the
  ``cvx`` fitter method. This logic has been reworked so that the ``cvx``
  fitter method is only used if ``cvxpy`` is installed and an SDP solver is present
  that can be used. Otherwise, the ``lstsq`` fitter is used.

- Fixes an edge case in
  :meth:`qiskit.ignis.mitigation.measurement.fitters.MeasurementFitter.apply`
  for input that has invalid or incorrect state labels that don't match
  the calibration circuit. Previously, this would not error and just return
  an empty result. Instead now this case is correctly caught and a
  ``QiskitError`` exception is raised when using incorrect labels.

Aqua 0.7.3
==========

.. _Release Notes_0.7.3_Upgrade Notes:

Upgrade Notes
-------------

- The `cvxpy <https://www.cvxpy.org/>`__ dependency which is required for
  the svm classifier has been removed from the requirements list and made
  an optional dependency. This is because installing cvxpy is not seamless
  in every environment and often requires a compiler be installed to run.
  To use the svm classifier now you'll need to install cvxpy by either
  running ``pip install cvxpy<1.1.0`` or to install it with aqua running
  ``pip install qiskit-aqua[cvx]``.


.. _Release Notes_0.7.3_Bug Fixes:

Bug Fixes
---------

- The ``compose`` method of the ``CircuitOp`` used ``QuantumCircuit.combine`` which has been
  changed to use ``QuantumCircuit.compose``. Using combine leads to the problem that composing
  an operator with a ``CircuitOp`` based on a named register does not chain the operators but
  stacks them. E.g. composing ``Z ^ 2`` with a circuit based on a 2-qubit named register yielded
  a 4-qubit operator instead of a 2-qubit operator.

- The ``MatrixOp.to_instruction`` method previously returned an operator and not
  an instruction. This method has been updated to return an Instruction.
  Note that this only works if the operator primitive is unitary, otherwise
  an error is raised upon the construction of the instruction.

- The ``__hash__`` method of the ``PauliOp`` class used the ``id()`` method
  which prevents set comparisons to work as expected since they rely on hash
  tables and identical objects used to not have identical hashes. Now, the
  implementation uses a hash of the string representation inline with the
  implementation in the ``Pauli`` class.

IBM Q Provider 0.7.2
====================

No Change


*************
Qiskit 0.19.4
*************

Terra 0.14.2
============

.. _Release Notes_0.14.2_Upgrade Notes:

Upgrade Notes
-------------

- The ``circuit_to_gate`` and ``circuit_to_instruction`` converters had
  previously automatically included the generated gate or instruction in the
  active ``SessionEquivalenceLibrary``. These converters now accept an
  optional ``equivalence_library`` keyword argument to specify if and where
  the converted instances should be registered. The default behavior is not
  to register the converted instance.


.. _Release Notes_0.14.2_Bug Fixes:

Bug Fixes
---------

- Implementations of the multi-controlled X Gate (``MCXGrayCode``,
  ``MCXRecursive`` and ``MCXVChain``) have had their ``name``
  properties changed to more accurately describe their
  implementation (``mcx_gray``, ``mcx_recursive``, and
  ``mcx_vchain`` respectively.) Previously, these gates shared the
  name ``mcx` with ``MCXGate``, which caused these gates to be
  incorrectly transpiled and simulated.

- ``ControlledGate`` instances with a set ``ctrl_state`` were in some cases
  not being evaluated as equal, even if the compared gates were equivalent.
  This has been resolved.

- Fixed the SI unit conversion for :py:class:`qiskit.pulse.SetFrequency`. The
  ``SetFrequency`` instruction should be in Hz on the frontend and has to be
  converted to GHz when ``SetFrequency`` is converted to ``PulseQobjInstruction``.

- Open controls were implemented by modifying a gate\'s
  definition. However, when the gate already exists in the basis,
  this definition is not used, which yields incorrect circuits sent
  to a backend. This modifies the unroller to output the definition
  if it encounters a controlled gate with open controls.

Aer 0.5.2
=========

No Change

Ignis 0.3.0
===========

No Change

Aqua 0.7.2
==========

Prelude
-------
VQE expectation computation with Aer qasm_simulator now defaults to a
computation that has the expected shot noise behavior.

Upgrade Notes
-------------
- `cvxpy <https://github.com/cvxgrp/cvxpy/>`_ is now in the requirements list
  as a dependency for qiskit-aqua. It is used for the quadratic program solver
  which is used as part of the :class:`qiskit.aqua.algorithms.QSVM`. Previously
  ``cvxopt`` was an optional dependency that needed to be installed to use
  this functionality. This is no longer required as cvxpy will be installed
  with qiskit-aqua.
- For state tomography run as part of :class:`qiskit.aqua.algorithms.HHL` with
  a QASM backend the tomography fitter function
  :meth:`qiskit.ignis.verification.StateTomographyFitter.fit` now gets called
  explicitly with the method set to ``lstsq`` to always use the least-squares
  fitting. Previously it would opportunistically try to use the ``cvx`` fitter
  if ``cvxpy`` were installed. But, the ``cvx`` fitter depends on a
  specifically configured ``cvxpy`` installation with an SDP solver installed
  as part of ``cvxpy`` which is not always present in an environment with
  ``cvxpy`` installed.
- The VQE expectation computation using qiskit-aer's
  :class:`qiskit.providers.aer.extensions.SnapshotExpectationValue` instruction
  is not enabled by default anymore. This was changed to be the default in
  0.7.0 because it is significantly faster, but it led to unexpected ideal
  results without shot noise (see
  `#1013 <https://github.com/Qiskit/qiskit-aqua/issues/1013>`_ for more
  details). The default has now changed back to match user expectations. Using
  the faster expectation computation is now opt-in by setting the new
  ``include_custom`` kwarg to ``True`` on the
  :class:`qiskit.aqua.algorithms.VQE` constructor.

New Features
------------
- A new kwarg ``include_custom`` has been added to the constructor for
  :class:`qiskit.aqua.algorithms.VQE` and it's subclasses (mainly
  :class:`qiskit.aqua.algorithms.QAOA`). When set to true and the
  ``expectation`` kwarg is set to ``None`` (the default) this will enable
  the use of VQE expectation computation with Aer's ``qasm_simulator``
  :class:`qiskit.providers.aer.extensions.SnapshotExpectationValue` instruction.
  The special Aer snapshot based computation is much faster but with the ideal
  output similar to state vector simulator.

IBM Q Provider 0.7.2
====================

No Change

*************
Qiskit 0.19.3
*************

Terra 0.14.1
============

No Change

Aer 0.5.2
=========

Bug Fixes
---------

- Fixed bug with statevector and unitary simulators running a number of (parallel)
  shots equal to the number of CPU threads instead of only running a single shot.

- Fixes the "diagonal" qobj gate instructions being applied incorrectly
  in the density matrix Qasm Simulator method.

- Fixes bug where conditional gates were not being applied correctly
  on the density matrix simulation method.

- Fix bug in CZ gate and Z gate for "density_matrix_gpu" and
  "density_matrix_thrust" QasmSimulator methods.

- Fixes issue where memory requirements of simulation were not being checked
  on the QasmSimulator when using a non-automatic simulation method.

- Fixed a memory leak that effected the GPU simulator methods

Ignis 0.3.0
===========

No Change

Aqua 0.7.1
==========

No Change

IBM Q Provider 0.7.2
====================

Bug Fixes
---------

- :meth:`qiskit.provider.ibmq.IBMQBackend.jobs` will now return the correct
  list of :class:`~qiskit.provider.ibmq.job.IBMQJob` objects when the
  ``status`` kwarg is set to ``'RUNNING'``. Fixes
  `#523 <https://github.com/Qiskit/qiskit-ibmq-provider/issues/523>`_

- The package metadata has been updated to properly reflect the dependency
  on ``qiskit-terra`` >= 0.14.0. This dependency was implicitly added as
  part of the 0.7.0 release but was not reflected in the package requirements
  so it was previously possible to install ``qiskit-ibmq-provider`` with a
  version of ``qiskit-terra`` which was too old. Fixes
  `#677 <https://github.com/Qiskit/qiskit-ibmq-provider/issues/677>`_

*************
Qiskit 0.19.0
*************

Terra 0.14.0
============

.. _Release Notes_0.14.0_Prelude:

Prelude
-------

The 0.14.0 release includes several new features and bug fixes. The biggest
change for this release is the introduction of a quantum circuit library
in :mod:`qiskit.circuit.library`, containing some circuit families of
interest.

The circuit library gives users access to a rich set of well-studied
circuit families, instances of which can be used as benchmarks,
as building blocks in building more complex circuits, or
as a tool to explore quantum computational advantage over classical.
The contents of this library will continue to grow and mature.

The initial release of the circuit library contains:

* ``standard_gates``: these are fixed-width gates commonly used as primitive
  building blocks, consisting of 1, 2, and 3 qubit gates. For example
  the :class:`~qiskit.circuit.library.XGate`,
  :class:`~qiskit.circuit.library.RZZGate` and
  :class:`~qiskit.circuit.library.CSWAPGate`. The old location of these
  gates under ``qiskit.extensions.standard`` is deprecated.
* ``generalized_gates``: these are families that can generalize to arbitrarily
  many qubits, for example a :class:`~qiskit.circuit.library.Permutation` or
  :class:`~qiskit.circuit.library.GMS` (Global Molmer-Sorensen gate).
* ``boolean_logic``: circuits that transform basis states according to simple
  Boolean logic functions, such as :class:`~qiskit.circuit.library.ADD` or
  :class:`~qiskit.circuit.library.XOR`.
* ``arithmetic``: a set of circuits for doing classical arithmetic such as
  :class:`~qiskit.circuit.library.WeightedAdder` and
  :class:`~qiskit.circuit.library.IntegerComparator`.
* ``basis_changes``: circuits such as the quantum Fourier transform,
  :class:`~qiskit.circuit.library.QFT`, that mathematically apply basis
  changes.
* ``n_local``: patterns to easily create large circuits with rotation and
  entanglement layers, such as  :class:`~qiskit.circuit.library.TwoLocal`
  which uses single-qubit rotations and two-qubit entanglements.
* ``data_preparation``: circuits that take classical input data and encode it
  in a quantum state that is difficult to simulate, e.g.
  :class:`~qiskit.circuit.library.PauliFeatureMap` or
  :class:`~qiskit.circuit.library.ZZFeatureMap`.
* Other circuits that have proven interesting in the literature, such as
  :class:`~qiskit.circuit.library.QuantumVolume`,
  :class:`~qiskit.circuit.library.GraphState`, or
  :class:`~qiskit.circuit.library.IQP`.

To allow easier use of these circuits as building blocks, we have introduced
a :meth:`~qiskit.circuit.QuantumCircuit.compose` method of
:class:`qiskit.circuit.QuantumCircuit` for composition of circuits either
with other circuits (by welding them at the ends and optionally permuting
wires) or with other simpler gates::

  >>> lhs.compose(rhs, qubits=[3, 2], inplace=True)

.. parsed-literal::
                  ┌───┐                   ┌─────┐                ┌───┐
      lqr_1_0: ───┤ H ├───    rqr_0: ──■──┤ Tdg ├    lqr_1_0: ───┤ H ├───────────────
                  ├───┤              ┌─┴─┐└─────┘                ├───┤
      lqr_1_1: ───┤ X ├───    rqr_1: ┤ X ├───────    lqr_1_1: ───┤ X ├───────────────
               ┌──┴───┴──┐           └───┘                    ┌──┴───┴──┐┌───┐
      lqr_1_2: ┤ U1(0.1) ├  +                     =  lqr_1_2: ┤ U1(0.1) ├┤ X ├───────
               └─────────┘                                    └─────────┘└─┬─┘┌─────┐
      lqr_2_0: ─────■─────                           lqr_2_0: ─────■───────■──┤ Tdg ├
                  ┌─┴─┐                                          ┌─┴─┐        └─────┘
      lqr_2_1: ───┤ X ├───                           lqr_2_1: ───┤ X ├───────────────
                  └───┘                                          └───┘
      lcr_0: 0 ═══════════                           lcr_0: 0 ═══════════════════════
      lcr_1: 0 ═══════════                           lcr_1: 0 ═══════════════════════

With this, Qiskit's circuits no longer assume an implicit
initial state of :math:`|0\rangle`, and will not be drawn with this
initial state. The all-zero initial state is still assumed on a backend
when a circuit is executed.


.. _Release Notes_0.14.0_New Features:

New Features
------------

- A new method, :meth:`~qiskit.circuit.EquivalenceLibrary.has_entry`, has been
  added to the :class:`qiskit.circuit.EquivalenceLibrary` class to quickly
  check if a given gate has any known decompositions in the library.

- A new class :class:`~qiskit.circuit.library.IQP`, to construct an
  instantaneous quantum polynomial circuit, has been added to the circuit
  library module :mod:`qiskit.circuit.library`.

- A new :meth:`~qiskit.circuit.QuantumCircuit.compose` method has been added
  to :class:`qiskit.circuit.QuantumCircuit`. It allows
  composition of two quantum circuits without having to turn one into
  a gate or instruction. It also allows permutations of qubits/clbits
  at the point of composition, as well as optional inplace modification.
  It can also be used in place of
  :meth:`~qiskit.circuit.QuantumCircuit.append()`, as it allows
  composing instructions and operators onto the circuit as well.

- :class:`qiskit.circuit.library.Diagonal` circuits have been added to the
  circuit library. These circuits implement diagonal quantum operators
  (consisting of non-zero elements only on the diagonal). They are more
  efficiently simulated by the Aer simulator than dense matrices.

- Add :meth:`~qiskit.quantum_info.Clifford.from_label` method to the
  :class:`qiskit.quantum_info.Clifford` class for initializing as the
  tensor product of single-qubit I, X, Y, Z, H, or S gates.

- Schedule transformer :func:`qiskit.pulse.reschedule.compress_pulses`
  performs an optimization pass to reduce the usage of waveform
  memory in hardware by replacing multiple identical instances of
  a pulse in a pulse schedule with a single pulse.
  For example::

      from qiskit.pulse import reschedule

      schedules = []
      for _ in range(2):
          schedule = Schedule()
          drive_channel = DriveChannel(0)
          schedule += Play(SamplePulse([0.0, 0.1]), drive_channel)
          schedule += Play(SamplePulse([0.0, 0.1]), drive_channel)
          schedules.append(schedule)

      compressed_schedules = reschedule.compress_pulses(schedules)

- The :class:`qiskit.transpiler.Layout` has a new method
  :meth:`~qiskit.transpiler.Layout.reorder_bits` that is used to reorder a
  list of virtual qubits based on the layout object.

- Two new methods have been added to the
  :class:`qiskit.providers.models.PulseBackendConfiguration` for
  interacting with channels.

  * :meth:`~qiskit.providers.models.PulseBackendConfiguration.get_channel_qubits`
    to get a list of all qubits operated by the given channel and
  * :meth:`~qiskit.providers.models.PulseBackendConfiguration.get_qubit_channel`
    to get a list of channels operating on the given qubit.

- New :class:`qiskit.extensions.HamiltonianGate` and
  :meth:`qiskit.circuit.QuantumCircuit.hamiltonian()` methods are
  introduced, representing Hamiltonian evolution of the circuit
  wavefunction by a user-specified Hermitian Operator and evolution time.
  The evolution time can be a :class:`~qiskit.circuit.Parameter`, allowing
  the creation of parameterized UCCSD or QAOA-style circuits which compile to
  ``UnitaryGate`` objects if ``time`` parameters are provided. The Unitary of
  a ``HamiltonianGate`` with Hamiltonian Operator ``H`` and time parameter
  ``t`` is :math:`e^{-iHt}`.

- The circuit library module :mod:`qiskit.circuit.library` now provides a
  new boolean logic AND circuit, :class:`qiskit.circuit.library.AND`, and
  OR circuit, :class:`qiskit.circuit.library.OR`, which implement the
  respective operations on a variable number of provided qubits.

- New fake backends are added under :mod:`qiskit.test.mock`. These include
  mocked versions of ``ibmq_armonk``, ``ibmq_essex``, ``ibmq_london``,
  ``ibmq_valencia``, ``ibmq_cambridge``, ``ibmq_paris``, ``ibmq_rome``, and
  ``ibmq_athens``. As with other fake backends, these include snapshots of
  calibration data (i.e. ``backend.defaults()``) and error data (i.e.
  ``backend.properties()``) taken from the real system, and can be used for
  local testing, compilation and simulation.

- The ``last_update_date`` parameter for
  :class:`~qiskit.providers.models.BackendProperties` can now also be
  passed in as a ``datetime`` object. Previously only a string in
  ISO8601 format was accepted.

- Adds :meth:`qiskit.quantum_info.Statevector.from_int` and
  :meth:`qiskit.quantum_info.DensityMatrix.from_int` methods that allow
  constructing a computational basis state for specified system dimensions.

- The methods on the :class:`qiskit.circuit.QuantumCircuit` class for adding
  gates (for example :meth:`~qiskit.circuit.QuantumCircuit.h`) which were
  previously added dynamically at run time to the class definition have been
  refactored to be statically defined methods of the class. This means that
  static analyzer (such as IDEs) can now read these methods.


.. _Release Notes_0.14.0_Upgrade Notes:

Upgrade Notes
-------------

- A new package,
  `python-dateutil <https://pypi.org/project/python-dateutil/>`_, is now
  required and has been added to the requirements list. It is being used
  to parse datetime strings received from external providers in
  :class:`~qiskit.providers.models.BackendProperties` objects.

- The marshmallow schema classes in :mod:`qiskit.providers.models` have been
  removed since they are no longer used by the BackendObjects.

- The output of the ``to_dict()`` method for the classes in
  :mod:`qiskit.providers.models` is no longer in a format for direct JSON
  serialization. Depending on the content contained in instances of these
  class there may be numpy arrays and/or complex numbers in the fields of the dict.
  If you're JSON serializing the output of the to_dict methods you should
  ensure your JSON encoder can handle numpy arrays and complex numbers. This
  includes:

  * :meth:`qiskit.providers.models.BackendConfiguration.to_dict`
  * :meth:`qiskit.providers.models.BackendProperties.to_dict`
  * :meth:`qiskit.providers.models.BackendStatus.to_dict`
  * :meth:`qiskit.providers.models.QasmBackendConfiguration.to_dict`
  * :meth:`qiskit.providers.models.PulseBackendConfiguration.to_dict`
  * :meth:`qiskit.providers.models.UchannelLO.to_dict`
  * :meth:`qiskit.providers.models.GateConfig.to_dict`
  * :meth:`qiskit.providers.models.PulseDefaults.to_dict`
  * :meth:`qiskit.providers.models.Command.to_dict`
  * :meth:`qiskit.providers.models.JobStatus.to_dict`
  * :meth:`qiskit.providers.models.Nduv.to_dict`
  * :meth:`qiskit.providers.models.Gate.to_dict`


.. _Release Notes_0.14.0_Deprecation Notes:

Deprecation Notes
-----------------

- The :meth:`qiskit.dagcircuit.DAGCircuit.compose` method now takes a list
  of qubits/clbits that specify the positional order of bits to compose onto.
  The dictionary-based method of mapping using the ``edge_map`` argument is
  deprecated and will be removed in a future release.

- The ``combine_into_edge_map()`` method for the
  :class:`qiskit.transpiler.Layout` class has been deprecated and will be
  removed in a future release. Instead, the new method
  :meth:`~qiskit.transpiler.Layout.reorder_bits` should be used to reorder
  a list of virtual qubits according to the layout object.

- Passing a :class:`qiskit.pulse.ControlChannel` object in via the
  parameter ``channel`` for the
  :class:`qiskit.providers.models.PulseBackendConfiguration` method
  :meth:`~qiskit.providers.models.PulseBackendConfiguration.control` has been
  deprecated and will be removed in a future release. The
  ``ControlChannel`` objects are now generated from the backend configuration
  ``channels`` attribute which has the information of all channels and the
  qubits they operate on. Now, the method
  :meth:`~qiskit.providers.models.PulseBackendConfiguration.control`
  is expected to take the parameter ``qubits`` of the form
  ``(control_qubit, target_qubit)`` and type ``list``
  or ``tuple``, and returns a list of control channels.

- The ``AND`` and ``OR`` methods of :class:`qiskit.circuit.QuantumCircuit`
  are deprecated and will be removed in a future release. Instead you should
  use the circuit library boolean logic classes
  :class:`qiskit.circuit.library.AND` amd :class:`qiskit.circuit.library.OR`
  and then append those objects to your class. For example::

    from qiskit import QuantumCircuit
    from qiskit.circuit.library import AND

    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)

    qc_and = AND(2)

    qc.compose(qc_and, inplace=True)

- The ``qiskit.extensions.standard`` module is deprecated and will be
  removed in a future release. The gate classes in that module have been
  moved to :mod:`qiskit.circuit.library.standard_gates`.


.. _Release Notes_0.14.0_Bug Fixes:

Bug Fixes
---------

- The :class:`qiskit.circuit.QuantumCircuit` methods
  :meth:`~qiskit.circuit.QuantumCircuit.inverse`,
  :meth:`~qiskit.circuit.QuantumCircuit.mirror` methods, as well as
  the ``QuantumCircuit.data`` setter would generate an invalid circuit when
  used on a parameterized circuit instance. This has been resolved and
  these methods should now work with a parameterized circuit. Fixes
  `#4235 <https://github.com/Qiskit/qiskit-terra/issues/4235>`_

- Previously when creating a controlled version of a standard qiskit
  gate if a ``ctrl_state`` was specified a generic ``ControlledGate``
  object would be returned whereas without it a standard qiskit
  controlled gate would be returned if it was defined. This PR
  allows standard qiskit controlled gates to understand
  ``ctrl_state``.

  Additionally, this PR fixes what might be considered a bug where
  setting the ``ctrl_state`` of an already controlled gate would
  assume the specified state applied to the full control width
  instead of the control qubits being added. For instance,::

    circ = QuantumCircuit(2)
    circ.h(0)
    circ.x(1)
    gate = circ.to_gate()
    cgate = gate.control(1)
    c3gate = cgate.control(2, ctrl_state=0)

  would apply ``ctrl_state`` to all three control qubits instead of just
  the two control qubits being added.

- Fixed a bug in :func:`~qiskit.quantum_info.random_clifford` that stopped it
  from sampling the full Clifford group. Fixes
  `#4271 <https://github.com/Qiskit/qiskit-terra/issues/4271>`_

- The :class:`qiskit.circuit.Instruction` method
  :meth:`qiskit.circuit.Instruction.is_parameterized` method had previously
  returned ``True`` for any ``Instruction`` instance which had a
  :class:`qiskit.circuit.Parameter` in any element of its ``params`` array,
  even if that ``Parameter`` had been fully bound. This has been corrected so
  that ``.is_parameterized`` will return ``False`` when the instruction is
  fully bound.

- :meth:`qiskit.circuit.ParameterExpression.subs` had not correctly detected
  some cases where substituting parameters would result in a two distinct
  :class:`~qiskit.circuit.Parameters` objects in an expression with the same
  name. This has been corrected so a ``CircuitError`` will be raised in these
  cases.

- Improve performance of :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` for low-qubit circuit
  simulations by optimizing the class ``__init__`` methods. Fixes
  `#4281 <https://github.com/Qiskit/qiskit-terra/issues/4281>`_

- The function :func:`qiskit.compiler.transpile` now correctly handles when
  the parameter ``basis_gates`` is set to ``None``. This will allow any gate
  in the output tranpiled circuit, including gates added by the transpilation
  process. Note that using this parameter may have some
  unintended consequences during optimization. Some transpiler passes
  depend on having a ``basis_gates`` set. For example,
  :class:`qiskit.transpiler.passes.Optimize1qGates` only optimizes the chains
  of u1, u2, and u3 gates and without ``basis_gates`` it is unable to unroll
  gates that otherwise could be optimized:

  .. code-block:: python

    from qiskit import *

    q = QuantumRegister(1, name='q')
    circuit = QuantumCircuit(q)
    circuit.h(q[0])
    circuit.u1(0.1, q[0])
    circuit.u2(0.1, 0.2, q[0])
    circuit.h(q[0])
    circuit.u3(0.1, 0.2, 0.3, q[0])

    result = transpile(circuit, basis_gates=None, optimization_level=3)
    result.draw()

  .. parsed-literal::
        ┌───┐┌─────────────┐┌───┐┌─────────────────┐
   q_0: ┤ H ├┤ U2(0.1,0.3) ├┤ H ├┤ U3(0.1,0.2,0.3) ├
        └───┘└─────────────┘└───┘└─────────────────┘

  Fixes `#3017 <https://github.com/Qiskit/qiskit-terra/issues/3017>`_


.. _Release Notes_0.14.0_Other Notes:

Other Notes
-----------

- The objects in :mod:`qiskit.providers.models` which were previously
  constructed using the marshmallow library have been refactored to not
  depend on marshmallow. This includes:

  * :class:`~qiskit.providers.models.BackendConfiguration`
  * :class:`~qiskit.providers.models.BackendProperties`
  * :class:`~qiskit.providers.models.BackendStatus`
  * :class:`~qiskit.providers.models.QasmBackendConfiguration`
  * :class:`~qiskit.providers.models.PulseBackendConfiguration`
  * :class:`~qiskit.providers.models.UchannelLO`
  * :class:`~qiskit.providers.models.GateConfig`
  * :class:`~qiskit.providers.models.PulseDefaults`
  * :class:`~qiskit.providers.models.Command`
  * :class:`~qiskit.providers.models.JobStatus`
  * :class:`~qiskit.providers.models.Nduv`
  * :class:`~qiskit.providers.models.Gate`

  These should be drop-in replacements without any noticeable change but
  specifics inherited from marshmallow may not work. Please file issues for
  any incompatibilities found.

Aer 0.5.1
=========

No Change


Ignis 0.3.0
===========

No Change

Aqua 0.7.0
==========

Prelude
-------

The Qiskit Aqua 0.7.0 release introduces a lot of new functionality along
with an improved integration with :class:`qiskit.circuit.QuantumCircuit`
objects. The central contributions are the Qiskit's optimization module,
a complete refactor on Operators, using circuits as native input for the
algorithms and removal of the declarative JSON API.

Optimization module
^^^^^^^^^^^^^^^^^^^
The :mod:`qiskit.optimization`` module now offers functionality for modeling
and solving quadratic programs. It provides various near-term quantum and
conventional algorithms, such as the ``MinimumEigenOptimizer``
(covering e.g. ``VQE`` or ``QAOA``) or ``CplexOptimizer``, as well as
a set of converters to translate between different
problem representations, such as ``QuadraticProgramToQubo``.
See the
`changelog <https://github.com/Qiskit/qiskit-aqua/blob/master/CHANGELOG.md>`_
for a list of the added features.

Operator flow
^^^^^^^^^^^^^
The operator logic provided in :mod:`qiskit.aqua.operators`` was completely
refactored and is now a full set of tools for constructing
physically-intuitive quantum computations. It contains state functions,
operators and measurements and internally relies on Terra's Operator
objects. Computing expectation values and evolutions was heavily simplified
and objects like the ``ExpectationFactory`` produce the suitable, most
efficient expectation algorithm based on the Operator input type.
See the `changelog <https://github.com/Qiskit/qiskit-aqua/blob/master/CHANGELOG.md>`_
for a overview of the added functionality.

Native circuits
^^^^^^^^^^^^^^^
Algorithms commonly use parameterized circuits as input, for example the
VQE, VQC or QSVM. Previously, these inputs had to be of type
``VariationalForm`` or ``FeatureMap`` which were wrapping the circuit
object. Now circuits are natively supported in these algorithms, which
means any individually constructed ``QuantumCircuit`` can be passed to
these algorithms. In combination with the release of the circuit library
which offers a wide collection of circuit families, it is now easy to
construct elaborate circuits as algorithm input.

Declarative JSON API
^^^^^^^^^^^^^^^^^^^^
The ability of running algorithms using dictionaries as parameters as well
as using the Aqua interfaces GUI has been removed.


IBM Q Provider 0.7.0
====================

.. _Release Notes_0.7.0_New Features:

New Features
------------

- A new exception, :class:`qiskit.providers.ibmq.IBMQBackendJobLimitError`,
  is now raised if a job could not be submitted because the limit on active
  jobs has been reached.

- :class:`qiskit.providers.ibmq.job.IBMQJob` and
  :class:`qiskit.providers.ibmq.managed.ManagedJobSet` each has two new methods
  ``update_name`` and ``update_tags``.
  They are used to change the name and tags of a job or a job set, respectively.

- :meth:`qiskit.providers.ibmq.IBMQFactory.save_account` and
  :meth:`qiskit.providers.ibmq.IBMQFactory.enable_account` now accept optional
  parameters ``hub``, ``group``, and ``project``, which allow specifying a default
  provider to save to disk or use, respectively.


.. _Release Notes_0.7.0_Upgrade Notes:

Upgrade Notes
-------------

- The :class:`qiskit.providers.ibmq.job.IBMQJob` methods ``creation_date`` and
  ``time_per_step`` now return date time information as a ``datetime`` object in
  local time instead of UTC. Similarly, the parameters ``start_datetime`` and
  ``end_datetime``, of
  :meth:`qiskit.providers.ibmq.IBMQBackendService.jobs` and
  :meth:`qiskit.providers.ibmq.IBMQBackend.jobs` can now be specified in local time.

- The :meth:`qiskit.providers.ibmq.job.QueueInfo.format` method now uses a custom
  ``datetime`` to string formatter, and the package
  `arrow <https://pypi.org/project/arrow/>`_ is no longer required and has been
  removed from the requirements list.


.. _Release Notes_0.7.0_Deprecation Notes:

Deprecation Notes
-----------------

- The :meth:`~qiskit.providers.ibmq.job.IBMQJob.from_dict` and
  :meth:`~qiskit.providers.ibmq.job.IBMQJob.to_dict` methods of
  :class:`qiskit.providers.ibmq.job.IBMQJob` are deprecated and will be removed in
  the next release.


.. _Release Notes_0.7.0_Bug Fixes:

Bug Fixes
---------

- Fixed an issue where ``nest_asyncio.apply()`` may raise an exception if there is
  no asyncio loop due to threading.


*************
Qiskit 0.18.3
*************

Terra 0.13.0
============

No Change

Aer 0.5.1
==========

.. _Release Notes_0.5.1_Upgrade Notes:

Upgrade Notes
-------------

- Changes how transpilation passes are handled in the C++ Controller classes
  so that each pass must be explicitly called. This allows for greater
  customization on when each pass should be called, and with what parameters.
  In particular this enables setting different parameters for the gate
  fusion optimization pass depending on the QasmController simulation method.

- Add ``gate_length_units`` kwarg to
  :meth:`qiskit.providers.aer.noise.NoiseModel.from_device`
  for specifying custom ``gate_lengths`` in the device noise model function
  to handle unit conversions for internal code.

- Add Controlled-Y ("cy") gate to the Stabilizer simulator methods supported
  gateset.

- For Aer's backend the jsonschema validation of input qobj objects from
  terra is now opt-in instead of being enabled by default. If you want
  to enable jsonschema validation of qobj set the ``validate`` kwarg on
  the :meth:`qiskit.providers.aer.QasmSimualtor.run` method for the backend
  object to ``True``.


.. _Release Notes_0.5.1_Bug Fixes:

Bug Fixes
---------

- Remove "extended_stabilizer" from the automatically selected simulation
  methods. This is needed as the extended stabilizer method is not exact
  and may give incorrect results for certain circuits unless the user
  knows how to optimize its configuration parameters.

  The automatic method now only selects from "stabilizer", "density_matrix",
  and "statevector" methods. If a non-Clifford circuit that is too large for
  the statevector method is executed an exception will be raised suggesting
  you could try explicitly using the "extended_stabilizer" or
  "matrix_product_state" methods instead.

- Fixes Controller classes so that the ReduceBarrier transpilation pass is
  applied first. This prevents barrier instructions from preventing truncation
  of unused qubits if the only instruction defined on them was a barrier.

- Disables gate fusion for the matrix product state simulation method as this
  was causing issues with incorrect results being returned in some cases.

- Fix error in gate time unit conversion for device noise model with thermal
  relaxation errors and gate errors. The error probability the depolarizing
  error was being  calculated with gate time in microseconds, while for
  thermal relaxation it was being calculated in nanoseconds. This resulted
  in no depolarizing error being applied as the incorrect units would make
  the device seem to be coherence limited.

- Fix bug in incorrect composition of QuantumErrors when the qubits of
  composed instructions differ.

- Fix issue where the "diagonal" gate is checked to be unitary with too
  high a tolerance. This was causing diagonals generated from Numpy functions
  to often fail the test.

- Fix remove-barrier circuit optimization pass to be applied before qubit
  trucation. This fixes an issue where barriers inserted by the Terra
  transpiler across otherwise inactive qubits would prevent them from being
  truncated.

Ignis 0.3.0
===========

No Change


Aqua 0.6.6
==========

No Change


IBM Q Provider 0.6.1
====================

No Change


*************
Qiskit 0.18.0
*************

.. _Release Notes_0.13.0:

Terra 0.13.0
============

.. _Release Notes_0.13.0_Prelude:

Prelude
-------

The 0.13.0 release includes many big changes. Some highlights for this
release are:

For the transpiler we have switched the graph library used to build the
:class:`qiskit.dagcircuit.DAGCircuit` class which is the underlying data
structure behind all operations to be based on
`retworkx <https://pypi.org/project/retworkx/>`_ for greatly improved
performance. Circuit transpilation speed in the 0.13.0 release should
be significanlty faster than in previous releases.

There has been a significant simplification to the style in which Pulse
instructions are built. Now, ``Command`` s are deprecated and a unified
set of :class:`~qiskit.pulse.instructions.Instruction` s are supported.

The :mod:`qiskit.quantum_info` module includes several new functions
for generating random operators (such as Cliffords and quantum channels)
and for computing the diamond norm of quantum channels; upgrades to the
:class:`~qiskit.quantum_info.Statevector` and
:class:`~qiskit.quantum_info.DensityMatrix` classes to support
computing measurement probabilities and sampling measurements; and several
new classes are based on the symplectic representation
of Pauli matrices. These new classes include Clifford operators
(:class:`~qiskit.quantum_info.Clifford`), N-qubit matrices that are
sparse in the Pauli basis (:class:`~qiskit.quantum_info.SparsePauliOp`),
lists of Pauli's (:class:`~qiskit.quantum_info.PauliTable`),
and lists of stabilizers (:class:`~qiskit.quantum_info.StabilizerTable`).

This release also has vastly improved documentation across Qiskit,
including improved documentation for the :mod:`qiskit.circuit`,
:mod:`qiskit.pulse` and :mod:`qiskit.quantum_info` modules.

Additionally, the naming of gate objects and
:class:`~qiskit.circuit.QuantumCircuit` methods have been updated to be
more consistent. This has resulted in several classes and methods being
deprecated as things move to a more consistent naming scheme.

For full details on all the changes made in this release see the detailed
release notes below.


.. _Release Notes_0.13.0_New Features:

New Features
------------

- Added a new circuit library module :mod:`qiskit.circuit.library`. This will
  be a place for constructors of commonly used circuits that can be used as
  building blocks for larger circuits or applications.

- The :class:`qiskit.providers.BaseJob` class has four new methods:

  * :meth:`~qiskit.providers.BaseJob.done`
  * :meth:`~qiskit.providers.BaseJob.running`
  * :meth:`~qiskit.providers.BaseJob.cancelled`
  * :meth:`~qiskit.providers.BaseJob.in_final_state`

  These methods are used to check wheter a job is in a given job status.

- Add ability to specify control conditioned on a qubit being in the
  ground state. The state of the control qubits is represented by an
  integer. For example::

    from qiskit import QuantumCircuit
    from qiskit.extensions.standard import XGate

    qc = QuantumCircuit(4)
    cgate = XGate().control(3, ctrl_state=6)
    qc.append(cgate, [0, 1, 2, 3])

  Creates a four qubit gate where the fourth qubit gets flipped if
  the first qubit is in the ground state and the second and third
  qubits are in the excited state. If ``ctrl_state`` is ``None``, the
  default, control is conditioned on all control qubits being
  excited.

- A new jupyter widget, ``%circuit_library_info`` has been added to
  :mod:`qiskit.tools.jupyter`. This widget is used for visualizing
  details about circuits built from the circuit library. For example

  .. jupyter-execute::

      from qiskit.circuit.library import XOR
      import qiskit.tools.jupyter
      circuit = XOR(5, seed=42)
      %circuit_library_info circuit

- A new kwarg option, ``formatted`` ,  has been added to
  :meth:`qiskit.circuit.QuantumCircuit.qasm` . When set to ``True`` the
  method will print a syntax highlighted version (using pygments) to
  stdout and return ``None`` (which differs from the normal behavior of
  returning the QASM code as a string).

- A new kwarg option, ``filename`` , has been added to
  :meth:`qiskit.circuit.QuantumCircuit.qasm`. When set to a path the method
  will write the QASM code to that file. It will then continue to output as
  normal.

- A new instruction :py:class:`~qiskit.pulse.SetFrequency` which allows users
  to change the frequency of the :class:`~qiskit.pulse.PulseChannel`. This is
  done in the following way::

      from qiskit.pulse import Schedule
      from qiskit.pulse import SetFrequency

      sched = pulse.Schedule()
      sched += SetFrequency(5.5e9, DriveChannel(0))

  In this example, the frequency of all pulses before the ``SetFrequency``
  command will be the default frequency and all pulses applied to drive
  channel zero after the ``SetFrequency`` command will be at 5.5 GHz. Users
  of ``SetFrequency`` should keep in mind any hardware limitations.

- A new method, :meth:`~qiskit.circuit.QuantumCircuit.assign_parameters`
  has been added to the :class:`qiskit.circuit.QuantumCircuit` class. This
  method accepts a parameter dictionary with both floats and Parameters
  objects in a single dictionary. In other words this new method allows you
  to bind floats, Parameters or both in a single dictionary.

  Also, by using the ``inplace`` kwarg it can be specified you can optionally
  modify the original circuit in place. By default this is set to ``False``
  and a copy of the original circuit will be returned from the method.

- A new method :meth:`~qiskit.circuit.QuantumCircuit.num_nonlocal_gates`
  has been added to the :class:`qiskit.circuit.QuantumCircuit` class.
  This method will return the number of gates in a circuit that involve 2 or
  or more qubits. These gates are more costly in terms of time and error to
  implement.

- The :class:`qiskit.circuit.QuantumCircuit` method
  :meth:`~qiskit.circuit.QuantumCircuit.iso` for adding an
  :class:`~qiskit.extensions.Isometry` gate to the circuit has a new alias. You
  can now call :meth:`qiskit.circuit.QuantumCircuit.isometry` in addition to
  calling ``iso``.

- A ``description`` attribute has been added to the
  :class:`~qiskit.transpiler.CouplingMap` class for storing a short
  description for different coupling maps (e.g. full, grid, line, etc.).

- A new method :meth:`~qiskit.dagcircuit.DAGCircuit.compose` has been added to
  the :class:`~qiskit.dagcircuit.DAGCircuit` class for composing two circuits
  via their DAGs.

  .. code-block:: python

      dag_left.compose(dag_right, edge_map={right_qubit0: self.left_qubit1,
                                        right_qubit1: self.left_qubit4,
                                        right_clbit0: self.left_clbit1,
                                        right_clbit1: self.left_clbit0})

  .. parsed-literal::

                  ┌───┐                    ┌─────┐┌─┐
      lqr_1_0: ───┤ H ├───     rqr_0: ──■──┤ Tdg ├┤M├
                  ├───┤               ┌─┴─┐└─┬─┬─┘└╥┘
      lqr_1_1: ───┤ X ├───     rqr_1: ┤ X ├──┤M├───╫─
               ┌──┴───┴──┐            └───┘  └╥┘   ║
      lqr_1_2: ┤ U1(0.1) ├  +  rcr_0: ════════╬════╩═  =
               └─────────┘                    ║
      lqr_2_0: ─────■─────     rcr_1: ════════╩══════
                  ┌─┴─┐
      lqr_2_1: ───┤ X ├───
                  └───┘
      lcr_0:   ═══════════

      lcr_1:   ═══════════

                  ┌───┐
      lqr_1_0: ───┤ H ├──────────────────
                  ├───┤        ┌─────┐┌─┐
      lqr_1_1: ───┤ X ├─────■──┤ Tdg ├┤M├
               ┌──┴───┴──┐  │  └─────┘└╥┘
      lqr_1_2: ┤ U1(0.1) ├──┼──────────╫─
               └─────────┘  │          ║
      lqr_2_0: ─────■───────┼──────────╫─
                  ┌─┴─┐   ┌─┴─┐  ┌─┐   ║
      lqr_2_1: ───┤ X ├───┤ X ├──┤M├───╫─
                  └───┘   └───┘  └╥┘   ║
      lcr_0:   ═══════════════════╩════╬═
                                       ║
      lcr_1:   ════════════════════════╩═

- The mock backends in ``qiskit.test.mock`` now have a functional ``run()``
  method that will return results similar to the real devices. If
  ``qiskit-aer`` is installed a simulation will be run with a noise model
  built from the device snapshot in the fake backend.  Otherwise,
  :class:`qiskit.providers.basicaer.QasmSimulatorPy` will be used to run an
  ideal simulation. Additionally, if a pulse experiment is passed to ``run``
  and qiskit-aer is installed the ``PulseSimulator`` will be used to simulate
  the pulse schedules.

- The :meth:`qiskit.result.Result` method
  :meth:`~qiskit.result.Result.get_counts` will now return a list of all the
  counts available when there are multiple circuits in a job. This works when
  ``get_counts()`` is called with no arguments.

  The main consideration for this feature was for drawing all the results
  from multiple circuits in the same histogram. For example it is now
  possible to do something like:

  .. jupyter-execute::

      from qiskit import execute
      from qiskit import QuantumCircuit
      from qiskit.providers.basicaer import BasicAer
      from qiskit.visualization import plot_histogram

      sim = BasicAer.get_backend('qasm_simulator')

      qc = QuantumCircuit(2)
      qc.h(0)
      qc.cx(0, 1)
      qc.measure_all()
      result = execute([qc, qc, qc], sim).result()

      plot_histogram(result.get_counts())

- A new kwarg, ``initial_state`` has been added to the
  :func:`qiskit.visualization.circuit_drawer` function and the
  :class:`~qiskit.circuit.QuantumCircuit` method
  :meth:`~qiskit.circuit.QuantumCircuit.draw`. When set to ``True`` the
  initial state will be included in circuit visualizations for all backends.
  For example:

  .. jupyter-execute::

      from qiskit import QuantumCircuit

      circuit = QuantumCircuit(2)
      circuit.measure_all()
      circuit.draw(output='mpl', initial_state=True)

- It is now possible to insert a callable into a :class:`qiskit.pulse.InstructionScheduleMap`
  which returns a new :class:`qiskit.pulse.Schedule` when it is called with parameters.
  For example:

  .. code-block::

     def test_func(x):
        sched = Schedule()
        sched += pulse_lib.constant(int(x), amp_test)(DriveChannel(0))
        return sched

     inst_map = InstructionScheduleMap()
     inst_map.add('f', (0,), test_func)
     output_sched = inst_map.get('f', (0,), 10)
     assert output_sched.duration == 10

- Two new gate classes, :class:`qiskit.extensions.iSwapGate` and
  :class:`qiskit.extensions.DCXGate`, along with their
  :class:`~qiskit.circuit.QuantumCircuit` methods
  :meth:`~qiskit.circuit.QuantumCircuit.iswap` and
  :meth:`~qiskit.circuit.QuantumCircuit.dcx` have been added to the standard
  extensions. These gates, which are locally equivalent to each other, can be
  used to enact particular XY interactions. A brief motivation for these gates
  can be found in:
  `arxiv.org/abs/quant-ph/0209035 <https://arxiv.org/abs/quant-ph/0209035>`_

- The :class:`qiskit.providers.BaseJob` class now has a new method
  :meth:`~qiskit.providers.BaseJob.wait_for_final_state` that polls for the
  job status until the job reaches a final state (such as ``DONE`` or
  ``ERROR``). This method also takes an optional ``callback`` kwarg which
  takes a Python callable that will be called during each iteration of the
  poll loop.

- The ``search_width`` and ``search_depth`` attributes of the
  :class:`qiskit.transpiler.passes.LookaheadSwap` pass are now settable when
  initializing the pass. A larger search space can often lead to more
  optimized circuits, at the cost of longer run time.

- The number of qubits in
  :class:`~qiskit.providers.models.BackendConfiguration` can now be accessed
  via the property
  :py:attr:`~qiskit.providers.models.BackendConfiguration.num_qubits`. It
  was previously only accessible via the ``n_qubits`` attribute.

- Two new methods, :meth:`~qiskit.quantum_info.OneQubitEulerDecomposer.angles`
  and :meth:`~qiskit.quantum_info.OneQubitEulerDecomposer.angles_and_phase`,
  have been added to the :class:`qiskit.quantum_info.OneQubitEulerDecomposer`
  class. These methods will return the relevant parameters without
  validation, and calling the ``OneQubitEulerDecomposer`` object will
  perform the full synthesis with validation.

- An ``RR`` decomposition basis has been added to the
  :class:`qiskit.quantum_info.OneQubitEulerDecomposer` for decomposing an
  arbitrary 2x2 unitary into a two :class:`~qiskit.extensions.RGate`
  circuit.

- Adds the ability to set ``qargs`` to objects which are subclasses
  of the abstract ``BaseOperator`` class. This is done by calling the
  object ``op(qargs)`` (where ``op`` is an operator class) and will return
  a shallow copy of the original object with a qargs property set. When
  such an object is used with the
  :meth:`~qiskit.quantum_info.Operator.compose` or
  :meth:`~qiskit.quantum_info.Operator.dot` methods the internal value for
  qargs will be used when the ``qargs`` method kwarg is not used. This
  allows for subsystem composition using binary operators, for example::

      from qiskit.quantum_info import Operator

      init = Operator.from_label('III')
      x = Operator.from_label('X')
      h = Operator.from_label('H')
      init @ x([0]) @ h([1])

- Adds :class:`qiskit.quantum_info.Clifford` operator class to the
  `quantum_info` module. This operator is an efficient symplectic
  representation an N-qubit unitary operator from the Clifford group. This
  class includes a :meth:`~qiskit.quantum_info.Clifford.to_circuit` method
  for compilation into a :class:`~qiskit.QuantumCircuit` of Clifford gates
  with a minimal number of CX gates for up to 3-qubits. It also providers
  general compilation for N > 3 qubits but this method is not optimal in
  the number of two-qubit gates.

- Adds :class:`qiskit.quantum_info.SparsePauliOp` operator class. This is an
  efficient representaiton of an N-qubit matrix that is sparse in the Pauli
  basis and uses a :class:`qiskit.quantum_info.PauliTable` and vector of
  complex coefficients for its data structure.

  This class supports much of the same functionality of the
  :class:`qiskit.quantum_info.Operator` class so
  :class:`~qiskit.quantum_info.SparsePauliOp` objects can be tensored,
  composed, scalar multiplied, added and subtracted.

  Numpy arrays or :class:`~qiskit.quantum_info.Operator` objects can be
  converted to a :class:`~qiskit.quantum_info.SparsePauliOp` using the
  `:class:`~qiskit.quantum_info.SparsePauliOp.from_operator` method.
  :class:`~qiskit.quantum_info.SparsePauliOp` can be convered to a sparse
  csr_matrix or dense Numpy array using the
  :class:`~qiskit.quantum_info.SparsePauliOp.to_matrix` method, or to an
  :class:`~qiskit.quantum_info.Operator` object using the
  :class:`~qiskit.quantum_info.SparsePauliOp.to_operator` method.

  A :class:`~qiskit.quantum_info.SparsePauliOp` can be iterated over
  in terms of its :class:`~qiskit.quantum_info.PauliTable` components and
  coefficients, its coefficients and Pauli string labels using the
  :meth:`~qiskit.quantum_info.SparsePauliOp.label_iter` method, and the
  (dense or sparse) matrix components using the
  :meth:`~qiskit.quantum_info.SparsePauliOp.matrix_iter` method.

- Add :meth:`qiskit.quantum_info.diamond_norm` function for computing the
  diamond norm (completely-bounded trace-norm) of a quantum channel. This
  can be used to compute the distance between two quantum channels using
  ``diamond_norm(chan1 - chan2)``.

- A new class :class:`qiskit.quantum_info.PauliTable` has been added. This
  is an efficient symplectic representation of a list of N-qubit Pauli
  operators. Some features of this class are:

    * :class:`~qiskit.quantum_info.PauliTable` objects may be composed, and
      tensored which will return a :class:`~qiskit.quantum_info.PauliTable`
      object with the combination of the operation (
      :meth:`~qiskit.quantum_info.PauliTable.compose`,
      :meth:`~qiskit.quantum_info.PauliTable.dot`,
      :meth:`~qiskit.quantum_info.PauliTable.expand`,
      :meth:`~qiskit.quantum_info.PauliTable.tensor`) between each element
      of  the first table, with each element of the second table.

    * Addition of two tables acts as list concatination of the terms in each
      table (``+``).

    * Pauli tables can be sorted by lexicographic (tensor product) order or
      by Pauli weights (:meth:`~qiskit.quantum_info.PauliTable.sort`).

    * Duplicate elements can be counted and deleted
      (:meth:`~qiskit.quantum_info.PauliTable.unique`).

    * The PauliTable may be iterated over in either its native symplectic
      boolean array representation, as Pauli string labels
      (:meth:`~qiskit.quantum_info.PauliTable.label_iter`), or as dense
      Numpy array or sparse CSR matrices
      (:meth:`~qiskit.quantum_info.PauliTable.matrix_iter`).

    * Checking commutation between elements of the Pauli table and another
      Pauli (:meth:`~qiskit.quantum_info.PauliTable.commutes`) or Pauli
      table (:meth:`~qiskit.quantum_info.PauliTable.commutes_with_all`)

  See the :class:`qiskit.quantum_info.PauliTable` class API documentation for
  additional details.

- Adds :class:`qiskit.quantum_info.StabilizerTable` class. This is a subclass
  of the :class:`qiskit.quantum_info.PauliTable` class which includes a
  boolean phase vector along with the Pauli table array. This represents a
  list of Stabilizer operators which are real-Pauli operators with +1 or -1
  coefficient. Because the stabilizer matrices are real the ``"Y"`` label
  matrix is defined as ``[[0, 1], [-1, 0]]``. See the API documentation for
  additional information.

- Adds :func:`qiskit.quantum_info.pauli_basis` function which returns an N-qubit
  Pauli basis as a :class:`qiskit.quantum_info.PauliTable` object. The ordering
  of this basis can either be by standard lexicographic (tensor product) order,
  or by the number of non-identity Pauli terms (weight).

- Adds :class:`qiskit.quantum_info.ScalarOp` operator class that represents
  a scalar multiple of an identity operator. This can be used to initialize
  an identity on arbitrary dimension subsystems and it will be implicitly
  converted to other ``BaseOperator`` subclasses (such as an
  :class:`qiskit.quantum_info.Operator` or
  :class:`qiskit.quantum_info.SuperOp`) when it is composed with,
  or added to, them.

  Example: Identity operator

  .. code-block::

      from qiskit.quantum_info import ScalarOp, Operator

      X = Operator.from_label('X')
      Z = Operator.from_label('Z')

      init = ScalarOp(2 ** 3)  # 3-qubit identity
      op = init @ X([0]) @ Z([1]) @ X([2])  # Op XZX

- A new method, :meth:`~qiskit.quantum_info.Operator.reshape`, has been added
  to the :class:`qiskit.quantum_innfo.Operator` class that returns a shallow
  copy of an operator subclass with reshaped subsystem input or output dimensions.
  The combined dimensions of all subsystems must be the same as the original
  operator or an exception will be raised.

- Adds :func:`qiskit.quantum_info.random_clifford` for generating a random
  :class:`qiskit.quantum_info.Clifford` operator.

- Add :func:`qiskit.quantum_info.random_quantum_channel` function
  for generating a random quantum channel with fixed
  :class:`~qiskit.quantum_info.Choi`-rank in the
  :class:`~qiskit.quantum_info.Stinespring` representation.

- Add :func:`qiskit.quantum_info.random_hermitian` for generating
  a random Hermitian :class:`~qiskit.quantum_info.Operator`.

- Add :func:`qiskit.quantum_info.random_statevector` for generating
  a random :class:`~qiskit.quantum_info.Statevector`.

- Adds :func:`qiskit.quantum_info.random_pauli_table` for generating a random
  :class:`qiskit.quantum_info.PauliTable`.

- Adds :func:`qiskit.quantum_info.random_stabilizer_table` for generating a random
  :class:`qiskit.quantum_info.StabilizerTable`.

- Add a ``num_qubits`` attribute to :class:`qiskit.quantum_info.StateVector` and
  :class:`qiskit.quantum_info.DensityMatrix` classes. This returns the number of
  qubits for N-qubit states and returns ``None`` for non-qubit states.

- Adds :meth:`~qiskit.quantum_info.Statevector.to_dict` and
  :meth:`~qiskit.quantum_info.DensityMatrix.to_dict` methods to convert
  :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` objects into Bra-Ket notation
  dictionary.

  Example

  .. jupyter-execute::

    from qiskit.quantum_info import Statevector

    state = Statevector.from_label('+0')
    print(state.to_dict())

  .. jupyter-execute::

    from qiskit.quantum_info import DensityMatrix

    state = DensityMatrix.from_label('+0')
    print(state.to_dict())

- Adds :meth:`~qiskit.quantum_info.Statevector.probabilities` and
  :meth:`~qiskit.quantum_info.DensityMatrix.probabilities` to
  :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` classes which return an
  array of measurement outcome probabilities in the computational
  basis for the specified subsystems.

  Example

  .. jupyter-execute::

    from qiskit.quantum_info import Statevector

    state = Statevector.from_label('+0')
    print(state.probabilities())

  .. jupyter-execute::

    from qiskit.quantum_info import DensityMatrix

    state = DensityMatrix.from_label('+0')
    print(state.probabilities())

- Adds :meth:`~qiskit.quantum_info.Statevector.probabilities_dict` and
  :meth:`~qiskit.quantum_info.DensityMatrix.probabilities_dict` to
  :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` classes which return a
  count-style dictionary array of measurement outcome probabilities
  in the computational basis for the specified subsystems.

  .. jupyter-execute::

    from qiskit.quantum_info import Statevector

    state = Statevector.from_label('+0')
    print(state.probabilities_dict())

  .. jupyter-execute::

    from qiskit.quantum_info import DensityMatrix

    state = DensityMatrix.from_label('+0')
    print(state.probabilities_dict())

- Add :meth:`~qiskit.quantum_info.Statevector.sample_counts` and
  :meth:`~qiskit.quantum_info.Statevector.sample_memory` methods to the
  :class:`~qiskit.quantum_info.Statevector`
  and :class:`~qiskit.quantum_info.DensityMatrix` classes for sampling
  measurement outcomes on subsystems.

  Example:

    Generate a counts dictionary by sampling from a statevector

    .. jupyter-execute::

      from qiskit.quantum_info import Statevector

      psi = Statevector.from_label('+0')
      shots = 1024

      # Sample counts dictionary
      counts = psi.sample_counts(shots)
      print('Measure both:', counts)

      # Qubit-0
      counts0 = psi.sample_counts(shots, [0])
      print('Measure Qubit-0:', counts0)

      # Qubit-1
      counts1 = psi.sample_counts(shots, [1])
      print('Measure Qubit-1:', counts1)

    Return the array of measurement outcomes for each sample

    .. jupyter-execute::

      from qiskit.quantum_info import Statevector

      psi = Statevector.from_label('-1')
      shots = 10

      # Sample memory
      mem = psi.sample_memory(shots)
      print('Measure both:', mem)

      # Qubit-0
      mem0 = psi.sample_memory(shots, [0])
      print('Measure Qubit-0:', mem0)

      # Qubit-1
      mem1 = psi.sample_memory(shots, [1])
      print('Measure Qubit-1:', mem1)

- Adds a :meth:`~qiskit.quantum_info.Statevector.measure` method to the
  :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` quantum state classes. This
  allows sampling a single measurement outcome from the specified subsystems
  and collapsing the statevector to the post-measurement computational basis
  state. For example

  .. jupyter-execute::

    from qiskit.quantum_info import Statevector

    psi = Statevector.from_label('+1')

    # Measure both qubits
    outcome, psi_meas = psi.measure()
    print("measure([0, 1]) outcome:", outcome, "Post-measurement state:")
    print(psi_meas)

    # Measure qubit-1 only
    outcome, psi_meas = psi.measure([1])
    print("measure([1]) outcome:", outcome, "Post-measurement state:")
    print(psi_meas)

- Adds a :meth:`~qiskit.quantum_info.Statevector.reset` method to the
  :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` quantum state classes. This
  allows reseting some or all subsystems to the :math:`|0\rangle` state.
  For example

  .. jupyter-execute::

    from qiskit.quantum_info import Statevector

    psi = Statevector.from_label('+1')

    # Reset both qubits
    psi_reset = psi.reset()
    print("Post reset state: ")
    print(psi_reset)

    # Reset qubit-1 only
    psi_reset = psi.reset([1])
    print("Post reset([1]) state: ")
    print(psi_reset)

- A new visualization function
  :func:`qiskit.visualization.visualize_transition` for visualizing
  single qubit gate transitions has been added. It takes in a single qubit
  circuit and returns an animation of qubit state transitions on a Bloch
  sphere. To use this function you must have installed
  the dependencies for and configured globally a matplotlib animtion
  writer. You can refer to the `matplotlib documentation
  <https://matplotlib.org/api/animation_api.html#writer-classes>`_ for
  more details on this. However, in the default case simply ensuring
  that `FFmpeg <https://www.ffmpeg.org/>`_ is installed is sufficient to
  use this function.

  It supports circuits with the following gates:

  * :class:`~qiskit.extensions.HGate`
  * :class:`~qiskit.extensions.XGate`
  * :class:`~qiskit.extensions.YGate`
  * :class:`~qiskit.extensions.ZGate`
  * :class:`~qiskit.extensions.RXGate`
  * :class:`~qiskit.extensions.RYGate`
  * :class:`~qiskit.extensions.RZGate`
  * :class:`~qiskit.extensions.SGate`
  * :class:`~qiskit.extensions.SdgGate`
  * :class:`~qiskit.extensions.TGate`
  * :class:`~qiskit.extensions.TdgGate`
  * :class:`~qiskit.extensions.U1Gate`

  For example:

  .. jupyter-execute::

    from qiskit.visualization import visualize_transition
    from qiskit import *

    qc = QuantumCircuit(1)
    qc.h(0)
    qc.ry(70,0)
    qc.rx(90,0)
    qc.rz(120,0)

    visualize_transition(qc, fpg=20, spg=1, trace=True)

- :func:`~qiskit.execute.execute` has a new kwarg ``schedule_circuit``. By
  setting ``schedule_circuit=True`` this enables scheduling of the circuit
  into a :class:`~qiskit.pulse.Schedule`. This allows users building
  :class:`qiskit.circuit.QuantumCircuit` objects to make use of custom
  scheduler  methods, such as the ``as_late_as_possible`` and
  ``as_soon_as_possible`` methods.
  For example::

      job = execute(qc, backend, schedule_circuit=True,
                    scheduling_method="as_late_as_possible")

- A new environment variable ``QISKIT_SUPPRESS_PACKAGING_WARNINGS`` can be
  set to ``Y`` or ``y`` which will suppress the warnings about
  ``qiskit-aer`` and ``qiskit-ibmq-provider`` not being installed at import
  time. This is useful for users who are only running qiskit-terra (or just
  not qiskit-aer and/or qiskit-ibmq-provider) and the warnings are not an
  indication of a potential packaging problem. You can set the environment
  variable to ``N`` or ``n`` to ensure that warnings are always enabled
  even if the user config file is set to disable them.

- A new user config file option, ``suppress_packaging_warnings`` has been
  added. When set to ``true`` in your user config file like::

      [default]
      suppress_packaging_warnings = true

  it will suppress the warnings about  ``qiskit-aer`` and
  ``qiskit-ibmq-provider`` not being installed at import time. This is useful
  for users who are only running qiskit-terra (or just not qiskit-aer and/or
  qiskit-ibmq-provider) and the warnings are not an indication of a potential
  packaging problem. If the user config file is set to disable the warnings
  this can be overriden by setting the ``QISKIT_SUPPRESS_PACKAGING_WARNINGS``
  to ``N`` or ``n``

- :func:`qiskit.compiler.transpile()` has two new kwargs, ``layout_method``
  and ``routing_method``. These allow you to select a particular method for
  placement and routing of circuits on constrained architectures. For,
  example::

      transpile(circ, backend, layout_method='dense',
                routing_method='lookahead')

  will run :class:`~qiskit.transpiler.passes.DenseLayout` layout pass and
  :class:`~qiskit.transpiler.passes.LookaheadSwap` routing pass.

- There has been a significant simplification to the style in which Pulse
  instructions are built.

  With the previous style, ``Command`` s were called with channels to make
  an :py:class:`~qiskit.pulse.instructions.Instruction`. The usage of both
  commands and instructions was a point of confusion. This was the previous
  style::

      sched += Delay(5)(DriveChannel(0))
      sched += ShiftPhase(np.pi)(DriveChannel(0))
      sched += SamplePulse([1.0, ...])(DriveChannel(0))
      sched += Acquire(100)(AcquireChannel(0), MemorySlot(0))

  or, equivalently (though less used)::

      sched += DelayInstruction(Delay(5), DriveChannel(0))
      sched += ShiftPhaseInstruction(ShiftPhase(np.pi), DriveChannel(0))
      sched += PulseInstruction(SamplePulse([1.0, ...]), DriveChannel(0))
      sched += AcquireInstruction(Acquire(100), AcquireChannel(0),
                                  MemorySlot(0))

  Now, rather than build a command *and* an instruction, each command has
  been migrated into an instruction::

      sched += Delay(5, DriveChannel(0))
      sched += ShiftPhase(np.pi, DriveChannel(0))
      sched += Play(SamplePulse([1.0, ...]), DriveChannel(0))
      sched += SetFrequency(5.5, DriveChannel(0))  # New instruction!
      sched += Acquire(100, AcquireChannel(0), MemorySlot(0))

- There is now a :py:class:`~qiskit.pulse.instructions.Play` instruction
  which takes a description of a pulse envelope and a channel. There is a
  new :py:class:`~qiskit.pulse.pulse_lib.Pulse` class in the
  :mod:`~qiskit.pulse.pulse_lib` from which the pulse envelope description
  should subclass.

  For example::

      Play(SamplePulse([0.1]*10), DriveChannel(0))
      Play(ConstantPulse(duration=10, amp=0.1), DriveChannel(0))


.. _Release Notes_0.13.0_Upgrade Notes:

Upgrade Notes
-------------

- The :class:`qiskit.dagcircuit.DAGNode` method ``pop`` which was deprecated
  in the 0.9.0 release has been removed. If you were using this method you
  can leverage Python's ``del`` statement or ``delattr()`` function
  to perform the same task.

- A new optional visualization requirement,
  `pygments <https://pygments.org/>`_ , has been added. It is used for
  providing syntax highlighting of OpenQASM 2.0 code in Jupyter widgets and
  optionally for the :meth:`qiskit.circuit.QuantumCircuit.qasm` method. It
  must be installed (either with ``pip install pygments`` or
  ``pip install qiskit-terra[visualization]``) prior to using the
  ``%circuit_library_info`` widget in :mod:`qiskit.tools.jupyter` or
  the ``formatted`` kwarg on the :meth:`~qiskit.circuit.QuantumCircuit.qasm`
  method.

- The pulse ``buffer`` option found in :class:`qiskit.pulse.Channel` and
  :class:`qiskit.pulse.Schedule` was deprecated in Terra 0.11.0 and has now
  been removed. To add a delay on a channel or in a schedule, specify it
  explicitly in your Schedule with a Delay::

      sched = Schedule()
      sched += Delay(5)(DriveChannel(0))

- ``PulseChannelSpec``, which was deprecated in Terra 0.11.0, has now been
  removed. Use BackendConfiguration instead::

      config = backend.configuration()
      drive_chan_0 = config.drives(0)
      acq_chan_0 = config.acquires(0)

  or, simply reference the channel directly, such as ``DriveChannel(index)``.

- An import path was deprecated in Terra 0.10.0 and has now been removed: for
  ``PulseChannel``, ``DriveChannel``, ``MeasureChannel``, and
  ``ControlChannel``, use ``from qiskit.pulse.channels import X`` in place of
  ``from qiskit.pulse.channels.pulse_channels import X``.

- The pass :class:`qiskit.transpiler.passes.CSPLayout` (which was introduced
  in the 0.11.0 release) has been added to the preset pass manager for
  optimization levels 2 and 3. For level 2, there is a call limit of 1,000
  and a timeout of 10 seconds. For level 3, the call limit is 10,000 and the
  timeout is 1 minute.

  Now that the pass is included in the preset pass managers the
  `python-constraint <https://pypi.org/project/python-constraint/>`_ package
  is not longer an optional dependency and has been added to the requirements
  list.

- The ``TranspileConfig`` class which was previously used to set
  run time configuration for a :class:`qiskit.transpiler.PassManager` has
  been removed and replaced by a new class
  :class:`qiskit.transpile.PassManagerConfig`. This new class has been
  structured to include only the information needed to construct a
  :class:`~qiskit.transpiler.PassManager`. The attributes of this class are:

  * ``initial_layout``
  * ``basis_gates``
  * ``coupling_map``
  * ``backend_properties``
  * ``seed_transpiler``

- The function ``transpile_circuit`` in
  :mod:`qiskit.transpiler` has been removed. To transpile a circuit with a
  custom :class:`~qiskit.transpiler.PassManager` now you should use the
  :meth:`~qiskit.transpiler.PassManager.run` method of the
  :class:~qiskit.transpiler.PassManager` object.

- The :class:`~qiskit.circuit.QuantumCircuit` method
  :meth:`~qiskit.circuit.QuantumCircuit.draw` and
  :func:`qiskit.visualization.circuit_drawer` function will no longer include
  the initial state included in visualizations by default. If you would like to
  retain the initial state in the output visualization you need to set the
  ``initial_state`` kwarg to ``True``. For example, running:

  .. jupyter-execute::

      from qiskit import QuantumCircuit

      circuit = QuantumCircuit(2)
      circuit.measure_all()
      circuit.draw(output='text')

  This no longer includes the initial state. If you'd like to retain it you can run:

  .. jupyter-execute::

      from qiskit import QuantumCircuit

      circuit = QuantumCircuit(2)
      circuit.measure_all()
      circuit.draw(output='text', initial_state=True)


- :func:`qiskit.compiler.transpile` (and :func:`qiskit.execute.execute`,
  which uses ``transpile`` internally) will now raise an error when the
  ``pass_manager`` kwarg is set and a value is set for other kwargs that
  are already set in an instantiated :class:`~qiskit.transpiler.PassManager`
  object. Previously, these conflicting kwargs would just be silently
  ignored and the values in the ``PassManager`` instance would be used. For
  example::

      from qiskit.circuit import QuantumCircuit
      from qiskit.transpiler.pass_manager_config import PassManagerConfig
      from qiskit.transpiler import preset_passmanagers
      from qiskit.compiler import transpile

      qc = QuantumCircuit(5)

      config = PassManagerConfig(basis_gates=['u3', 'cx'])
      pm = preset_passmanagers.level_0_pass_manager(config)
      transpile(qc, optimization_level=3, pass_manager=pm)

  will now raise an error while prior to this release the value in ``pm``
  would just silently be used and the value for the ``optimization_level``
  kwarg would be ignored. The ``transpile`` kwargs this applies to are:

  * ``optimization_level``
  * ``basis_gates``
  * ``coupling_map``
  * ``seed_transpiler``
  * ``backend_properties``
  * ``initial_layout``
  * ``layout_method``
  * ``routing_method``
  * ``backend``

- The :class:`~qiskit.quantum_info.Operator`,
  :class:`~qiskit.quantum_info.Clifford`,
  :class:`~qiskit.quantum_info.SparsePauliOp`,
  :class:`~qiskit.quantum_info.PauliTable`,
  :class:`~qiskit.quantum_info.StabilizerTable`, operator classes have an added
  ``call`` method that allows them to assign a `qargs` to the operator for use
  with the :meth:`~qiskit.quantum_info.Operator.compose`,
  :meth:`~qiskit.quantum_info.Operator.dot`,
  :meth:`~qiskit.quantum_info.Statevector.evolve`,``+``, and ``-`` operations.

- The addition method of the :class:`qiskit.quantum_info.Operator`, class now accepts a
  ``qarg`` kwarg to allow adding a smaller operator to a larger one assuming identities
  on the other subsystems (same as for ``qargs`` on
  :meth:`~qiskit.quantum_info.Operator.compose` and
  :meth:`~qiskit.quantum_info.Operator.dot` methods). This allows
  subsystem addition using the call method as with composition. This support is
  added to all BaseOperator subclasses (:class:`~qiskit.quantum_info.ScalarOp`,
  :class:`~qiskit.quantum_info.Operator`,
  :class:`~qiskit.quantum_info.QuantumChannel`).

  For example:

  .. code-block::

    from qiskit.quantum_info import Operator, ScalarOp

    ZZ = Operator.from_label('ZZ')

    # Initialize empty Hamiltonian
    n_qubits = 10
    ham = ScalarOp(2 ** n_qubits, coeff=0)

    # Add 2-body nearest neighbour terms
    for j in range(n_qubits - 1):
        ham = ham + ZZ([j, j+1])

- The ``BaseOperator`` class has been updated so that addition,
  subtraction and scalar multiplication are no longer abstract methods. This
  means that they are no longer required to be implemented in subclasses if
  they are not supported. The base class will raise a ``NotImplementedError``
  when the methods are not defined.

- The :func:`qiskit.quantum_info.random_density_matrix` function will
  now return a random :class:`~qiskit.quantum_info.DensityMatrix` object. In
  previous releases it returned a numpy array.

- The :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` classes no longer copy the
  input array if it is already the correct dtype.

- `fastjsonschema <https://pypi.org/project/fastjsonschema/>`_ is added as a
  dependency. This is used for much faster validation of qobj dictionaries
  against the JSON schema when the ``to_dict()`` method is called on qobj
  objects with the ``validate`` keyword argument set to ``True``.

- The qobj construction classes in :mod:`qiskit.qobj` will no longer validate
  against the qobj jsonschema by default. These include the following classes:

  * :class:`qiskit.qobj.QasmQobjInstruction`
  * :class:`qiskit.qobj.QobjExperimentHeader`
  * :class:`qiskit.qobj.QasmQobjExperimentConfig`
  * :class:`qiskit.qobj.QasmQobjExperiment`
  * :class:`qiskit.qobj.QasmQobjConfig`
  * :class:`qiskit.qobj.QobjHeader`
  * :class:`qiskit.qobj.PulseQobjInstruction`
  * :class:`qiskit.qobj.PulseQobjExperimentConfig`
  * :class:`qiskit.qobj.PulseQobjExperiment`
  * :class:`qiskit.qobj.PulseQobjConfig`
  * :class:`qiskit.qobj.QobjMeasurementOption`
  * :class:`qiskit.qobj.PulseLibraryItem`
  * :class:`qiskit.qobj.QasmQobjInstruction`
  * :class:`qiskit.qobj.QasmQobjExperimentConfig`
  * :class:`qiskit.qobj.QasmQobjExperiment`
  * :class:`qiskit.qobj.QasmQobjConfig`
  * :class:`qiskit.qobj.QasmQobj`
  * :class:`qiskit.qobj.PulseQobj`

  If you were relying on this validation or would like to validate them
  against the qobj schema this can be done by setting the ``validate`` kwarg
  to ``True`` on :meth:`~qiskit.qobj.QasmQobj.to_dict` method from either of
  the top level Qobj classes :class:`~qiskit.qobj.QasmQobj` or
  :class:`~qiskit.qobj.PulseQobj`. For example:

  .. code-block:

      from qiskit import qobj

      my_qasm = qobj.QasmQobj(
          qobj_id='12345',
          header=qobj.QobjHeader(),
          config=qobj.QasmQobjConfig(shots=1024, memory_slots=2,
                                     max_credits=10),
          experiments=[
              qobj.QasmQobjExperiment(instructions=[
                  qobj.QasmQobjInstruction(name='u1', qubits=[1],
                                           params=[0.4]),
                  qobj.QasmQobjInstruction(name='u2', qubits=[1],
                                           params=[0.4, 0.2])
              ])
          ]
      )
      qasm_dict = my_qasm.to_dict(validate=True)

  which will validate the output dictionary against the Qobj jsonschema.

- The output dictionary from :meth:`qiskit.qobj.QasmQobj.to_dict` and
  :meth:`qiskit.qobj.PulseQobj.to_dict` is no longer in a format for direct
  json serialization as expected by IBMQ's API. These Qobj objects are
  the current format we use for passing experiments to providers/backends
  and while having a dictionary format that could just be passed to the IBMQ
  API directly was moderately useful for ``qiskit-ibmq-provider``, it made
  things more difficult for other providers. Especially for providers that
  wrap local simulators. Moving forward the definitions of what is passed
  between providers and the IBMQ API request format will be further decoupled
  (in a backwards compatible manner) which should ease the burden of writing
  providers and backends.

  In practice, the only functional difference between the output of these
  methods now and previous releases is that complex numbers are represented
  with the ``complex`` type and numpy arrays are not silently converted to
  list anymore. If you were previously calling ``json.dumps()`` directly on
  the output of ``to_dict()`` after this release a custom json encoder will
  be needed to handle these cases. For example::

      import json

      from qiskit.circuit import ParameterExpression
      from qiskit import qobj

      my_qasm = qobj.QasmQobj(
          qobj_id='12345',
          header=qobj.QobjHeader(),
          config=qobj.QasmQobjConfig(shots=1024, memory_slots=2,
                                     max_credits=10),
          experiments=[
              qobj.QasmQobjExperiment(instructions=[
                  qobj.QasmQobjInstruction(name='u1', qubits=[1],
                                           params=[0.4]),
                  qobj.QasmQobjInstruction(name='u2', qubits=[1],
                                           params=[0.4, 0.2])
              ])
          ]
      )
      qasm_dict = my_qasm.to_dict()

      class QobjEncoder(json.JSONEncoder):
          """A json encoder for pulse qobj"""
          def default(self, obj):
              # Convert numpy arrays:
              if hasattr(obj, 'tolist'):
                  return obj.tolist()
              # Use Qobj complex json format:
              if isinstance(obj, complex):
                  return (obj.real, obj.imag)
              if isinstance(obj, ParameterExpression):
                  return float(obj)
              return json.JSONEncoder.default(self, obj)

      json_str = json.dumps(qasm_dict, cls=QobjEncoder)

  will generate a json string in the same exact manner that
  ``json.dumps(my_qasm.to_dict())`` did in previous releases.

- ``CmdDef`` has been deprecated since Terra 0.11.0 and has been removed.
  Please continue to use :py:class:`~qiskit.pulse.InstructionScheduleMap`
  instead.

- The methods ``cmds`` and ``cmd_qubits`` in
  :py:class:`~qiskit.pulse.InstructionScheduleMap` have been deprecated
  since Terra 0.11.0 and have been removed. Please use ``instructions``
  and ``qubits_with_instruction`` instead.

- PulseDefaults have reported ``qubit_freq_est`` and ``meas_freq_est`` in
  Hz rather than GHz since Terra release 0.11.0. A warning which notified
  of this change has been removed.

- The previously deprecated (in the 0.11.0 release) support for passsing in
  :class:`qiskit.circuit.Instruction` parameters of types ``sympy.Basic``,
  ``sympy.Expr``, ``qiskit.qasm.node.node.Node`` (QASM AST node) and
  ``sympy.Matrix`` has been removed. The supported types for instruction
  parameters are:

  * ``int``
  * ``float``
  * ``complex``
  * ``str``
  * ``list``
  * ``np.ndarray``
  * :class:`qiskit.circuit.ParameterExpression`

- The following properties of
  :py:class:`~qiskit.providers.models.BackendConfiguration`:

  * ``dt``
  * ``dtm``
  * ``rep_time``

  all have units of seconds. Prior to release 0.11.0, ``dt`` and ``dtm`` had
  units of nanoseconds. Prior to release 0.12.0, ``rep_time`` had units of
  microseconds. The warnings alerting users of these changes have now been
  removed from ``BackendConfiguration``.

- A new requirement has been added to the requirements list,
  `retworkx <https://pypi.org/project/retworkx/>`_. It is an Apache 2.0
  licensed graph library that has a similar API to networkx and is being used
  to significantly speed up the :class:`qiskit.dagcircuit.DAGCircuit`
  operations as part of the transpiler. There are binaries published on PyPI
  for all the platforms supported by Qiskit Terra but if you're using a
  platform where there aren't precompiled binaries published refer to the
  `retworkx documentation
  <https://retworkx.readthedocs.io/en/stable/README.html#installing-retworkx>`_
  for instructions on pip installing from sdist.

  If you encounter any issues with the transpiler or DAGCircuit class as part
  of the transition you can switch back to the previous networkx
  implementation by setting the environment variable ``USE_RETWORKX`` to
  ``N``. This option will be removed in the 0.14.0 release.


.. _Release Notes_0.13.0_Deprecation Notes:

Deprecation Notes
-----------------

- Passing in the data to the constructor for
  :class:`qiskit.dagcircuit.DAGNode` as a dictionary arg ``data_dict``
  is deprecated and will be removed in a future release. Instead you should
  now pass the fields in as kwargs to the constructor. For example the
  previous behavior of::

    from qiskit.dagcircuit import DAGNode

    data_dict = {
        'type': 'in',
        'name': 'q_0',
    }
    node = DAGNode(data_dict)

  should now be::

    from qiskit.dagcircuit import DAGNode

    node = DAGNode(type='in', name='q_0')

- The naming of gate objects and methods have been updated to be more
  consistent. The following changes have been made:

  * The Pauli gates all have one uppercase letter only (``I``, ``X``, ``Y``,
    ``Z``)
  * The parameterized Pauli gates (i.e. rotations) prepend the uppercase
    letter ``R`` (``RX``, ``RY``, ``RZ``)
  * A controlled version prepends the uppercase letter ``C`` (``CX``,
    ``CRX``, ``CCX``)
  * Gates are named according to their action, not their alternative names
    (``CCX``, not ``Toffoli``)

  The old names have been deprecated and will be removed in a future release.
  This is a list of the changes showing the old and new class, name attribute,
  and methods. If a new column is blank then there is no change for that.

  .. list-table:: Gate Name Changes
     :header-rows: 1

     * - Old Class
       - New Class
       - Old Name Attribute
       - New Name Attribute
       - Old :class:`qiskit.circuit.QuantumCircuit` method
       - New :class:`qiskit.circuit.QuantumCircuit` method
     * - ``ToffoliGate``
       - :class:`~qiskit.extensions.CCXGate`
       - ``ccx``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.ccx` and
         :meth:`~qiskit.circuit.QuantumCircuit.toffoli`
       -
     * - ``CrxGate``
       - :class:`~qiskit.extensions.CRXGate`
       - ``crx``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.crx`
       -
     * - ``CryGate``
       - :class:`~qiskit.extensions.CRYGate`
       - ``cry``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.cry`
       -
     * - ``CrzGate``
       - :class:`~qiskit.extensions.CRZGate`
       - ``crz``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.crz`
       -
     * - ``FredkinGate``
       - :class:`~qiskit.extensions.CSwapGate`
       - ``cswap``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.cswap` and
         :meth:`~qiskit.circuit.QuantumCircuit.fredkin`
       -
     * - ``Cu1Gate``
       - :class:`~qiskit.extensions.CU1Gate`
       - ``cu1``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.cu1`
       -
     * - ``Cu3Gate``
       - :class:`~qiskit.extensions.CU3Gate`
       - ``cu3``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.cu3`
       -
     * - ``CnotGate``
       - :class:`~qiskit.extensions.CXGate`
       - ``cx``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.cx` and
         :meth:`~qiskit.circuit.QuantumCircuit.cnot`
       -
     * - ``CyGate``
       - :class:`~qiskit.extensions.CYGate`
       - ``cy``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.cy`
       -
     * - ``CzGate``
       - :class:`~qiskit.extensions.CZGate`
       - ``cz``
       -
       - :meth:`~qiskit.circuit.QuantumCircuit.cz`
       -
     * - ``DiagGate``
       - :class:`~qiskit.extensions.DiagonalGate`
       - ``diag``
       - ``diagonal``
       - ``diag_gate``
       - :meth:`~qiskit.circuit.QuantumCircuit.diagonal`
     * - ``IdGate``
       - :class:`~qiskit.extensions.IGate`
       - ``id``
       -
       - ``iden``
       - :meth:`~qiskit.circuit.QuantumCircuit.i` and
         :meth:`~qiskit.circuit.QuantumCircuit.id`
     * - :class:`~qiskit.extensions.Isometry`
       -
       - ``iso``
       - ``isometry``
       - :meth:`~qiskit.circuit.QuantumCircuit.iso`
       - :meth:`~qiskit.circuit.QuantumCircuit.isometry`
         and :meth:`~qiskit.circuit.QuantumCircuit.iso`
     * - ``UCG``
       - :class:`~qiskit.extensions.UCGate`
       - ``multiplexer``
       -
       - ``ucg``
       - :meth:`~qiskit.circuit.QuantumCircuit.uc`
     * - ``UCRot``
       - :class:`~qiskit.extensions.UCPauliRotGate`
       -
       -
       -
       -
     * - ``UCX``
       - :class:`~qiskit.extensions.UCRXGate`
       - ``ucrotX``
       - ``ucrx``
       - ``ucx``
       - :meth:`~qiskit.circuit.QuantumCircuit.ucrx`
     * - ``UCY``
       - :class:`~qiskit.extensions.UCRYGate`
       - ``ucroty``
       - ``ucry``
       - ``ucy``
       - :meth:`~qiskit.circuit.QuantumCircuit.ucry`
     * - ``UCZ``
       - :class:`~qiskit.extensions.UCRZGate`
       - ``ucrotz``
       - ``ucrz``
       - ``ucz``
       - :meth:`~qiskit.circuit.QuantumCircuit.ucrz`

- The kwarg ``period`` for the function
  :func:`~qiskit.pulse.pulse_lib.square`,
  :func:`~qiskit.pulse.pulse_lib.sawtooth`, and
  :func:`~qiskit.pulse.pulse_lib.triangle` in
  :mod:`qiskit.pulse.pulse_lib` is now deprecated and will be removed in a
  future release. Instead you should now use the ``freq`` kwarg to set
  the frequency.

- The ``DAGCircuit.compose_back()`` and ``DAGCircuit.extend_back()`` methods
  are deprecated and will be removed in a future release. Instead you should
  use the :meth:`qiskit.dagcircuit.DAGCircuit.compose` method, which is a more
  general and more flexible method that provides the same functionality.

- The ``callback`` kwarg of the :class:`qiskit.transpiler.PassManager` class's
  constructor has been deprecated and will be removed in a future release.
  Instead of setting it at the object level during creation it should now
  be set as a kwarg parameter on the :meth:`qiskit.transpiler.PassManager.run`
  method.

- The ``n_qubits`` and ``numberofqubits`` keywords are deprecated throughout
  Terra and replaced by ``num_qubits``. The old names will be removed in
  a future release. The objects affected by this change are listed below:

  .. list-table:: New Methods
     :header-rows: 1

     * - Class
       - Old Method
       - New Method
     * - :class:`~qiskit.circuit.QuantumCircuit`
       - ``n_qubits``
       - :meth:`~qiskit.circuit.QuantumCircuit.num_qubits`
     * - :class:`~qiskit.quantum_info.Pauli`
       - ``numberofqubits``
       - :meth:`~qiskit.quantum_info.Pauli.num_qubits`

  .. list-table:: New arguments
     :header-rows: 1

     * - Function
       - Old Argument
       - New Argument
     * - :func:`~qiskit.circuit.random.random_circuit`
       - ``n_qubits``
       - ``num_qubits``
     * - :class:`~qiskit.extensions.MSGate`
       - ``n_qubit``
       - ``num_qubits``

- The function ``qiskit.quantum_info.synthesis.euler_angles_1q`` is now
  deprecated. It has been superseded by the
  :class:`qiskit.quantum_info.OneQubitEulerDecomposer` class which provides
  the same functionality through::

      OneQubitEulerDecomposer().angles(mat)

- The ``pass_manager`` kwarg for the :func:`qiskit.compiler.transpile`
  has been deprecated and will be removed in a future release. Moving forward
  the preferred way to transpile a circuit with a custom
  :class:`~qiskit.transpiler.PassManager` object is to use the
  :meth:`~qiskit.transpiler.PassManager.run` method of the ``PassManager``
  object.

- The :func:`qiskit.quantum_info.random_state` function has been deprecated
  and will be removed in a future release. Instead you should use the
  :func:`qiskit.quantum_info.random_statevector` function.

- The ``add``, ``subtract``, and ``multiply`` methods of the
  :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` classes are deprecated and will
  be removed in a future release. Instead you shoulde use ``+``, ``-``, ``*``
  binary operators instead.

- Deprecates :meth:`qiskit.quantum_info.Statevector.to_counts`,
  :meth:`qiskit.quantum_info.DensityMatrix.to_counts`, and
  :func:`qiskit.quantum_info.counts.state_to_counts`. These functions
  are superseded by the class methods
  :meth:`qiskit.quantum_info.Statevector.probabilities_dict` and
  :meth:`qiskit.quantum_info.DensityMatrix.probabilities_dict`.

- :py:class:`~qiskit.pulse.pulse_lib.SamplePulse` and
  :py:class:`~qiskit.pulse.pulse_lib.ParametricPulse` s (e.g. ``Gaussian``)
  now subclass from :py:class:`~qiskit.pulse.pulse_lib.Pulse` and have been
  moved to the :mod:`qiskit.pulse.pulse_lib`. The previous path via
  ``pulse.commands`` is deprecated and will be removed in a future release.

- ``DelayInstruction`` has been deprecated and replaced by
  :py:class:`~qiskit.pulse.instruction.Delay`. This new instruction has been
  taken over the previous ``Command`` ``Delay``. The migration pattern is::

      Delay(<duration>)(<channel>) -> Delay(<duration>, <channel>)
      DelayInstruction(Delay(<duration>), <channel>)
          -> Delay(<duration>, <channel>)

  Until the deprecation period is over, the previous ``Delay`` syntax of
  calling a command on a channel will also be supported::

      Delay(<phase>)(<channel>)

  The new ``Delay`` instruction does not support a ``command`` attribute.

- ``FrameChange`` and ``FrameChangeInstruction`` have been deprecated and
  replaced by :py:class:`~qiskit.pulse.instructions.ShiftPhase`. The changes
  are::

      FrameChange(<phase>)(<channel>) -> ShiftPhase(<phase>, <channel>)
      FrameChangeInstruction(FrameChange(<phase>), <channel>)
          -> ShiftPhase(<phase>, <channel>)

  Until the deprecation period is over, the previous FrameChange syntax of
  calling a command on a channel will be supported::

      ShiftPhase(<phase>)(<channel>)

- The ``call`` method of :py:class:`~qiskit.pulse.pulse_lib.SamplePulse` and
  :py:class:`~qiskit.pulse.pulse_lib.ParametricPulse` s have been deprecated.
  The migration is as follows::

      Pulse(<*args>)(<channel>) -> Play(Pulse(*args), <channel>)

- ``AcquireInstruction`` has been deprecated and replaced by
  :py:class:`~qiskit.pulse.instructions.Acquire`. The changes are::

      Acquire(<duration>)(<**channels>) -> Acquire(<duration>, <**channels>)
      AcquireInstruction(Acquire(<duration>), <**channels>)
          -> Acquire(<duration>, <**channels>)

  Until the deprecation period is over, the previous Acquire syntax of
  calling the command on a channel will be supported::

      Acquire(<duration>)(<**channels>)


.. _Release Notes_0.13.0_Bug Fixes:

Bug Fixes
---------

- The :class:`~qiskit.transpiler.passes.BarrierBeforeFinalMeasurements`
  transpiler pass, included in the preset transpiler levels when targeting
  a physical device, previously inserted a barrier across only measured
  qubits. In some cases, this allowed the transpiler to insert a swap after a
  measure operation, rendering the circuit invalid for current
  devices. The pass has been updated so that the inserted barrier
  will span all qubits on the device. Fixes
  `#3937 <https://github.com/Qiskit/qiskit-terra/issues/3937>`_

- When extending a :class:`~qiskit.circuit.QuantumCircuit` instance
  (extendee) with another circuit (extension), the circuit is taken via
  reference. If a circuit is extended with itself that leads to an infinite
  loop as extendee and extension are the same. This bug has been resolved by
  copying the extension if it is the same object as the extendee.
  Fixes `#3811 <https://github.com/Qiskit/qiskit-terra/issues/3811>`_

- Fixes a case in :meth:`qiskit.result.Result.get_counts`, where the results
  for an expirement could not be referenced if the experiment was initialized
  as a Schedule without a name. Fixes
  `#2753 <https://github.com/Qiskit/qiskit-terra/issues/2753>`_

- Previously, replacing :class:`~qiskit.circuit.Parameter` objects in a
  circuit with new Parameter objects prior to decomposing a circuit would
  result in the substituted values not correctly being substituted into the
  decomposed gates. This has been resolved such that binding and
  decomposition may occur in any order.

- The matplotlib output backend for the
  :func:`qiskit.visualization.circuit_drawer` function and
  :meth:`qiskit.circuit.QuantumCircuit.draw` method drawer has been fixed
  to render :class:`~qiskit.extensions.CU1Gate` gates correctly.
  Fixes `#3684 <https://github.com/Qiskit/qiskit-terra/issues/3684>`_

- A bug in :meth:`qiskit.circuit.QuantumCircuit.from_qasm_str` and
  :meth:`qiskit.circuit.QuantumCircuit.from_qasm_file` when
  loading QASM with custom gates defined has been fixed. Now, loading
  this QASM::

      OPENQASM 2.0;
      include "qelib1.inc";
      gate rinv q {sdg q; h q; sdg q; h q; }
      qreg q[1];
      rinv q[0];

  is equivalent to the following circuit::

      rinv_q = QuantumRegister(1, name='q')
      rinv_gate = QuantumCircuit(rinv_q, name='rinv')
      rinv_gate.sdg(rinv_q)
      rinv_gate.h(rinv_q)
      rinv_gate.sdg(rinv_q)
      rinv_gate.h(rinv_q)
      rinv = rinv_gate.to_instruction()
      qr = QuantumRegister(1, name='q')
      expected = QuantumCircuit(qr, name='circuit')
      expected.append(rinv, [qr[0]])

  Fixes `#1566 <https://github.com/Qiskit/qiskit-terra/issues/1566>`_

- Allow quantum circuit Instructions to have list parameter values. This is
  used in Aer for expectation value snapshot parameters for example
  ``params = [[1.0, 'I'], [1.0, 'X']]]`` for :math:`\langle I + X\rangle`.

- Previously, for circuits containing composite gates (those created via
  :meth:`qiskit.circuit.QuantumCircuit.to_gate` or
  :meth:`qiskit.circuit.QuantumCircuit.to_instruction` or their corresponding
  converters), attempting to bind the circuit more than once would result in
  only the first bind value being applied to all circuits when transpiled.
  This has been resolved so that the values provided for subsequent binds are
  correctly respected.


.. _Release Notes_0.13.0_Other Notes:

Other Notes
-----------

- The qasm and pulse qobj classes:

  * :class:`~qiskit.qobj.QasmQobjInstruction`
  * :class:`~qiskit.qobj.QobjExperimentHeader`
  * :class:`~qiskit.qobj.QasmQobjExperimentConfig`
  * :class:`~qiskit.qobj.QasmQobjExperiment`
  * :class:`~qiskit.qobj.QasmQobjConfig`
  * :class:`~qiskit.qobj.QobjHeader`
  * :class:`~qiskit.qobj.PulseQobjInstruction`
  * :class:`~qiskit.qobj.PulseQobjExperimentConfig`
  * :class:`~qiskit.qobj.PulseQobjExperiment`
  * :class:`~qiskit.qobj.PulseQobjConfig`
  * :class:`~qiskit.qobj.QobjMeasurementOption`
  * :class:`~qiskit.qobj.PulseLibraryItem`
  * :class:`~qiskit.qobj.QasmQobjInstruction`
  * :class:`~qiskit.qobj.QasmQobjExperimentConfig`
  * :class:`~qiskit.qobj.QasmQobjExperiment`
  * :class:`~qiskit.qobj.QasmQobjConfig`
  * :class:`~qiskit.qobj.QasmQobj`
  * :class:`~qiskit.qobj.PulseQobj`

  from :mod:`qiskit.qobj` have all been reimplemented without using the
  marsmallow library. These new implementations are designed to be drop-in
  replacement (except for as noted in the upgrade release notes) but
  specifics inherited from marshmallow may not work. Please file issues for
  any incompatibilities found.

Aer 0.5.0
=========

Added
-----
 - Add support for terra diagonal gate
 - Add support for parameterized qobj

Fixed
-----
 - Added postfix for linux on Raspberry Pi
 - Handle numpy array inputs from qobj

Ignis 0.3.0
===========

Added
-----

* API documentation
* CNOT-Dihedral randomized benchmarking
* Accreditation module for output accrediation of noisy devices
* Pulse calibrations for single qubits
* Pulse Discriminator
* Entanglement verification circuits
* Gateset tomography for single-qubit gate sets
* Adds randomized benchmarking utility functions ``calculate_1q_epg``,
  ``calculate_2q_epg`` functions to calculate 1 and 2-qubit error per gate from
  error per Clifford
* Adds randomized benchmarking utility functions ``calculate_1q_epc``,
  ``calculate_2q_epc`` for calculating 1 and 2-qubit error per Clifford from error
  per gate

Changed
-------
* Support integer labels for qubits in tomography
* Support integer labels for measurement error mitigation

Deprecated
----------
* Deprecates ``twoQ_clifford_error`` function. Use ``calculate_2q_epc`` instead.
* Python 3.5 support in qiskit-ignis is deprecated. Support will be removed on
  the upstream python community's end of life date for the version, which is
  09/13/2020.

Aqua 0.6.5
==========

No Change

IBM Q Provider 0.6.0
====================

No Change

*************
Qiskit 0.17.0
*************

Terra 0.12.0
============

No Change

Aer 0.4.1
=========

No Change

Ignis 0.2.0
===========

No Change

Aqua 0.6.5
==========

No Change

IBM Q Provider 0.6.0
====================

New Features
------------

- There are three new exceptions: ``VisualizationError``, ``VisualizationValueError``,
  and ``VisualizationTypeError``. These are now used in the visualization modules when
  an exception is raised.
- You can now set the logging level and specify a log file using the environment
  variables ``QSIKIT_IBMQ_PROVIDER_LOG_LEVEL`` and ``QISKIT_IBMQ_PROVIDER_LOG_FILE``,
  respectively. Note that the name of the logger is ``qiskit.providers.ibmq``.
- :class:`qiskit.providers.ibmq.job.IBMQJob` now has a new method
  :meth:`~qiskit.providers.ibmq.job.IBMQJob.scheduling_mode` that returns the scheduling
  mode the job is in.
- IQX-related tutorials that used to be in ``qiskit-iqx-tutorials`` are now in
  ``qiskit-ibmq-provider``.

Changed
-------

- :meth:`qiskit.providers.ibmq.IBMQBackend.jobs` now accepts a new boolean parameter
  ``descending``, which can be used to indicate whether the jobs should be returned in
  descending or ascending order.
- :class:`qiskit.providers.ibmq.managed.IBMQJobManager` now looks at the job limit and waits
  for old jobs to finish before submitting new ones if the limit has been reached.
- :meth:`qiskit.providers.ibmq.IBMQBackend.status` now raises a
  :class:`qiskit.providers.ibmq.IBMQBackendApiProtocolError` exception
  if there was an issue with validating the status.

*************
Qiskit 0.16.0
*************

Terra 0.12.0
============

No Change

Aer 0.4.0
=========

No Change

Ignis 0.2.0
===========

No Change

Aqua 0.6.4
==========

No Change

IBM Q Provider 0.5.0
====================

New Features
------------

- Some of the visualization and Jupyter tools, including gate/error map and
  backend information, have been moved from ``qiskit-terra`` to ``qiskit-ibmq-provider``.
  They are now under the :mod:`qiskit.providers.ibmq.jupyter` and
  :mod:`qiskit.providers.ibmq.visualization`. In addition, you can now
  use ``%iqx_dashboard`` to get a dashboard that provides both job and
  backend information.

Changed
-------

- JSON schema validation is no longer run by default on Qobj objects passed
  to :meth:`qiskit.providers.ibmq.IBMQBackend.run`. This significantly speeds
  up the execution of the `run()` method. Qobj objects are still validated on the
  server side, and invalid Qobjs will continue to raise exceptions. To force local
  validation, set ``validate_qobj=True`` when you invoke ``run()``.

*************
Qiskit 0.15.0
*************

Terra 0.12.0
============

Prelude
-------

The 0.12.0 release includes several new features and bug fixes. The biggest
change for this release is the addition of support for parametric pulses to
OpenPulse. These are Pulse commands which take parameters rather than sample
points to describe a pulse. 0.12.0 is also the first release to include
support for Python 3.8. It also marks the beginning of the deprecation for
Python 3.5 support, which will be removed when the upstream community stops
supporting it.


.. _Release Notes_0.12.0_New Features:

New Features
------------

- The pass :class:`qiskit.transpiler.passes.CSPLayout` was extended with two
  new parameters: ``call_limit`` and ``time_limit``. These options allow
  limiting how long the pass will run. The option ``call_limit`` limits the
  number of times that the recursive function in the backtracking solver may
  be called. Similarly, ``time_limit`` limits how long (in seconds) the solver
  will be allowed to run. The defaults are ``1000`` calls and ``10`` seconds
  respectively.

- :class:`qiskit.pulse.Acquire` can now be applied to a single qubit.
  This makes pulse programming more consistent and easier to reason
  about, as now all operations apply to a single channel.
  For example::

    acquire = Acquire(duration=10)
    schedule = Schedule()
    schedule.insert(60, acquire(AcquireChannel(0), MemorySlot(0), RegisterSlot(0)))
    schedule.insert(60, acquire(AcquireChannel(1), MemorySlot(1), RegisterSlot(1)))

- A new method :meth:`qiskit.transpiler.CouplingMap.draw` was added to
  :class:`qiskit.transpiler.CouplingMap` to generate a graphviz image from
  the coupling map graph. For example:

  .. jupyter-execute::

      from qiskit.transpiler import CouplingMap

      coupling_map = CouplingMap(
          [[0, 1], [1, 0], [1, 2], [1, 3], [2, 1], [3, 1], [3, 4], [4, 3]])
      coupling_map.draw()

- Parametric pulses have been added to OpenPulse. These are pulse commands
  which are parameterized and understood by the backend. Arbitrary pulse
  shapes are still supported by the SamplePulse Command. The new supported
  pulse classes are:

    - :class:`qiskit.pulse.ConstantPulse`
    - :class:`qiskit.pulse.Drag`
    - :class:`qiskit.pulse.Gaussian`
    - :class:`qiskit.pulse.GaussianSquare`

  They can be used like any other Pulse command. An example::

      from qiskit.pulse import (Schedule, Gaussian, Drag, ConstantPulse,
                                GaussianSquare)

      sched = Schedule(name='parametric_demo')
      sched += Gaussian(duration=25, sigma=4, amp=0.5j)(DriveChannel(0))
      sched += Drag(duration=25, amp=0.1, sigma=5, beta=4)(DriveChannel(1))
      sched += ConstantPulse(duration=25, amp=0.3+0.1j)(DriveChannel(1))
      sched += GaussianSquare(duration=1500, amp=0.2, sigma=8,
                              width=140)(MeasureChannel(0)) << sched.duration

  The resulting schedule will be similar to a SamplePulse schedule built
  using :mod:`qiskit.pulse.pulse_lib`, however, waveform sampling will be
  performed by the backend. The method :meth:`qiskit.pulse.Schedule.draw`
  can still be used as usual. However, the command will be converted to a
  ``SamplePulse`` with the
  :meth:`qiskit.pulse.ParametricPulse.get_sample_pulse` method, so the
  pulse shown may not sample the continuous function the same way that the
  backend will.

  This feature can be used to construct Pulse programs for any backend, but
  the pulses will be converted to ``SamplePulse`` objects if the backend does
  not support parametric pulses. Backends which support them will have the
  following new attribute::

      backend.configuration().parametric_pulses: List[str]
      # e.g. ['gaussian', 'drag', 'constant']

  Note that the backend does not need to support all of the parametric
  pulses defined in Qiskit.

  When the backend supports parametric pulses, and the Pulse schedule is
  built with them, the assembled Qobj is significantly smaller. The size
  of a PulseQobj built entirely with parametric pulses is dependent only
  on the number of instructions, whereas the size of a PulseQobj built
  otherwise will grow with the duration of the instructions (since every
  sample must be specified with a value).

- Added utility functions, :func:`qiskit.scheduler.measure` and
  :func:`qiskit.scheduler.measure_all` to `qiskit.scheduler` module. These
  functions return a :class:`qiskit.pulse.Schedule` object which measures
  qubits using OpenPulse. For example::

      from qiskit.scheduler import measure, measure_all

      measure_q0_schedule = measure(qubits=[0], backend=backend)
      measure_all_schedule = measure_all(backend)
      measure_custom_schedule = measure(qubits=[0],
                                        inst_map=backend.defaults().instruction_schedule_map,
                                        meas_map=[[0]],
                                        qubit_mem_slots={0: 1})

- Pulse :class:`qiskit.pulse.Schedule` objects now have better
  representations that for simple schedules should be valid Python
  expressions.

  for example:

  .. jupyter-execute::

      from qiskit import pulse

      sched = pulse.Schedule(name='test')
      sched += pulse.SamplePulse(
          [0., 0,], name='test_pulse')(pulse.DriveChannel(0))
      sched += pulse.FrameChange(1.0)(pulse.DriveChannel(0))
      print(sched)

- The :class:`qiskit.circuit.QuantumCircuit` methods
  :meth:`qiskit.circuit.QuantumCircuit.measure_active`,
  :meth:`qiskit.circuit.QuantumCircuit.measure_all`, and
  :meth:`qiskit.circuit.QuantumCircuit.remove_final_measurements` now have
  an addition kwarg ``inplace``. When ``inplace`` is set to ``False`` the
  function will return a modified **copy** of the circuit. This is different
  from the default behavior which will modify the circuit object in-place and
  return nothing.

- Several new constructor methods were added to the
  :class:`qiskit.transpiler.CouplingMap` class for building objects
  with basic qubit coupling graphs. The new constructor methods are:

    - :meth:`qiskit.transpiler.CouplingMap.from_full`
    - :meth:`qiskit.transpiler.CouplingMap.from_line`
    - :meth:`qiskit.transpiler.CouplingMap.from_ring`
    - :meth:`qiskit.transpiler.CouplingMap.from_grid`

  For example, to use the new constructors to get a coupling map of 5
  qubits connected in a linear chain you can now run:

  .. jupyter-execute::

      from qiskit.transpiler import CouplingMap

      coupling_map = CouplingMap.from_line(5)
      coupling_map.draw()

- Introduced a new pass
  :class:`qiskit.transpiler.passes.CrosstalkAdaptiveSchedule`. This
  pass aims to reduce the impact of crosstalk noise on a program. It
  uses crosstalk characterization data from the backend to schedule gates.
  When a pair of gates has high crosstalk, they get serialized using a
  barrier. Naive serialization is harmful because it incurs decoherence
  errors. Hence, this pass uses a SMT optimization approach to compute a
  schedule which minimizes the impact of crosstalk as well as decoherence
  errors.

  The pass takes as input a circuit which is already transpiled onto
  the backend i.e., the circuit is expressed in terms of physical qubits and
  swap gates have been inserted and decomposed into CNOTs if required. Using
  this circuit and crosstalk characterization data, a
  `Z3 optimization <https://github.com/Z3Prover/z3>`_ is used to construct a
  new scheduled circuit as output.

  To use the pass on a circuit circ::

    dag = circuit_to_dag(circ)
    pass_ = CrosstalkAdaptiveSchedule(backend_prop, crosstalk_prop)
    scheduled_dag = pass_.run(dag)
    scheduled_circ = dag_to_circuit(scheduled_dag)

  ``backend_prop`` is a :class:`qiskit.providers.models.BackendProperties`
  object for the target backend. ``crosstalk_prop`` is a dict which specifies
  conditional error rates. For two gates ``g1`` and ``g2``,
  ``crosstalk_prop[g1][g2]`` specifies the conditional error rate of ``g1``
  when ``g1`` and ``g2`` are executed simultaneously. A method for generating
  ``crosstalk_prop`` will be added in a future release of qiskit-ignis. Until
  then you'll either have to already know the crosstalk properties of your
  device, or manually write your own device characterization experiments.

- In the preset pass manager for optimization level 1,
  :func:`qiskit.transpiler.preset_passmanagers.level_1_pass_manager` if
  :class:`qiskit.transpiler.passes.TrivialLayout` layout pass is not a
  perfect match for a particular circuit, then
  :class:`qiskit.transpiler.passes.DenseLayout` layout pass is used
  instead.

- Added a new abstract method
  :meth:`qiskit.quantum_info.Operator.dot` to
  the abstract ``BaseOperator`` class, so it is included for all
  implementations of that abstract
  class, including :class:`qiskit.quantum_info.Operator` and
  ``QuantumChannel`` (e.g., :class:`qiskit.quantum_info.Choi`)
  objects. This method returns the right operator multiplication
  ``a.dot(b)`` :math:`= a \cdot b`. This is equivalent to
  calling the operator
  :meth:`qiskit.quantum_info.Operator.compose` method with the kwarg
  ``front`` set to ``True``.

- Added :func:`qiskit.quantum_info.average_gate_fidelity` and
  :func:`qiskit.quantum_info.gate_error` functions to the
  :mod:`qiskit.quantum_info` module for working with
  :class:`qiskit.quantum_info.Operator` and ``QuantumChannel``
  (e.g., :class:`qiskit.quantum_info.Choi`) objects.

- Added the :func:`qiskit.quantum_info.partial_trace` function to the
  :mod:`qiskit.quantum_info` that works with
  :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` quantum state classes.
  For example::

      from qiskit.quantum_info.states import Statevector
      from qiskit.quantum_info.states import DensityMatrix
      from qiskit.quantum_info.states import partial_trace

      psi = Statevector.from_label('10+')
      partial_trace(psi, [0, 1])
      rho = DensityMatrix.from_label('10+')
      partial_trace(rho, [0, 1])

- When :meth:`qiskit.circuit.QuantumCircuit.draw` or
  :func:`qiskit.visualization.circuit_drawer` is called with the
  ``with_layout`` kwarg set True (the default) the output visualization
  will now display the physical qubits as integers to clearly
  distinguish them from the virtual qubits.

  For Example:

  .. jupyter-execute::

      from qiskit import QuantumCircuit
      from qiskit import transpile
      from qiskit.test.mock import FakeVigo

      qc = QuantumCircuit(3)
      qc.h(0)
      qc.cx(0, 1)
      qc.cx(0, 2)
      transpiled_qc = transpile(qc, FakeVigo())
      transpiled_qc.draw(output='mpl')

- Added new state measure functions to the :mod:`qiskit.quantum_info`
  module: :func:`qiskit.quantum_info.entropy`,
  :func:`qiskit.quantum_info.mutual_information`,
  :func:`qiskit.quantum_info.concurrence`, and
  :func:`qiskit.quantum_info.entanglement_of_formation`. These functions work
  with the :class:`qiskit.quantum_info.Statevector` and
  :class:`qiskit.quantum_info.DensityMatrix` classes.

- The decomposition methods for single-qubit gates in
  :class:`qiskit.quantum_info.synthesis.one_qubit_decompose.OneQubitEulerDecomposer` have
  been expanded to now also include the ``'ZXZ'`` basis, characterized by three rotations
  about the  Z,X,Z axis. This now means that a general 2x2 Operator can be
  decomposed into following bases: ``U3``, ``U1X``, ``ZYZ``, ``ZXZ``,
  ``XYX``, ``ZXZ``.


.. _Release Notes_0.12.0_Known Issues:

Known Issues
------------

- Running functions that use :func:`qiskit.tools.parallel_map` (for example
  :func:`qiskit.execute.execute`, :func:`qiskit.compiler.transpile`, and
  :meth:`qiskit.transpiler.PassManager.run`) may not work when
  called from a script running outside of a ``if __name__ == '__main__':``
  block when using Python 3.8 on MacOS. Other environments are unaffected by
  this issue. This is due to changes in how parallel processes are launched
  by Python 3.8 on MacOS. If ``RuntimeError`` or ``AttributeError`` are
  raised by scripts that are directly calling ``parallel_map()`` or when
  calling a function that uses it internally with Python 3.8 on MacOS
  embedding the script calls inside ``if __name__ == '__main__':`` should
  workaround the issue. For example::

      from qiskit import QuantumCircuit, QiskitError
      from qiskit import execute, BasicAer

      qc1 = QuantumCircuit(2, 2)
      qc1.h(0)
      qc1.cx(0, 1)
      qc1.measure([0,1], [0,1])
      # making another circuit: superpositions
      qc2 = QuantumCircuit(2, 2)
      qc2.h([0,1])
      qc2.measure([0,1], [0,1])
      execute([qc1, qc2], BasicAer.get_backend('qasm_simulator'))

  should be changed to::

      from qiskit import QuantumCircuit, QiskitError
      from qiskit import execute, BasicAer

      def main():
          qc1 = QuantumCircuit(2, 2)
          qc1.h(0)
          qc1.cx(0, 1)
          qc1.measure([0,1], [0,1])
          # making another circuit: superpositions
          qc2 = QuantumCircuit(2, 2)
          qc2.h([0,1])
          qc2.measure([0,1], [0,1])
          execute([qc1, qc2], BasicAer.get_backend('qasm_simulator'))

      if __name__ == '__main__':
          main()

  if errors are encountered with Python 3.8 on MacOS.


.. _Release Notes_0.12.0_Upgrade Notes:

Upgrade Notes
-------------

- The value of the ``rep_time`` parameter for Pulse backend's configuration
  object is now in units of seconds, not microseconds. The first time a
  ``PulseBackendConfiguration`` object is initialized it will raise a single
  warning to the user to indicate this.

- The ``rep_time`` argument for :func:`qiskit.compiler.assemble` now takes
  in a value in units of seconds, not microseconds. This was done to make
  the units with everything else in pulse. If you were passing in a value for
  ``rep_time`` ensure that you update the value to account for this change.

- The value of the ``base_gate`` property of
  :class:`qiskit.circuit.ControlledGate` objects has been changed from the
  class of the base gate to an instance of the class of the base gate.

- The ``base_gate_name`` property of :class:`qiskit.circuit.ControlledGate`
  has been removed; you can get the name of the base gate by accessing
  ``base_gate.name`` on the object. For example::

      from qiskit import QuantumCircuit
      from qiskit.extensions import HGate

      qc = QuantumCircuit(3)
      cch_gate = HGate().control(2)
      base_gate_name = cch_gate.base_gate.name

- Changed :class:`qiskit.quantum_info.Operator` magic methods so that
  ``__mul__`` (which gets executed by python's multiplication operation,
  if the left hand side of the operation has it defined) implements right
  matrix multiplication (i.e. :meth:`qiskit.quantum_info.Operator.dot`), and
  ``__rmul__`` (which gets executed by python's multiplication operation
  from the right hand side of the operation if the left does not have
  ``__mul__`` defined) implements scalar multiplication (i.e.
  :meth:`qiskit.quantum_info.Operator.multiply`). Previously both methods
  implemented scalar multiplciation.

- The second argument of the :func:`qiskit.quantum_info.process_fidelity`
  function, ``target``, is now optional. If a target unitary is not
  specified, then process fidelity of the input channel with the identity
  operator will be returned.

- :func:`qiskit.compiler.assemble` will now respect the configured
  ``max_shots`` value for a backend. If a value for the ``shots`` kwarg is
  specified that exceed the max shots set in the backend configuration the
  function will now raise a ``QiskitError`` exception. Additionally, if no
  shots argument is provided the default value is either 1024 (the previous
  behavior) or ``max_shots`` from the backend, whichever is lower.


.. _Release Notes_0.12.0_Deprecation Notes:

Deprecation Notes
-----------------

- Methods for adding gates to a :class:`qiskit.circuit.QuantumCircuit` with
  abbreviated keyword arguments (e.g. ``ctl``, ``tgt``) have had their keyword
  arguments renamed to be more descriptive (e.g. ``control_qubit``,
  ``target_qubit``). The old names have been deprecated. A table including the
  old and new calling signatures for the ``QuantumCircuit`` methods is included below.

  .. list-table:: New signatures for ``QuantumCircuit`` gate methods
     :header-rows: 1

     * - Instruction Type
       - Former Signature
       - New Signature
     * - :class:`qiskit.extensions.HGate`
       - ``qc.h(q)``
       - ``qc.h(qubit)``
     * - :class:`qiskit.extensions.CHGate`
       - ``qc.ch(ctl, tgt)``
       - ``qc.ch((control_qubit, target_qubit))``
     * - :class:`qiskit.extensions.IdGate`
       - ``qc.iden(q)``
       - ``qc.iden(qubit)``
     * - :class:`qiskit.extensions.RGate`
       - ``qc.iden(q)``
       - ``qc.iden(qubit)``
     * - :class:`qiskit.extensions.RGate`
       - ``qc.r(theta, phi, q)``
       - ``qc.r(theta, phi, qubit)``
     * - :class:`qiskit.extensions.RXGate`
       - ``qc.rx(theta, q)``
       - ``qc.rx(theta, qubit)``
     * - :class:`qiskit.extensions.CrxGate`
       - ``qc.crx(theta, ctl, tgt)``
       - ``qc.crx(theta, control_qubit, target_qubit)``
     * - :class:`qiskit.extensions.RYGate`
       - ``qc.ry(theta, q)``
       - ``qc.ry(theta, qubit)``
     * - :class:`qiskit.extensions.CryGate`
       - ``qc.cry(theta, ctl, tgt)``
       - ``qc.cry(theta, control_qubit, target_qubit)``
     * - :class:`qiskit.extensions.RZGate`
       - ``qc.rz(phi, q)``
       - ``qc.rz(phi, qubit)``
     * - :class:`qiskit.extensions.CrzGate`
       - ``qc.crz(theta, ctl, tgt)``
       - ``qc.crz(theta, control_qubit, target_qubit)``
     * - :class:`qiskit.extensions.SGate`
       - ``qc.s(q)``
       - ``qc.s(qubit)``
     * - :class:`qiskit.extensions.SdgGate`
       - ``qc.sdg(q)``
       - ``qc.sdg(qubit)``
     * - :class:`qiskit.extensions.FredkinGate`
       - ``qc.cswap(ctl, tgt1, tgt2)``
       - ``qc.cswap(control_qubit, target_qubit1, target_qubit2)``
     * - :class:`qiskit.extensions.TGate`
       - ``qc.t(q)``
       - ``qc.t(qubit)``
     * - :class:`qiskit.extensions.TdgGate`
       - ``qc.tdg(q)``
       - ``qc.tdg(qubit)``
     * - :class:`qiskit.extensions.U1Gate`
       - ``qc.u1(theta, q)``
       - ``qc.u1(theta, qubit)``
     * - :class:`qiskit.extensions.Cu1Gate`
       - ``qc.cu1(theta, ctl, tgt)``
       - ``qc.cu1(theta, control_qubit, target_qubit)``
     * - :class:`qiskit.extensions.U2Gate`
       - ``qc.u2(phi, lam, q)``
       - ``qc.u2(phi, lam, qubit)``
     * - :class:`qiskit.extensions.U3Gate`
       - ``qc.u3(theta, phi, lam, q)``
       - ``qc.u3(theta, phi, lam, qubit)``
     * - :class:`qiskit.extensions.Cu3Gate`
       - ``qc.cu3(theta, phi, lam, ctl, tgt)``
       - ``qc.cu3(theta, phi, lam, control_qubit, target_qubit)``
     * - :class:`qiskit.extensions.XGate`
       - ``qc.x(q)``
       - ``qc.x(qubit)``
     * - :class:`qiskit.extensions.CnotGate`
       - ``qc.cx(ctl, tgt)``
       - ``qc.cx(control_qubit, target_qubit)``
     * - :class:`qiskit.extensions.ToffoliGate`
       - ``qc.ccx(ctl1, ctl2, tgt)``
       - ``qc.ccx(control_qubit1, control_qubit2, target_qubit)``
     * - :class:`qiskit.extensions.YGate`
       - ``qc.y(q)``
       - ``qc.y(qubit)``
     * - :class:`qiskit.extensions.CyGate`
       - ``qc.cy(ctl, tgt)``
       - ``qc.cy(control_qubit, target_qubit)``
     * - :class:`qiskit.extensions.ZGate`
       - ``qc.z(q)``
       - ``qc.z(qubit)``
     * - :class:`qiskit.extensions.CzGate`
       - ``qc.cz(ctl, tgt)``
       - ``qc.cz(control_qubit, target_qubit)``

- Running :class:`qiskit.pulse.Acquire` on multiple qubits has been
  deprecated and will be removed in a future release. Additionally, the
  :class:`qiskit.pulse.AcquireInstruction` parameters ``mem_slots`` and
  ``reg_slots`` have been deprecated. Instead ``reg_slot`` and ``mem_slot``
  should be used instead.

- The attribute of the :class:`qiskit.providers.models.PulseDefaults` class
  ``circuit_instruction_map`` has been deprecated and will be removed in a
  future release. Instead you should use the new attribute
  ``instruction_schedule_map``. This was done to match the type of the
  value of the attribute, which is an ``InstructionScheduleMap``.

- The :class:`qiskit.pulse.PersistentValue` command is deprecated and will
  be removed in a future release. Similar functionality can be achieved with
  the :class:`qiskit.pulse.ConstantPulse` command (one of the new parametric
  pulses). Compare the following::

      from qiskit.pulse import Schedule, PersistentValue, ConstantPulse, \
                               DriveChannel

      # deprecated implementation
      sched_w_pv = Schedule()
      sched_w_pv += PersistentValue(value=0.5)(DriveChannel(0))
      sched_w_pv += PersistentValue(value=0)(DriveChannel(0)) << 10

      # preferred implementation
      sched_w_const = Schedule()
      sched_w_const += ConstantPulse(duration=10, amp=0.5)(DriveChannel(0))

- Python 3.5 support in qiskit-terra is deprecated. Support will be
  removed in the first release after the upstream Python community's end of
  life date for the version, which is 09/13/2020.

- The ``require_cptp`` kwarg of the
  :func:`qiskit.quantum_info.process_fidelity` function has been
  deprecated and will be removed in a future release. It is superseded by
  two separate kwargs ``require_cp`` and ``require_tp``.

- Setting the ``scale`` parameter for
  :meth:`qiskit.circuit.QuantumCircuit.draw` and
  :func:`qiskit.visualization.circuit_drawer` as the first positional
  argument is deprecated and will be removed in a future release. Instead you
  should use ``scale`` as keyword argument.

- The :mod:`qiskit.tools.qi.qi` module is deprecated and will be removed in a
  future release. The legacy functions in the module have all been superseded
  by functions and classes in the :mod:`qiskit.quantum_info` module. A table
  of the deprecated functions and their replacement are below:

  .. list-table:: ``qiskit.tools.qi.qi`` replacements
     :header-rows: 1

     * - Deprecated
       - Replacement
     * - :func:`qiskit.tools.partial_trace`
       - :func:`qiskit.quantum_info.partial_trace`
     * - :func:`qiskit.tools.choi_to_pauli`
       - :class:`qiskit.quantum_info.Choi` and :class:`quantum_info.PTM`
     * - :func:`qiskit.tools.chop`
       - ``numpy.round``
     * - ``qiskit.tools.qi.qi.outer``
       - ``numpy.outer``
     * - :func:`qiskit.tools.concurrence`
       - :func:`qiskit.quantum_info.concurrence`
     * - :func:`qiskit.tools.shannon_entropy`
       - :func:`qiskit.quantum_info.shannon_entropy`
     * - :func:`qiskit.tools.entropy`
       - :func:`qiskit.quantum_info.entropy`
     * - :func:`qiskit.tools.mutual_information`
       - :func:`qiskit.quantum_info.mutual_information`
     * - :func:`qiskit.tools.entanglement_of_formation`
       - :func:`qiskit.quantum_info.entanglement_of_formation`
     * - :func:`qiskit.tools.is_pos_def`
       - ``quantum_info.operators.predicates.is_positive_semidefinite_matrix``

- The :mod:`qiskit.quantum_info.states.states` module is deprecated and will
  be removed in a future release. The legacy functions in the module have
  all been superseded by functions and classes in the
  :mod:`qiskit.quantum_info` module.

  .. list-table:: ``qiskit.quantum_info.states.states`` replacements
     :header-rows: 1

     * - Deprecated
       - Replacement
     * - ``qiskit.quantum_info.states.states.basis_state``
       - :meth:`qiskit.quantum_info.Statevector.from_label`
     * - ``qiskit.quantum_info.states.states.projector``
       - :class:`qiskit.quantum_info.DensityMatrix`

- The ``scaling`` parameter of the ``draw()`` method for the ``Schedule`` and
  ``Pulse`` objects was deprecated and will be removed in a future release.
  Instead the new ``scale`` parameter should be used. This was done to have
  a consistent argument between pulse and circuit drawings. For example::

      #The consistency in parameters is seen below
      #For circuits
      circuit = QuantumCircuit()
      circuit.draw(scale=0.2)
      #For pulses
      pulse = SamplePulse()
      pulse.draw(scale=0.2)
      #For schedules
      schedule = Schedule()
      schedule.draw(scale=0.2)


.. _Release Notes_0.12.0_Bug Fixes:

Bug Fixes
---------

- Previously, calling :meth:`qiskit.circuit.QuantumCircuit.bind_parameters`
  prior to decomposing a circuit would result in the bound values not being
  correctly substituted into the decomposed gates. This has been resolved
  such that binding and decomposition may occur in any order. Fixes
  `issue #2482 <https://github.com/Qiskit/qiskit-terra/issues/2482>`_ and
  `issue #3509 <https://github.com/Qiskit/qiskit-terra/issues/3509>`_

- The ``Collect2qBlocks`` pass had previously not considered classical
  conditions when determining whether to include a gate within an
  existing block. In some cases, this resulted in classical
  conditions being lost when transpiling with
  ``optimization_level=3``. This has been resolved so that classically
  conditioned gates are never included in a block.
  Fixes `issue #3215 <https://github.com/Qiskit/qiskit-terra/issues/3215>`_

- All the output types for the circuit drawers in
  :meth:`qiskit.circuit.QuantumCircuit.draw` and
  :func:`qiskit.visualization.circuit_drawer` have fixed and/or improved
  support for drawing controlled custom gates. Fixes
  `issue #3546 <https://github.com/Qiskit/qiskit-terra/issues/3546>`_,
  `issue #3763 <https://github.com/Qiskit/qiskit-terra/issues/3763>`_,
  and `issue #3764 <https://github.com/Qiskit/qiskit-terra/issues/3764>`_

- Explanation and examples have been added to documentation for the
  :class:`qiskit.circuit.QuantumCircuit` methods for adding gates:
  :meth:`qiskit.circuit.QuantumCircuit.ccx`,
  :meth:`qiskit.circuit.QuantumCircuit.ch`,
  :meth:`qiskit.circuit.QuantumCircuit.crz`,
  :meth:`qiskit.circuit.QuantumCircuit.cswap`,
  :meth:`qiskit.circuit.QuantumCircuit.cu1`,
  :meth:`qiskit.circuit.QuantumCircuit.cu3`,
  :meth:`qiskit.circuit.QuantumCircuit.cx`,
  :meth:`qiskit.circuit.QuantumCircuit.cy`,
  :meth:`qiskit.circuit.QuantumCircuit.cz`,
  :meth:`qiskit.circuit.QuantumCircuit.h`,
  :meth:`qiskit.circuit.QuantumCircuit.iden`,
  :meth:`qiskit.circuit.QuantumCircuit.rx`,
  :meth:`qiskit.circuit.QuantumCircuit.ry`,
  :meth:`qiskit.circuit.QuantumCircuit.rz`,
  :meth:`qiskit.circuit.QuantumCircuit.s`,
  :meth:`qiskit.circuit.QuantumCircuit.sdg`,
  :meth:`qiskit.circuit.QuantumCircuit.swap`,
  :meth:`qiskit.circuit.QuantumCircuit.t`,
  :meth:`qiskit.circuit.QuantumCircuit.tdg`,
  :meth:`qiskit.circuit.QuantumCircuit.u1`,
  :meth:`qiskit.circuit.QuantumCircuit.u2`,
  :meth:`qiskit.circuit.QuantumCircuit.u3`,
  :meth:`qiskit.circuit.QuantumCircuit.x`,
  :meth:`qiskit.circuit.QuantumCircuit.y`,
  :meth:`qiskit.circuit.QuantumCircuit.z`. Fixes
  `issue #3400 <https://github.com/Qiskit/qiskit-terra/issues/3400>`_

- Fixes for handling of complex number parameter in circuit visualization.
  Fixes `issue #3640 <https://github.com/Qiskit/qiskit-terra/issues/3640>`_


.. _Release Notes_0.12.0_Other Notes:

Other Notes
-----------

- The transpiler passes in the :mod:`qiskit.transpiler.passes` directory have
  been organized into subdirectories to better categorize them by
  functionality. They are still all accessible under the
  ``qiskit.transpiler.passes`` namespace.

Aer 0.4.0
=========

Added
-----
 * Added ``NoiseModel.from_backend`` for building a basic device noise model for an IBMQ
   backend (\#569)
 * Added multi-GPU enabled simulation methods to the ``QasmSimulator``,
   ``StatevectorSimulator``, and ``UnitarySimulator``. The qasm simulator has gpu version
   of the density matrix and statevector methods and can be accessed using
   ``"method": "density_matrix_gpu"`` or ``"method": "statevector_gpu"`` in ``backend_options``.
   The statevector simulator gpu method can be accessed using ``"method": "statevector_gpu"``.
   The unitary simulator GPU method can be accessed using ``"method": "unitary_gpu"``. These
   backends use CUDA and require an NVidia GPU.(\#544)
 * Added ``PulseSimulator`` backend (\#542)
 * Added ``PulseSystemModel`` and ``HamiltonianModel`` classes to represent models to be used
   in ``PulseSimulator`` (\#496, \#493)
 * Added ``duffing_model_generators`` to generate ``PulseSystemModel`` objects from a list
   of parameters (\#516)
 * Migrated ODE function solver to C++ (\#442, \#350)
 * Added high level pulse simulator tests (\#379)
 * CMake BLAS_LIB_PATH flag to set path to look for BLAS lib (\#543)

Changed
-------

 * Changed the structure of the ``src`` directory to organise simulator source code.
   Simulator controller headers were moved to ``src/controllers`` and simulator method State
   headers are in ``src/simulators`` (\#544)
 * Moved the location of several functions (\#568):
   * Moved contents of ``qiskit.provider.aer.noise.errors`` into
   the ``qiskit.providers.noise`` module
   * Moved contents of ``qiskit.provider.aer.noise.utils`` into
   the ``qiskit.provider.aer.utils`` module.
 * Enabled optimization to aggregate consecutive gates in a circuit (fusion) by default (\#579).

Deprecated
----------
 * Deprecated ``utils.qobj_utils`` functions (\#568)
 * Deprecated ``qiskit.providers.aer.noise.device.basic_device_noise_model``. It is superseded
   by the ``NoiseModel.from_backend`` method (\#569)

Removed
-------
 * Removed ``NoiseModel.as_dict``, ``QuantumError.as_dict``, ``ReadoutError.as_dict``, and
   ``QuantumError.kron`` methods that were deprecated in 0.3 (\#568).

Ignis 0.2
=========

No Change

Aqua 0.6
========

No Change

IBM Q Provider 0.4.6
====================

Added
-----

- Several new methods were added to
  :class:`IBMQBackend<qiskit.providers.ibmq.ibmqbackend.IBMQBackend>`:

    * :meth:`~qiskit.providers.ibmq.job.IBMQJob.wait_for_final_state`
      blocks until the job finishes. It takes a callback function that it will invoke
      after every query to provide feedback.
    * :meth:`~qiskit.providers.ibmq.ibmqbackend.IBMQBackend.active_jobs` returns
      the jobs submitted to a backend that are currently in an unfinished status.
    * :meth:`~qiskit.providers.ibmq.ibmqbackend.IBMQBackend.job_limit` returns the
      job limit for a backend.
    * :meth:`~qiskit.providers.ibmq.ibmqbackend.IBMQBackend.remaining_jobs_count` returns the
      number of jobs that you can submit to the backend before job limit is reached.

- :class:`~qiskit.providers.ibmq.job.QueueInfo` now has a new
  :meth:`~qiskit.providers.ibmq.job.QueueInfo.format` method that returns a
  formatted string of the queue information.

- :class:`IBMQJob<qiskit.providers.ibmq.job.IBMQJob>` now has three new methods:
  :meth:`~qiskit.providers.ibmq.job.IBMQJob.done`,
  :meth:`~qiskit.providers.ibmq.job.IBMQJob.running`, and
  :meth:`~qiskit.providers.ibmq.job.IBMQJob.cancelled` that are used to indicate job status.

- :meth:`qiskit.providers.ibmq.ibmqbackend.IBMQBackend.run()` now accepts an optional `job_tags`
  parameter. If specified, the `job_tags` are assigned to the job, which can later be used
  as a filter in :meth:`qiskit.providers.ibmq.ibmqbackend.IBMQBackend.jobs()`.

- :class:`~qiskit.providers.ibmq.managed.IBMQJobManager` now has a new method
  :meth:`~qiskit.providers.ibmq.managed.IBMQJobManager.retrieve_job_set()` that allows
  you to retrieve a previously submitted job set using the job set ID.

Changed
-------

- The ``Exception`` hierarchy has been refined with more specialized classes.
  You can, however, continue to catch their parent exceptions (such
  as ``IBMQAccountError``). Also, the exception class ``IBMQApiUrlError``
  has been replaced by ``IBMQAccountCredentialsInvalidUrl`` and
  ``IBMQAccountCredentialsInvalidToken``.

Deprecated
----------

- The use of proxy urls without a protocol (e.g. ``http://``) is deprecated
  due to recent Python changes.

*************
Qiskit 0.14.0
*************

Terra 0.11.0
============

.. _Release Notes_0.11.0_Prelude:

Prelude
-------

The 0.11.0 release includes several new features and bug fixes. The biggest
change for this release is the addition of the pulse scheduler. This allows
users to define their quantum program as a ``QuantumCircuit`` and then map it
to the underlying pulse instructions that will control the quantum hardware to
implement the circuit.

.. _Release Notes_0.11.0_New Features:

New Features
------------

- Added 5 new commands to easily retrieve user-specific data from
  ``BackendProperties``: ``gate_property``, ``gate_error``, ``gate_length``,
  ``qubit_property``, ``t1``, ``t2``, ``readout_error`` and ``frequency``.
  They return the specific values of backend properties. For example::

    from qiskit.test.mock import FakeOurense
    backend = FakeOurense()
    properties = backend.properties()

    gate_property = properties.gate_property('u1')
    gate_error = properties.gate_error('u1', 0)
    gate_length = properties.gate_length('u1', 0)
    qubit_0_property = properties.qubit_property(0)
    t1_time_0 = properties.t1(0)
    t2_time_0 = properties.t2(0)
    readout_error_0 = properties.readout_error(0)
    frequency_0 = properties.frequency(0)

- Added method ``Instruction.is_parameterized()`` to check if an instruction
  object is parameterized. This method returns ``True`` if and only if
  instruction has a ``ParameterExpression`` or ``Parameter`` object for one
  of its params.

- Added a new analysis pass ``Layout2qDistance``. This pass allows to "score"
  a layout selection, once ``property_set['layout']`` is set.  The score will
  be the sum of distances for each two-qubit gate in the circuit, when they
  are not directly connected. This scoring does not consider direction in the
  coupling map. The lower the number, the better the layout selection is.

  For example, consider a linear coupling map ``[0]--[2]--[1]`` and the
  following circuit::

      qr = QuantumRegister(2, 'qr')
      circuit = QuantumCircuit(qr)
      circuit.cx(qr[0], qr[1])

  If the layout is ``{qr[0]:0, qr[1]:1}``, ``Layout2qDistance`` will set
  ``property_set['layout_score'] = 1``. If the layout
  is ``{qr[0]:0, qr[1]:2}``, then the result
  is ``property_set['layout_score'] = 0``. The lower the score, the better.

- Added ``qiskit.QuantumCircuit.cnot`` as an alias for the ``cx`` method of
  ``QuantumCircuit``. The names ``cnot`` and ``cx`` are often used
  interchangeably now the `cx` method can be called with either name.

- Added ``qiskit.QuantumCircuit.toffoli`` as an alias for the ``ccx`` method
  of ``QuantumCircuit``. The names ``toffoli`` and ``ccx`` are often used
  interchangeably now the `ccx` method can be called with either name.

- Added ``qiskit.QuantumCircuit.fredkin`` as an alias for the ``cswap``
  method of ``QuantumCircuit``. The names ``fredkin`` and ``cswap`` are
  often used interchangeably now the `cswap` method can be called with
  either name.

- The ``latex`` output mode for ``qiskit.visualization.circuit_drawer()`` and
  the ``qiskit.circuit.QuantumCircuit.draw()`` method now has a mode to
  passthrough raw latex from gate labels and parameters. The syntax
  for doing this mirrors matplotlib's
  `mathtext mode <https://matplotlib.org/tutorials/text/mathtext.html>`__
  syntax. Any portion of a label string between a pair of '$' characters will
  be treated as raw latex and passed directly into the generated output latex.
  This can be leveraged to add more advanced formatting to circuit diagrams
  generated with the latex drawer.

  Prior to this release all gate labels were run through a utf8 -> latex
  conversion to make sure that the output latex would compile the string as
  expected. This is still what happens for all portions of a label outside
  the '$' pair. Also if you want to use a dollar sign in your label make sure
  you escape it in the label string (ie ``'\$'``).

  You can mix and match this passthrough with the utf8 -> latex conversion to
  create the exact label you want, for example::

      from qiskit import circuit
      circ = circuit.QuantumCircuit(2)
      circ.h([0, 1])
      circ.append(circuit.Gate(name='α_gate', num_qubits=1, params=[0]), [0])
      circ.append(circuit.Gate(name='α_gate$_2$', num_qubits=1, params=[0]), [1])
      circ.append(circuit.Gate(name='\$α\$_gate', num_qubits=1, params=[0]), [1])
      circ.draw(output='latex')

  will now render the first custom gate's label as ``α_gate``, the second
  will be ``α_gate`` with a 2 subscript, and the last custom gate's label
  will be ``$α$_gate``.

- Add ``ControlledGate`` class for representing controlled
  gates. Controlled gate instances are created with the
  ``control(n)`` method of ``Gate`` objects where ``n`` represents
  the number of controls. The control qubits come before the
  controlled qubits in the new gate. For example::

    from qiskit import QuantumCircuit
    from qiskit.extensions import HGate
    hgate = HGate()
    circ = QuantumCircuit(4)
    circ.append(hgate.control(3), [0, 1, 2, 3])
    print(circ)

  generates::

    q_0: |0>──■──
              │
    q_1: |0>──■──
              │
    q_2: |0>──■──
            ┌─┴─┐
    q_3: |0>┤ H ├
            └───┘

- Allowed values of ``meas_level`` parameters and fields can now be a member
  from the `IntEnum` class ``qiskit.qobj.utils.MeasLevel``. This can be used
  when calling ``execute`` (or anywhere else ``meas_level`` is specified) with
  a pulse experiment. For example::

    from qiskit import QuantumCircuit, transpile, schedule, execute
    from qiskit.test.mock import FakeOpenPulse2Q
    from qiskit.qobj.utils import MeasLevel, MeasReturnType

    backend = FakeOpenPulse2Q()
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0,1)
    qc_transpiled = transpile(qc, backend)
    sched = schedule(qc_transpiled, backend)
    execute(sched, backend, meas_level=MeasLevel.CLASSIFIED)

  In this above example, ``meas_level=MeasLevel.CLASSIFIED`` and
  ``meas_level=2`` can be used interchangably now.

- A new layout selector based on constraint solving is included. `CSPLayout` models the problem
  of finding a layout as a constraint problem and uses recursive backtracking to solve it.

  .. code-block:: python

     cmap16 = CouplingMap(FakeRueschlikon().configuration().coupling_map)

     qr = QuantumRegister(5, 'q')
     circuit = QuantumCircuit(qr)
     circuit.cx(qr[0], qr[1])
     circuit.cx(qr[0], qr[2])
     circuit.cx(qr[0], qr[3])

     pm = PassManager(CSPLayout(cmap16))
     circuit_after = pm.run(circuit)
     print(pm.property_set['layout'])


  .. code-block:: python

      Layout({
      1: Qubit(QuantumRegister(5, 'q'), 1),
      2: Qubit(QuantumRegister(5, 'q'), 0),
      3: Qubit(QuantumRegister(5, 'q'), 3),
      4: Qubit(QuantumRegister(5, 'q'), 4),
      15: Qubit(QuantumRegister(5, 'q'), 2)
      })


  The parameter ``CSPLayout(...,strict_direction=True)`` is more restrictive
  but it will guarantee there is no need of running ``CXDirection`` after.

  .. code-block:: python

      pm = PassManager(CSPLayout(cmap16, strict_direction=True))
      circuit_after = pm.run(circuit)
      print(pm.property_set['layout'])

  .. code-block:: python

      Layout({
      8: Qubit(QuantumRegister(5, 'q'), 4),
      11: Qubit(QuantumRegister(5, 'q'), 3),
      5: Qubit(QuantumRegister(5, 'q'), 1),
      6: Qubit(QuantumRegister(5, 'q'), 0),
      7: Qubit(QuantumRegister(5, 'q'), 2)
      })

  If the constraint system is not solvable, the `layout` property is not set.

  .. code-block:: python

      circuit.cx(qr[0], qr[4])
      pm = PassManager(CSPLayout(cmap16))
      circuit_after = pm.run(circuit)
      print(pm.property_set['layout'])

  .. code-block:: python

      None

- PulseBackendConfiguration (accessed normally as backend.configuration())
  has been extended with useful methods to explore its data and the
  functionality that exists in PulseChannelSpec. PulseChannelSpec will be
  deprecated in the future. For example::

      backend = provider.get_backend(backend_name)
      config = backend.configuration()
      q0_drive = config.drive(0)  # or, DriveChannel(0)
      q0_meas = config.measure(0)  # MeasureChannel(0)
      q0_acquire = config.acquire(0)  # AcquireChannel(0)
      config.hamiltonian  # Returns a dictionary with hamiltonian info
      config.sample_rate()  # New method which returns 1 / dt

- ``PulseDefaults`` (accessed normally as ``backend.defaults()``) has an
  attribute, ``circuit_instruction_map`` which has the methods of CmdDef.
  The new `circuit_instruction_map` is an ``InstructionScheduleMap`` object
  with three new functions beyond what CmdDef had:

   * qubit_instructions(qubits) returns the operations defined for the qubits
   * assert_has(instruction, qubits) raises an error if the op isn't defined
   * remove(instruction, qubits) like pop, but doesn't require parameters

  There are some differences from the CmdDef:

   * ``__init__`` takes no arguments
   * ``cmds`` and ``cmd_qubits`` are deprecated and replaced with
     ``instructions`` and ``qubits_with_instruction``

  Example::

      backend = provider.get_backend(backend_name)
      inst_map = backend.defaults().circuit_instruction_map
      qubit = inst_map.qubits_with_instruction('u3')[0]
      x_gate = inst_map.get('u3', qubit, P0=np.pi, P1=0, P2=np.pi)
      pulse_schedule = x_gate(DriveChannel(qubit))

- A new kwarg parameter, ``show_framechange_channels`` to optionally disable
  displaying channels with only framechange instructions in pulse
  visualizations was added to the ``qiskit.visualization.pulse_drawer()``
  function and ``qiskit.pulse.Schedule.draw()`` method. When this new kwarg
  is set to ``False`` the output pulse schedule visualization will not
  include any channels that only include frame changes.

  For example:

  .. jupyter-execute::

      from qiskit.pulse import *
      from qiskit.pulse import pulse_lib

      gp0 = pulse_lib.gaussian(duration=20, amp=1.0, sigma=1.0)
      sched = Schedule()
      channel_a = DriveChannel(0)
      channel_b = DriveChannel(1)
      sched = sched.append(gp0(channel_a))
      sched = sched.insert(60, FrameChange(phase=-1.57)(channel_a))
      sched = sched.insert(0, PersistentValue(value=0.2 + 0.4j)(
          channel_a))
      sched = sched.insert(30, FrameChange(phase=-1.50)(channel_b))
      sched = sched.insert(70, FrameChange(phase=1.50)(channel_b))

      sched.draw(show_framechange_channels=False)

- A new utility function ``qiskit.result.marginal_counts()`` is added
  which allows marginalization of the counts over some indices of interest.
  This is useful when more qubits are measured than needed, and one wishes
  to get the observation counts for some subset of them only.

- When ``passmanager.run(...)`` is invoked with more than one circuit, the
  transpilation of these circuits will run in parallel.

- PassManagers can now be sliced to create a new PassManager containing a
  subset of passes using the square bracket operator. This allow running or
  drawing a portion of the PassManager for easier testing and visualization.
  For example let's try to draw the first 3 passes of a PassManager pm, or
  run just the second pass on our circuit:

  .. code-block:: python

    pm[0:4].draw()
    circuit2 = pm[1].run(circuit)

  Also now, PassManagers can be created by adding two PassManagers or by
  directly adding a pass/list of passes to a PassManager.

  .. code-block:: python

    pm = pm1[0] + pm2[1:3]
    pm += [setLayout, unroller]

- A basic ``scheduler`` module has now been added to Qiskit. The `scheduler`
  schedules an input transpiled ``QuantumCircuit`` into a pulse
  ``Schedule``. The scheduler accepts as input a ``Schedule`` and either a
  pulse ``Backend``, or a ``CmdDef`` which relates circuit ``Instruction``
  objects on specific qubits to pulse Schedules and a ``meas_map`` which
  determines which measurements must occur together.

  Scheduling example::

    from qiskit import QuantumCircuit, transpile, schedule
    from qiskit.test.mock import FakeOpenPulse2Q

    backend = FakeOpenPulse2Q()
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0,1)
    qc_transpiled = transpile(qc, backend)
    schedule(qc_transpiled, backend)

  The scheduler currently supports two scheduling policies,
  `as_late_as_possible` (``alap``) and `as_soon_as_possible` (``asap``), which
  respectively schedule pulse instructions to occur as late as
  possible or as soon as possible across qubits in a circuit.
  The scheduling policy may be selected with the input argument ``method``,
  for example::

    schedule(qc_transpiled, backend, method='alap')

  It is easy to use a pulse ``Schedule`` within a ``QuantumCircuit`` by
  mapping it to a custom circuit instruction such as a gate which may be used
  in a ``QuantumCircuit``. To do this, first, define the custom gate and then
  add an entry into the ``CmdDef`` for the gate, for each qubit that the gate
  will be applied to. The gate can then be used in the ``QuantumCircuit``.
  At scheduling time the gate will be mapped to the underlying pulse schedule.
  Using this technique allows easy integration with preexisting qiskit modules
  such as Ignis.

  For example::

      from qiskit import pulse, circuit, schedule
      from qiskit.pulse import pulse_lib

      custom_cmd_def = pulse.CmdDef()

      # create custom gate
      custom_gate = circuit.Gate(name='custom_gate', num_qubits=1, params=[])

      # define schedule for custom gate
      custom_schedule = pulse.Schedule()
      custom_schedule += pulse_lib.gaussian(20, 1.0, 10)(pulse.DriveChannel)

      # add schedule to custom gate with same name
      custom_cmd_def.add('custom_gate', (0,), custom_schedule)

      # use custom gate in a circuit
      custom_qc = circuit.QuantumCircuit(1)
      custom_qc.append(custom_gate, qargs=[0])

      # schedule the custom gate
      schedule(custom_qc, cmd_def=custom_cmd_def, meas_map=[[0]])


.. _Release Notes_0.11.0_Known Issues:

Known Issues
------------

- The feature for transpiling in parallel when ``passmanager.run(...)`` is
  invoked with more than one circuit is not supported under Windows. See
  `#2988 <https://github.com/Qiskit/qiskit-terra/issues/2988>`__ for more
  details.


.. _Release Notes_0.11.0_Upgrade Notes:

Upgrade Notes
-------------

- The ``qiskit.pulse.channels.SystemTopology`` class was used as a helper
  class for ``PulseChannelSpec``. It has been removed since with the deprecation
  of ``PulseChannelSpec`` and changes to ``BackendConfiguration`` make it
  unnecessary.

- The previously deprecated representation of qubits and classical bits as
  tuple, which was deprecated in the 0.9 release, has been removed. The use
  of ``Qubit`` and ``Clbit`` objects is the new way to represent qubits and
  classical bits.

- The previously deprecated representation of the basis set as single string
  has been removed. A list of strings is the new preferred way.

- The method ``BaseModel.as_dict``, which was deprecated in the 0.9 release,
  has been removed in favor of the method ``BaseModel.to_dict``.

- In PulseDefaults (accessed normally as backend.defaults()),
  ``qubit_freq_est`` and ``meas_freq_est`` are now returned in Hz rather than
  GHz. This means the new return values are 1e9 * their previous value.

- `dill <https://pypi.org/project/dill/>`__ was added as a requirement. This
  is needed to enable running ``passmanager.run()`` in parallel for more than
  one circuit.

- The previously deprecated gate ``UBase``, which was deprecated
  in the 0.9 release, has been removed. The gate ``U3Gate``
  should be used instead.

- The previously deprecated gate ``CXBase``, which was deprecated
  in the 0.9 release, has been removed. The gate ``CnotGate``
  should be used instead.

- The instruction ``snapshot`` used to implicitly convert the ``label``
  parameter to string. That conversion has been removed and an error is raised
  if a string is not provided.

- The previously deprecated gate ``U0Gate``, which was deprecated
  in the 0.9 release, has been removed. The gate ``IdGate``
  should be used instead to insert delays.


.. _Release Notes_0.11.0_Deprecation Notes:

Deprecation Notes
-----------------

- The ``qiskit.pulse.CmdDef`` class has been deprecated. Instead you should
  use the ``qiskit.pulse.InstructionScheduleMap``. The
  ``InstructionScheduleMap`` object for a pulse enabled system can be
  accessed at ``backend.defaults().instruction_schedules``.

- ``PulseChannelSpec`` is being deprecated. Use ``BackendConfiguration``
  instead. The backend configuration is accessed normally as
  ``backend.configuration()``. The config has been extended with most of
  the functionality of PulseChannelSpec, with some modifications as follows,
  where `0` is an exemplary qubit index::

      pulse_spec.drives[0]   -> config.drive(0)
      pulse_spec.measures[0] -> config.measure(0)
      pulse_spec.acquires[0] -> config.acquire(0)
      pulse_spec.controls[0] -> config.control(0)

  Now, if there is an attempt to get a channel for a qubit which does not
  exist for the device, a ``BackendConfigurationError`` will be raised with
  a helpful explanation.

  The methods ``memoryslots`` and ``registerslots`` of the PulseChannelSpec
  have not been migrated to the backend configuration. These classical
  resources are not restrained by the physical configuration of a backend
  system. Please instantiate them directly::

      pulse_spec.memoryslots[0] -> MemorySlot(0)
      pulse_spec.registerslots[0] -> RegisterSlot(0)

  The ``qubits`` method is not migrated to backend configuration. The result
  of ``qubits`` can be built as such::

      [q for q in range(backend.configuration().n_qubits)]

- ``Qubit`` within ``pulse.channels`` has been deprecated. They should not
  be used. It is possible to obtain channel <=> qubit mappings through the
  BackendConfiguration (or backend.configuration()).

- The function ``qiskit.visualization.circuit_drawer.qx_color_scheme()`` has
  been deprecated. This function is no longer used internally and doesn't
  reflect the current IBM QX style. If you were using this function to
  generate a style dict locally you must save the output from it and use
  that dictionary directly.

- The Exception ``TranspilerAccessError`` has been deprecated. An
  alternative function ``TranspilerError`` can be used instead to provide
  the same functionality. This alternative function provides the exact same
  functionality but with greater generality.

- Buffers in Pulse are deprecated. If a nonzero buffer is supplied, a warning
  will be issued with a reminder to use a Delay instead. Other options would
  include adding samples to a pulse instruction which are (0.+0.j) or setting
  the start time of the next pulse to ``schedule.duration + buffer``.

- Passing in ``sympy.Basic``, ``sympy.Expr`` and ``sympy.Matrix`` types as
  instruction parameters are deprecated and will be removed in a future
  release. You'll need to convert the input to one of the supported types
  which are:

   * ``int``
   * ``float``
   * ``complex``
   * ``str``
   * ``np.ndarray``


.. _Release Notes_0.11.0_Bug Fixes:

Bug Fixes
---------

- The Collect2qBlocks and CommutationAnalysis passes in the transpiler had been
  unable to process circuits containing Parameterized gates, preventing
  Parameterized circuits from being transpiled at optimization_level 2 or
  above. These passes have been corrected to treat Parameterized gates as
  opaque.

- The align_measures function had an issue where Measure stimulus
  pulses weren't properly aligned with Acquire pulses, resulting in
  an error. This has been fixed.

- Uses of ``numpy.random.seed`` have been removed so that calls of qiskit
  functions do not affect results of future calls to ``numpy.random``

- Fixed race condition occurring in the job monitor when
  ``job.queue_position()`` returns ``None``. ``None`` is a valid
  return from ``job.queue_position()``.

- Backend support for ``memory=True`` now checked when that kwarg is passed.
  ``QiskitError`` results if not supported.

- When transpiling without a coupling map, there were no check in the amount
  of qubits of the circuit to transpile. Now the transpile process checks
  that the backend has enough qubits to allocate the circuit.


.. _Release Notes_0.11.0_Other Notes:

Other Notes
-----------

- The ``qiskit.result.marginal_counts()`` function replaces a similar utility
  function in qiskit-ignis
  ``qiskit.ignis.verification.tomography.marginal_counts()``, which
  will be deprecated in a future qiskit-ignis release.

- All sympy parameter output type support have been been removed (or
  deprecated as noted) from qiskit-terra. This includes sympy type
  parameters in ``QuantumCircuit`` objects, qasm ast nodes, or ``Qobj``
  objects.

Aer 0.3
=======

No Change

Ignis 0.2
=========

No Change

Aqua 0.6
========

No Change

IBM Q Provider 0.4
==================

Prelude
-------

The 0.4.0 release is the first release that makes use of all the features
of the new IBM Q API. In particular, the ``IBMQJob`` class has been revamped in
order to be able to retrieve more information from IBM Q, and a Job Manager
class has been added for allowing a higher-level and more seamless usage of
large or complex jobs. If you have not upgraded from the legacy IBM Q
Experience or QConsole yet, please ensure to revisit the release notes for
IBM Q Provider 0.3 (Qiskit 0.11) for more details on how to make the
transition. The legacy accounts will no longer be supported as of this release.


New Features
------------

Job modifications
^^^^^^^^^^^^^^^^^

The ``IBMQJob`` class has been revised, and now mimics more closely to the
contents of a remote job along with new features:

* You can now assign a name to a job, by specifying
  ``IBMQBackend.run(..., job_name='...')`` when submitting a job. This name
  can be retrieved via ``IBMQJob.name()`` and can be used for filtering.
* Jobs can now be shared with other users at different levels (global, per
  hub, group or project) via an optional ``job_share_level`` parameter when
  submitting the job.
* ``IBMQJob`` instances now have more attributes, reflecting the contents of the
  remote IBM Q jobs. This implies that new attributes introduced by the IBM Q
  API will automatically and immediately be available for use (for example,
  ``job.new_api_attribute``). The new attributes will be promoted to methods
  when they are considered stable (for example, ``job.name()``).
* ``.error_message()`` returns more information on why a job failed.
* ``.queue_position()`` accepts a ``refresh`` parameter for forcing an update.
* ``.result()`` accepts an optional ``partial`` parameter, for returning
  partial results, if any, of jobs that failed. Be aware that ``Result``
  methods, such as ``get_counts()`` will raise an exception if applied on
  experiments that failed.

Please note that the changes include some low-level modifications of the class.
If you were creating the instances manually, note that:

* the signature of the constructor has changed to account for the new features.
* the ``.submit()`` method can no longer be called directly, and jobs are
  expected to be submitted either via the synchronous ``IBMQBackend.run()`` or
  via the Job Manager.

Job Manager
^^^^^^^^^^^

A new Job Manager (``IBMQJobManager``) has been introduced, as a higher-level
mechanism for handling jobs composed of multiple circuits or pulse schedules.
The Job Manager aims to provide a transparent interface, intelligently splitting
the input into efficient units of work and taking full advantage of the
different components. It will be expanded on upcoming versions, and become the
recommended entry point for job submission.

Its ``.run()`` method receives a list of circuits or pulse schedules, and
returns a ``ManagedJobSet instance``, which can then be used to track the
statuses and results of these jobs. For example::

    from qiskit.providers.ibmq.managed import IBMQJobManager
    from qiskit.circuit.random import random_circuit
    from qiskit import IBMQ
    from qiskit.compiler import transpile

    provider = IBMQ.load_account()
    backend = provider.backends.ibmq_ourense

    circs = []
    for _ in range(1000000):
        circs.append(random_circuit(2, 2))
    transpile(circs, backend=backend)

    # Farm out the jobs.
    jm = IBMQJobManager()
    job_set = jm.run(circs, backend=backend, name='foo')

    job_set.statuses()    # Gives a list of job statuses
    job_set.report()    # Prints detailed job information
    results = job_set.results()
    counts = results.get_counts(5)   # Returns data for experiment 5


provider.backends modifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``provider.backends`` member, which was previously a function that returned
a list of backends, has been promoted to a service. This implies that it can
be used both in the previous way, as a ``.backends()`` method, and also as a
``.backends`` attribute with expanded capabilities:

* it contains the existing backends from that provider as attributes, which
  can be used for autocompletion. For example::

      my_backend = provider.get_backend('ibmq_qasm_simulator')

  is equivalent to::

      my_backend = provider.backends.ibmq_qasm_simulator

* the ``provider.backends.jobs()`` and ``provider.backends.retrieve_job()``
  methods can be used for retrieving provider-wide jobs.


Other changes
^^^^^^^^^^^^^

* The ``backend.properties()`` function now accepts an optional ``datetime``
  parameter. If specified, the function returns the backend properties
  closest to, but older than, the specified datetime filter.
* Some ``warnings`` have been toned down to ``logger.warning`` messages.


*************
Qiskit 0.13.0
*************

Terra 0.10.0
============

.. _Release Notes_0.10.0_Prelude:

Prelude
-------

The 0.10.0 release includes several new features and bug fixes. The biggest
change for this release is the addition of initial support for using Qiskit
with trapped ion trap backends.


.. _Release Notes_0.10.0_New Features:

New Features
------------

- Introduced new methods in ``QuantumCircuit`` which allows the seamless adding or removing
  of measurements at the end of a circuit.

  ``measure_all()``
    Adds a ``barrier`` followed by a ``measure`` operation to all qubits in the circuit.
    Creates a ``ClassicalRegister`` of size equal to the number of qubits in the circuit,
    which store the measurements.

  ``measure_active()``
    Adds a ``barrier`` followed by a ``measure`` operation to all active qubits in the circuit.
    A qubit is active if it has at least one other operation acting upon it.
    Creates a ``ClassicalRegister`` of size equal to the number of active qubits in the circuit,
    which store the measurements.

  ``remove_final_measurements()``
    Removes all final measurements and preceeding ``barrier`` from a circuit.
    A measurement is considered "final" if it is not followed by any other operation,
    excluding barriers and other measurements.
    After the measurements are removed, if all of the classical bits in the ``ClassicalRegister``
    are idle (have no operations attached to them), then the ``ClassicalRegister`` is removed.

  Examples::

        # Using measure_all()
        circuit = QuantumCircuit(2)
        circuit.h(0)
        circuit.measure_all()
        circuit.draw()

        # A ClassicalRegister with prefix measure was created.
        # It has 2 clbits because there are 2 qubits to measure

                     ┌───┐ ░ ┌─┐
             q_0: |0>┤ H ├─░─┤M├───
                     └───┘ ░ └╥┘┌─┐
             q_1: |0>──────░──╫─┤M├
                           ░  ║ └╥┘
        measure_0: 0 ═════════╩══╬═
                                 ║
        measure_1: 0 ════════════╩═


        # Using measure_active()
        circuit = QuantumCircuit(2)
        circuit.h(0)
        circuit.measure_active()
        circuit.draw()

        # This ClassicalRegister only has 1 clbit because only 1 qubit is active

                     ┌───┐ ░ ┌─┐
             q_0: |0>┤ H ├─░─┤M├
                     └───┘ ░ └╥┘
             q_1: |0>──────░──╫─
                           ░  ║
        measure_0: 0 ═════════╩═


        # Using remove_final_measurements()
        # Assuming circuit_all and circuit_active are the circuits from the measure_all and
        # measure_active examples above respectively

        circuit_all.remove_final_measurements()
        circuit_all.draw()
        # The ClassicalRegister is removed because, after the measurements were removed,
        # all of its clbits were idle

                ┌───┐
        q_0: |0>┤ H ├
                └───┘
        q_1: |0>─────


        circuit_active.remove_final_measurements()
        circuit_active.draw()
        # This will result in the same circuit

                ┌───┐
        q_0: |0>┤ H ├
                └───┘
        q_1: |0>─────

- Initial support for executing experiments on ion trap backends has been
  added.

- An Rxx gate (rxx) and a global Mølmer–Sørensen gate (ms) have been added
  to the standard gate set.

- A Cnot to Rxx/Rx/Ry decomposer ``cnot_rxx_decompose`` and a single qubit
  Euler angle decomposer ``OneQubitEulerDecomposer`` have been added to the
  ``quantum_info.synthesis`` module.

- A transpiler pass ``MSBasisDecomposer`` has been added to unroll circuits
  defined over U3 and Cnot gates into a circuit defined over Rxx,Ry and Rx.
  This pass will be included in preset pass managers for backends which
  include the 'rxx' gate in their supported basis gates.

- The backends in ``qiskit.test.mock`` now contain a snapshot of real
  device calibration data. This is accessible via the ``properties()`` method
  for each backend. This can be used to test any code that depends on
  backend properties, such as noise-adaptive transpiler passes or device
  noise models for simulation. This will create a faster testing and
  development cycle without the need to go to live backends.

- Allows the Result class to return partial results. If a valid result schema
  is loaded that contains some experiments which succeeded and some which
  failed, this allows accessing the data from experiments that succeeded,
  while raising an exception for experiments that failed and displaying the
  appropriate error message for the failed results.

- An ``ax`` kwarg has been added to the following visualization functions:

   * ``qiskit.visualization.plot_histogram``
   * ``qiskit.visualization.plot_state_paulivec``
   * ``qiskit.visualization.plot_state_qsphere``
   * ``qiskit.visualization.circuit_drawer`` (``mpl`` backend only)
   * ``qiskit.QuantumCircuit.draw`` (``mpl`` backend only)

  This kwarg is used to pass in a ``matplotlib.axes.Axes`` object to the
  visualization functions. This enables integrating these visualization
  functions into a larger visualization workflow. Also, if an `ax` kwarg is
  specified then there is no return from the visualization functions.

- An ``ax_real`` and ``ax_imag`` kwarg has been added to the
  following visualization functions:

   * ``qiskit.visualization.plot_state_hinton``
   * ``qiskit.visualization.plot_state_city``

  These new kargs work the same as the newly added ``ax`` kwargs for other
  visualization functions. However because these plots use two axes (one for
  the real component, the other for the imaginary component). Having two
  kwargs also provides the flexibility to only generate a visualization for
  one of the components instead of always doing both. For example::

      from matplotlib import pyplot as plt
      from qiskit.visualization import plot_state_hinton

      ax = plt.gca()

      plot_state_hinton(psi, ax_real=ax)

  will only generate a plot of the real component.

- A given pass manager now can be edited with the new method `replace`. This method allows to
  replace a particular stage in a pass manager, which can be handy when dealing with preset
  pass managers. For example, let's edit the layout selector of the pass manager used at
  optimization level 0:

  .. code-block:: python

    from qiskit.transpiler.preset_passmanagers.level0 import level_0_pass_manager
    from qiskit.transpiler.transpile_config import TranspileConfig

    pass_manager = level_0_pass_manager(TranspileConfig(coupling_map=CouplingMap([[0,1]])))

    pass_manager.draw()

  .. code-block::

    [0] FlowLinear: SetLayout
    [1] Conditional: TrivialLayout
    [2] FlowLinear: FullAncillaAllocation, EnlargeWithAncilla, ApplyLayout
    [3] FlowLinear: Unroller

  The layout selection is set in the stage `[1]`. Let's replace it with `DenseLayout`:

  .. code-block:: python

    from qiskit.transpiler.passes import DenseLayout

    pass_manager.replace(1, DenseLayout(coupling_map), condition=lambda property_set: not property_set['layout'])
    pass_manager.draw()

  .. code-block::

    [0] FlowLinear: SetLayout
    [1] Conditional: DenseLayout
    [2] FlowLinear: FullAncillaAllocation, EnlargeWithAncilla, ApplyLayout
    [3] FlowLinear: Unroller

  If you want to replace it without any condition, you can use set-item shortcut:

  .. code-block:: python

    pass_manager[1] = DenseLayout(coupling_map)
    pass_manager.draw()

  .. code-block::

    [0] FlowLinear: SetLayout
    [1] FlowLinear: DenseLayout
    [2] FlowLinear: FullAncillaAllocation, EnlargeWithAncilla, ApplyLayout
    [3] FlowLinear: Unroller

- Introduced a new pulse command ``Delay`` which may be inserted into a pulse
  ``Schedule``. This command accepts a ``duration`` and may be added to any
  ``Channel``. Other commands may not be scheduled on a channel during a delay.

  The delay can be added just like any other pulse command. For example::

    from qiskit import pulse
    from qiskit.pulse.utils import pad

    dc0 = pulse.DriveChannel(0)

    delay = pulse.Delay(1)
    test_pulse = pulse.SamplePulse([1.0])

    sched = pulse.Schedule()
    sched += test_pulse(dc0).shift(1)

    # build padded schedule by hand
    ref_sched = delay(dc0) | sched

    # pad schedule
    padded_sched = pad(sched)

    assert padded_sched == ref_sched

  One may also pass additional channels to be padded and a time to pad until,
  for example::

    from qiskit import pulse
    from qiskit.pulse.utils import pad

    dc0 = pulse.DriveChannel(0)
    dc1 = pulse.DriveChannel(1)

    delay = pulse.Delay(1)
    test_pulse = pulse.SamplePulse([1.0])

    sched = pulse.Schedule()
    sched += test_pulse(dc0).shift(1)

    # build padded schedule by hand
    ref_sched = delay(dc0) | delay(dc1) |  sched

    # pad schedule across both channels until up until the first time step
    padded_sched = pad(sched, channels=[dc0, dc1], until=1)

    assert padded_sched == ref_sched


.. _Release Notes_0.10.0_Upgrade Notes:

Upgrade Notes
-------------

- Assignments and modifications to the ``data`` attribute of
  ``qiskit.QuantumCircuit`` objects are now validated following the same
  rules used throughout the ``QuantumCircuit`` API. This was done to
  improve the performance of the circuits API since we can now assume the
  ``data`` attribute is in a known format. If you were manually modifying
  the ``data`` attribute of a circuit object before this may no longer work
  if your modifications resulted in a data structure other than the list
  of instructions with context in the format ``[(instruction, qargs, cargs)]``

- The transpiler default passmanager for optimization level 2 now uses the
  ``DenseLayout`` layout selection mechanism by default instead of
  ``NoiseAdaptiveLayout``. The ``Denselayout`` pass has also been modified
  to be made noise-aware.

- The deprecated ``DeviceSpecification`` class has been removed. Instead you should
  use the ``PulseChannelSpec``. For example, you can run something like::

      device = pulse.PulseChannelSpec.from_backend(backend)
      device.drives[0]    # for DeviceSpecification, this was device.q[0].drive
      device.memoryslots  # this was device.mem

- The deprecated module ``qiskit.pulse.ops`` has been removed. Use
  ``Schedule`` and ``Instruction`` methods directly. For example, rather
  than::

      ops.union(schedule_0, schedule_1)
      ops.union(instruction, schedule)  # etc

  Instead please use::

      schedule_0.union(schedule_1)
      instruction.union(schedule)

  This same pattern applies to other ``ops`` functions: ``insert``, ``shift``,
  ``append``, and ``flatten``.


.. _Release Notes_0.10.0_Deprecation Notes:

Deprecation Notes
-----------------

- Using the ``control`` property of ``qiskit.circuit.Instruction`` for
  classical control is now deprecated. In the future this property will be
  used for quantum control. Classically conditioned operations will instead
  be handled by the ``condition`` property of ``qiskit.circuit.Instruction``.

- Support for setting ``qiskit.circuit.Instruction`` parameters with an object
  of type ``qiskit.qasm.node.Node`` has been deprecated. ``Node`` objects that
  were previously used as parameters should be converted to a supported type
  prior to initializing a new ``Instruction`` object or calling the
  ``Instruction.params`` setter. Supported types are ``int``, ``float``,
  ``complex``, ``str``, ``qiskit.circuit.ParameterExpression``, or
  ``numpy.ndarray``.

- In the qiskit 0.9.0 release the representation of bits (both qubits and
  classical bits) changed from tuples of the form ``(register, index)`` to be
  instances of the classes ``qiskit.circuit.Qubit`` and
  ``qiskit.circuit.Clbit``. For backwards compatibility comparing
  the equality between a legacy tuple and the bit classes was supported as
  everything transitioned from tuples to being objects. This support is now
  deprecated and will be removed in the future. Everything should use the bit
  classes instead of tuples moving forward.

- When the ``mpl`` output is used for either ``qiskit.QuantumCircuit.draw()``
  or ``qiskit.visualization.circuit_drawer()`` and the ``style`` kwarg is
  used, passing in unsupported dictionary keys as part of the ``style```
  dictionary is now deprecated. Where these unknown arguments were previously
  silently ignored, in the future, unsupported keys will raise an exception.

- The ``line length`` kwarg for the ``qiskit.QuantumCircuit.draw()`` method
  and the ``qiskit.visualization.circuit_drawer()`` function with the text
  output mode is deprecated. It has been replaced by the ``fold`` kwarg which
  will behave identically for the text output mode (but also now supports
  the mpl output mode too). ``line_length`` will be removed in a future
  release so calls should be updated to use ``fold`` instead.

- The ``fold`` field in the ``style`` dict kwarg for the
  ``qiskit.QuantumCircuit.draw()`` method and the
  ``qiskit.visualization.circuit_drawer()`` function has been deprecated. It
  has been replaced by the ``fold`` kwarg on both functions. This kwarg
  behaves identically to the field in the style dict.


.. _Release Notes_0.10.0_Bug Fixes:

Bug Fixes
---------

- Instructions layering which underlies all types of circuit drawing has
  changed to address right/left justification. This sometimes results in
  output which is topologically equivalent to the rendering in prior versions
  but visually different than previously rendered. Fixes
  `issue #2802 <https://github.com/Qiskit/qiskit-terra/issues/2802>`_

- Add ``memory_slots`` to ``QobjExperimentHeader`` of pulse Qobj. This fixes
  a bug in the data format of ``meas_level=2`` results of pulse experiments.
  Measured quantum states are returned as a bit string with zero padding
  based on the number set for ``memory_slots``.

- Fixed the visualization of the rzz gate in the latex circuit drawer to match
  the cu1 gate to reflect the symmetry in the rzz gate. The fix is based on
  the cds command of the qcircuit latex package. Fixes
  `issue #1957 <https://github.com/Qiskit/qiskit-terra/issues/1957>`_


.. _Release Notes_0.10.0_Other Notes:

Other Notes
-----------

- ``matplotlib.figure.Figure`` objects returned by visualization functions
  are no longer always closed by default. Instead the returned figure objects
  are only closed if the configured matplotlib backend is an inline jupyter
  backend(either set with ``%matplotlib inline`` or
  ``%matplotlib notebook``). Output figure objects are still closed with
  these backends to avoid duplicate outputs in jupyter notebooks (which is
  why the ``Figure.close()`` were originally added).

Aer 0.3
=======

No Change

Ignis 0.2
=========

No Change

Aqua 0.6
========

No Change

IBM Q Provider 0.3
==================

No Change

*************
Qiskit 0.12.0
*************

.. _Release Notes_0.9.0:

Terra 0.9
=========

.. _Release Notes_0.9.0_Prelude:

Prelude
-------

The 0.9 release includes many new features and many bug fixes. The biggest
changes for this release are new debugging capabilities for PassManagers. This
includes a function to visualize a PassManager, the ability to add a callback
function to a PassManager, and logging of passes run in the PassManager.
Additionally, this release standardizes the way that you can set an initial
layout for your circuit. So now you can leverage ``initial_layout`` the kwarg
parameter on ``qiskit.compiler.transpile()`` and ``qiskit.execute()`` and the
qubits in the circuit will get laid out on the desire qubits on the device.
Visualization of circuits will now also show this clearly when visualizing a
circuit that has been transpiled with a layout.

.. _Release Notes_0.9.0_New Features:

New Features
------------

- A ``DAGCircuit`` object (i.e. the graph representation of a QuantumCircuit where
  operation dependencies are explicit) can now be visualized with the ``.draw()``
  method. This is in line with Qiskit's philosophy of easy visualization.
  Other objects which support a ``.draw()`` method are ``QuantumCircuit``,
  ``PassManager``, and ``Schedule``.

- Added a new visualization function
  ``qiskit.visualization.plot_error_map()`` to plot the error map for a given
  backend. It takes in a backend object from the qiskit-ibmq-provider and
  will plot the current error map for that device.

- Both ``qiskit.QuantumCircuit.draw()`` and
  ``qiskit.visualization.circuit_drawer()`` now support annotating the
  qubits in the visualization with layout information. If the
  ``QuantumCircuit`` object being drawn includes layout metadata (which is
  normally only set on the circuit output from ``transpile()`` calls) then
  by default that layout will be shown on the diagram. This is done for all
  circuit drawer backends. For example::

      from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
      from qiskit.compiler import transpile

      qr = QuantumRegister(2, 'userqr')
      cr = ClassicalRegister(2, 'c0')
      qc = QuantumCircuit(qr, cr)
      qc.h(qr[0])
      qc.cx(qr[0], qr[1])
      qc.y(qr[0])
      qc.x(qr[1])
      qc.measure(qr, cr)

      # Melbourne coupling map
      coupling_map = [[1, 0], [1, 2], [2, 3], [4, 3], [4, 10], [5, 4],
                      [5, 6], [5, 9], [6, 8], [7, 8], [9, 8], [9, 10],
                      [11, 3], [11, 10], [11, 12], [12, 2], [13, 1],
                      [13, 12]]
      qc_result = transpile(qc, basis_gates=['u1', 'u2', 'u3', 'cx', 'id'],
                            coupling_map=coupling_map, optimization_level=0)
      qc.draw(output='text')

  will yield a diagram like::

                        ┌──────────┐┌──────────┐┌───┐┌──────────┐┌──────────────────┐┌─┐
         (userqr0) q0|0>┤ U2(0,pi) ├┤ U2(0,pi) ├┤ X ├┤ U2(0,pi) ├┤ U3(pi,pi/2,pi/2) ├┤M├───
                        ├──────────┤└──────────┘└─┬─┘├──────────┤└─┬─────────────┬──┘└╥┘┌─┐
         (userqr1) q1|0>┤ U2(0,pi) ├──────────────■──┤ U2(0,pi) ├──┤ U3(pi,0,pi) ├────╫─┤M├
                        └──────────┘                 └──────────┘  └─────────────┘    ║ └╥┘
        (ancilla0) q2|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
        (ancilla1) q3|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
        (ancilla2) q4|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
        (ancilla3) q5|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
        (ancilla4) q6|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
        (ancilla5) q7|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
        (ancilla6) q8|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
        (ancilla7) q9|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
       (ancilla8) q10|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
       (ancilla9) q11|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
      (ancilla10) q12|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
      (ancilla11) q13|0>──────────────────────────────────────────────────────────────╫──╫─
                                                                                      ║  ║
                c0_0: 0 ══════════════════════════════════════════════════════════════╩══╬═
                                                                                         ║
                c0_1: 0 ═════════════════════════════════════════════════════════════════╩═

  If you do not want the layout to be shown on transpiled circuits (or any
  other circuits with a layout set) there is a new boolean kwarg for both
  functions, ``with_layout`` (which defaults ``True``), which when set
  ``False`` will disable the layout annotation in the output circuits.

- A new analysis pass ``CountOpsLongest`` was added to retrieve the number
  of operations on the longest path of the DAGCircuit. When used it will
  add a ``count_ops_longest_path`` key to the property set dictionary.
  You can add it to your a passmanager with something like::

      from qiskit.transpiler.passes import CountOpsLongestPath
      from qiskit.transpiler.passes import CxCancellation
      from qiskit.transpiler import PassManager

      pm = PassManager()
      pm.append(CountOpsLongestPath())

  and then access the longest path via the property set value with something
  like::

      pm.append(
          CxCancellation(),
          condition=lambda property_set: property_set[
              'count_ops_longest_path'] < 5)

  which will set a condition on that pass based on the longest path.

- Two new functions, ``sech()`` and ``sech_deriv()`` were added to the pulse
  library module ``qiskit.pulse.pulse_lib`` for creating an unnormalized
  hyperbolic secant ``SamplePulse`` object and an unnormalized hyperbolic
  secant derviative ``SamplePulse`` object respectively.

- A new kwarg option ``vertical_compression`` was added to the
  ``QuantumCircuit.draw()`` method and the
  ``qiskit.visualization.circuit_drawer()`` function. This option only works
  with the ``text`` backend. This option can be set to either ``high``,
  ``medium`` (the default), or ``low`` to adjust how much vertical space is
  used by the output visualization.

- A new kwarg boolean option ``idle_wires`` was added to the
  ``QuantumCircuit.draw()`` method and the
  ``qiskit.visualization.circuit_drawer()`` function. It works for all drawer
  backends. When ``idle_wires`` is set False in a drawer call the drawer will
  not draw any bits that do not have any circuit elements in the output
  quantum circuit visualization.

- A new PassManager visualizer function
  ``qiskit.visualization.pass_mamanger_drawer()`` was added. This function
  takes in a PassManager object and will generate a flow control diagram
  of all the passes run in the PassManager.

- When creating a PassManager you can now specify a callback function that
  if specified will be run after each pass is executed. This function gets
  passed a set of kwargs on each call with the state of the pass manager after
  each pass execution. Currently these kwargs are:

  * ``pass_`` (``Pass``): the pass being run
  * ``dag`` (``DAGCircuit``): the dag output of the pass
  * ``time`` (``float``): the time to execute the pass
  * ``property_set`` (``PropertySet``): the property set
  * ``count`` (``int``): the index for the pass execution

  However, it's worth noting that while these arguments are set for the 0.9
  release they expose the internals of the pass manager and are subject to
  change in future release.

  For example you can use this to create a callback function that will
  visualize the circuit output after each pass is executed::

      from qiskit.transpiler import PassManager

      def my_callback(**kwargs):
          print(kwargs['dag'])

      pm = PassManager(callback=my_callback)

  Additionally you can specify the callback function when using
  ``qiskit.compiler.transpile()``::

      from qiskit.compiler import transpile

      def my_callback(**kwargs):
          print(kwargs['pass'])

      transpile(circ, callback=my_callback)

- A new method ``filter()`` was added to the ``qiskit.pulse.Schedule`` class.
  This enables filtering the instructions in a schedule. For example,
  filtering by instruction type::

      from qiskit.pulse import Schedule
      from qiskit.pulse.commands import Acquire
      from qiskit.pulse.commands import AcquireInstruction
      from qiskit.pulse.commands import FrameChange

      sched = Schedule(name='MyExperiment')
      sched.insert(0, FrameChange(phase=-1.57)(device))
      sched.insert(60, Acquire(5))
      acquire_sched = sched.filter(instruction_types=[AcquireInstruction])

- Additional decomposition methods for several types of gates. These methods
  will use different decomposition techniques to break down a gate into
  a sequence of CNOTs and single qubit gates. The following methods are
  added:

  +--------------------------------+---------------------------------------+
  | Method                         | Description                           |
  +================================+=======================================+
  | ``QuantumCircuit.iso()``       | Add an arbitrary isometry from m to n |
  |                                | qubits to a circuit. This allows for  |
  |                                | attaching arbitrary unitaries on n    |
  |                                | qubits (m=n) or to prepare any state  |
  |                                | of n qubits (m=0)                     |
  +--------------------------------+---------------------------------------+
  | ``QuantumCircuit.diag_gate()`` | Add a diagonal gate to the circuit    |
  +--------------------------------+---------------------------------------+
  | ``QuantumCircuit.squ()``       | Decompose an arbitrary 2x2 unitary    |
  |                                | into three rotation gates and add to  |
  |                                | a circuit                             |
  +--------------------------------+---------------------------------------+
  | ``QuantumCircuit.ucg()``       | Attach an uniformly controlled gate   |
  |                                | (also called a multiplexed gate) to a |
  |                                | circuit                               |
  +--------------------------------+---------------------------------------+
  | ``QuantumCircuit.ucx()``       | Attach a uniformly controlled (also   |
  |                                | called multiplexed) Rx rotation gate  |
  |                                | to a circuit                          |
  +--------------------------------+---------------------------------------+
  | ``QuantumCircuit.ucy()``       | Attach a uniformly controlled (also   |
  |                                | called multiplexed) Ry rotation gate  |
  |                                | to a circuit                          |
  +--------------------------------+---------------------------------------+
  | ``QuantumCircuit.ucz()``       | Attach a uniformly controlled (also   |
  |                                | called multiplexed) Rz rotation gate  |
  |                                | to a circuit                          |
  +--------------------------------+---------------------------------------+

- Addition of Gray-Synth and Patel–Markov–Hayes algorithms for
  synthesis of CNOT-Phase and CNOT-only linear circuits. These functions
  allow the synthesis of circuits that consist of only CNOT gates given
  a linear function or a circuit that consists of only CNOT and phase gates
  given a matrix description.

- A new function ``random_circuit`` was added to the
  ``qiskit.circuit.random`` module. This function will generate a random
  circuit of a specified size by randomly selecting different gates and
  adding them to the circuit. For example, you can use this to generate a
  5-qubit circuit with a depth of 10 using::

      from qiskit.circuit.random import random_circuit

      circ = random_circuit(5, 10)

- A new kwarg ``output_names`` was added to the
  ``qiskit.compiler.transpile()`` function. This kwarg takes in a string
  or a list of strings and uses those as the value of the circuit name for
  the output circuits that get returned by the ``transpile()`` call. For
  example::

      from qiskit.compiler import transpile
      my_circs = [circ_a, circ_b]
      tcirc_a, tcirc_b = transpile(my_circs,
                                   output_names=['Circuit A', 'Circuit B'])

  the ``name`` attribute on tcirc_a and tcirc_b will be ``'Circuit A'`` and
  ``'Circuit B'`` respectively.

- A new method ``equiv()`` was added to the ``qiskit.quantum_info.Operator``
  and ``qiskit.quantum_info.Statevector`` classes. These methods are used
  to check whether a second ``Operator`` object or ``Statevector`` is
  equivalent up to global phase.

- The user config file has several new options:

  * The ``circuit_drawer`` field now accepts an `auto` value. When set as
    the value for the ``circuit_drawer`` field the default drawer backend
    will be `mpl` if it is available, otherwise the `text` backend will be
    used.
  * A new field ``circuit_mpl_style`` can be used to set the default style
    used by the matplotlib circuit drawer. Valid values for this field are
    ``bw`` and ``default`` to set the default to a black and white or the
    default color style respectively.
  * A new field ``transpile_optimization_level`` can be used to set the
    default transpiler optimization level to use for calls to
    ``qiskit.compiler.transpile()``. The value can be set to either 0, 1, 2,
    or 3.

- Introduced a new pulse command ``Delay`` which may be inserted into a pulse
  ``Schedule``. This command accepts a ``duration`` and may be added to any
  ``Channel``. Other commands may not be scheduled on a channel during a delay.

  The delay can be added just like any other pulse command. For example::

    from qiskit import pulse

    drive_channel = pulse.DriveChannel(0)
    delay = pulse.Delay(20)

    sched = pulse.Schedule()
    sched += delay(drive_channel)


.. _Release Notes_0.9.0_Upgrade Notes:

Upgrade Notes
-------------

- The previously deprecated ``qiskit._util`` module has been removed.
  ``qiskit.util`` should be used instead.

- The ``QuantumCircuit.count_ops()`` method now returns an ``OrderedDict``
  object instead of a ``dict``. This should be compatible for most use cases
  since ``OrderedDict`` is a ``dict`` subclass. However type checks and
  other class checks might need to be updated.

- The ``DAGCircuit.width()`` method now returns the total number quantum bits
  and classical bits. Before it would only return the number of quantum bits.
  If you require just the number of quantum bits you can use
  ``DAGCircuit.num_qubits()`` instead.

- The function ``DAGCircuit.num_cbits()`` has been removed. Instead you can
  use ``DAGCircuit.num_clbits()``.

- Individual quantum bits and classical bits are no longer represented as
  ``(register, index)`` tuples. They are now instances of `Qubit` and
  `Clbit` classes. If you're dealing with individual bits make sure that
  you update any usage or type checks to look for these new classes instead
  of tuples.

- The preset passmanager classes
  ``qiskit.transpiler.preset_passmanagers.default_pass_manager`` and
  ``qiskit.transpiler.preset_passmanagers.default_pass_manager_simulator``
  (which were the previous default pass managers for
  ``qiskit.compiler.transpile()`` calls) have been removed. If you were
  manually using this pass managers switch to the new default,
  ``qiskit.transpile.preset_passmanagers.level1_pass_manager``.

- The ``LegacySwap`` pass has been removed. If you were using it in a custom
  pass manager, it's usage can be replaced by the ``StochasticSwap`` pass,
  which is a faster more stable version. All the preset passmanagers have
  been updated to use ``StochasticSwap`` pass instead of the ``LegacySwap``.

- The following deprecated ``qiskit.dagcircuit.DAGCircuit`` methods have been
  removed:

  * ``DAGCircuit.get_qubits()`` - Use ``DAGCircuit.qubits()`` instead
  * ``DAGCircuit.get_bits()`` - Use ``DAGCircuit.clbits()`` instead
  * ``DAGCircuit.qasm()`` - Use a combination of
    ``qiskit.converters.dag_to_circuit()`` and ``QuantumCircuit.qasm()``. For
    example::

      from qiskit.dagcircuit import DAGCircuit
      from qiskit.converters import dag_to_circuit
      my_dag = DAGCircuit()
      qasm = dag_to_circuit(my_dag).qasm()

  * ``DAGCircuit.get_op_nodes()`` - Use ``DAGCircuit.op_nodes()`` instead.
    Note that the return type is a list of ``DAGNode`` objects for
    ``op_nodes()`` instead of the list of tuples previously returned by
    ``get_op_nodes()``.
  * ``DAGCircuit.get_gate_nodes()`` - Use ``DAGCircuit.gate_nodes()``
    instead. Note that the return type is a list of ``DAGNode`` objects for
    ``gate_nodes()`` instead of the list of tuples previously returned by
    ``get_gate_nodes()``.
  * ``DAGCircuit.get_named_nodes()`` - Use ``DAGCircuit.named_nodes()``
    instead. Note that the return type is a list of ``DAGNode`` objects for
    ``named_nodes()`` instead of the list of node_ids previously returned by
    ``get_named_nodes()``.
  * ``DAGCircuit.get_2q_nodes()`` - Use ``DAGCircuit.twoQ_gates()``
    instead. Note that the return type is a list of ``DAGNode`` objects for
    ``twoQ_gates()`` instead of the list of data_dicts previously returned by
    ``get_2q_nodes()``.
  * ``DAGCircuit.get_3q_or_more_nodes()`` - Use
    ``DAGCircuit.threeQ_or_more_gates()`` instead. Note that the return type
    is a list of ``DAGNode`` objects for ``threeQ_or_more_gates()`` instead
    of the list of tuples previously returned by ``get_3q_or_more_nodes()``.

- The following ``qiskit.dagcircuit.DAGCircuit`` methods had deprecated
  support for accepting a ``node_id`` as a parameter. This has been removed
  and now only ``DAGNode`` objects are accepted as input:

  * ``successors()``
  * ``predecessors()``
  * ``ancestors()``
  * ``descendants()``
  * ``bfs_successors()``
  * ``quantum_successors()``
  * ``remove_op_node()``
  * ``remove_ancestors_of()``
  * ``remove_descendants_of()``
  * ``remove_nonancestors_of()``
  * ``remove_nondescendants_of()``
  * ``substitute_node_with_dag()``

- The ``qiskit.dagcircuit.DAGCircuit`` method ``rename_register()`` has been
  removed. This was unused by all the qiskit code. If you were relying on it
  externally you'll have to re-implement is an external function.

- The ``qiskit.dagcircuit.DAGCircuit`` property ``multi_graph`` has been
  removed. Direct access to the underlying ``networkx`` ``multi_graph`` object
  isn't supported anymore. The API provided by the ``DAGCircuit`` class should
  be used instead.

- The deprecated exception class ``qiskit.qiskiterror.QiskitError`` has been
  removed. Instead you should use ``qiskit.exceptions.QiskitError``.

- The boolean kwargs, ``ignore_requires`` and ``ignore_preserves`` from
  the ``qiskit.transpiler.PassManager`` constructor have been removed. These
  are no longer valid options.

- The module ``qiskit.tools.logging`` has been removed. This module was not
  used by anything and added nothing over the interfaces that Python's
  standard library ``logging`` module provides. If you want to set a custom
  formatter for logging use the standard library ``logging`` module instead.

- The ``CompositeGate`` class has been removed. Instead you should
  directly create a instruction object from a circuit and append that to your
  circuit. For example, you can run something like::

      custom_gate_circ = qiskit.QuantumCircuit(2)
      custom_gate_circ.x(1)
      custom_gate_circ.h(0)
      custom_gate_circ.cx(0, 1)
      custom_gate = custom_gate_circ.to_instruction()

- The previously deprecated kwargs, ``seed`` and ``config`` for
  ``qiskit.compiler.assemble()`` have been removed use ``seed_simulator`` and
  ``run_config`` respectively instead.

- The previously deprecated converters
  ``qiskit.converters.qobj_to_circuits()`` and
  ``qiskit.converters.circuits_to_qobj()`` have been removed. Use
  ``qiskit.assembler.disassemble()`` and ``qiskit.compiler.assemble()``
  respectively instead.

- The previously deprecated kwarg ``seed_mapper`` for
  ``qiskit.compiler.transpile()`` has been removed. Instead you should use
  ``seed_transpiler``

- The previously deprecated kwargs ``seed``, ``seed_mapper``, ``config``,
  and ``circuits`` for the ``qiskit.execute()`` function have been removed.
  Use ``seed_simulator``, ``seed_transpiler``, ``run_config``, and
  ``experiments`` arguments respectively instead.

- The previously deprecated ``qiskit.tools.qcvv`` module has been removed
  use qiskit-ignis instead.

- The previously deprecated functions ``qiskit.transpiler.transpile()`` and
  ``qiskit.transpiler.transpile_dag()`` have been removed. Instead you should
  use ``qiskit.compiler.transpile``. If you were using ``transpile_dag()``
  this can be replaced by running::

      circ = qiskit.converters.dag_to_circuit(dag)
      out_circ = qiskit.compiler.transpile(circ)
      qiskit.converters.circuit_to_dag(out_circ)

- The previously deprecated function ``qiskit.compile()`` has been removed
  instead you should use ``qiskit.compiler.transpile()`` and
  ``qiskit.compiler.assemble()``.

- The jupyter cell magic ``%%qiskit_progress_bar`` from
  ``qiskit.tools.jupyter`` has been changed to a line magic. This was done
  to better reflect how the magic is used and how it works. If you were using
  the ``%%qiskit_progress_bar`` cell magic in an existing notebook, you will
  have to update this to be a line magic by changing it to be
  ``%qiskit_progress_bar`` instead. Everything else should behave
  identically.

- The deprecated function ``qiskit.tools.qi.qi.random_unitary_matrix()``
  has been removed. You should use the
  ``qiskit.quantum_info.random.random_unitary()`` function instead.

- The deprecated function ``qiskit.tools.qi.qi.random_density_matrix()``
  has been removed. You should use the
  ``qiskit.quantum_info.random.random_density_matrix()`` function
  instead.

- The deprecated function ``qiskit.tools.qi.qi.purity()`` has been removed.
  You should the ``qiskit.quantum_info.purity()`` function instead.

- The deprecated ``QuantumCircuit._attach()`` method has been removed. You
  should use ``QuantumCircuit.append()`` instead.

- The ``qiskit.qasm.Qasm`` method ``get_filename()`` has been removed.
  You can use the ``return_filename()`` method instead.

- The deprecated ``qiskit.mapper`` module has been removed. The list of
  functions and classes with their alternatives are:

  * ``qiskit.mapper.CouplingMap``: ``qiskit.transpiler.CouplingMap`` should
    be used instead.
  * ``qiskit.mapper.Layout``: ``qiskit.transpiler.Layout`` should be used
    instead
  * ``qiskit.mapper.compiling.euler_angles_1q()``:
    ``qiskit.quantum_info.synthesis.euler_angles_1q()`` should be used
    instead
  * ``qiskit.mapper.compiling.two_qubit_kak()``:
    ``qiskit.quantum_info.synthesis.two_qubit_cnot_decompose()`` should be
    used instead.

  The deprecated exception classes ``qiskit.mapper.exceptions.CouplingError``
  and ``qiskit.mapper.exceptions.LayoutError`` don't have an alternative
  since they serve no purpose without a ``qiskit.mapper`` module.

- The ``qiskit.pulse.samplers`` module has been moved to
  ``qiskit.pulse.pulse_lib.samplers``. You will need to update imports of
  ``qiskit.pulse.samplers`` to ``qiskit.pulse.pulse_lib.samplers``.

- `seaborn`_ is now a dependency for the function
  ``qiskit.visualization.plot_state_qsphere()``. It is needed to generate
  proper angular color maps for the visualization. The
  ``qiskit-terra[visualization]`` extras install target has been updated to
  install ``seaborn>=0.9.0`` If you are using visualizations and specifically
  the ``plot_state_qsphere()`` function you can use that to install
  ``seaborn`` or just manually run ``pip install seaborn>=0.9.0``

  .. _seaborn: https://seaborn.pydata.org/

- The previously deprecated functions ``qiksit.visualization.plot_state`` and
  ``qiskit.visualization.iplot_state`` have been removed. Instead you should
  use the specific function for each plot type. You can refer to the
  following tables to map the deprecated functions to their equivalent new
  ones:

  ==================================  ========================
  Qiskit Terra 0.6                    Qiskit Terra 0.7+
  ==================================  ========================
  plot_state(rho)                     plot_state_city(rho)
  plot_state(rho, method='city')      plot_state_city(rho)
  plot_state(rho, method='paulivec')  plot_state_paulivec(rho)
  plot_state(rho, method='qsphere')   plot_state_qsphere(rho)
  plot_state(rho, method='bloch')     plot_bloch_multivector(rho)
  plot_state(rho, method='hinton')    plot_state_hinton(rho)
  ==================================  ========================

- The ``pylatexenc`` and ``pillow`` dependencies for the ``latex`` and
  ``latex_source`` circuit drawer backends are no longer listed as
  requirements. If you are going to use the latex circuit drawers ensure
  you have both packages installed or use the setuptools extras to install
  it along with qiskit-terra::

      pip install qiskit-terra[visualization]

- The root of the ``qiskit`` namespace will now emit a warning on import if
  either ``qiskit.IBMQ`` or ``qiskit.Aer`` could not be setup. This will
  occur whenever anything in the ``qiskit`` namespace is imported. These
  warnings were added to make it clear for users up front if they're running
  qiskit and the qiskit-aer and qiskit-ibmq-provider packages could not be
  found. It's not always clear if the packages are missing or python
  packaging/pip installed an element incorrectly until you go to use them and
  get an empty ``ImportError``. These warnings should make it clear up front
  if there these commonly used aliases are missing.

  However, for users that choose not to use either qiskit-aer or
  qiskit-ibmq-provider this might cause additional noise. For these users
  these warnings are easily suppressable using Python's standard library
  ``warnings``. Users can suppress the warnings by putting these two lines
  before any imports from qiskit::

      import warnings
      warnings.filterwarnings('ignore', category=RuntimeWarning,
                              module='qiskit')

  This will suppress the warnings emitted by not having qiskit-aer or
  qiskit-ibmq-provider installed, but still preserve any other warnings
  emitted by qiskit or any other package.


.. _Release Notes_0.9.0_Deprecation Notes:

Deprecation Notes
-----------------

- The ``U`` and ``CX`` gates have been deprecated. If you're using these gates
  in your code you should update them to use ``u3`` and ``cx`` instead. For
  example, if you're using the circuit gate functions ``circuit.u_base()``
  and ``circuit.cx_base()`` you should update these to be ``circuit.u3()`` and
  ``circuit.cx()`` respectively.

- The ``u0`` gate has been deprecated in favor of using multiple ``iden``
  gates and it will be removed in the future. If you're using the ``u0`` gate
  in your circuit you should update your calls to use ``iden``. For example,
  f you were using ``circuit.u0(2)`` in your circuit before that should be
  updated to be::

      circuit.iden()
      circuit.iden()

  instead.

- The ``qiskit.pulse.DeviceSpecification`` class is deprecated now. Instead
  you should use ``qiskit.pulse.PulseChannelSpec``.

- Accessing a ``qiskit.circuit.Qubit``, ``qiskit.circuit.Clbit``, or
  ``qiskit.circuit.Bit`` class by index is deprecated (for compatibility
  with the ``(register, index)`` tuples that these classes replaced).
  Instead you should use the ``register`` and ``index`` attributes.

- Passing in a bit to the ``qiskit.QuantumCircuit`` method ``append`` as
  a tuple ``(register, index)`` is deprecated. Instead bit objects should
  be used directly.

- Accessing the elements of a ``qiskit.transpiler.Layout`` object with a
  tuple ``(register, index)`` is deprecated. Instead a bit object should
  be used directly.

- The ``qiskit.transpiler.Layout`` constructor method
  ``qiskit.transpiler.Layout.from_tuplelist()`` is deprecated. Instead the
  constructor ``qiskit.transpiler.Layout.from_qubit_list()`` should be used.

- The module ``qiskit.pulse.ops`` has been deprecated. All the functions it
  provided:

  * ``union``
  * ``flatten``
  * ``shift``
  * ``insert``
  * ``append``

  have equivalent methods available directly on the ``qiskit.pulse.Schedule``
  and ``qiskit.pulse.Instruction`` classes. Those methods should be used
  instead.

- The ``qiskit.qasm.Qasm`` method ``get_tokens()`` is deprecated. Instead
  you should use the ``generate_tokens()`` method.

- The ``qiskit.qasm.qasmparser.QasmParser`` method ``get_tokens()`` is
  deprecated. Instead you should use the ``read_tokens()`` method.

- The ``as_dict()`` method for the Qobj class has been deprecated and will
  be removed in the future. You should replace calls to it with ``to_dict()``
  instead.


.. _Release Notes_0.9.0_Bug Fixes:

Bug Fixes
---------

- The definition of the ``CU3Gate`` has been changed to be equivalent to the
  canonical definition of a controlled ``U3Gate``.

- The handling of layout in the pass manager has been standardized. This
  fixes several reported issues with handling layout. The ``initial_layout``
  kwarg parameter on ``qiskit.compiler.transpile()`` and
  ``qiskit.execute()`` will now lay out your qubits from the circuit onto
  the desired qubits on the device when transpiling circuits.

- Support for n-qubit unitaries was added to the BasicAer simulator and
  ``unitary`` (arbitrary unitary gates) was added to the set of basis gates
  for the simulators

- The ``qiskit.visualization.plost_state_qsphere()`` has been updated to fix
  several issues with it. Now output Q Sphere visualization will be correctly
  generated and the following aspects have been updated:

  * All complementary basis states are antipodal
  * Phase is indicated by color of line and marker on sphere's surface
  * Probability is indicated by translucency of line and volume of marker on
     sphere's surface


.. _Release Notes_0.9.0_Other Notes:

Other Notes
-----------

- The default PassManager for ``qiskit.compiler.transpile()`` and
  ``qiskit.execute()`` has been changed to optimization level 1 pass manager
  defined at ``qiskit.transpile.preset_passmanagers.level1_pass_manager``.

- All the circuit drawer backends now will express gate parameters in a
  circuit as common fractions of pi in the output visualization. If the value
  of a parameter can be expressed as a fraction of pi that will be used
  instead of the numeric equivalent.

- When using ``qiskit.assembler.assemble_schedules()`` if you do not provide
  the number of memory_slots to use the number will be inferred based on the
  number of acquisitions in the input schedules.

- The deprecation warning on the ``qiskit.dagcircuit.DAGCircuit`` property
  ``node_counter`` has been removed. The behavior change being warned about
  was put into effect when the warning was added, so warning that it had
  changed served no purpose.

- Calls to ``PassManager.run()`` now will emit python logging messages at the
  INFO level for each pass execution. These messages will include the Pass
  name and the total execution time of the pass. Python's standard logging
  was used because it allows Qiskit-Terra's logging to integrate in a standard
  way with other applications and libraries. All logging for the transpiler
  occurs under the ``qiskit.transpiler`` namespace, as used by
  ``logging.getLogger('qiskit.transpiler``). For example, to turn on DEBUG
  level logging for the transpiler you can run::

      import logging

      logging.basicConfig()
      logging.getLogger('qiskit.transpiler').setLevel(logging.DEBUG)

  which will set the log level for the transpiler to DEBUG and configure
  those messages to be printed to stderr.

Aer 0.3
=======
- There's a new high-performance Density Matrix Simulator that can be used in
  conjunction with our noise models, to better simulate real world scenarios.
- We have added a Matrix Product State (MPS) simulator. MPS allows for
  efficient simulation of several classes of quantum circuits, even under
  presence of strong correlations and highly entangled states. For cases
  amenable to MPS, circuits with several hundred qubits and more can be exactly
  simulated, e.g., for the purpose of obtaining expectation values of observables.
- Snapshots can be performed in all of our simulators.
- Now we can measure sampling circuits with read-out errors too, not only ideal
  circuits.
- We have increased some circuit optimizations with noise presence.
- A better 2-qubit error approximations have been included.
- Included some tools for making certain noisy simulations easier to craft and
  faster to simulate.
- Increased performance with simulations that require less floating point
  numerical precision.

Ignis 0.2
=========

New Features
------------

- `Logging Module <https://github.com/Qiskit/qiskit-iqx-tutorials/blob/stable/0.12.x/qiskit/advanced/ignis/9_ignis_logging.ipynb>`_
- `Purity RB <https://github.com/Qiskit/qiskit-iqx-tutorials/blob/stable/0.12.x/qiskit/advanced/ignis/5c_purity_rb.ipynb>`_
- `Interleaved RB <https://github.com/Qiskit/qiskit-iqx-tutorials/blob/stable/0.12.x/qiskit/advanced/ignis/5b_interleaved_rb.ipynb>`_
- `Repetition Code for Verification <https://github.com/Qiskit/qiskit-iqx-tutorials/blob/stable/0.12.x/qiskit/advanced/ignis/8_repetition_code.ipynb>`_
- Seed values can now be arbitrarily added to RB (not just in order)
- Support for adding multiple results to measurement mitigation
- RB Fitters now support providing guess values

Bug Fixes
---------

- Fixed a bug in RB fit error
- Fixed a bug in the characterization fitter when selecting a qubit index to
  fit

Other Notes
-----------

- Measurement mitigation now operates in parallel when applied to multiple
  results
- Guess values for RB fitters are improved

Aqua 0.6
========

Added
-----

- Relative-Phase Toffoli gates ``rccx`` (with 2 controls) and ``rcccx``
  (with 3 controls).
- Variational form ``RYCRX``
- A new ``'basic-no-ancilla'`` mode to ``mct``.
- Multi-controlled rotation gates ``mcrx``, ``mcry``, and ``mcrz`` as a general
  ``u3`` gate is not supported by graycode implementation
- Chemistry: ROHF open-shell support

  * Supported for all drivers: Gaussian16, PyQuante, PySCF and PSI4
  * HartreeFock initial state, UCCSD variational form and two qubit reduction for
    parity mapping now support different alpha and beta particle numbers for open
    shell support

- Chemistry: UHF open-shell support

  * Supported for all drivers: Gaussian16, PyQuante, PySCF and PSI4
  * QMolecule extended to include integrals, coefficients etc for separate beta

- Chemistry: QMolecule extended with integrals in atomic orbital basis to
  facilitate common access to these for experimentation

  * Supported for all drivers: Gaussian16, PyQuante, PySCF and PSI4

- Chemistry: Additional PyQuante and PySCF driver configuration

  * Convergence tolerance and max convergence iteration controls.
  * For PySCF initial guess choice

- Chemistry: Processing output added to debug log from PyQuante and PySCF
  computations (Gaussian16 and PSI4 outputs were already added to debug log)
- Chemistry: Merged qiskit-chemistry into qiskit-aqua
- Add ``MatrixOperator``, ``WeightedPauliOperator`` and
  ``TPBGroupedPauliOperator`` class.
- Add ``evolution_instruction`` function to get registerless instruction of
  time evolution.
- Add ``op_converter`` module to unify the place in charge of converting
  different types of operators.
- Add ``Z2Symmetries`` class to encapsulate the Z2 symmetries info and has
  helper methods for tapering an Operator.
- Amplitude Estimation: added maximum likelihood postprocessing and confidence
  interval computation.
- Maximum Likelihood Amplitude Estimation (MLAE): Implemented new algorithm for
  amplitude estimation based on maximum likelihood estimation, which reduces
  number of required qubits and circuit depth.
- Added (piecewise) linearly and polynomially controlled Pauli-rotation
  circuits.
- Add ``q_equation_of_motion`` to study excited state of a molecule, and add
  two algorithms to prepare the reference state.

Changed
-------

- Improve ``mct``'s ``'basic'`` mode by using relative-phase Toffoli gates to
  build intermediate results.
- Adapt to Qiskit Terra's newly introduced ``Qubit`` class.
- Prevent ``QPE/IQPE`` from modifying input ``Operator`` objects.
- The PyEDA dependency was removed;
  corresponding oracles' underlying logic operations are now handled by SymPy.
- Refactor the ``Operator`` class, each representation has its own class
  ``MatrixOperator``, ``WeightedPauliOperator`` and ``TPBGroupedPauliOperator``.
- The ``power`` in ``evolution_instruction`` was applied on the theta on the
  CRZ gate directly, the new version repeats the circuits to implement power.
- CircuitCache is OFF by default, and it can be set via environment variable now
  ``QISKIT_AQUA_CIRCUIT_CACHE``.

Bug Fixes
---------

- A bug where ``TruthTableOracle`` would build incorrect circuits for truth
  tables with only a single ``1`` value.
- A bug caused by ``PyEDA``'s indeterminism.
- A bug with ``QPE/IQPE``'s translation and stretch computation.
- Chemistry: Bravyi-Kitaev mapping fixed when num qubits was not a power of 2
- Setup ``initial_layout`` in ``QuantumInstance`` via a list.

Removed
-------

- General multi-controlled rotation gate ``mcu3`` is removed and replaced by
  multi-controlled rotation gates ``mcrx``, ``mcry``, and ``mcrz``

Deprecated
----------
- The ``Operator`` class is deprecated, in favor of using ``MatrixOperator``,
  ``WeightedPauliOperator`` and ``TPBGroupedPauliOperator``.


IBM Q Provider 0.3
==================

No change


*************
Qiskit 0.11.1
*************

We have bumped up Qiskit micro version to 0.11.1 because IBM Q Provider has
bumped its micro version as well.

Terra 0.8
=========

No Change

Aer 0.2
=======

No change

Ignis 0.1
=========

No Change

Aqua 0.5
========

``qiskit-aqua`` has been updated to ``0.5.3`` to fix code related to
changes in how gates inverses are done.

IBM Q Provider 0.3
==================

The ``IBMQProvider`` has been updated to version ``0.3.1`` to fix
backward compatibility issues and work with the default 10 job
limit in single calls to the IBM Q API v2.


***********
Qiskit 0.11
***********

We have bumped up Qiskit minor version to 0.11 because IBM Q Provider has bumped up
its minor version too.
On Aer, we have jumped from 0.2.1 to 0.2.3 because there was an issue detected
right after releasing 0.2.2 and before Qiskit 0.11 went online.

Terra 0.8
=========

No Change

Aer 0.2
=======

New features
------------

- Added support for multi-controlled phase gates
- Added optimized anti-diagonal single-qubit gates

Improvements
------------

- Introduced a technique called Fusion that increments performance of circuit execution
  Tuned threading strategy to gain performance in most common scenarios.
- Some of the already implemented error models have been polished.



Ignis 0.1
=========

No Change

Aqua 0.5
========

No Change

IBM Q Provider 0.3
==================

The ``IBMQProvider`` has been updated in order to default to use the new
`IBM Q Experience v2 <https://quantum-computing.ibm.com>`__. Accessing the legacy IBM Q Experience v1 and QConsole
will still be supported during the 0.3.x line until its final deprecation one
month from the release. It is encouraged to update to the new IBM Q
Experience to take advantage of the new functionality and features.

Updating to the new IBM Q Experience v2
---------------------------------------

If you have credentials for the legacy IBM Q Experience stored on disk, you
can make use of the interactive helper::

    from qiskit import IBMQ

    IBMQ.update_account()


For more complex cases or fine tuning your configuration, the following methods
are available:

* the ``IBMQ.delete_accounts()`` can be used for resetting your configuration
  file.
* the ``IBMQ.save_account('MY_TOKEN')`` method can be used for saving your
  credentials, following the instructions in the `IBM Q Experience v2 <https://quantum-computing.ibm.com>`__
  account page.

Updating your programs
----------------------

When using the new IBM Q Experience v2 through the provider, access to backends
is done via individual ``provider`` instances (as opposed to accessing them
directly through the ``qiskit.IBMQ`` object as in previous versions), which
allows for more granular control over the project you are using.

You can get a reference to the ``providers`` that you have access to using the
``IBMQ.providers()`` and ``IBMQ.get_provider()`` methods::

    from qiskit import IBMQ

    provider = IBMQ.load_account()
    my_providers = IBMQ.providers()
    provider_2 = IBMQ.get_provider(hub='A', group='B', project='C')


For convenience, ``IBMQ.load_account()`` and ``IBMQ.enable_account()`` will
return a provider for the open access project, which is the default in the new
IBM Q Experience v2.

For example, the following program in previous versions::

    from qiskit import IBMQ

    IBMQ.load_accounts()
    backend = IBMQ.get_backend('ibmqx4')
    backend_2 = IBMQ.get_backend('ibmq_qasm_simulator', hub='HUB2')

Would be equivalent to the following program in the current version::

    from qiskit import IBMQ

    provider = IBMQ.load_account()
    backend = provider.get_backend('ibmqx4')
    provider_2 = IBMQ.get_provider(hub='HUB2')
    backend_2 = provider_2.get_backend('ibmq_qasm_simulator')

You can find more information and details in the `IBM Q Provider documentation <https://github.com/Qiskit/qiskit-ibmq-provider>`__.


***********
Qiskit 0.10
***********

Terra 0.8
=========

No Change

Aer 0.2
=======

No Change

Ignis 0.1
=========

No Change

Aqua 0.5
========

No Change

IBM Q Provider 0.2
==================

New Features
------------

- The ``IBMQProvider`` supports connecting to the new version of the IBM Q API.
  Please note support for this version is still experimental :pull_ibmq-provider:`78`.
- Added support for Circuits through the new API :pull_ibmq-provider:`79`.


Bug Fixes
---------

- Fixed incorrect parsing of some API hub URLs :pull_ibmq-provider:`77`.
- Fixed noise model handling for remote simulators :pull_ibmq-provider:`84`.


**********
Qiskit 0.9
**********

Terra 0.8
=========



Highlights
----------

- Introduction of the Pulse module under ``qiskit.pulse``, which includes
  tools for building pulse commands, scheduling them on pulse channels,
  visualization, and running them on IBM Q devices.
- Improved QuantumCircuit and Instruction classes, allowing for the
  composition of arbitrary sub-circuits into larger circuits, and also
  for creating parameterized circuits.
- A powerful Quantum Info module under ``qiskit.quantum_info``, providing
  tools to work with operators and channels and to use them inside circuits.
- New transpiler optimization passes and access to predefined transpiling
  routines.



New Features
------------

- The core ``StochasticSwap`` routine is implemented in `Cython <https://cython.org/>`__.
- Added ``QuantumChannel`` classes for manipulating quantum channels and CPTP
  maps.
- Support for parameterized circuits.
- The ``PassManager`` interface has been improved and new functions added for
  easier interaction and usage with custom pass managers.
- Preset ``PassManager``\s are now included which offer a predetermined pipeline
  of transpiler passes.
- User configuration files to let local environments override default values
  for some functions.
- New transpiler passes: ``EnlargeWithAncilla``, ``Unroll2Q``,
  ``NoiseAdaptiveLayout``, ``OptimizeSwapBeforeMeasure``,
  ``RemoveDiagonalGatesBeforeMeasure``, ``CommutativeCancellation``,
  ``Collect2qBlocks``, and ``ConsolidateBlocks``.


Compatibility Considerations
----------------------------

As part of the 0.8 release the following things have been deprecated and will
either be removed or changed in a backwards incompatible manner in a future
release. While not strictly necessary these are things to adjust for before the
0.9 (unless otherwise noted) release to avoid a breaking change in the future.

* The methods prefixed by ``_get`` in the ``DAGCircuit`` object are being
  renamed without that prefix.
* Changed elements in ``couplinglist`` of ``CouplingMap`` from tuples to lists.
* Unroller bases must now be explicit, and violation raises an informative
  ``QiskitError``.
* The ``qiskit.tools.qcvv`` package is deprecated and will be removed in the in
  the future. You should migrate to using the Qiskit Ignis which replaces this
  module.
* The ``qiskit.compile()`` function is now deprecated in favor of explicitly
  using the ``qiskit.compiler.transpile()`` function to transform a circuit,
  followed by ``qiskit.compiler.assemble()`` to make a Qobj out of
  it. Instead of ``compile(...)``, use ``assemble(transpile(...), ...)``.
* ``qiskit.converters.qobj_to_circuits()`` has been deprecated and will be
  removed in a future release. Instead
  ``qiskit.assembler.disassemble()`` should be used to extract
  ``QuantumCircuit`` objects from a compiled Qobj.
* The ``qiskit.mapper`` namespace has been deprecated. The ``Layout`` and
  ``CouplingMap`` classes can be accessed via ``qiskit.transpiler``.
* A few functions in ``qiskit.tools.qi.qi`` have been deprecated and
  moved to ``qiskit.quantum_info``.

Please note that some backwards incompatible changes have been made during this
release. The following notes contain information on how to adapt to these
changes.

IBM Q Provider
^^^^^^^^^^^^^^

The IBM Q provider was previously included in Terra, but it has been split out
into a separate package ``qiskit-ibmq-provider``. This will need to be
installed, either via pypi with ``pip install qiskit-ibmq-provider`` or from
source in order to access ``qiskit.IBMQ`` or ``qiskit.providers.ibmq``. If you
install qiskit with ``pip install qiskit``, that will automatically install
all subpackages of the Qiskit project.



Cython Components
^^^^^^^^^^^^^^^^^

Starting in the 0.8 release the core stochastic swap routine is now implemented
in `Cython <https://cython.org/>`__. This was done to significantly improve the performance of the
swapper, however if you build Terra from source or run on a non-x86 or other
platform without prebuilt wheels and install from source distribution you'll
need to make sure that you have Cython installed prior to installing/building
Qiskit Terra. This can easily be done with pip/pypi: ``pip install Cython``.




Compiler Workflow
^^^^^^^^^^^^^^^^^

The ``qiskit.compile()`` function has been deprecated and replaced by first
calling ``qiskit.compiler.transpile()`` to run optimization and mapping on a
circuit, and then ``qiskit.compiler.assemble()`` to build a Qobj from that
optimized circuit to send to a backend. While this is only a deprecation it
will emit a warning if you use the old ``qiskit.compile()`` call.

**transpile(), assemble(), execute() parameters**

These functions are heavily overloaded and accept a wide range of inputs.
They can handle circuit and pulse inputs. All kwargs except for ``backend``
for these functions now also accept lists of the previously accepted types.
The ``initial_layout`` kwarg can now be supplied as a both a list and dictionary,
e.g. to map a Bell experiment on qubits 13 and 14, you can supply:
``initial_layout=[13, 14]`` or ``initial_layout={qr[0]: 13, qr[1]: 14}``



Qobj
^^^^

The Qobj class has been split into two separate subclasses depending on the
use case, either ``PulseQobj`` or ``QasmQobj`` for pulse and circuit jobs
respectively. If you're interacting with Qobj directly you may need to
adjust your usage accordingly.

The ``qiskit.qobj.qobj_to_dict()`` is removed. Instead use the ``to_dict()``
method of a Qobj object.



Visualization
^^^^^^^^^^^^^

The largest change to the visualization module is it has moved from
``qiskit.tools.visualization`` to ``qiskit.visualization``. This was done to
indicate that the visualization module is more than just a tool. However, since
this interface was declared stable in the 0.7 release the public interface off
of ``qiskit.tools.visualization`` will continue to work. That may change in a
future release, but it will be deprecated prior to removal if that happens.

The previously deprecated functions, ``plot_circuit()``,
``latex_circuit_drawer()``, ``generate_latex_source()``, and
``matplotlib_circuit_drawer()`` from ``qiskit.tools.visualization`` have been
removed. Instead of these functions, calling
``qiskit.visualization.circuit_drawer()`` with the appropriate arguments should
be used.

The previously deprecated ``plot_barriers`` and ``reverse_bits`` keys in
the ``style`` kwarg dictionary are deprecated, instead the
``qiskit.visualization.circuit_drawer()`` kwargs ``plot_barriers`` and
``reverse_bits`` should be used.

The Wigner plotting functions ``plot_wigner_function``, ``plot_wigner_curve``,
``plot_wigner_plaquette``, and ``plot_wigner_data`` previously in the
``qiskit.tools.visualization._state_visualization`` module have been removed.
They were never exposed through the public stable interface and were not well
documented. The code to use this feature can still be accessed through the
qiskit-tutorials repository.



Mapper
^^^^^^

The public api from ``qiskit.mapper`` has been moved into ``qiskit.transpiler``.
While it has only been deprecated in this release, it will be removed in the
0.9 release so updating your usage of ``Layout`` and ``CouplingMap`` to import
from ``qiskit.transpiler`` instead of ``qiskit.mapper`` before that takes place
will avoid any surprises in the future.






Aer 0.2
=======

New Features
------------

- Added multiplexer gate :pull_aer:`192`
- Added ``remap_noise_model`` function to ``noise.utils`` :pull_aer:`181`
- Added ``__eq__`` method to ``NoiseModel``, ``QuantumError``, ``ReadoutError``
  :pull_aer:`181`
- Added support for labelled gates in noise models :pull_aer:`175`
- Added optimized ``mcx``, ``mcy``, ``mcz``, ``mcu1``, ``mcu2``, ``mcu3``,
  gates to ``QubitVector`` :pull_aer:`124`
- Added optimized controlled-swap gate to ``QubitVector`` :pull_aer:`142`
- Added gate-fusion optimization for ``QasmController``, which is enabled by
  setting ``fusion_enable=true`` :pull_aer:`136`
- Added better management of failed simulations :pull_aer:`167`
- Added qubits truncate optimization for unused qubits :pull_aer:`164`
- Added ability to disable depolarizing error on device noise model
  :pull_aer:`131`
- Added initialize simulator instruction to ``statevector_state``
  :pull_aer:`117`, :pull_aer:`137`
- Added coupling maps to simulators :pull_aer:`93`
- Added circuit optimization framework :pull_aer:`83`
- Added benchmarking :pull_aer:`71`, :pull_aer:`177`
- Added wheels support for Debian-like distributions :pull_aer:`69`
- Added autoconfiguration of threads for qasm simulator :pull_aer:`61`
- Added Simulation method based on Stabilizer Rank Decompositions :pull_aer:`51`
- Added ``basis_gates`` kwarg to ``NoiseModel`` init :pull_aer:`175`.
- Added an optional parameter to ``NoiseModel.as_dict()`` for returning
  dictionaries that can be serialized using the standard json library directly
  :pull_aer:`165`
- Refactor thread management :pull_aer:`50`
- Improve noise transformations :pull_aer:`162`
- Improve error reporting :pull_aer:`160`
- Improve efficiency of parallelization with ``max_memory_mb`` a new parameter
  of ``backend_opts`` :pull_aer:`61`
- Improve u1 performance in ``statevector`` :pull_aer:`123`


Bug Fixes
---------

- Fixed OpenMP clashing problems on macOS for the Terra add-on :pull_aer:`46`




Compatibility Considerations
----------------------------

- Deprecated ``"initial_statevector"`` backend option for ``QasmSimulator`` and
  ``StatevectorSimulator`` :pull_aer:`185`
- Renamed ``"chop_threshold"`` backend option to ``"zero_threshold"`` and
  changed default value to 1e-10 :pull_aer:`185`



Ignis 0.1
=========

New Features
------------

* Quantum volume
* Measurement mitigation using tensored calibrations
* Simultaneous RB has the option to align Clifford gates across subsets
* Measurement correction can produce a new calibration for a subset of qubits



Compatibility Considerations
----------------------------

* RB writes to the minimal set of classical registers (it used to be
  Q[i]->C[i]). This change enables measurement correction with RB.
  Unless users had external analysis code, this will not change outcomes.
  RB circuits from 0.1 are not compatible with 0.1.1 fitters.




Aqua 0.5
========

New Features
------------

* Implementation of the HHL algorithm supporting ``LinearSystemInput``
* Pluggable component ``Eigenvalues`` with variant ``EigQPE``
* Pluggable component ``Reciprocal`` with variants ``LookupRotation`` and
  ``LongDivision``
* Multiple-Controlled U1 and U3 operations ``mcu1`` and ``mcu3``
* Pluggable component ``QFT`` derived from component ``IQFT``
* Summarized the transpiled circuits at the DEBUG logging level
* ``QuantumInstance`` accepts ``basis_gates`` and ``coupling_map`` again.
* Support to use ``cx`` gate for the entanglement in ``RY`` and ``RYRZ``
  variational form (``cz`` is the default choice)
* Support to use arbitrary mixer Hamiltonian in QAOA, allowing use of QAOA
  in constrained optimization problems [arXiv:1709.03489]
* Added variational algorithm base class ``VQAlgorithm``, implemented by
  ``VQE`` and ``QSVMVariational``
* Added ``ising/docplex.py`` for automatically generating Ising Hamiltonian
  from optimization models of DOcplex
* Added ``'basic-dirty-ancilla``' mode for ``mct``
* Added ``mcmt`` for Multi-Controlled, Multi-Target gate
* Exposed capabilities to generate circuits from logical AND, OR, DNF
  (disjunctive normal forms), and CNF (conjunctive normal forms) formulae
* Added the capability to generate circuits from ESOP (exclusive sum of
  products) formulae with optional optimization based on Quine-McCluskey and ExactCover
* Added ``LogicalExpressionOracle`` for generating oracle circuits from
  arbitrary Boolean logic expressions (including DIMACS support) with optional
  optimization capability
* Added ``TruthTableOracle`` for generating oracle circuits from truth-tables
  with optional optimization capability
* Added ``CustomCircuitOracle`` for generating oracle from user specified
  circuits
* Added implementation of the Deutsch-Jozsa algorithm
* Added implementation of the Bernstein-Vazirani algorithm
* Added implementation of the Simon's algorithm
* Added implementation of the Shor's algorithm
* Added optional capability for Grover's algorithm to take a custom
  initial state (as opposed to the default uniform superposition)
* Added capability to create a ``Custom`` initial state using existing
  circuit
* Added the ADAM (and AMSGRAD) optimization algorithm
* Multivariate distributions added, so uncertainty models now have univariate
  and multivariate distribution components
* Added option to include or skip the swaps operations for qft and iqft
  circuit constructions
* Added classical linear system solver ``ExactLSsolver``
* Added parameters ``auto_hermitian`` and ``auto_resize`` to ``HHL`` algorithm
  to support non-Hermitian and non :math:`2^n` sized matrices by default
* Added another feature map, ``RawFeatureVector``, that directly maps feature
  vectors to qubits' states for classification
* ``SVM_Classical`` can now load models trained by ``QSVM``



Bug Fixes
---------

* Fixed ``ising/docplex.py`` to correctly multiply constant values in constraints
* Fixed package setup to correctly identify namespace packages using
  ``setuptools.find_namespace_packages``



Compatibility Considerations
----------------------------

* ``QuantumInstance`` does not take ``memory`` anymore.
* Moved command line and GUI to separate repo
  (``qiskit_aqua_uis``)
* Removed the ``SAT``-specific oracle (now supported by
  ``LogicalExpressionOracle``)
* Changed ``advanced`` mode implementation of ``mct``: using simple ``h`` gates
  instead of ``ch``, and fixing the old recursion step in ``_multicx``
* Components ``random_distributions`` renamed to ``uncertainty_models``
* Reorganized the constructions of various common gates (``ch``, ``cry``,
  ``mcry``, ``mct``, ``mcu1``, ``mcu3``, ``mcmt``, ``logic_and``, and
  ``logic_or``) and circuits (``PhaseEstimationCircuit``,
  ``BooleanLogicCircuits``, ``FourierTransformCircuits``,
  and ``StateVectorCircuits``) under the ``circuits`` directory
* Renamed the algorithm ``QSVMVariational`` to ``VQC``, which stands for
  Variational Quantum Classifier
* Renamed the algorithm ``QSVMKernel`` to ``QSVM``
* Renamed the class ``SVMInput`` to ``ClassificationInput``
* Renamed problem type ``'svm_classification'`` to ``'classification'``
* Changed the type of ``entangler_map`` used in ``FeatureMap`` and
  ``VariationalForm`` to list of lists



IBM Q Provider 0.1
==================

New Features
------------

- This is the first release as a standalone package. If you
  are installing Terra standalone you'll also need to install the
  ``qiskit-ibmq-provider`` package with ``pip install qiskit-ibmq-provider`` if
  you want to use the IBM Q backends.

- Support for non-Qobj format jobs has been removed from
  the provider. You'll have to convert submissions in an older format to
  Qobj before you can submit.



**********
Qiskit 0.8
**********

In Qiskit 0.8 we introduced the Qiskit Ignis element. It also includes the
Qiskit Terra element 0.7.1 release which contains a bug fix for the BasicAer
Python simulator.

Terra 0.7
=========

No Change

Aer 0.1
=======

No Change

Ignis 0.1
=========

This is the first release of Qiskit Ignis.



**********
Qiskit 0.7
**********

In Qiskit 0.7 we introduced Qiskit Aer and combined it with Qiskit Terra.



Terra 0.7
=========

New Features
------------

This release includes several new features and many bug fixes. With this release
the interfaces for circuit diagram, histogram, bloch vectors, and state
visualizations are declared stable. Additionally, this release includes a
defined and standardized bit order/endianness throughout all aspects of Qiskit.
These are all declared as stable interfaces in this release which won't have
breaking changes made moving forward, unless there is appropriate and lengthy
deprecation periods warning of any coming changes.

There is also the introduction of the following new features:

- A new ASCII art circuit drawing output mode
- A new circuit drawing interface off of ``QuantumCircuit`` objects that
  enables calls of ``circuit.draw()`` or ``print(circuit)`` to render a drawing
  of circuits
- A visualizer for drawing the DAG representation of a circuit
- A new quantum state plot type for hinton diagrams in the local matplotlib
  based state plots
- 2 new constructor methods off the ``QuantumCircuit`` class
  ``from_qasm_str()`` and ``from_qasm_file()`` which let you easily create a
  circuit object from OpenQASM
- A new function ``plot_bloch_multivector()`` to plot Bloch vectors from a
  tensored state vector or density matrix
- Per-shot measurement results are available in simulators and select devices.
  These can be accessed by setting the ``memory`` kwarg to ``True`` when
  calling ``compile()`` or ``execute()`` and then accessed using the
  ``get_memory()`` method on the ``Result`` object.
- A ``qiskit.quantum_info`` module with revamped Pauli objects and methods for
  working with quantum states
- New transpile passes for circuit analysis and transformation:
  ``CommutationAnalysis``, ``CommutationTransformation``, ``CXCancellation``,
  ``Decompose``, ``Unroll``, ``Optimize1QGates``, ``CheckMap``,
  ``CXDirection``, ``BarrierBeforeFinalMeasurements``
- New alternative swap mapper passes in the transpiler:
  ``BasicSwap``, ``LookaheadSwap``, ``StochasticSwap``
- More advanced transpiler infrastructure with support for analysis passes,
  transformation passes, a global ``property_set`` for the pass manager, and
  repeat-until control of passes



Compatibility Considerations
----------------------------

As part of the 0.7 release the following things have been deprecated and will
either be removed or changed in a backwards incompatible manner in a future
release. While not strictly necessary these are things to adjust for before the
next release to avoid a breaking change.

- ``plot_circuit()``, ``latex_circuit_drawer()``, ``generate_latex_source()``,
  and ``matplotlib_circuit_drawer()`` from qiskit.tools.visualization are
  deprecated. Instead the ``circuit_drawer()`` function from the same module
  should be used, there are kwarg options to mirror the functionality of all
  the deprecated functions.
- The current default output of ``circuit_drawer()`` (using latex and falling
  back on python) is deprecated and will be changed to just use the ``text``
  output by default in future releases.
- The ``qiskit.wrapper.load_qasm_string()`` and
  ``qiskit.wrapper.load_qasm_file()`` functions are deprecated and the
  ``QuantumCircuit.from_qasm_str()`` and
  ``QuantumCircuit.from_qasm_file()`` constructor methods should be used
  instead.
- The ``plot_barriers`` and ``reverse_bits`` keys in the ``style`` kwarg
  dictionary are deprecated, instead the
  ``qiskit.tools.visualization.circuit_drawer()`` kwargs ``plot_barriers`` and
  ``reverse_bits`` should be used instead.
- The functions ``plot_state()`` and ``iplot_state()`` have been depreciated.
  Instead the functions ``plot_state_*()`` and ``iplot_state_*()`` should be
  called for the visualization method required.
- The ``skip_transpiler`` argument has been deprecated from ``compile()`` and
  ``execute()``. Instead you can use the ``PassManager`` directly, just set
  the ``pass_manager`` to a blank ``PassManager`` object with ``PassManager()``
- The ``transpile_dag()`` function ``format`` kwarg for emitting different
  output formats is deprecated, instead you should convert the default output
  ``DAGCircuit`` object to the desired format.
- The unrollers have been deprecated, moving forward only DAG to DAG unrolling
  will be supported.

Please note that some backwards-incompatible changes have been made during this
release. The following notes contain information on how to adapt to these
changes.

Changes to Result objects
^^^^^^^^^^^^^^^^^^^^^^^^^

As part of the rewrite of the Results object to be more consistent and a
stable interface moving forward a few changes have been made to how you access
the data stored in the result object. First the ``get_data()`` method has been
renamed to just ``data()``. Accompanying that change is a change in the data
format returned by the function. It is now returning the raw data from the
backends instead of doing any post-processing. For example, in previous
versions you could call::

   result = execute(circuit, backend).result()
   unitary = result.get_data()['unitary']
   print(unitary)

and that would return the unitary matrix like::

   [[1+0j, 0+0.5j], [0-0.5j][-1+0j]]

But now if you call (with the renamed method)::

   result.data()['unitary']

it will return something like::

   [[[1, 0], [0, -0.5]], [[0, -0.5], [-1, 0]]]

To get the post processed results in the same format as before the 0.7 release
you must use the ``get_counts()``, ``get_statevector()``, and ``get_unitary()``
methods on the result object instead of ``get_data()['counts']``,
``get_data()['statevector']``, and ``get_data()['unitary']`` respectively.

Additionally, support for ``len()`` and indexing on a ``Result`` object has
been removed. Instead you should deal with the output from the post processed
methods on the Result objects.

Also, the ``get_snapshot()`` and ``get_snapshots()`` methods from the
``Result`` class have been removed. Instead you can access the snapshots
using ``Result.data()['snapshots']``.


Changes to Visualization
^^^^^^^^^^^^^^^^^^^^^^^^

The largest change made to visualization in the 0.7 release is the removal of
Matplotlib and other visualization dependencies from the project requirements.
This was done to simplify the requirements and configuration required for
installing Qiskit. If you plan to use any visualizations (including all the
jupyter magics) except for the ``text``, ``latex``, and ``latex_source``
output for the circuit drawer you'll you must manually ensure that
the visualization dependencies are installed. You can leverage the optional
requirements to the Qiskit Terra package to do this::

   pip install qiskit-terra[visualization]

Aside from this there have been changes made to several of the interfaces
as part of the stabilization which may have an impact on existing code.
The first is the ``basis`` kwarg in the ``circuit_drawer()`` function
is no longer accepted. If you were relying on the ``circuit_drawer()`` to
adjust the basis gates used in drawing a circuit diagram you will have to
do this priort to calling ``circuit_drawer()``. For example::

   from qiskit.tools import visualization
   visualization.circuit_drawer(circuit, basis_gates='x,U,CX')

will have to be adjusted to be::

   from qiskit import BasicAer
   from qiskit import transpiler
   from qiskit.tools import visualization
   backend = BasicAer.backend('qasm_simulator')
   draw_circ = transpiler.transpile(circuit, backend, basis_gates='x,U,CX')
   visualization.circuit_drawer(draw_circ)

Moving forward the ``circuit_drawer()`` function will be the sole interface
for circuit drawing in the visualization module. Prior to the 0.7 release there
were several other functions which either used different output backends or
changed the output for drawing circuits. However, all those other functions
have been deprecated and that functionality has been integrated as options
on ``circuit_drawer()``.

For the other visualization functions, ``plot_histogram()`` and
``plot_state()`` there are also a few changes to check when upgrading. First
is the output from these functions has changed, in prior releases these would
interactively show the output visualization. However that has changed to
instead return a ``matplotlib.Figure`` object. This provides much more
flexibility and options to interact with the visualization prior to saving or
showing it. This will require adjustment to how these functions are consumed.
For example, prior to this release when calling::

   plot_histogram(counts)
   plot_state(rho)

would open up new windows (depending on matplotlib backend) to display the
visualization. However starting in the 0.7 you'll have to call ``show()`` on
the output to mirror this behavior. For example::

   plot_histogram(counts).show()
   plot_state(rho).show()

or::

   hist_fig = plot_histogram(counts)
   state_fig = plot_state(rho)
   hist_fig.show()
   state_fig.show()

Note that this is only for when running outside of Jupyter. No adjustment is
required inside a Jupyter environment because Jupyter notebooks natively
understand how to render ``matplotlib.Figure`` objects.

However, returning the Figure object provides additional flexibility for
dealing with the output. For example instead of just showing the figure you
can now directly save it to a file by leveraging the ``savefig()`` method.
For example::

   hist_fig = plot_histogram(counts)
   state_fig = plot_state(rho)
   hist_fig.savefig('histogram.png')
   state_fig.savefig('state_plot.png')

The other key aspect which has changed with these functions is when running
under jupyter. In the 0.6 release ``plot_state()`` and ``plot_histogram()``
when running under jupyter the default behavior was to use the interactive
Javascript plots if the externally hosted Javascript library for rendering
the visualization was reachable over the network. If not it would just use
the matplotlib version. However in the 0.7 release this no longer the case,
and separate functions for the interactive plots, ``iplot_state()`` and
``iplot_histogram()`` are to be used instead. ``plot_state()`` and
``plot_histogram()`` always use the matplotlib versions.

Additionally, starting in this release the ``plot_state()`` function is
deprecated in favor of calling individual methods for each method of plotting
a quantum state. While the ``plot_state()`` function will continue to work
until the 0.9 release, it will emit a warning each time it is used. The

==================================  ========================
Qiskit Terra 0.6                    Qiskit Terra 0.7+
==================================  ========================
plot_state(rho)                     plot_state_city(rho)
plot_state(rho, method='city')      plot_state_city(rho)
plot_state(rho, method='paulivec')  plot_state_paulivec(rho)
plot_state(rho, method='qsphere')   plot_state_qsphere(rho)
plot_state(rho, method='bloch')     plot_bloch_multivector(rho)
plot_state(rho, method='hinton')    plot_state_hinton(rho)
==================================  ========================

The same is true for the interactive JS equivalent, ``iplot_state()``. The
function names are all the same, just with a prepended `i` for each function.
For example, ``iplot_state(rho, method='paulivec')`` is
``iplot_state_paulivec(rho)``.

Changes to Backends
^^^^^^^^^^^^^^^^^^^

With the improvements made in the 0.7 release there are a few things related
to backends to keep in mind when upgrading. The biggest change is the
restructuring of the provider instances in the root  ``qiskit``` namespace.
The ``Aer`` provider is not installed by default and requires the installation
of the ``qiskit-aer`` package. This package contains the new high performance
fully featured simulator. If you installed via ``pip install qiskit`` you'll
already have this installed. The python simulators are now available under
``qiskit.BasicAer`` and the old C++ simulators are available with
``qiskit.LegacySimulators``. This also means that the implicit fallback to
python based simulators when the C++ simulators are not found doesn't exist
anymore. If you ask for a local C++ based simulator backend, and it can't be
found an exception will be raised instead of just using the python simulator
instead.

Additionally the previously deprecation top level functions ``register()`` and
``available_backends()`` have been removed. Also, the deprecated
``backend.parameters()`` and ``backend.calibration()`` methods have been
removed in favor of ``backend.properties()``. You can refer to the 0.6 release
notes section :ref:`backends` for more details on these changes.

The ``backend.jobs()`` and ``backend.retrieve_jobs()`` calls no longer return
results from those jobs. Instead you must call the ``result()`` method on the
returned jobs objects.

Changes to the compiler, transpiler, and unrollers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As part of an effort to stabilize the compiler interfaces there have been
several changes to be aware of when leveraging the compiler functions.
First it is important to note that the ``qiskit.transpiler.transpile()``
function now takes a QuantumCircuit object (or a list of them) and returns
a QuantumCircuit object (or a list of them). The DAG processing is done
internally now.

You can also easily switch between circuits, DAGs, and Qobj now using the
functions in ``qiskit.converters``.




Aer 0.1
=======

New Features
------------

Aer provides three simulator backends:

- ``QasmSimulator``: simulate experiments and return measurement outcomes
- ``StatevectorSimulator``: return the final statevector for a quantum circuit
  acting on the all zero state
- ``UnitarySimulator``: return the unitary matrix for a quantum circuit

``noise`` module: contains advanced noise modeling features for the
``QasmSimulator``

- ``NoiseModel``, ``QuantumError``, ``ReadoutError`` classes for simulating a
  Qiskit quantum circuit in the presence of errors
- ``errors`` submodule including functions for generating ``QuantumError``
  objects for the following types of quantum errors: Kraus, mixed unitary,
  coherent unitary, Pauli, depolarizing, thermal relaxation, amplitude damping,
  phase damping, combined phase and amplitude damping
- ``device`` submodule for automatically generating a noise model based on the
  ``BackendProperties`` of a device

``utils`` module:

- ``qobj_utils`` provides functions for directly modifying a Qobj to insert
  special simulator instructions not yet supported through the Qiskit Terra API.


Aqua 0.4
========

New Features
------------

- Programmatic APIs for algorithms and components -- each component can now be
  instantiated and initialized via a single (non-empty) constructor call
- ``QuantumInstance`` API for algorithm/backend decoupling --
  ``QuantumInstance`` encapsulates a backend and its settings
- Updated documentation and Jupyter Notebooks illustrating the new programmatic
  APIs
- Transparent parallelization for gradient-based optimizers
- Multiple-Controlled-NOT (cnx) operation
- Pluggable algorithmic component ``RandomDistribution``
- Concrete implementations of ``RandomDistribution``:
  ``BernoulliDistribution``, ``LogNormalDistribution``,
  ``MultivariateDistribution``, ``MultivariateNormalDistribution``,
  ``MultivariateUniformDistribution``, ``NormalDistribution``,
  ``UniformDistribution``, and ``UnivariateDistribution``
- Concrete implementations of ``UncertaintyProblem``:
  ``FixedIncomeExpectedValue``, ``EuropeanCallExpectedValue``, and
  ``EuropeanCallDelta``
- Amplitude Estimation algorithm
- Qiskit Optimization: New Ising models for optimization problems exact cover,
  set packing, vertex cover, clique, and graph partition
- Qiskit AI:

  - New feature maps extending the ``FeatureMap`` pluggable interface:
    ``PauliExpansion`` and ``PauliZExpansion``
  - Training model serialization/deserialization mechanism

- Qiskit Finance:

  - Amplitude estimation for Bernoulli random variable: illustration of
    amplitude estimation on a single qubit problem
  - Loading of multiple univariate and multivariate random distributions
  - European call option: expected value and delta (using univariate
    distributions)
  - Fixed income asset pricing: expected value (using multivariate
    distributions)

- The Pauli string in ``Operator`` class is aligned with Terra 0.7. Now the
  order of a n-qubit pauli string is ``q_{n-1}...q{0}`` Thus, the (de)serialier
  (``save_to_dict`` and ``load_from_dict``) in the ``Operator`` class are also
  changed to adopt the changes of ``Pauli`` class.

Compatibility Considerations
----------------------------

- ``HartreeFock`` component of pluggable type ``InitialState`` moved to Qiskit
  Chemistry
- ``UCCSD`` component of pluggable type ``VariationalForm`` moved to Qiskit
  Chemistry


**********
Qiskit 0.6
**********

Terra 0.6
=========

Highlights
----------

This release includes a redesign of internal components centered around a new,
formal communication format (Qobj), along with long awaited features to
improve the user experience as a whole. The highlights, compared to the 0.5
release, are:

- Improvements for inter-operability (based on the Qobj specification) and
  extensibility (facilities for extending Qiskit with new backends in a
  seamless way)
- New options for handling credentials and authentication for the IBM Q
  backends, aimed at simplifying the process and supporting automatic loading
  of user credentials
- A revamp of the visualization utilities: stylish interactive visualizations
  are now available for Jupyter users, along with refinements for the circuit
  drawer (including a matplotlib-based version)
- Performance improvements centered around circuit transpilation: the basis for
  a more flexible and modular architecture have been set, including
  parallelization of the circuit compilation and numerous optimizations


Compatibility Considerations
----------------------------

Please note that some backwards-incompatible changes have been introduced
during this release -- the following notes contain information on how to adapt
to the new changes.

Removal of ``QuantumProgram``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As hinted during the 0.5 release, the deprecation of the  ``QuantumProgram``
class has now been completed and is no longer available, in favor of working
with the individual components (:class:`~qiskit.backends.basejob.BaseJob`,
:class:`~qiskit._quantumcircuit.QuantumCircuit`,
:class:`~qiskit._classicalregister.ClassicalRegister`,
:class:`~qiskit._quantumregister.QuantumRegister`,
:mod:`~qiskit`) directly.

Please check the :ref:`0.5 release notes <quantum-program-0-5>` and the
examples for details about the transition::


  from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
  from qiskit import Aer, execute

  q = QuantumRegister(2)
  c = ClassicalRegister(2)
  qc = QuantumCircuit(q, c)

  qc.h(q[0])
  qc.cx(q[0], q[1])
  qc.measure(q, c)

  backend = get_backend('qasm_simulator')

  job_sim = execute(qc, backend)
  sim_result = job_sim.result()

  print("simulation: ", sim_result)
  print(sim_result.get_counts(qc))


IBM Q Authentication and ``Qconfig.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The managing of credentials for authenticating when using the IBM Q backends has
been expanded, and there are new options that can be used for convenience:

1. save your credentials in disk once, and automatically load them in future
   sessions. This provides a one-off mechanism::

     from qiskit import IBMQ
     IBMQ.save_account('MY_API_TOKEN', 'MY_API_URL')

   afterwards, your credentials can be automatically loaded from disk by invoking
   :meth:`~qiskit.backends.ibmq.ibmqprovider.IBMQ.load_accounts`::

     from qiskit import IBMQ
     IBMQ.load_accounts()

   or you can load only specific accounts if you only want to use those in a session::

     IBMQ.load_accounts(project='MY_PROJECT')

2. use environment variables. If ``QE_TOKEN`` and ``QE_URL`` is set, the
   ``IBMQ.load_accounts()`` call will automatically load the credentials from
   them.

Additionally, the previous method of having a ``Qconfig.py`` file in the
program folder and passing the credentials explicitly is still supported.


.. _backends:

Working with backends
^^^^^^^^^^^^^^^^^^^^^

A new mechanism has been introduced in Terra 0.6 as the recommended way for
obtaining a backend, allowing for more powerful and unified filtering and
integrated with the new credentials system. The previous top-level methods
:meth:`~qiskit.wrapper._wrapper.register`,
:meth:`~qiskit.wrapper._wrapper.available_backends` and
:meth:`~qiskit.wrapper._wrapper.get_backend` are still supported, but will
deprecated in upcoming versions in favor of using the `qiskit.IBMQ` and
`qiskit.Aer` objects directly, which allow for more complex filtering.

For example, to list and use a local backend::

  from qiskit import Aer

  all_local_backends = Aer.backends(local=True)  # returns a list of instances
  qasm_simulator = Aer.backends('qasm_simulator')

And for listing and using remote backends::

  from qiskit import IBMQ

  IBMQ.enable_account('MY_API_TOKEN')
  5_qubit_devices = IBMQ.backends(simulator=True, n_qubits=5)
  ibmqx4 = IBMQ.get_backend('ibmqx4')

Please note as well that the names of the local simulators have been
simplified. The previous names can still be used, but it is encouraged to use
the new, shorter names:

=============================  ========================
Qiskit Terra 0.5               Qiskit Terra 0.6
=============================  ========================
'local_qasm_simulator'         'qasm_simulator'
'local_statevector_simulator'  'statevector_simulator'
'local_unitary_simulator_py'   'unitary_simulator'
=============================  ========================


Backend and Job API changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Jobs submitted to IBM Q backends have improved capabilities. It is possible
  to cancel them and replenish credits (``job.cancel()``), and to retrieve
  previous jobs executed on a specific backend either by job id
  (``backend.retrieve_job(job_id)``) or in batch of latest jobs
  (``backend.jobs(limit)``)

* Properties for checking each individual job status (``queued``, ``running``,
  ``validating``, ``done`` and ``cancelled``) no longer exist. If you
  want to check the job status, use the identity comparison against
  ``job.status``::

    from qiskit.backends import JobStatus

    job = execute(circuit, backend)
    if job.status() is JobStatus.RUNNING:
        handle_job(job)

Please consult the new documentation of the
:class:`~qiskit.backends.ibmq.ibmqjob.IBMQJob` class to get further insight
in how to use the simplified API.

* A number of members of :class:`~qiskit.backends.basebackend.BaseBackend`
  and :class:`~qiskit.backends.basejob.BaseJob` are no longer properties,
  but methods, and as a result they need to be invoked as functions.

  =====================  ========================
  Qiskit Terra 0.5       Qiskit Terra 0.6
  =====================  ========================
  backend.name           backend.name()
  backend.status         backend.status()
  backend.configuration  backend.configuration()
  backend.calibration    backend.properties()
  backend.parameters     backend.jobs()
                         backend.retrieve_job(job_id)
  job.status             job.status()
  job.cancelled          job.queue_position()
  job.running            job.cancel()
  job.queued
  job.done
  =====================  ========================


Better Jupyter tools
^^^^^^^^^^^^^^^^^^^^

The new release contains improvements to the user experience while using
Jupyter notebooks.

First, new interactive visualizations of counts histograms and quantum states
are provided:
:meth:`~qiskit.tools.visualization.plot_histogram` and
:meth:`~qiskit.tools.visualization.plot_state`.
These methods will default to the new interactive kind when the environment
is Jupyter and internet connection exists.

Secondly, the new release provides Jupyter cell magics for keeping track of
the progress of your code. Use ``%%qiskit_job_status`` to keep track of the
status of submitted jobs to IBM Q backends. Use ``%%qiskit_progress_bar`` to
keep track of the progress of compilation/execution.



**********
Qiskit 0.5
**********

Terra 0.5
=========

Highlights
----------

This release brings a number of improvements to Qiskit, both for the user
experience and under the hood. Please refer to the full changelog for a
detailed description of the changes - the highlights are:

* new ``statevector`` :mod:`simulators <qiskit.backends.local>` and feature and
  performance improvements to the existing ones (in particular to the C++
  simulator), along with a reorganization of how to work with backends focused
  on extensibility and flexibility (using aliases and backend providers)
* reorganization of the asynchronous features, providing a friendlier interface
  for running jobs asynchronously via :class:`Job` instances
* numerous improvements and fixes throughout the Terra as a whole, both for
  convenience of the users (such as allowing anonymous registers) and for
  enhanced functionality (such as improved plotting of circuits)


Compatibility Considerations
----------------------------

Please note that several backwards-incompatible changes have been introduced
during this release as a result of the ongoing development. While some of these
features will continue to be supported during a period of time before being
fully deprecated, it is recommended to update your programs in order to prepare
for the new versions and take advantage of the new functionality.

.. _quantum-program-0-5:


``QuantumProgram`` changes
^^^^^^^^^^^^^^^^^^^^^^^^^^

Several methods of the :class:`~qiskit.QuantumProgram` class are on their way
to being deprecated:

* methods for interacting **with the backends and the API**:

  The recommended way for opening a connection to the IBM Q API and for using
  the backends is through the
  top-level functions directly instead of
  the ``QuantumProgram`` methods. In particular, the
  :func:`qiskit.register` method provides the equivalent of the previous
  :func:`qiskit.QuantumProgram.set_api` call. In a similar vein, there is a new
  :func:`qiskit.available_backends`, :func:`qiskit.get_backend` and related
  functions for querying the available backends directly. For example, the
  following snippet for version 0.4::

    from qiskit import QuantumProgram

    quantum_program = QuantumProgram()
    quantum_program.set_api(token, url)
    backends = quantum_program.available_backends()
    print(quantum_program.get_backend_status('ibmqx4')

  would be equivalent to the following snippet for version 0.5::

    from qiskit import register, available_backends, get_backend

    register(token, url)
    backends = available_backends()
    backend = get_backend('ibmqx4')
    print(backend.status)

* methods for **compiling and executing programs**:

  The top-level functions now also provide
  equivalents for the :func:`qiskit.QuantumProgram.compile` and
  :func:`qiskit.QuantumProgram.execute` methods. For example, the following
  snippet from version 0.4::

    quantum_program.execute(circuit, args, ...)

  would be equivalent to the following snippet for version 0.5::

    from qiskit import execute

    execute(circuit, args, ...)

In general, from version 0.5 onwards we encourage to try to make use of the
individual objects and classes directly instead of relying on
``QuantumProgram``. For example, a :class:`~qiskit.QuantumCircuit` can be
instantiated and constructed by appending :class:`~qiskit.QuantumRegister`,
:class:`~qiskit.ClassicalRegister`, and gates directly. Please check the
update example in the Quickstart section, or the
``using_qiskit_core_level_0.py`` and ``using_qiskit_core_level_1.py``
examples on the main repository.

Backend name changes
^^^^^^^^^^^^^^^^^^^^

In order to provide a more extensible framework for backends, there have been
some design changes accordingly:

* **local simulator names**

  The names of the local simulators have been homogenized in order to follow
  the same pattern: ``PROVIDERNAME_TYPE_simulator_LANGUAGEORPROJECT`` -
  for example, the C++ simulator previously named ``local_qiskit_simulator``
  is now ``local_qasm_simulator_cpp``. An overview of the current
  simulators:

  * ``QASM`` simulator is supposed to be like an experiment. You apply a
    circuit on some qubits, and observe measurement results - and you repeat
    for many shots to get a histogram of counts via ``result.get_counts()``.
  * ``Statevector`` simulator is to get the full statevector (:math:`2^n`
    amplitudes) after evolving the zero state through the circuit, and can be
    obtained via ``result.get_statevector()``.
  * ``Unitary`` simulator is to get the unitary matrix equivalent of the
    circuit, returned via ``result.get_unitary()``.
  * In addition, you can get intermediate states from a simulator by applying
    a ``snapshot(slot)`` instruction at various spots in the circuit. This will
    save the current state of the simulator in a given slot, which can later
    be retrieved via ``result.get_snapshot(slot)``.

* **backend aliases**:

  The SDK now provides an "alias" system that allows for automatically using
  the most performant simulator of a specific type, if it is available in your
  system. For example, with the following snippet::

    from qiskit import get_backend

    backend = get_backend('local_statevector_simulator')

  the backend will be the C++ statevector simulator if available, falling
  back to the Python statevector simulator if not present.

More flexible names and parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Several functions of the SDK have been made more flexible and user-friendly:

* **automatic circuit and register names**

  :class:`qiskit.ClassicalRegister`, :class:`qiskit.QuantumRegister` and
  :class:`qiskit.QuantumCircuit` can now be instantiated without explicitly
  giving them a name - a new autonaming feature will automatically assign them
  an identifier::

    q = QuantumRegister(2)

  Please note as well that the order of the parameters have been swapped
  ``QuantumRegister(size, name)``.

* **methods accepting names or instances**

  In combination with the autonaming changes, several methods such as
  :func:`qiskit.Result.get_data` now accept both names and instances for
  convenience. For example, when retrieving the results for a job that has a
  single circuit such as::

    qc = QuantumCircuit(..., name='my_circuit')
    job = execute(qc, ...)
    result = job.result()

  The following calls are equivalent::

    data = result.get_data('my_circuit')
    data = result.get_data(qc)
    data = result.get_data()
