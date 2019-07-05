.. _variational-forms:

=================
Variational Forms
=================

In quantum mechanics, the *variational method* is one way of finding approximations to the lowest
energy eigenstate, or *ground state*, and some excited states. This allows calculating approximate
wave functions, such as molecular orbitals.  The basis for this method is the *variational
principle*.

The variational method consists of choosing a *trial wave function*, or *variational form*, that
depends on one or more parameters, and finding the values of these parameters for which the
expectation value of the energy is the lowest possible.  The wave function obtained by fixing the
parameters to such values is then an approximation to the ground state wave function, and the
expectation value of the energy in that state is an upper bound to the ground state energy. Quantum
variational algorithms, such as :ref:`vqe`, apply the variational method. As such, they require a
variational form.

In Aqua, variational forms are pluggable entities.  Practitioners who want to use Aqua mainly
as a tool to experiment with :ref:`quantum-algorithms`, and particularly
with variational algorithms, will need to make use of variational forms.  On the other hand,
researchers who want the advance the field of quantum computing, and design and develop new
variational forms, can do so by extending Aqua with new variational forms, which will be
dynamically discovered at run time and made available for use by quantum variational algorithms.

.. topic:: Extending the Variational Form Library

    Consistent with its unique  design, Aqua has a modular and
    extensible architecture. Algorithms and their supporting objects, such as variational forms
    for quantum variational algorithms, are pluggable modules in Aqua.
    New variational forms for quantum variational algorithms are typically installed in the
    ``qiskit/aqua/components/variational_forms``
    folder and derive from the ``VariationalForm`` class.
    Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new components can register themselves
    as Aqua extensions and be dynamically discovered at run time independent of their
    location in the file system.
    This is done in order to encourage researchers and
    developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research contributions.

    When a variational form is used at run time, the ``__init__`` method will be
    called with parameters as per the schema. The number of qubits will also be supplied
    as the value of the parameter following ``self`` in the method argument list.
    During initialization, in ``__init__``, the variational form should set the
    number of parameters it has and their bounds, as in the following example:

    .. code:: python

        self._num_parameters = num_qubits * (depth + 1)
        self._bounds = [(-np.pi, np.pi)
                        for _ in range(self._num_parameters)]

    These values will later be used by the variational algorithm in conjunction with the optimizer.
    Note that the above example is correct when none of qubits are unentangled.

    The variational form can also
    indicate a *preferred initial point*.  This feature is particularly useful when there are
    reasons to believe that the solution point is close to a particular point, which can then
    be provided as the preferred initial point.  As an example,
    when building the dissociation profile of a molecule, it is likely that
    using the previous computed optimal solution as the starting initial point for the
    next interatomic distance is going to reduce the number of iterations necessary for the
    variational algorithm to converge.  Aqua provides
    `a tutorial detailing this use case <https://github.com/Qiskit/qiskit-tutorials/blob/\
    master/community/chemistry/h2_vqe_initial_point.ipynb>`__.

    :ref:`vqe` can, therefore, take an optional initial point from the user
    as the value of the ``initial_point`` parameter, specified as a list of ``float`` values.
    The length of this list must match the number of the parameters expected by the variational
    form being used. If the user does not supply a preferred initial point, then VQE will look
    to the variational form for a preferred value.
    If the variational form returns ``None``,
    then a random point will be generated within the parameter bounds set, as per above.
    If the variational form provides ``None`` as the lower bound, then VQE
    will default it to :math:`-2\pi`; similarly, if the variational form returns ``None`` as
    the upper bound, the default value will be :math:`2\pi`.

.. seealso::

    Section ":ref:`aqua-extending`" provides more
    details on how to extend Aqua with new components.

.. topic:: Entangler Map Associated with a Variational Form

    A variational form is associated with an entangler map, which specifies the entanglement
    of the qubits. An entangler map can be envisioned (and that is also how it is implemented
    in Aqua) as a list such that each element in the list is a list where the first element
    is source qubit :math:`k` and the second element is target qubit :math:`l`.
    Indexes are non-negative integer values from :math:`0` to :math:`q - 1`, where :math:`q`
    is the total number of qubits.  The following Python list shows a possible entangler
    map: ``[[0, 1], [1, 2], [0, 3]]`` for :math:`q=4`.

Currently, Aqua supplies the following variational forms:

- :ref:`ry`
- :ref:`ryrz`
- :ref:`uccsd`
- :ref:`swaprz`

