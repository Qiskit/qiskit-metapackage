.. _feature-maps:

===================
Feature Maps
===================

In machine learning, pattern recognition and image processing, a *feature map*
starts from an initial set of measured data and builds derived values (also known as
*features*) intended to be informative and non-redundant, facilitating the subsequent
learning and generalization steps, and in some cases leading to better human
interpretations. A feature map is related to *dimensionality reduction*; it
involves reducing the amount of resources required to describe a large set of data.
When performing analysis of complex data, one of the major problems stems from the
number of variables involved. Analysis with a large number of variables generally
requires a large amount of memory and computation power, and may even cause a
classification algorithm to overfit to training samples and generalize poorly to new
samples.  When the input data to an algorithm is too large to be processed and is
suspected to be redundant (for example, the same measurement is provided in both
pounds and kilograms), then it can be transformed into a reduced set of features,
named a *feature vector*.
The process of determining a subset of the initial features is called *feature selection*.
The selected features are expected to contain the relevant information from the input data,
so that the desired task can be performed by using the reduced representation instead
of the complete initial data.

Aqua provides an extensible library of feature-map techniques, to be used in
:ref:`aqua-ai` and, more generally, in any quantum computing experiment that may
require constructing combinations of variables to get around the problems mentioned
above, while still describing the data with sufficient accuracy.

.. topic:: Extending the Feature Map Library

    Consistent with its unique design, Aqua has a modular and
    extensible architecture. Algorithms and their supporting objects, such as
    feature-map techniques for Artificial Intelligence,
    are pluggable modules in Aqua.
    New feature maps are typically installed in the
    ``qiskit_aqua/utils/feature_maps``
    folder and derive from the ``FeatureMap`` class.
    Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new components can register themselves
    as Aqua extensions and be dynamically discovered at run time independent of their
    location in the file system.
    This is done in order to encourage researchers and
    developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research contributions.


.. topic:: Entangler Map Associated with a Feature Map

    A feature map is associated with an entangler map, which specifies the entanglement of the qubits.
    An entangler map can be envisioned (and that is also how it is implemented in Aqua)
    as a dictionary :math:`D` such that each entry in the dictionary has a source qubit
    index as the key :math:`k`, with the corresponding value :math:`D(k) = v` being a list of target qubit
    indexes to which qubit
    :math:`k` is entangled.  Indexes are non-negative integer values from :math:`0` to :math:`q - 1`, where :math:`q`
    is the total number of qubits.  The following Python dictionary shows a possible entangler map: ``{0: [1, 2], 1: [3]}``.


Currently, Aqua supplies the following feature maps:

- :ref:`firstorderexpansion`
- :ref:`secondorderexpansion`
- :ref:`paulizexpansion`
- :ref:`pauliexpansion`
- :ref:`rawfeaturevector`

.. _firstorderexpansion:

---------------------
First Order Expansion
---------------------

The First Order Expansion feature map transform data :math:`\vec{x} \in \mathbb{R}^n`
according to the following equation, and then concatenates the same circuit :math:`d` times,
where :math:`d` is the depth of the circuit:

  :math:`U_{\Phi(\vec{x})}=\exp\left(i\sum_{S\subseteq[n]}\phi_S(\vec{x})\prod_{i\inS}Z_i\right)`

where :math:`S \in \{ 0, 1, ..., n-1 \}, \phi_{i}(\vec{x}) = x_i`.


The following allows a specific form to be configured in the
``feature_map`` section of the Aqua
:ref:`aqua-input-file` when the ``name`` field
is set to ``FirstOrderExpansion``:

- The depth of the circuit:

  .. code:: python

      depth = 1 | 2 | ...

  This parameter takes an ``int`` value greater than ``0``.  The default value is ``2``.

.. topic:: Declarative Name

   When referring to the First Order Expansion feature map declaratively inside Aqua, its code ``name``, by which Aqua
   dynamically discovers and loads it,
   is ``FirstOrderExpansion``.

.. _secondorderexpansion:

----------------------
Second Order Expansion
----------------------

The Second Order Expansion feature map transform data :math:`\vec{x} \in \mathbb{R}^n`
according to the following equation, and then duplicate the same circuit with depth :math:`d` times,
where :math:`d` is the depth of the circuit:

:math:`U_{\Phi(\vec{x})}=\exp\left(i\sum_{S\subseteq [n]}\phi_S(\vec{x}) \prod_{i \in S} Z_i\right)`

where :math:`S \in \{0, 1, ..., n-1, (0, 1), (0, 2), ..., (n-2, n-1)\},
\phi_{i}(\vec{x}) = x_i, \phi_{(i,j)}(\vec{x}) = (\pi - x_i) * (\pi - x_j)`.


