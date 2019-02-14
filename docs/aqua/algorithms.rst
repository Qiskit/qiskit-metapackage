.. _algorithms:

==========
Algorithms
==========

Aqua is an extensible collection of algorithms and utilities for use with quantum computers to
carry out research and investigate how to solve problems using near-term
quantum applications on short depth circuits. The applications can span
different domains. Aqua uses
`Terra <https://www.qiskit.org/terra>`__ for the generation, compilation and execution
of the quantum circuits modeling the specific problems.

The following `quantum algorithms <#quantum-algorithms>`__ are part of Aqua:

-  :ref:`Variational Quantum Eigensolver (VQE)`
-  :ref:`Quantum Approximate Optimization Algorithm (QAOA)`
-  :ref:`Evolution of Hamiltonian (EOH)`
-  :ref:`Quantum Phase Estimation (QPE)`
-  :ref:`Iterative Quantum Phase Estimation (IQPE)`
-  :ref:`Amplitude Estimation`
-  :ref:`Quantum Grover Search`
-  :ref:`Deutsch Jozsa`
-  :ref:`Bernstein Vazirani`
-  :ref:`Simon`
-  :ref:`Support Vector Machine Quantum Kernel (QSVM Kernel)`
-  :ref:`Support Vector Machine Variational (QSVM Variational)`
-  :ref:`HHL algorithm for solving linear systems (HHL)`

Aqua includes  also some `classical algorithms <#classical-reference-algorithms>`__
for generating reference values. This feature of Aqua may be
useful to quantum algorithm researchers interested in generating, comparing and contrasting
results in the near term while experimenting with, developing and testing
quantum algorithms:

-  :ref:`Exact Eigensolver`
-  :ref:`CPLEX Ising`
-  :ref:`Support Vector Machine Radial Basis Function Kernel (SVM Classical)`

.. topic:: Extending the Algorithm Library

    Algorithms and many of the components they use have been designed to be
    pluggable. A new algorithm may be developed according to the specific Application Programming Interface (API)
    provided by Aqua, and by simply adding its code to the collection of existing
    algorithms, that new algorithm  will be immediately recognized via dynamic lookup,
    and made available for use within the framework of Aqua.
    Specifically, to develop and deploy any new algorithm, the new algorithm class should derive from the ``QuantumAlgorithm`` class.
    Along with any supporting  module, for immediate dynamic discovery, the new algorithm class
    can simply be placed in an appropriate folder in the ``qiskit_aqua\algorithms`` directory, just like the
    existing algorithms.  Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new components can register themselves
    as Aqua extensions and be dynamically discovered at run time independent of their
    location in the file system.
    This is done in order to encourage researchers and
    developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research contributions.


.. seealso::

    Section :ref:`aqua-extending` provides more
    details on how to extend Aqua with new components.


.. _mct:

.. topic:: Multiple-Control Toffoli (MCT) Operation

    The *Multiple-Control Toffoli (mct)* operation, as the name suggests, is
    a generalization of the quantum Toffoli gate s.t. one target qubit is
    controlled by an arbitrary number of control qubits for a NOT (`x`) operation.
    The MCT operation can be used as the building block
    for implementing various different quantum algorithms, such as Grover's
    search algorithm.

    For the different numbers 0, 1, 2, … of controls, we have corresponding
    quantum gates ``x``, ``cx``, ``ccx``, ... The first three are basic/well-known
    quantum gates. In Aqua, the mct operation provides support for arbitrary
    numbers of controls, in particular, 3 or above.

    Currently three different implementation strategies are included: *basic*,
    *advanced*, and *noancilla*. The basic mode employs a textbook
    implementation, where a series of ``ccx`` Toffoli gates are linked
    together in a ``V`` shape to achieve the desired Multiple-Control Toffoli
    operation. This mode requires :math:`n-2` ancillary qubits, where
    :math:`n` is the number of controls. For the advanced mode, the ``cccx``
    and ``ccccx`` operations are achieved without needing ancillary
    qubits. Multiple-Control Toffoli operations for higher
    number of controls (5 and above) are implemented recursively using these
    lower-number-of-control cases. For the noancilla mode, no ancillary
    qubits are needed even for higher number of controls. This uses a
    technique of spliting multiple-control Toffoli operations, which is
    efficient up to 8 controls but gets inefficient in the number of required
    basic gates for values above. This technique relies on ``mcu1``, see
    :ref:`mcux` for more information.

    Aqua's mct operation can be invoked from a ``QuantumCircuit`` object
    using the ``mct`` API, which expects a list ``q_controls`` of control qubits,
    a target qubit ``q_target``, and a list ``q_ancilla`` of ancillary qubits.
    An optional keyword argument ``mode`` can also be passed in to indicate
    whether the ``'basic'``, ``'advanced'``, or ``'noancilla'`` mode is chosen.
    If omitted, this argument defaults to ``'basic'``.