.. _ry:

--
Ry
--

The Ry trial wave function is layers of :math:`y` rotations with entanglements.
When none of qubits are unentangled to other qubits the number of parameters
and the entanglement gates themselves have no additional parameters,
the number of optimizer parameters this form creates and uses is given by :math:`q \times (d + 1)`,
where :math:`q` is the total number of qubits and :math:`d` is the depth of the circuit.
Nonetheless, in some cases, if an ``entangler_map`` does not include all qubits, that is, some
qubits are not entangled by other qubits. The number of parameters is reduced by :math:`d \times q'
` where :math:`q'` is the number of unentangled qubits.
This is because adding more parameters to the unentangled qubits only introduce overhead without
bring any benefit; furthermore, theoretically, applying multiple Ry gates in a row can be reduced
to one Ry gate with the summed rotation angles.

If the form uses entanglement gates with parameters (such as ``'crx'``) the number of parameters
increases by the number of entanglements. For instance with ``'linear'`` or ``'sca'`` entanglement
the total number of parameters is :math:`2q \times (d + 1/2)`. For ``'full'`` entanglement an
additional :math:`q \times (q - 1)/2 \times d` parameters, hence a total of
:math:`d \times q \times (q + 1) / 2 + q`. It is possible to skip the final layer or :math:`y`
rotations by setting the argument ``skip_final_ry`` to ``True``.
Then the number of parameters in above formulae decreases by :math:`q`.

The following allows a specific form to be configured in the
``variational_form`` section of the Aqua
:ref:`aqua-input-file` when the ``name`` field
is set to ``RY``:

- The depth of the circuit:

  .. code:: python

      depth = 1 | 2 | ...

  This parameter takes an ``int`` value greater than ``0``.  The default value is ``3``.

- A ``str`` value representing the type of entanglement to use:

  .. code:: python

      entanglement = "full" | "linear" | "sca"

  Only three ``str`` values are supported: ``"full"``, ``"linear"`` and ``"sca"``. The first
  two correspond to the *full* (or *all-to-all*) and *linear* (or *next-neighbor coupling*)
  entangler maps, respectively.
  With full entanglement, each qubit is entangled with all the others; with linear entanglement,
  qubit :math:`i` is entangled with qubit :math:`i + 1`, for all
  :math:`i \in \{0, 1, ... , q - 2\}`, where :math:`q` is the total number of qubits.

  The entanglement type ``"sca"`` stands for *shifted-circular-alternating* entanglement.
  This entanglement is a generalised and modified version of the proposed circuit 14 in
  `Sim et al. <https://arxiv.org/abs/1905.10876>`__. It consists of circular entanglement
  where the ''long'' entanglement connecting the first with the last qubit is shifted by one
  each block.  Furthermore the role of control and target qubits are swapped every block
  (therefore alternating).

- A list of list of non-negative ``int`` values specifying the entangler map:

  .. code:: python

      entangler_map = [[0, 1], [0, 2], ... [0, q - 1], [1: 2], ..., [q - 2, q - 1]]

  The ``entanglement`` parameter defined above can be overridden by an entangler map explicitly
  specified as the value of the ``entangler_map`` parameter, if an entanglement map different
  from full or linear is desired.
  As explained more generally above, the form of the map is a list; each element in the
  list is a pair of a source qubit and a target qubit index.
  Indexes are ``int`` values from :math:`0` to :math:`q-1`, where :math:`q` is the total number of
  qubits,
  as in the following example:

  .. code:: python

      entangler_map = [[0, 1], [0, 2], [1, 3]]

  .. warning::

     The source qubit index is excluded from the target qubit index.
     In other words, qubit :math:`i` cannot be both source and target qubit indexes.

     Furthermore, by default, if
     the ``entangler_map`` parameter specifies that :math:`[i, j]`, where
     :math:`i,j \in \{0, 1, q-1\}, i \neq j`, then it cannot also specify
     :math:`[j, i]`.  A run-time error will be generated if double entanglement is configured.
     This
     restriction can be lifted programmatically by setting the ``allow_double_entanglement``
     boolean flag to ``True`` inside the
     ``validate_entangler_map`` method in the ``entangler_map`` Application Programming
     Interface (API).

  .. warning::

     When configured declaratively,
     Aqua and its domain specific applications
     (:ref:`aqua-chemistry`, :ref:`aqua-ai`, :ref:`aqua-optimization` and :ref:`aqua-finance`)
     do not expose a configuration parameter in
     a ``VariationalForm`` object to set
     the number of qubits that will be used in an experiment.  This is because, when it is used as
     a tool to execute experiments,
     Aqua is working at a higher, more abstract level.  In such cases, the number of qubits
     is computed internally at run time based on the particular experiment, and passed
     programmatically to
     the ``__init__`` initialization method of the ``VariationalForm`` object.
     Manually configuring the entangler map, therefore,
     requires knowing the number of qubits :math:`q`, since the qubit indexes allowed
     in the entangler map comfiguration can only take ``int`` values from :math:`0` to :math:`q-1`.
     Providing an entangler
     map with indexes outside of this range will generate a run-time error.  Therefore, caution
     should be used when manually configuring the entangler map.