The following allows a specific form to be configured in the
``feature_map`` section of the Aqua
:ref:`aqua-input-file` when the ``name`` field
is set to ``SecondOrderExpansion``:

- The depth of the circuit:

  .. code:: python

      depth = 1 | 2 | ...

  This parameter takes an ``int`` value greater than ``0``.  The default value is ``2``.

- A ``str`` value representing the type of entanglement to use:

  .. code:: python

      entanglement = "full" | "linear"

  Only two ``str`` values are supported: ``"full"`` and ``"linear"``, corresponding to the *full* (or *all-to-all*) and
  *linear* (or *next-neighbor coupling*) entangler maps, respectively.  With full entanglement, each qubit is entangled with
  all the
  others; with linear entanglement, qubit :math:`i` is entangled with qubit :math:`i + 1`, for all :math:`i \in \{0, 1, ... ,
  q - 2\}`,
  where :math:`q` is the total number of qubits.

- A dictionary of lists of non-negative ``int`` values specifying the entangler map:

  .. code:: python

      entangler_map = {0: [1 | ... | q - 1], 1: [0 | 2 | ... | q - 1], ... , q - 1: [0 | 1 | ... | q - 2]}

  The ``entanglement`` parameter defined above can be overridden by an entangler map explicitly specified as the value of the
  ``entangler_map`` parameter, if an entanglement map different
  from full or linear is desired.
  As explained more generally above, the form of the map is a dictionary; each entry in the dictionary has a source qubit
  index as the key, with the corresponding value being a list of target qubit indexes to which the source qubit should
  be entangled.
  Indexes are ``int`` values from :math:`0` to :math:`q-1`, where :math:`q` is the total number of qubits,
  as in the following example:

  .. code:: python

      entangler_map = {0: [1, 2], 1: [3]}

  .. warning::

     The source qubit index is excluded from the list of its corresponding target qubit indexes.  In other words,
     qubit :math:`i` cannot be in the list :math:`D(i)` of qubits mapped to qubit :math:`i` itself.

     Furthermore, by default, if
     the ``entangler_map`` parameter specifies that :math:`j \in D(i)`, where :math:`i,j \in \{0, 1, q-1\}, i \neq j`, then it
     cannot also specify
     :math:`j \in D(i)`.  A run-time error will be generated if double entanglement is configured.  This
     restriction can be lifted programmatically by setting the ``allow_double_entanglement`` boolean flag to ``True`` inside
     the
     ``validate_entangler_map`` method in the ``entangler_map`` Application Programming Interface (API).

  .. warning::

     When configured declaratively,
     Aqua and its domain specific applications
     (:ref:`aqua-chemistry`, :ref:`aqua-ai`, :ref:`aqua-optimization` and :ref:`aqua-finance`)
     do not expose a configuration parameter in
     a ``FeatureMap`` object to set
     the number of qubits that will be used in an experiment.  This is because, when it is used as a tool to execute
     experiments,
     Aqua is working at a higher, more abstract level.  In such cases, the number of qubits
     is computed internally at run time based on the particular experiment, and passed programmatically to construct the ``FeatureMap`` object.
     Manually configuring the entangler map, therefore,
     requires knowing the number of qubits :math:`q`, since the qubit indexes allowed
     in the entangler map comfiguration can only take ``int`` values from :math:`0` to :math:`q-1`.  Providing an entangler
     map with indexes outside of this range will generate a run-time error.  Therefore, caution should be used when
     manually configuring the entangler map.


.. topic:: Declarative Name

   When referring to SecondOrderExpansion declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers
   and loads it,
   is ``SecondOrderExpansion``.


.. _paulizexpansion:

----------------------
Pauli Z Expansion
----------------------

The Pauli Z Expansion feature map transform data :math:`\vec{x} \in \mathbb{R}^n`
according to the following equation, and then duplicate the same circuit with depth :math:`d` times,
where :math:`d` is the depth of the circuit:

:math:`U_{\Phi(\vec{x})}=\exp\left(i \sum_{S\subseteq[n]}\phi_S(\vec{x})\prod_{i\inS}Z_i\right)`

where :math:`S \in \{\binom{n}{k}\ combinations,\ k = 1,... n\}, \phi_S(\vec{x}) = x_i` if
:math:`k=1`, otherwise :math:`\phi_S(\vec{x}) = \prod_S(\pi - x_j)`, where :math:`j \in S`. Please
refer to :ref:`firstorderexpansion` and :ref:`secondorderexpansion` for the cases of :math:`k=1`
and :math:`k=2`, respectively.


The following allows a specific form to be configured in the
``feature_map`` section of the Aqua
:ref:`aqua-input-file` when the ``name`` field
is set to ``PauliZExpansion``:

