.. _random-distributions:

====================
Random Distributions
====================

A random distribution is an implementation of a circuit factory that provides a way to construct a
quantum circuit to prepare a state which corresponds to a random distribution.
More precisely, the resulting state together with an affine map can be used to sample from the
considered distribution.
The qubits are measured and then mapped to the desired range using the affine map.

In the following, we discuss the currently existing implementations.

------------------------
Univariate Distributions
------------------------

.. topic:: Univariate Distribution

    This provides a circuit factory to load a general univariate distribution that is defined by an array of
    probabilities and the interval of interest. It calls the custom state initialization to prepare a quantum state
    such that the squared amplitudes correspond to the probabilities.
    The given lower and upper bound define the range of interest, and the number of qubits specifies the number of
    grid points in between (=2**n, for n qubits).

    .. code:: python

        # parameters
        low = 0
        high = 2*np.pi
        num_qubits = 5

        # build (arbitrary) empirical distribution
        probabilities = np.sin(np.linspace(low, high, 2**num_qubits))+1
        probabilities = probabilities / sum(histogram)

        # initialize distribution
        univariate = UnivariateDistribution(num_qubits, probabilities, low, high)

        # create circuit
        q = QuantumRegister(num_qubits)
        qc = QuantumCircuit(q)
        univariate.build(qc, q)


.. topic:: Bernoulli Distribution

    Distribution with only two values (low, high) and the corresponding probabilities represented by a single qubit.

    .. code:: python

        # parameters
        low = 0
        high = 1
        probability = 0.3

        # initialize distribution
        bernoulli = BernoulliDistribution(probability, low, high)

        # create circuit
        q = QuantumRegister(num_qubits)
        qc = QuantumCircuit(q)
        bernoulli.build(qc, q)


.. topic:: Uniform Distribution

    Uniform distribution is defined by the number of qubits that should be used to represent the distribution,
    as well as the lower bound and upper bound of the considered interval.

    .. code:: python

        # parameters
        low = 0
        high = 3
        num_qubits = 3

        # initialize distribution
        uniform = UniformDistribution(num_qubits, low, high)

        # create circuit for distribution
        q = QuantumRegister(num_qubits)
        qc = QuantumCircuit(q)
        uniform.build(qc, q)


.. topic:: Normal Distribution

    Normal distribution, truncated to lower and upper bound and discretized on a grid defined by the number of qubits.

    .. code:: python

        # parameters
        low = 0
        high = 10
        num_qubits = 5

        # initialize distribution
        mu = 1.5
        sigma = 0.5
        normal = NormalDistribution(num_qubits, mu, sigma, low, high)

        # create circuit for distribution
        q = QuantumRegister(num_qubits)
        qc = QuantumCircuit(q)
        normal.build(qc, q)


.. topic:: Log-Normal Distribution

    Log-normal distribution, truncated to lower and upper bound and discretized on a grid defined by the number of qubits.

    .. code:: python

        # parameters
        low = 0
        high = 10
        num_qubits = 5

        # initialize distribution
        mu = 1.5
        sigma = 0.5
        lognormal = LogNormalDistribution(num_qubits, mu, sigma, low, high)

        # create circuit for distribution
        q = QuantumRegister(num_qubits)
        qc = QuantumCircuit(q)
        lognormal.build(qc, q)

--------------------------
Multivariate Distributions
--------------------------

.. topic:: Multivariate Distribution

    This provides a circuit factory to load a general multivariate distribution that is defined by an array of
    probabilities and the box of interest (given interval per dimension). It calls the custom state initialization
    to prepare a quantum state such that the squared amplitudes correspond to the probabilities.
    The given lower and upper bounds per dimension define the range of interest, and the number of qubits
    per dimension specifies the number of grid points in between (=2**n, for n qubits).

    .. code:: python

        # parameters
        low = [0, 0]
        high = [1, 1]
        num_qubits = [2, 2]

        # build (arbitrary) empirical distribution
        probabilities = np.random.uniform(size=(4, 4))
        probabilities = probabilities / sum(histogram)

        # initialize distribution
        multivariate = MultivariateDistribution(num_qubits, probabilities, low, high)

        # create circuit
        q = QuantumRegister(num_qubits)
        qc = QuantumCircuit(q)
        multivariate.build(qc, q)

.. topic:: Multivariate Uniform Distribution

    Provides a circuit factory to build a multivariate uniform distribution.
    Although this just results in a Hadamard gate on all involved qubits, the lower and upper bounds and the
    assignment of the qubits to the different dimensions is important if used in a particular application.

    .. code:: python

        # specify the number of qubits that are used to represent the different dimenions of the uncertainty model
        num_qubits = [2, 3]

        # specify the lower and upper bounds for the different dimension
        low = [-1, -2]
        high = [1, 2]

        # construct random distribution
        multivariate = MultivariateUniformDistribution(num_qubits, low, high)

        # create circuit for distribution
        q = QuantumRegister(num_qubits)
        qc = QuantumCircuit(q)
        multivariate.build(qc, q)

.. topic:: Multivariate Normal Distribution

    Provides a circuit factory to load a (discretized and truncated) normal distribution into a quantum state.
    Truncation bounds are given by lower and upper bound and discretization is specified by the number of qubits per
    dimension.

    .. code:: python

        # specify the number of qubits that are used to represent the different dimensions of the uncertainty model
        num_qubits = [2, 3]

        # specify the lower and upper bounds for the different dimension
        low = [-1, -2]
        high = [1, 2]
        mu = np.zeros(2)
        sigma = np.eye(2)

        # construct random distribution
        multivariate_normal = MultivariateNormalDistribution(num_qubits, low, high, mu, sigma)

        # create circuit for distribution
        q = QuantumRegister(num_qubits)
        qc = QuantumCircuit(q)
        multivariate_normal.build(qc, q)