- The boolean value to skip applying gates on unentangled qubits:

  .. code:: python

      skip_unentangled_qubits : bool

  This default value is ``False``. If a given ``entangler_map`` does not entangle some qubits,
  this might imply that the users would like to keep as is. A use case is that users have another
  circuit works on that qubit and would like to keep intact without varying it/them.



.. topic:: Declarative Name

   When referring to Ry declaratively inside Aqua, its code ``name``, by which Aqua dynamically
   discovers and loads it,
   is ``RY``.

.. _ryrz:

----
RyRz
----

The RyRz trial wave function is layers of :math:`y` plus :math:`z` rotations with entanglements.
When none of qubits are unentangled to other qubits, the number of optimizer parameters this form
creates and uses is given by :math:`q \times (d + 1) \times 2`, where :math:`q` is the total
number of qubits and :math:`d` is the depth of the circuit.
Nonetheless, in some cases, if an ``entangler_map`` does not include all qubits, that is, some
qubits are not entangled by other qubits. The number of parameters is reduced by :math:`d \times
q' \times 2` where :math:`q'` is the number of unentangled qubits.
This is because adding more parameters to the unentangled qubits only introduce overhead without
bring any benefit; furthermore, theoretically, applying multiple Ry and Rz gates in a row can be
reduced to one Ry gate and one Rz gate with the summed rotation angles.


The parameters of RyRz can be configured after selecting ``RYRZ`` as the value of the ``name``
field in the
``variational_form`` section of the Aqua :ref:`aqua-input-file`.  These parameters are ``depth``,
``entanglement``, ``entangler_map``, and ``skip_unentangled_qubits`` --- the same
as those of :ref:`Ry`.

.. topic:: Declarative Name

   When referring to RyRz declaratively inside Aqua, its code ``name``, by which Aqua dynamically
   discovers and loads it,
   is ``RYRZ``.

.. _uccsd:

---------------------------------------------------
Unitary Coupled Cluster Singles and Doubles (UCCSD)
---------------------------------------------------

UCCSD lends itself to chemistry experiments and it is, therefore, suitable for use in
:ref:`aqua-chemistry`.
However, it is still a general variational form which can theoretically be used also in
more general experiments.

.. seealso::
    The applicability of UCCSD to chemistry is
    described in `arXiv:1805.04340 <https://arxiv.org/abs/1805.04340>`__.

.. topic:: Particle Preservation

    Particle preservation plays an important role when computing the excited states of
    a molecule.  Without particle preservation, the result of the computation of the excited states
    would be polluted with the presence of ionized states, where some of the initial particles may
    be missing, or additional particles would be accounted for that were not there in the initial
    configuration.

In general, Unitary Coupled Cluster (UCC) preserves the number of particles across the computation
and, consequently,
the number of electrons.  This is true, in particular, for UCCSD.
Therefore, the initial state should be prepared with the desired number of electrons in the
:ref:`hartree-fock` state.
For a neutral molecule, the number of electrons equals
the number of protons.

Note that the UCCSD implementation does not require the use of Trotter steps in the expansion of
the
cluster operators.  Assuming that :math:`T_1` and :math:`T_2` are the
cluster operators for the single and double excitations, respectively,
the Trotter expansion can be written as
:math:`e^{(T_1-{T_1}^\dagger)+(T_2-{T_2}^\dagger)}`.
This amount can be approximated as
:math:`\left(e^{\left(T_1-{T_1}^\dagger\right)/n}e^{\left(T_2-{T_2}^\dagger\right)/n}\right)^n`.
This approximation becomes exact in the limit :math:`n \rightarrow \infty`.
However, `it has been shown <https://arxiv.org/abs/1805.04340>`__ that the variational approach
gives good accuracy
with just a single Trotter step.