- The depth of the circuit:

  .. code:: python

      depth = 1 | 2 | ...

  This parameter takes an ``int`` value greater than ``0``.  The default value is ``2``.

- The order of pauli Z, i.e., the :math:`k` in the above equation:

  .. code:: python

      z_order = 1 | 2 | ...

  This parameter takes an ``int`` value greater than ``0``.  The default value is ``2``.

- A ``str`` value representing the type of entanglement to use:

  .. code:: python

      entanglement = "full" | "linear"

  Only two ``str`` values are supported: ``"full"`` and ``"linear"``, corresponding to the *full*
  (or *all-to-all*) and *linear* (or *next-neighbor coupling*) entangler maps, respectively.  With
  full entanglement, each qubit is entangled with  all the others; with linear entanglement, qubit
  :math:`i` is entangled with qubit :math:`i + 1`, for all :math:`i \in \{0, 1, ... , q - 2\}`,
  where :math:`q` is the total number of qubits.

- A dictionary of lists of non-negative ``int`` values specifying the entangler map:

  .. code:: python

      entangler_map = {0: [1 | ... | q - 1], 1: [0 | 2 | ... | q - 1], ... , q - 1: [0 | 1 | ... | q - 2]}

  The ``entanglement`` parameter defined above can be overridden by an entangler map explicitly specified as the value of the
  ``entangler_map`` parameter, if an entanglement map different
  from full or linear is desired.
  As explained more generally above, the form of the map is a dictionary; each entry in the dictionary has a source qubit
  index as the key, with the corresponding value being a list of target qubit indexes to which the source qubit should
  be entangled.
  Indexes are ``int`` values from :math:`0` to :math:`q-1`, where :math:`q` is the total number of qubits,
  as in the following example:

  .. code:: python

      entangler_map = {0: [1, 2], 1: [3]}

  .. warning::

     The source qubit index is excluded from the list of its corresponding target qubit indexes.  In other words,
     qubit :math:`i` cannot be in the list :math:`D(i)` of qubits mapped to qubit :math:`i` itself.

     Furthermore, by default, if
     the ``entangler_map`` parameter specifies that :math:`j \in D(i)`, where :math:`i,j \in \{0, 1, q-1\}, i \neq j`, then it
     cannot also specify
     :math:`j \in D(i)`.  A run-time error will be generated if double entanglement is configured.  This
     restriction can be lifted programmatically by setting the ``allow_double_entanglement`` boolean flag to ``True`` inside
     the
     ``validate_entangler_map`` method in the ``entangler_map`` Application Programming Interface (API).

  .. warning::

     When configured declaratively,
     Aqua and its domain specific applications
     (:ref:`aqua-chemistry`, :ref:`aqua-ai`, :ref:`aqua-optimization` and :ref:`aqua-finance`)
     do not expose a configuration parameter in
     a ``FeatureMap`` object to set
     the number of qubits that will be used in an experiment.  This is because, when it is used as a tool to execute
     experiments,
     Aqua is working at a higher, more abstract level.  In such cases, the number of qubits
     is computed internally at run time based on the particular experiment, and passed programmatically to construct the ``FeatureMap`` object.
     Manually configuring the entangler map, therefore,
     requires knowing the number of qubits :math:`q`, since the qubit indexes allowed
     in the entangler map comfiguration can only take ``int`` values from :math:`0` to :math:`q-1`.  Providing an entangler
     map with indexes outside of this range will generate a run-time error.  Therefore, caution should be used when
     manually configuring the entangler map.


.. topic:: Declarative Name

   When referring to PauliZExpansion declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers
   and loads it,
   is ``PauliZExpansion``.

.. _pauliexpansion:

----------------------
Pauli Expansion
----------------------

The Pauli Expansion feature map transform data :math:`\vec{x} \in \mathbb{R}^n`
according to the following equation, and then duplicate the same circuit with depth :math:`d` times,
where :math:`d` is the depth of the circuit:

:math:`U_{\Phi(\vec{x})}=\exp\left(i\sum_{S\subseteq [n]} \phi_S(\vec{x})\prod_{i\in S} P_i\right)`

where :math:`S \in \{\binom{n}{k}\ combinations,\ k = 1,... n \}, \phi_S(\vec{x}) = x_i` if
:math:`k=1`, otherwise :math:`\phi_S(\vec{x}) = \prod_S(\pi - x_j)`, where :math:`j \in S`, and
:math:`P_i \in \{ I, X, Y, Z \}` Please refer to :ref:`firstorderexpansion` and
:ref:`secondorderexpansion` for the cases of :math:`k = 1` and :math:`P_0 = Z` and :math:`k = 2`
and :math:`P_0 = Z\ and\ P_1 P_0 = ZZ`, respectively.