.. _mcux:

.. topic:: Multiple-Control U1 and U3 Rotation (MCU1 and MCU3) Operation

    The *Multiple-Control Rotation (mcu)* operation, implements a U1 (`u1`)
    or a U3 (`u3`) rotation gate on a single target qubit with an arbitrary
    number of control qubits. The MCU1 operation takes one rotation angle
    as input parameter, whereas the MCU3 operation takes three for arbitrary
    rotations. No ancillary qubits are needed. It is efficiently implemented
    by using a grey code sequence for up to 8 control qubits. For larger
    number of controls this implementation gets very inefficient.

    Aqua's mcu1 and mcu3 operations can be invoked from a ``QuantumCircuit``
    object and expect a list ``control_qubits`` of control qubits and a target
    qubit ``target_qubit`` as well as an angle ``theta`` for the mcu1 and
    additionally two angles ``phi`` and ``lam`` for the mcu3.


.. _mcmt:

.. topic:: Multiple-Control Multiple-Target (MCMT) Operation

    The *Multiple-Control Multiple-Target (mcmt)* operation, as the name suggests,
    allows to generalize a single-control, single-target gate (such as `cz`) to
    support multiple control qubits and multiple target qubits.
    In other words, the single-control gate passed as argument is applied to all
    the target qubits if all the control qubits are active.

    The kind of gate to apply can be passed as a parameter and should be a single
    control gate already defined for a ``QuantumCircuit`` object (such as
    ``QuantumCircuit.cz`` or ``QuantumCircuit.ch``).

    Currently, just one implementation strategy is implemented: *basic*. It
    employs almost the same strategy adopted for the basic mode of `mct`:
    multiple Toffoli gates are chained together to get the logical `AND` of
    all the control qubits on a single ancilla qubit, which is then used as the
    control of the single-control gate function.

    This mode requires :math:`n-1` ancillary qubits, where :math:`n` is the
    number of controls. Compare this with ``mct`` mode which uses :math:`n-2`
    ancillary qubits for the same strategy. The difference is due to the fact
    that in ``mct`` the chain ends with a single ``ccx`` writing on the target
    qubit, while in ``mcmt`` the chain ends with the ``ccx`` writing on an
    ancillary qubit, which is then used as the control qubit of the single-control
    gate function.

    Aqua's mcmt operation can be invoked from a ``QuantumCircuit`` object
    using the ``mcmt`` API, which expects a list ``q_controls`` of control qubits,
    a list ``q_targets`` of target qubits, a list ``q_ancilla`` of ancillary qubits
    that must be off and are promised to be off after the function call, and a
    function ``single_control_gate_fun`` which is the generic function to
    apply to the ``q_targets`` qubits. An optional keyword argument ``mode`` can
    also be passed in to indicate the mode, but at the moment only the ``'basic'``
    mode is supported. If omitted, this argument defaults to ``'basic'``.


.. _logic_expr:

.. topic:: Circuit Construction for Logic Expressions

    Aqua includes utilities for constructing circuits for simple logic expressions.
    Currently three types of logic expressions are supported:
    Conjunctive Normal Forms (``CNF``), Disjunctive Normal Forms (``DNF``), and
    Exclusive Sum of Products (``ESOP``).
    These utilities are used internally by Aqua for constructing :ref:`oracles`,
    and can be accessed programmatically to build circuits for other purposes.
    For initialization of each of the three types of objects,
    the corresponding logic expression
    can be specified as a list of lists of non-zero integers,
    where each integer's absolute value indicates a variable,
    and a negative sign would indicate the negation of the corresponding variable.
    The logic operations represented by the inner and outer lists
    depend on the particular type (CNF, DNF, or ESOP) of objects being created.

    The current implementations use Aqua's :ref:`mct` operations,
    where no optimizations (e.g. minimization)
    are carried out on the input logic expressions, yet.


.. _quantum-algorithms:

------------------
Quantum Algorithms
------------------

In this section, we describe the quantum algorithms currently available in Aqua.

.. note::

    Aqua requires associating a quantum device or simulator to any experiment that uses a quantum
    algorithm.  This is done by configuring the ``"backend"`` section of the experiment to be run.
    Consult the documentation on the :ref:`aqua-input-file` for more details.