Rather than allowing single and double excitations with all particles and all unoccupied orbitals,
the particles and unoccupied orbitals can be restricted to a so called *active space*. This allows
UCCSD to have a simpler form and correspondingly a shorter circuit. While simpler, this will result
in an approximation
of the exact value. The acceptability of such approximation depends on the active space chosen.

The following parameters allow a specific form to be configured:

- The depth of the circuit in use:

  .. code:: python

      depth = 1 | 2 | ...

  This parameter takes a positive ``int`` value, representing the depth of the circuit.
  The default value is ``1``.
  Differently from the heuristic trial wave function approach, in UCCSD we do not need repetition
  of the circuit.

- The total number of spin orbitals for which the variational form is to be created:

  .. code:: python

      num_orbitals = 1 | 2 | ...

  This parameter expects a positive ``int`` value.

- The total number of particles for which the variational form is to be created:

  .. code:: python

      num_particles = [int, int] or 1 | 2 | ...

  This parameter expects a list of two integers for number of alpha and beta electrons or,
  for closed shell backward compatibility, a single ``int`` value which will be divided by
  two internally to form number of alpha and beta electrons.

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

- The number of time slices to use in the expansion:

  .. code::

      num_time_slices = 0 | 1 | ...

  This parameter expects a non-negative ``int`` value.  The default value is ``1``.

- A list of occupied orbitals whose particles are to be used in the creation of single
  and double excitations:

  .. code:: python

      active_occupied = [int, int, ... , int]

  This parameter expects to be assigned a list of ``int`` values. By default, ``active_occupied`` is
  assigned ``None``, corresponding to a configuration in which none of occupied orbitals is excluded
  from the computation.
  Spin orbitals are as in the diagram below, where ``No`` and ``Nv`` indicate the number of
  active occupied alpha orbitals and active unoccupied virtual alpha orbitals, respectively.

  .. code::

                 alpha or up electrons                          beta or down electrons
    /-------------------------------------------\   /-------------------------------------------\
    0      1           No-1 No             No+Nv-1  No+Nv                                 2(No+Nv)-1
    \---------------------/\--------------------/   \--------------------/\---------------------/
             occupied             virtual                  occupied                virtual

    0---------------------n 0-------------------m
        active_occupied       active_unoccupied
             range                  range

  The ``int`` values in the ``active_occupied`` list are orbital indices ranging from ``0`` to ``n``,
  where ``n = No - 1``. The user needs only to supply
  the indexes of the active occupied alpha orbitals desired in the computation,
  as the indexes of the active occupied beta orbitals can be computed.
  Indexes can be given with negative numbers too, in
  which case ``-1`` is the highest occupied orbital, ``-2`` the next one down, and so on.

- A list of active unoccupied orbitals to be used in the creation of single and double excitations:

  .. code::

      active_unoccupied = [int, int, ... , int]

  This parameter expects to be assigned a list of ``int`` values.  By default, the default value
  assigned to `active_unoccupied` is ``None``, which corresponds to the configuration in which none
  of the unoccupied orbitals is excluded from the computation.
  Particles from the ``active_occupied`` list are only allowed to be excited into
  orbitals defined by the ``active_unoccupied`` list.

  Assuming that ``Nv`` is the number of active unoccupied virtual alpha orbitals,
  the ``int`` values in the ``active_unoccupied`` list are orbital indices ranging from
  ``0`` to ``m``, where ``m = Nv - 1``.
  The user needs only to supply
  the indexes of the active unoccupied virtual alpha orbitals, as the indexes of the active
  unoccupied virtual beta orbitals can be computed.
  Indexes can be given with negative numbers too, in
  which case ``-1`` is the highest unoccupied virtual orbital, ``-2`` the next one down, and so on.

.. note::

    When executing an Aqua Chemistry problem, the user can configure two parameters
    in the ``operator`` section of the Aqua Chemistry
    :ref:`qiskit-chemistry-input-file`:
    ``freeze_core`` and ``orbital_reduction``.  These two parameters effectively allow the user
    to specify a set of orbitals to be removed from the computation of the molecular energy.
    Thus the orbitals configurable through UCCSD do not include the orbitals removed via
    the ``freeze_core`` and ``orbital_reduction`` parameters.  The orbitals remaining after that
    removal are reindexed and  partitioned according to the following:

    a. The indexes in the ``active_occupied`` list range from ``0`` to ``n``.
    b. The indexes in the ``active_unoccupied`` list range from ``0`` to ``m``.

