.. _initial-states:

==============
Initial States
==============

An *initial state* in Aqua is an object that defines a starting state for one of the
:ref:`variational-forms` and a trial state to be evolved by the :ref:`qpe` algorithm.
An initial state allows the user to define a state, either declaratively or programmatically, and
then provides a circuit that can take the starting point of all zero qubits to the defined state.

.. topic:: Extending the Initial States Library

    Consistent with its unique  design, Aqua has a modular and
    extensible architecture. Algorithms and their supporting objects, such as initial states for
    variational forms and :ref:`qpe`, are pluggable modules in Aqua.
    New initial states are typically installed in the ``qiskit_aqua/utils/initial_states`` folder
    and derive from the ``InitialState`` class.  Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new components can register themselves
    as Aqua extensions and be dynamically discovered at run time independent of their
    location in the file system.
    This is done in order to encourage researchers and
    developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research contributions.

Aqua supplies the following three initial states:

1. :ref:`zero`
2. :ref:`hartree-fock`
3. :ref:`custom`

----
Zero
----
This initial state is suitable for those situations in which the all-zeroes state is the desired
starting state. This is the case for a *vacuum state* in physics or chemistry. The zero initial
state has no parameters and is, therefore, not configurable.  Configuring the use of the zero
initial state will create the zero state based solely on the number of qubits.

.. topic:: Declarative Name

   When referring to the zero initial state declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``ZERO``.

.. _hartree-fock:

------------
Hartree-Fock
------------

This initial state is specific for chemistry-related experiments. It corresponds to a molecule's
*Hartree-Fock state*. In computational physics and chemistry, the Hartree–Fock method is a way to
approximate the determination of the wave function and the energy of a quantum many-body system in
a stationary state. The Hartree–Fock method often assumes that the exact, :math:`N`-body wave
function of the system can be approximated by a single Slater determinant in the case where the
particles are fermions) of :math:`N` spin-orbitals. By invoking the variational method, one can
derive a set of :math:`N`-coupled equations for the :math:`N` spin orbitals. A solution of these
equations yields the Hartree–Fock wave function and energy of the system. For both atoms and
molecules, the Hartree–Fock solution is the central starting point for most methods that describe
the many-electron system more accurately. In Aqua, for example, the Hartree-Fock solution is often
the ideal starting state for the :ref:`variational-forms`
and a trial state to be evolved by the :ref:`qpe` algorithm.
For example, when the transformation type of a chemistry operator is set to be particle hole,
then the configuration of the initial qubit state offsetting the computation of the final result
should be set to be the Hartree-Fock energy of the molecule in the
:ref:`aqua-chemistry-input-file`. Hartree-Fock is also the preferred initial state when using the
:ref:`uccsd` and :ref:`swaprz` variational forms.

The following parameters allow
the Hartree-Fock initial state to be configured:

- The total number of spin orbitals for which the Hartree-Fock initial state is to be created:

  .. code:: python

      num_orbitals = 1 | 2 | ...

  This parameter expects a positive ``int`` value.


- The total number of particles for which the Hartree-Fock initial state is to be created:

  .. code:: python

      num_particles = 1 | 2 | ...

  This parameter expects a positive ``int`` value.

-  The desired :ref:`translators` from fermions to qubits:

   .. code:: python

       qubit_mapping = jordan_wigner | parity | bravyi_kitaev

   This parameter takes a value of type ``str``.  Currently, only the three values
   above are supported, but new qubit mappings can easily be plugged in.
   Specifically:

   1. ``jordan_wigner`` corresponds to the :ref:`jordan-wigner` transformation.
   2. ``parity``, the default value for the ``qubit_mapping`` parameter, corresponds to the
      :ref:`parity` mapping transformation. When this mapping is selected,
      it is possible to reduce by 2 the number of qubits required by the computation
      without loss of precision by setting the ``two_qubit_reduction`` parameter to ``True``,
      as explained next.
   3. ``bravyi_kitaev`` corresponds to the :ref:`bravyi-kitaev` transformation,
      also known as *binary-tree-based qubit mapping*.

-  A Boolean flag specifying whether or not to apply the precision-preserving two-qubit reduction
   optimization:

   .. code:: python

       two_qubit_reduction : bool

   The default value for this parameter is ``True``.
   When the parity mapping is selected, and ``two_qubit_reduction`` is set to ``True``,
   then the operator can be reduced by two qubits without loss
   of precision.

   .. warning::
       If the mapping from fermionic to qubit is set to something other than
       the parity mapping, the value assigned to ``two_qubit_reduction`` is ignored.

