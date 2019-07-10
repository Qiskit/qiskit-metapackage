.. _neural-networks:

===================
Neural Networks
===================

A neural network is a parametrized network which may be defined as a artificial
neural network - classical neural network - or as parametrized quantum circuits
- quantum neural network. Furthermore, neural networks can be defined with respect
to a discriminative or generative task.

Aqua provides an library for quantum and classical neural networks which can be used to
build hybrid quantum classical AI models.

.. topic:: Extending the Neural Network Library

    Consistent with its unique design, Aqua has a modular and extensible architecture.
    Algorithms and their supporting objects, such as neural networks for Artificial Intelligence,
    are pluggable modules in Aqua.  New neural networks are typically installed in the
    ``qiskit/aqua/components/neural_networks`` folder and derive from the ``DiscriminativeNetwork``
    class for neural networks that are supposed to perform discriminative tasks and the
    ``GenerativeNetwork`` class for neural networks that are supposed to perform generative tasks.
    Aqua also allows for :ref:`aqua-dynamically-discovered-components`: new components can
    register themselves as Aqua extensions and be dynamically discovered at run time independent
    of their location in the file system.
    This is done in order to encourage researchers and developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research contributions.



Currently, Aqua supplies the following neural networks:

- :ref:`classicaldiscriminator`
- :ref:`numpydiscriminator`
- :ref:`quantumgenerator`

.. _classicaldiscriminator:

------------------------
Classical Discriminator
------------------------

This discriminator is given by a PyTorch neural network. Please note that PyTorch must be installed.
For installation instructions see https://pytorch.org/get-started/locally/.

The network is targeted at being used as part of the :ref:`qgan` algorithm.
Please refer to `qGAN <https://arxiv.org/abs/1904.00043>`__  for further details on this algorithm.
The discriminator takes an input vector where the number of represented features
:math:`n_features \geq 1` and outputs a label for the data sample, i.e. true/fake.


The following allows a specific form to be configured in the
``discriminative_network`` section of the Aqua
:ref:`aqua-input-file` when the ``name`` field
is set to ``ClassicalDiscriminator``:

- The dimension of the input vector :math:`n_features`:

  .. code:: python

      n_features = 1 | 2 | ...

  This parameter takes an ``int`` value greater or equal than ``1``.  The default value is ``1``.

- The dimension of the output vector :math:`n_out`. For a binary label this
  should always be set to ``1``.

  .. code:: python

      n_out = 1 | 2 | ...

  This parameter takes an ``int`` value greater or equal than ``1``.  The default value is ``1``.

.. topic:: Declarative Name

   When referring to the classical discriminator declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it, is ``ClassicalDiscriminator``.

.. _numpydiscriminator:

------------------------
Numpy Discriminator
------------------------

This discriminator is given by a NumPy neural network.


The network is targeted at being used as part of the :ref:`qgan` algorithm.
Please refer to `qGAN <https://arxiv.org/abs/1904.00043>`__  for further details on this algorithm.
The discriminator takes an input vector where the number of represented features
:math:`n_features \geq 1` and outputs a label for the data sample, i.e. true/fake.


The following allows a specific form to be configured in the
``discriminative_network`` section of the Aqua
:ref:`aqua-input-file` when the ``name`` field
is set to ``NumpyDiscriminator``:

- The dimension of the input vector :math:`n_features`:

  .. code:: python

      n_features = 1 | 2 | ...

  This parameter takes an ``int`` value greater or equal than ``1``.  The default value is ``1``.

- The dimension of the output vector :math:`n_out`. For a binary label this
  should always be set to ``1``.

  .. code:: python

      n_out = 1 | 2 | ...

  This parameter takes an ``int`` value greater or equal than ``1``.  The default value is ``1``.

.. topic:: Declarative Name

   When referring to the classical discriminator declaratively inside Aqua,
   its code ``name``, by which Aqua dynamically discovers and loads it, is ``NumpyDiscriminator``.


.. _quantumgenerator:

----------------------
Quantum Generator
----------------------

This generator is given by a variational quantum circuit, see :ref:`variational-forms`.
The network is targeted at being used as part of the :ref:`qgan` algorithm.
Please refer to `qGAN <https://arxiv.org/abs/1904.00043>`__  for further details on this algorithm.

The quantum generator generates outputs data samples which are fitted to a data grid.
This grid is defined by min/max data values and the number of qubits :math:`n` which
in turn define the representation resolution.

The following allows a specific form to be configured in the
``generative_network`` section of the Aqua
:ref:`aqua-input-file` when the ``name`` field
is set to ``QuantumGenerator``:

- The min/max data values for data dimension :math:`k`:

  .. code:: python

      bounds = [[min_1,max_1],...,[min_k,max_k]]

  This parameter takes an ``array``.

- Given data with dimension :math:`k`, the number of qubits used for the
  representation of dimension :math:`j \in [1, ..., k]`:

  .. code:: python

      nm_qubits = [n_1,..., n_k]

  This parameter takes an ``array`` of length :math:`k`. The use
  of :math:`n` qubits enables the representation of :math:`2**n` values.

- The generator circuit:

  .. code:: python

      generator_circuit

  The generator circuit must either be given as UnivariateVariationalDistribution for
  univariate data or as MultivariateVariationalDistribution for multivariate data.
  See :ref:`random-distributions`.


- Initial parameters used for the generator circuit:

  .. code:: python

      init_params = [param_0, ..., param_m]

  This parameter takes a ``1-``dimensional ``array``. The default value is ``None``.

- Snapshot directory, if given save intermediate parameter results to the given directory path:

  .. code:: python

      snapshot_dir = '...'

  This parameter takes a ``str``. The default value is ``None``.

.. topic:: Declarative Name

   When referring to the quantum generator declaratively inside Aqua,
   its code ``name``, by which Aqua dynamically discovers and loads it, is ``QuantumGenerator``.