.. note::

    When the ``auto_substitutions`` flag in the ``problem`` section of the Qiskit Chemistry
    :ref:`qiskit-chemistry-input-file`
    is set to ``True``, which is the default, the values of parameters
    ``num_particles`` and ``num_orbitals`` are automatically computed by Qiskit Chemistry
    when ``UCCSD`` is selected as the value of the ``name`` parameter in the ``variational_forms``
    section. As such, their configuration is disabled; the user will not be required, or even
    allowed, to assign values to these two parameters.  This is also reflected in the
    :ref:`qiskit-chemistry-gui`, where these parameters will be grayed out and uneditable as long
    as ``auto_substitutions`` is set to ``True`` in the ``problem`` section.
    Furthermore, Qiskit Chemistry automatically sets
    parameters ``qubit_mapping`` and ``two_qubit_reduction`` in section ``variational_form`` when
    ``UCCSD`` is selected as the value of the ``name``
    parameter.  Specifically, Qiskit Chemistry sets ``qubit_mapping`` and ``two_qubit_reduction``
    to the values the user assigned to them in the ``operator`` section
    of the input file in order to enforce parameter/value matching across these different
    sections.  As a result, the user will only have to configure ``qubit_mapping``
    and ``two_qubit_reduction`` in the ``operator`` section; the configuration of these two
    parameters in section ``variational_form`` is disabled,
    as reflected also in the GUI, where the values of these two parameters are only
    editable in the ``operator`` section, and otherwise grayed out in the
    ``variational_form`` sections.

    On the other hand, if ``auto_substitutions`` is set to ``False``,
    then the end user has the full responsibility for the entire
    configuration.

.. warning::

    Setting ``auto_substitutions`` to ``False``, while
    made possible for experimental purposes, should only
    be done with extreme care, since it could easily lead to misconfiguring
    the entire experiment and producing imprecise results.

.. topic:: Declarative Name

   When referring to UCCSD declaratively inside Aqua, its code ``name``, by which Aqua
   dynamically discovers and loads it, is ``UCCSD``.

.. _swaprz:

------
SwapRz
------

This trial wave function is layers of swap plus :math:`z` rotations with entanglements.
It was designed principally to be a particle-preserving variational form for
:ref:`aqua-chemistry`.

.. warning::

    Particle preservation with SwapRz is not guaranteed unless SwapRz is used in conjunction with
    the :ref:`jordan-wigner` qubit mapping and the :ref:`hartree-fock` initial state.

The parameters of SwapRz can be configured after selecting ``SWAPRZ`` as the value of the ``name``
field in the
``variational_form`` section of the Aqua
:ref:`aqua-input-file`.  These parameters are ``depth``. ``entanglement``, ``entangler_map``,
and ``skip_unentangled_qubits`` --- the same as those of :ref:`Ry`.

Based on the notation introduced above for the entangler map associated with a variational form,
for the case of none of qubits are unentangled to other qubits,
the number of optimizer parameters SwapRz creates and uses is given by
:math:`q + d \times \left(q + \sum_{k=0}^{q-1}|D(k)|\right)`, where :math:`|D(k)|` denotes the
*cardinality* of
:math:`D(k)` or, more precisely, the *length* of :math:`D(k)` (since :math:`D(k)` is not
just a set, but a list).
Nonetheless, in some cases, if an ``entangler_map`` does not include all qubits, that is, some
qubits are not entangled by other qubits. The number of parameters is reduced by :math:`d \times q'
` where :math:`q'` is the number of unentangled qubits.
This is because adding more Rz gates to the unentangled qubits only introduce overhead without
bring any benefit; furthermore, theoretically, applying multiple Rz gates in a row can be reduced
to one Rz gate with the summed rotation angles.


.. topic:: Particle Preservation

    Particle preservation plays an important role when computing the excited states of
    a molecule.  Without particle preservation, the result of the computation of the excited states
    would be polluted with the presence of ionized states, where some of the initial particles may
    be missing, or additional particles would be accounted for that were not there in the initial
    configuration.

.. topic:: Declarative Name

    When referring to SwapRz declaratively inside Aqua, its code ``name``, by which Aqua
    dynamically discovers and loads it, is ``SWAPRZ``.