.. note::

    When the ``auto_substitutions`` flag in the ``problem`` section of the
    :ref:`aqua-chemistry-input-file`
    is set to ``True``, which is the default, the values of parameters
    ``num_particles`` and ``num_orbitals`` are automatically computed by Aqua Chemistry
    when ``Hartree-Fock`` is selected as the value of the ``name`` parameter in the
    ``InitialState`` section. As such, their configuration is disabled; the user will not be
    required, or even allowed, to assign values to these two parameters. This is also reflected in
    the :ref:`aqua-chemistry-gui`, where these parameters will be grayed out and uneditable as
    long as ``auto_substitutions`` is set to ``True`` in the ``problem`` section. Furthermore,
    Aqua Chemistry automatically sets parameters ``qubit_mapping`` and ``two_qubit_reduction`` in
    section ``initial_state`` when ``HartreeFock`` is selected as the value of the ``name``
    parameter.  Specifically, Aqua Chemistry sets ``qubit_mapping`` and ``two_qubit_reduction``
    to the values the user assigned to them in the ``operator`` section
    of the input file in order to enforce parameter/value matching across these different
    sections.  As a result, the user will only have to configure ``qubit_mapping``
    and ``two_qubit_reduction`` in the ``operator`` section; the configuration of these two
    parameters in section ``initial_states`` is disabled,
    as reflected also in the GUI, where the values of these two parameters are only
    editable in the ``operator`` section, and otherwise grayed out in the
    ``initial_state`` section when the ``name`` parameter is set to ``HartreeFock``.

    On the other hand, if ``auto_substitutions`` is set to ``False``,
    then the end user has the full responsibility for the entire
    configuration.

.. warning::

    Setting ``auto_substitutions`` to ``False``, while
    made possible for experimental purposes, should only
    be done with extreme care, since it could easily lead to misconfiguring
    the entire experiment and producing imprecise results.

.. topic:: Declarative Name

   When referring to the Hartree-Fock initial state declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it, is ``HartreeFock``.


.. _custom-initial-states:

------
Custom
------

Should the :ref:`zero` and :ref:`hartree-fock` pre-defined initial states not meet the user's
needs for a particular quantum experiment, this option allows the user of Aqua to fully customize
the initial state (e.g. for :ref:`variational-forms` and the :ref:`qpe` algorithm) by directly
configuring a *custom probability distribution* for the state vector or even providing the
desired *custom quantum circuit*. No matter what custom probability distribution the user chooses,
the state vector will be normalized by Aqua, so the total probability represented is :math:`1.0`.
Setting up a custom probability distribution requires assigning a value to the following
parameters:

- A label specifying a predefined probability distribution used to configure the state vector:

  .. code:: python

      state = "zero" | "uniform" | "random"

  The ``state`` parameter accepts a ``str`` value.  Currently, the following three ``str``
  values are supported:

  1. ``"zero"`` --- This setting configures the state vector with the *zero probability
     distribution*, and is effectively equivalent to the :ref:`zero` initial state.
  2. ``"uniform"`` --- This setting configures the state vector with the *uniform probability
     distribution*.  All the qubits
     are set in superposition, each of them being initialized to the Hadamard gate, which means
     that a measurement will have equal probabilities to become :math:`1` or :math:`0`.
  3. ``"random"`` --- This setting assigns the elements of the state vector according to a random
     probability distribution.

- The state vector itself:

  .. code:: python

      state_vector : [complex, complex, ... , complex]

  The ``state_vector`` parameter allows a specific custom initial state to be defined as a
  list of ``complex`` numbers. The length of the list must be :math:`2^q`, where :math:`q` is the
  total number of qubits.

- The custom quantum circuit:

  .. code:: python

      circuit: QuantumCircuit

  The ``circuit`` parameter takes the value of a ``QuantumCircuit`` object representing
  the custom quantum circuit for the initial state.

  .. warning::

     The ``InitialState`` API exposes a constructor that
     allows for programmatically setting ``num_qubits``, the number of qubits in the
     ``InitialState`` object. However, when configured declaratively, Aqua and its domain specific
     applications
     (:ref:`aqua-chemistry`, :ref:`aqua-ai`, and :ref:`aqua-optimization`) do not expose a
     configuration parameter in an ``InitialState`` object to set the number of qubits to use in an
     experiment.  This is because, when it is used as a tool to execute experiments,
     Aqua is working at a higher, more abstract level.  In such cases, the number of qubits
     is computed internally at run time based on the particular experiment, and passed
     programmatically to the constructor.  Manually configuring the state vector, therefore,
     requires knowing the number of qubits :math:`q`, since the length of the state vector is
     :math:`2^q`.  Providing a state vector of the wrong size will generate a run-time error.
     Therefore, caution should be used when manually configuring the state vector. The same also
     applies when the actual custom circuit is directly supplied.

  .. note::

     The multiple ways of manually configuring an initial state abide to the following priority
     order: `circuit > state_vector > state`. So, when a higher order item is supplied, the
     lower-order item(s) will be ignored if also supplied.

.. topic:: Declarative Name

   When referring to the custom initial state declaratively inside Aqua, its code ``name``, by
   which Aqua dynamically discovers and loads it, is ``CUSTOM``.