.. _vqe:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Variational Quantum Eigensolver (VQE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`VQE <https://arxiv.org/abs/1304.3061>`__ is a hybrid algorithm that uses
the variational approach and interleaves quantum and classical computations in order to find
the minimum eigenvalue of the Hamiltonian :math:`H` of a given system.
An instance of VQE requires defining two algorithmic subcomponents:
a trial function from Aqua's :ref:`variational-forms` library, and a classical optimizer
from Aqua's :ref:`optimizers` library.  An initial state from Aqua's
:ref:`initial-states` library may be supplied too in order to
define the starting state for the trial function.

.. seealso::

    Refer to the documentation of :ref:`variational-forms`, :ref:`optimizers`
    and :ref:`initial-states` for more details.

Additionally, VQE can be configured with the following parameters:

-  A ``str`` value indicating the mode used by the ``Operator`` class for the computation:

   .. code:: python

       operator_mode : "matrix" | "paulis" | "grouped_paulis"

   If no value for ``operator_mode`` is specified, the default is ``"matrix"``.

-  The initial point for the search of the minimum eigenvalue:

   .. code:: python

       initial_point : [float, float, ... , float]

   An optional list of ``float`` values  may be provided as the starting point for the search of the minimum eigenvalue.
   This feature is particularly useful when there are reasons to believe that the
   solution point is close to a particular point, which can then be provided as the preferred initial point.  As an example,
   when building the dissociation profile of a molecule, it is likely that
   using the previous computed optimal solution as the starting initial point for the next interatomic distance is going
   to reduce the number of iterations necessary for the variational algorithm to converge.  Aqua provides
   `a tutorial detailing this use case <https://github.com/Qiskit/aqua-tutorials/blob/master/chemistry/h2_vqe_initial_point.ipynb>`__.

   The length of the ``initial_point`` list value must match the number of the parameters expected by the variational form being used.
   If the user does not supply a preferred initial point, then VQE will look to the variational form for a preferred value.
   If the variational form returns ``None``,
   then a random point will be generated within the parameter bounds set, as per above.
   If the variational form provides ``None`` as the lower bound, then VQE
   will default it to :math:`-2\pi`; similarly, if the variational form returns ``None`` as the upper bound, the default value will be :math:`2\pi`.


.. topic:: Declarative Name

   When referring to VQE declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``VQE``.

.. topic:: Problems Supported

   In Aqua, VQE supports the ``energy`` and ``ising`` problems.

.. _qaoa:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Quantum Approximate Optimization Algorithm (QAOA)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`QAOA <https://arxiv.org/abs/1411.4028>`__ is a well-known algorithm for finding approximate solutions to
combinatorial-optimization problems.
The QAOA implementation in Aqua directly uses `VQE <#variational-quantum-eigensolver-vqe>`__ for its general hybrid optimization structure.
However, unlike VQE, which can be configured with arbitrary variational forms,
QAOA uses its own fine-tuned variational form, which comprises :math:`p` parameterized global :math:`x` rotations and
:math:`p` different parameterizations of the problem hamiltonian.
As a result, unlike VQE, QAOA does not need to have a variational form specified as an input parameter,
and is configured mainly by a single integer parameter, ``p``,
which dictates the depth of the variational form, and thus affects the approximation quality.
An initial state from Aqua's :ref:`initial-states` library may be supplied as well.


.. seealso::

    Consult the documentation on :ref:`optimizers` and :ref:`initial-states` for more details.

In summary, QAOA can be configured with the following parameters:

-  A ``str`` value indicating the mode used by the ``Operator`` class for the computation:

   .. code:: python

       operator_mode : "matrix" | "paulis" | "grouped_paulis"

   If no value for ``operator_mode`` is specified, the default is ``"matrix"``.

-  A positive ``int`` value configuring the QAOA variational form depth, as discussed above:

   .. code:: python

       p = 1 | 2 | ...

   This has to be a positive ``int`` value.  The default is ``1``.

-  The initial point for the search of the minimum eigenvalue:

   .. code:: python

       initial_point : [float, float, ... , float]

   An optional list of :math:`2p` ``float`` values  may be provided as the starting ``beta`` and ``gamma`` parameters
   (as identically named in the original `QAOA paper <https://arxiv.org/abs/1411.4028>`__) for the QAOA variational form.
   If such list is not provided, QAOA will simply start with the all-zero vector.

Similar to VQE, an optimizer may also be specified.

.. topic:: Declarative Name

   When referring to QAOA declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it,
   is ``QAOA.Variational``.

.. topic:: Problems Supported

   In Aqua, QAOA supports the ``ising`` problem.

.. _dynamics:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Evolution of Hamiltonian (EOH)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

EOH provides the lower-level building blocks for simulating
universal quantum systems. For any given quantum system that can be
decomposed into local interactions (for example, a global hamiltonian as
the weighted sum of several Pauli spin operators), the local
interactions can then be used to approximate the global quantum system
via, for example, Lloyd’s method or Trotter-Suzuki decomposition.

.. warning::

    This algorithm only supports the local state vector simulator.

EOH can be configured with the following parameter settings:

-  Evolution time:

   .. code:: python

       evo_time : float

   A ``float`` value is expected.  The minimum value is ``0.0``.  The default value is ``1.0``.

-  The evolution mode of the computation:

   .. code:: python

       evo_mode = "matrix" | "circuit"

   Two ``str`` values are permitted: ``"matrix"`` or ``"circuit"``, with ``"circuit"`` being the default.

-  The number of time slices:

   .. code:: python

       num_time_slices = 0 | 1 | ...

   This has to be a non-negative ``int`` value.  The default is ``1``.

-  The expansion mode:

   .. code:: python

       expansion_mode = "trotter" | "suzuki"

   Two ``str`` values are permitted: ``"trotter"`` (Lloyd's method) or ``"suzuki"`` (for Trotter-Suzuki expansion),
   with  ``"trotter"`` being the default one.

-  The expansion order:

   .. code:: python

       expansion_order = 1 | 2 | ...

   This parameter sets the Trotter-Suzuki expansion order.  A positive ``int`` value is expected.  The default value is ``2``.

.. topic:: Declarative Name

   When referring to EOH declaratively inside Aqua, its code ``name``, by which
   Aqua dynamically discovers and loads it, is ``EOH``.

.. topic:: Problems Supported

   In Aqua, EOH supports the ``eoh`` problem.

.. _qpe:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Quantum Phase Estimation (QPE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

QPE (also sometimes abbreviated
as PEA, for *Phase Estimation Algorithm*), takes two quantum registers, *control* and *target*, where the
control consists of several qubits initially put in uniform
superposition, and the target a set of qubits prepared in an eigenstate
(or, oftentimes, a guess of the eigenstate) of the unitary operator of
a quantum system. QPE then evolves the target under the control using
:ref:`Dynamics` on the unitary operator. The information of the
corresponding eigenvalue is then *kicked-back* into the phases of the
control register, which can then be deconvoluted by an Inverse Quantum
Fourier Transform (IQFT), and measured for read-out in binary decimal
format.  QPE also requires a reasonably good estimate of the eigen wave function
to start the process. For example, when estimating molecular ground energies,
the :ref:`Hartree-Fock` method could be used to provide such trial eigen wave
functions.

.. seealso::

    Consult the documentation on :ref:`iqfts` and :ref:`initial-states`
    for more details.

In addition to requiring an IQFT and an initial state as part of its
configuration, QPE also exposes the following parameter settings:

-  The number of time slices:

   .. code:: python

       num_time_slices = 0 | 1 | ...

   This has to be a non-negative ``int`` value.  The default value is ``1``.

-  The expansion mode:

   .. code:: python

       expansion_mode = "trotter" | "suzuki"

   Two ``str`` values are permitted: ``"trotter"`` (Lloyd's method) or ``"suzuki"`` (for Trotter-Suzuki expansion),
   with  ``"trotter"`` being the default one.

-  The expansion order:

   .. code:: python

       expansion_order = 1 | 2 | ...

   This parameter sets the Trotter-Suzuki expansion order.  A positive ``int`` value is expected.  The default value is ``2``.

-  The number of ancillae:

   .. code:: python

       num_ancillae = 1 | 2 | ...

   This parameter sets the number of ancillary qubits to be used by QPE.  A positive ``int`` value is expected.
   The default value is ``1``.

.. topic:: Declarative Name

   When referring to QPE declaratively inside Aqua, its code ``name``, by which
   Aqua dynamically discovers and loads it, is ``QPE``.

.. topic:: Problems Supported

   In Aqua, QPE supports the ``energy`` problem.

.. _iqpe:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Iterative Quantum Phase Estimation (IQPE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IQPE, as its name
suggests, iteratively computes the phase so as to require fewer qubits.
It takes in the same set of parameters as `QPE <#quantum-phase-estimation-qpe>`__, except for the number of
ancillary qubits ``num_ancillae``, which is replaced by
``num_iterations`` (a positive ``int``, also defaulted to ``1``), and for the fact that an
Inverse Quantum Fourier Transform (IQFT) is not used for IQPE.

.. seealso::

    For more details, please see `arXiv:quant-ph/0610214 <https://arxiv.org/abs/quant-ph/0610214>`__.

.. topic:: Declarative Name

    When referring to IQPE declaratively inside Aqua, its code ``name``, by which
    Aqua dynamically discovers and loads it, is ``IQPE``.

.. topic:: Problems Supported

    In Aqua, IQPE supports the ``energy`` problem.


.. _ae:

^^^^^^^^^^^^^^^^^^^^
Amplitude Estimation
^^^^^^^^^^^^^^^^^^^^

*Amplitude Estimation* is a derivative of -  :ref:`Quantum Phase Estimation (QPE)`
applied to a particular operator :math:`A`.
:math:`A` is assumed to operate on :math:`n + 1` qubits (plus possible ancillary qubits)
where the :math:`n` qubits represent the uncertainty (in the form of a random distribution from the
:ref:`random-distributions` library)
and the last qubit, called the *objective qubit*, is used to represent the normalized objective value as its amplitude.
In other words,
:math:`A` is constructed such that the probability of measuring a '1' in the objective qubit is equal to the
value of interest.

.. seealso::

    Consult the documentation on -  :ref:`Quantum Phase Estimation (QPE)` for more details.
    Also, see `arXiv:1806.06893 <https://arxiv.org/abs/1806.06893>`_ for more details on Amplitude Estimation
    as well as its applications on finance problems.

In addition to relying on a ``QPE`` component
for building the Quantum Phase Estimation circuit,
in order to be properly constructed, an ``AmplitudeEstimation`` algorithm object
expects the following inputs:

-  The number of evaluation qubits:

   .. code:: python

       num_eval_qubits = 1 | 2 | ...

   This has to be a positive ``int`` value.

-  The uncertainty problem:

   .. code:: python

       a_factory

   A ``CircuitFactory`` object that represents the uncertainty problem, i.e., the :math:`A` operator mentioned above.

-  The optional problem unitary:

   .. code:: python

       q_factory

   An optional ``CircuitFactory`` object that represents the problem unitary,
   which, if left unspecified, will be automatically constructed from the ``a_factory``.

-  The Inverse Quantum Fourier Transform component:

   .. code:: python

       iqft

   The Inverse Quantum Fourier Transform pluggable component
   that's to be used to configure the ``PhaseEstimation`` component.
   The standard iqft will be used by default if left None.

.. topic:: Declarative Name

   When referring to Amplitude Estimation declaratively inside Aqua, its code ``name``, by which
   Aqua dynamically discovers and loads it, is ``AmplitudeEstimation``.

.. topic:: Problems Supported

   In Aqua, Amplitude Estimation supports the ``uncertainty`` problem.


.. _grover:

^^^^^^^^^^^^^^^^^^^^^
Quantum Grover Search
^^^^^^^^^^^^^^^^^^^^^

Grover’s Search is a well known quantum algorithm for searching through
unstructured collections of records for particular targets with quadratic
speedup compared to classical algorithms.

Given a set :math:`X` of :math:`N` elements :math:`X=\{x_1,x_2,\ldots,x_N\}`
and a boolean function :math:`f : X \rightarrow \{0,1\}`, the goal on an
*unstructured-search problem* is to find an element :math:`x^* \in X` such
that :math:`f(x^*)=1`.
Unstructured search is often alternatively formulated as a database search
problem, in which, given a database, the goal is to find in it an item that
meets some specification.
The search is called *unstructured* because there are no guarantees as to how
the database is ordered.  On a sorted database, for instance, one could perform
binary search to find an element in :math:`\mathbb{O}(\log N)` worst-case time.
Instead, in an unstructured-search problem, there is no prior knowledge about
the contents of the database. With classical circuits, there is no alternative
but to perform a linear number of queries to find the target element.
Conversely, Grover's Search algorithm allows to solve the unstructured-search
problem on a quantum computer in :math:`\mathcal{O}(\sqrt{N})` queries.

All that is needed for carrying out a search is an Grover oracle from Aqua's
:ref:`oracles` library for specifying the search criterion, which basically
indicates a hit or miss for any given record.  More formally, an Grover
*oracle* :math:`O_f` is an object implementing a boolean function
:math:`f` as specified above.  Given an input :math:`x \in X`,
:math:`O_f` returns :math:`f(x)`.  The details of how :math:`O_f` works are
unimportant; Grover's search algorithm treats the oracle as a black box.
Currently, Aqua provides the :ref:`sat`, which takes as input a SAT problem in
`DIMACS CNF
format <http://www.satcompetition.org/2009/format-benchmarks2009.html>`__
and constructs the corresponding quantum circuit.  Grover oracles are treated
as pluggable components in Aqua; researchers interested in
:ref:`aqua-extending` can design and implement new Grover oracles and extend
Aqua's Grover oracle library.

Grover's Search by default uses uniform superposition to initialize
its quantum state. However, an initial state from Aqua's
:ref:`initial-states` library may be supplied to
create any starting quantum state.
This could be useful, for example,
if the user already has some prior knowledge regarding
where the search target(s) might be located.

.. seealso::

    Refer to the documentation :ref:`initial-states` for more details.


Grover can also be configured with the following parameter settings:

-  Number of iterations:

   .. code:: python

       num_iterations = 1 | 2 | ...

   For the conventional Grover's search algorithm, the parameter
   ``num_iterations`` is used to specify how many times the marking and
   reflection phase sub-circuit is repeated to amplify the amplitude(s) of
   the target(s).
   A positive ``int`` value is expected. The default value is ``1``.

-  Incremental mode flag:

   .. code:: python

       incremental = False | True

   When run in ``incremental`` mode, the search task will be carried out in
   successive rounds, using circuits built with incrementally higher number
   of iterations for the repetition of the amplitude amplification until a
   target is found or the maximal number :math:`\log N` (:math:`N` being the
   total number of elements in the set from the oracle used) of iterations is
   reached.
   The implementation follows Section 4 of
   `Boyer et al. <https://arxiv.org/abs/quant-ph/9605034>`__
   The ``incremental`` boolean flag defaults to ``False``.
   When set ``True``, the other parameter ``num_iterations`` will be ignored.


.. topic:: Declarative Name

   When referring to Quantum Grover Search declaratively inside Aqua, its code
   ``name``, by which Aqua dynamically discovers and loads it, is ``Grover``.

.. topic:: Problems Supported

   In Aqua, Grover's Search algorithm supports the ``search`` problem.

.. _djalgorithm:

^^^^^^^^^^^^^
Deutsch-Jozsa
^^^^^^^^^^^^^

The Deutsch-Jozsa algorithm was one of the first known quantum algorithms that
showed an exponential speedup compared to a deterministic (non-probabilistic)
classical algorithm, given a black box oracle function.
The algorithm determines whether the given function
:math:`f:\{0,1\}^n \rightarrow \{0,1\}` is constant or balanced. A constant
function maps all inputs to 0 or 1, and a balanced function maps half of its
inputs to 0 and the other half to 1. The oracle implementation can be found
at :ref:`djoracle`

.. topic:: Declarative Name

   When referring to Deutsch-Jozsa declaratively inside Aqua, its code
   ``name``, by which Aqua dynamically discovers and loads it, is
   ``DeutschJozsa``.

.. topic:: Problems Supported

   In Aqua, the Deutsch-Jozsa algorithm supports the ``functionevaluation``
   problem.

.. _bvalgorithm:

^^^^^^^^^^^^^^^^^^
Bernstein-Vazirani
^^^^^^^^^^^^^^^^^^

The Bernstein-Vazirani algorithm is an extension / restriction of the
Deutsch-Jozsa algorithm. The goal of the algorithm is to determine a secret
string :math:`s \in \{0,1\}^n`, given a black box oracle function
that maps :math:`f:\{0,1\}^n \rightarrow \{0,1\}` such that
:math:`f(x)=s \cdot x (\bmod 2)`. The oracle implementation can be found at
:ref:`bvoracle`.

.. topic:: Declarative Name

   When referring to Bernstein-Vazirani declaratively inside Aqua, its code
   ``name``, by which Aqua dynamically discovers and loads it, is
   ``BernsteinVazirani``.

.. topic:: Problems Supported

   In Aqua, the Bernstein-Vazirani algorithm supports the
   ``hiddenstringfinding`` problem.

.. _simonalgorithm:

^^^^^
Simon
^^^^^

The Simon algorithm finds a hidden integer :math:`s \in \{0,1\}^n`
from an oracle :math:`f_s` that satisfies :math:`f_s(x) = f_s(y)` if and only
if :math:`y=x \oplus s` for all :math:`x \in \{0,1\}^n`. Thus, if
:math:`s = 0\ldots 0`, i.e., the all-zero bitstring, then :math:`f_s` is a
1-to-1 (or, permutation) function. Otherwise, if :math:`s \neq 0\ldots 0`,
then :math:`f_s` is a 2-to-1 function. The oracle implementation can be found
at :ref:`simonoracle`.

.. topic:: Declarative Name

   When referring to Simon declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it, is ``Simon``.

.. topic:: Problems Supported

   In Aqua, the Simon algorithm supports the ``periodfinding`` problem.


.. _svm-q-kernel:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Support Vector Machine Quantum Kernel (QSVM Kernel)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Classification algorithms and methods for machine learning are essential
for pattern recognition and data mining applications. Well known
techniques, such as support vector machines or neural networks, have
blossomed over the last two decades as a result of the spectacular
advances in classical hardware computational capabilities and speed.
This progress in computer power made it possible to apply techniques
theoretically developed towards the middle of the XX century on
classification problems that soon became increasingly challenging.

A key concept in classification methods is that of a kernel. Data cannot
typically be separated by a hyperplane in its original space. A common
technique used to find such a hyperplane consists on applying a
non-linear transformation function to the data. This function is called
a *feature map*, as it transforms the raw features, or measurable
properties, of the phenomenon or subject under study. Classifying in
this new feature space – and, as a matter of fact, also in any other
space, including the raw original one – is nothing more than seeing how
close data points are to each other. This is the same as computing the
inner product for each pair of data in the set. In fact we do not need
to compute the non-linear feature map for each datum, but only the inner
product of each pair of data points in the new feature space. This
collection of inner products is called the *kernel* and it is perfectly
possible to have feature maps that are hard to compute but whose kernels
are not.

The QSVM Kernel algorithm applies to classification problems that
require a feature map for which computing the kernel is not efficient
classically. This means that the required computational resources are
expected to scale exponentially with the size of the problem.
QSVM Kernel uses a Quantum processor to solve this problem by a direct
estimation of the kernel in the feature space. The method used falls in
the category of what is called *supervised learning*, consisting of a
*training phase* (where the kernel is calculated and the support vectors
obtained) and a *test or classification phase* (where new labelless data
is classified according to the solution found in the training phase).

QSVM Kernel can be configured with a ``bool`` parameter, indicating
whether or not to print additional information when the algorithm is running:

.. code:: python

    print_info : bool

The default is ``False``.

.. topic:: Declarative Name

   When referring to QSVM Kernel declaratively inside Aqua, its code ``name``, by which
   Aqua dynamically discovers and loads it, is ``QSVM.Kernel``.

.. topic:: Problems Supported

   In Aqua, QSVM Kernel  supports the ``svm_classification`` problem.

.. _svm-variational:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Support Vector Machine Variational (QSVM Variational)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just like QSVM Kernel, the QSVM Variational algorithm applies to
classification problems that require a feature map for which computing
the kernel is not efficient classically. QSVM Variational uses the variational method to solve such
problems in a quantum processor.  Specifically, it optimizes a
parameterized quantum circuit to provide a solution that cleanly
separates the data.

QSVM Variational can be configured with the following parameters:

-  The depth of the variational circuit to be optimized:

   .. code:: python

       circuit_depth = 3 | 4 | ...

   An integer value greater than or equal to ``3`` is expected.  The default is ``3``.

-  A Boolean indicating whether or not to print additional information when the algorithm is running:

   .. code:: python

       print_info : bool

   A ``bool`` value is expected.  The default is ``False``.

.. topic:: Declarative Name

   When referring to QSVM Variational declaratively inside Aqua, its code ``name``, by which
   Aqua dynamically discovers and loads it, is ``QSVM.Variational``.

.. topic:: Problems Supported

   In Aqua, QSVM Variational  supports the ``svm_classification`` problem.

.. _hhl:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
HHL algorithm for solving linear systems (HHL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *HHL algorithm* (after the author's surnames Harrow-Hassidim-Lloyd) is a
quantum algorithm to solve systems of linear equations :math:`A\overrightarrow{x}=\overrightarrow{b}`.
Using the Quantum Phase Estimation algorithm (:ref:`QPE`), the linear system
is transformed into diagonal form in which the matrix :math:`A` is easily
invertible. The inversion is achieved by rotating an ancillary qubit by an angle
:math:`\arcsin{ \frac{C}{\lambda_\mathrm{i}}}` around the y-axis where
:math:`\lambda_\mathrm{i}` are the eigenvalues of :math:`A`. After
uncomputing the register storing the eigenvalues using the inverse QPE,
one measures the ancillary qubit. A measurement of 1 indicates that the matrix
inversion succeeded. This leaves the system in a state proportional to the
solution vector :math:`|x\rangle`. In many cases one is not interested in the
single vector elements of :math:`|x\rangle` but only on certain properties.
These are accessible by using problem-specific operators. Another use-case is
the implementation in a larger quantum program.

Currently only hermitian matrices with a dimension of :math:`2^{n}` are
supported.

.. seealso::

    Consult the documentation on :ref:`iqfts`,  :ref:`initial-states`, :ref:`eigs`, :ref:`reciprocals`
    for more details. `The original paper is accessible on arxiv. <https://arxiv.org/abs/0811.3171>`__

HHL requires eigenvalue estimation using QPE (:ref:`eigs`), the eigenvalue
inversion (:ref:`reciprocals`), and a matrix and initial state as part of its
configuration.


.. topic:: Declarative Name

   When referring to HHL declaratively inside Aqua, its code ``name``, by which
   Aqua dynamically discovers and loads it, is ``HHL``.

.. topic:: Problems Supported

   In Aqua, HHL supports the ``linear_system`` problem.

.. _classical-reference-algorithms:

------------------------------
Classical Reference Algorithms
------------------------------

In this section, we describe the classical algorithms currently available in Aqua.
While these algorithms do not use a quantum device or simulator, and rely on
purely classical approaches, they may be useful in the
near term to generate reference values while experimenting with, developing and testing quantum
algorithms.

.. warning::

    Aqua prevents associating a quantum device or simulator to any experiment that uses a classical
    algorithm.  The ``"backend"`` section of an experiment to be conducted via a classical algorithm is
    disabled.

.. _exact-eigensolver:

^^^^^^^^^^^^^^^^^
Exact Eigensolver
^^^^^^^^^^^^^^^^^

Exact Eigensolver computes up to the first :math:`k` eigenvalues of a complex square matrix of dimension
:math:`n \times n`, with :math:`k \leq n`.
It can be configured with an ``int`` parameter ``k`` indicating the number of eigenvalues to compute:

.. code:: python

    k = 1 | 2 | ... | n

Specifically, the value of this parameter must be an ``int`` value ``k`` in the range :math:`[1,n]`. The default is ``1``.

.. topic:: Declarative Name

   When referring to Exact Eigensolver declaratively inside Aqua, its code ``name``, by which
   Aqua dynamically discovers and loads it, is ``ExactEigensolver``.

.. topic:: Problems Supported

   In Aqua, Exact Eigensolver supports the ``energy``, ``ising`` and ``excited_states``  problems.

.. _cplex:

^^^^^^^^^^^
CPLEX Ising
^^^^^^^^^^^

This algorithm uses the `IBM ILOG CPLEX Optimization
Studio <https://www.ibm.com/support/knowledgecenter/SSSA5P_12.8.0/ilog.odms.studio.help/Optimization_Studio/topics/COS_home.html>`__,
which should be installed along with its `Python API
<https://www.ibm.com/support/knowledgecenter/SSSA5P_12.8.0/ilog.odms.cplex.help/CPLEX/GettingStarted/topics/set_up/Python_setup.html>`__
for this algorithm to be operational. This algorithm currently
supports computing the energy of an Ising model Hamiltonian.

CPLEX Ising can be configured with the following parameters:

-  A time limit in seconds for the execution:

   .. code:: python

       timelimit = 1 | 2 | ...

   A positive ``int`` value is expected.  The default value is `600`.

-  The number of threads that CPLEX uses:

   .. code:: python

       thread = 0 | 1 | 2 | ...

   A non-negative ``int`` value is expected. Setting ``thread`` to ``0`` lets CPLEX decide the number of threads to allocate, but this may
   not be ideal for small problems.  Any value
   greater than ``0`` specifically sets the thread count.  The default value is ``1``, which is ideal for small problems.

-  Decides what CPLEX reports to the screen and records in a log during mixed integer optimization (MIP).

   .. code:: python

       display = 0 | 1 | 2 | 3 | 4 | 5

   An ``int`` value between ``0`` and ``5`` is expected.
   The amount of information displayed increases with increasing values of this parameter.
   By default, this value is set to ``2``.

.. topic:: Declarative Name

   When referring to CPLEX Ising declaratively inside Aqua, its code ``name``, by which
   Aqua dynamically discovers and loads it, is ``CPLEX.Ising``.

.. topic:: Problems Supported

   In Aqua, CPLEX supports the ``ising`` problem.

.. _avm-rbf-kernel:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Support Vector Machine Radial Basis Function Kernel (SVM Classical)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SVM Classical uses a classical approach to experiment with feature map classification
problems.
SVM Classical can be configured with a ``bool`` parameter,
indicating whether or not to print additional information when the algorithm is running:

.. code:: python

    print_info : bool

The default value for this parameter is ``False``.

.. topic:: Declarative Name

   When referring to SVM Classical declaratively inside Aqua, its code ``name``, by which
   Aqua dynamically discovers and loads it, is ``SVM``.

.. topic:: Problems Supported

   In Aqua, SVM Classical supports the ``svm_classification`` problem.