The following allows a specific form to be configured in the
``feature_map`` section of the Aqua
:ref:`aqua-input-file` when the ``name`` field
is set to ``PauliExpansion``:

- The depth of the circuit:

  .. code:: python

      depth = 1 | 2 | ...

  This parameter takes an ``int`` value greater than ``0``.  The default value is ``2``.

- The pauli string:

  .. code:: python

      paulis = list of string

  This parameter takes a list of paulis (a pauli is a any combination of I, X, Y ,Z).  The default value is ``['Z', 'ZZ']``. Note that the order of pauli label is counted from right to left as the notation used in Pauli class in Qiskit Terra.

- A ``str`` value representing the type of entanglement to use:

  .. code:: python

      entanglement = "full" | "linear"

  Only two ``str`` values are supported: ``"full"`` and ``"linear"``, corresponding to the *full* (or *all-to-all*) and
  *linear* (or *next-neighbor coupling*) entangler maps, respectively.  With full entanglement, each qubit is entangled with
  all the
  others; with linear entanglement, qubit :math:`i` is entangled with qubit :math:`i + 1`, for all :math:`i \in \{0, 1, ... ,
  q - 2\}`,
  where :math:`q` is the total number of qubits.

- A dictionary of lists of non-negative ``int`` values specifying the entangler map:

  .. code:: python

      entangler_map = {0: [1 | ... | q - 1], 1: [0 | 2 | ... | q - 1], ... , q - 1: [0 | 1 | ... | q - 2]}

  The ``entanglement`` parameter defined above can be overridden by an entangler map explicitly specified as the value of the
  ``entangler_map`` parameter, if an entanglement map different
  from full or linear is desired.
  As explained more generally above, the form of the map is a dictionary; each entry in the dictionary has a source qubit
  index as the key, with the corresponding value being a list of target qubit indexes to which the source qubit should
  be entangled.
  Indexes are ``int`` values from :math:`0` to :math:`q-1`, where :math:`q` is the total number of qubits,
  as in the following example:

  .. code:: python

      entangler_map = {0: [1, 2], 1: [3]}

  .. warning::

     The source qubit index is excluded from the list of its corresponding target qubit indexes.  In other words,
     qubit :math:`i` cannot be in the list :math:`D(i)` of qubits mapped to qubit :math:`i` itself.

     Furthermore, by default, if
     the ``entangler_map`` parameter specifies that :math:`j \in D(i)`, where :math:`i,j \in \{0, 1, q-1\}, i \neq j`, then it
     cannot also specify
     :math:`j \in D(i)`.  A run-time error will be generated if double entanglement is configured.  This
     restriction can be lifted programmatically by setting the ``allow_double_entanglement`` boolean flag to ``True`` inside
     the
     ``validate_entangler_map`` method in the ``entangler_map`` Application Programming Interface (API).

  .. warning::

     When configured declaratively,
     Aqua and its domain specific applications
     (:ref:`aqua-chemistry`, :ref:`aqua-ai`, :ref:`aqua-optimization` and :ref:`aqua-finance`)
     do not expose a configuration parameter in
     a ``FeatureMap`` object to set
     the number of qubits that will be used in an experiment.  This is because, when it is used as a tool to execute
     experiments,
     Aqua is working at a higher, more abstract level.  In such cases, the number of qubits
     is computed internally at run time based on the particular experiment, and passed programmatically to construct the ``FeatureMap`` object.
     Manually configuring the entangler map, therefore,
     requires knowing the number of qubits :math:`q`, since the qubit indexes allowed
     in the entangler map comfiguration can only take ``int`` values from :math:`0` to :math:`q-1`.  Providing an entangler
     map with indexes outside of this range will generate a run-time error.  Therefore, caution should be used when
     manually configuring the entangler map.


.. topic:: Declarative Name

   When referring to PauliExpansion declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers
   and loads it,
   is ``PauliExpansion``.

.. _rawfeaturevector:

------------------
Raw Feature Vector
------------------

As an alternative to the aforementioned feature maps,
the Raw Feature Vector can also be directly used as a feature map,
for which the raw feature vectors would be automatically padded with ending 0s if necessary,
to make sure vector length is a power of 2,
and normalized s.t. it is treated and used as an initial quantum state vector.
A raw feature vector feature map is constructed with a single parameter:

- The dimension of the feature vector:

  .. code:: python

      feature_dimension = 1 | 2 | ...

  This parameter takes an ``int`` value greater than ``0``.  The default value is ``2``.

.. topic:: Declarative Name

   When referring to the Raw Feature Vector feature map declaratively inside Aqua, its code ``name``, by which Aqua
   dynamically discovers and loads it,
   is ``RawFeatureVector``.
