###############
Release History
###############

*************
Release Notes
*************

==================
Qiskit Aqua 0.4.0
==================

In the `Qiskit <https://qiskit.org/>`__ ecosystem,
`Aqua <https://qiskit.org/aqua>`__ is the
`element <https://medium.com/qiskit/qiskit-and-its-fundamental-elements-bcd7ead80492>`__
that encompasses cross-domain quantum algorithms and applications
running on `Noisy Intermediate-Scale Quantum
(NISQ) <https://arxiv.org/abs/1801.00862>`__ computers. Aqua is an
open-source library completely written in Python and specifically
designed to be modular and extensible at multiple levels. Currently,
Aqua supports four applications, in domains that have long been
identified as potential areas for quantum computing: Chemistry,
Artificial Intelligence (AI), Optimization, and Finance. In this release,
we have added the following new features :

- Compatibility with Terra 0.7
- Compatibility with Aer 0.1
- Programmatic APIs for algorithms and components -- each component can now be instantiated and
  initialized via a single (non-empty) constructor call - ``QuantumInstance`` API for
  algorithm/backend decoupling -- ``QuantumInstance`` encapsulates a backend and its settings
- Updated documentation and Jupyter Notebooks illustrating the new programmatic APIs
- Transparent parallelization for gradient-based optimizers
- Multiple-Controlled-NOT (cnx) operation
- Pluggable algorithmic component ``RandomDistribution``
- Concrete implementations of ``RandomDistribution``: ``BernoulliDistribution``,
  ``LogNormalDistribution``, ``MultivariateDistribution``, ``MultivariateNormalDistribution``,
  ``MultivariateUniformDistribution``, ``NormalDistribution``, ``UniformDistribution``, and
  ``UnivariateDistribution``
- Pluggable algorithmic component:
- Concrete implementations of ``UncertaintyProblem``: ``FixedIncomeExpectedValue``,
  ``EuropeanCallExpectedValue``, and ``EuropeanCallDelta``
- Amplitude Estimation algorithm
- Qiskit Optimization: New Ising models for optimization problems exact cover, set packing, vertex
  cover, clique, and graph partition
- Qiskit AI:
   - New feature maps extending the ``FeatureMap`` pluggable interface: ``PauliExpansion`` and
     ``PauliZExpansion``
- Training model serialization/deserialization mechanism
- Qiskit Finance:
   - Amplitude estimation for Bernoulli random variable: illustration of amplitude estimation on a
     single qubit problem
   - Loading of multiple univariate and multivariate random distributions
   - European call option: expected value and delta (using univariate distributions)
   - Fixed income asset pricing: expected value (using multivariate distributions)

In this release, we have also removed the following new features:

- ``HartreeFock`` component of pluggable type ``InitialState`` moved to Qiskit Chemistry
- ``UCCSD`` component of pluggable type ``VariationalForm`` moved to Qiskit Chemistry

----------------------------------------------
New Features in the Aqua Library of Algorithms
----------------------------------------------

In this section, we describe the new features made available in Qiskit
Aqua 0.4 at the level of the library of algorithms.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Compatibility with Terra 0.7 and Aer 0.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aqua 0.4 is fully compatible with the latest version of Qiskit Terra,
0.7, and with the newly released Qiskit Aer 0.1. This allows you to
install and execute Aqua in the same Python environment as all the other
Qiskit elements and components.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
API-based Programmatic Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Aqua wizard allows you to use Aqua as a tool; you can configure and
execute quantum experiments without writing a line of code. However,
Aqua has a more powerful use case. In fact, Aqua is an extensible
library of quantum algorithms; users can extend it with new components
and program experiments by calling the Aqua APIs. In Aqua 0.4, we have
simplified the Aqua programmatic interface.

In previous versions of Aqua, in order to instantiate one of the
algorithmic components — such as algorithms, optimizers, variational
forms, oracles, feature maps and AI classifiers — you had to call either
the empty constructor or factory method of that component's class,
followed by a call to init_args containing the parameters needed for
that component to be initialized. That somewhat convoluted API structure
was implemented in order to reconcile a pure programmatic approach with
the declarative approach allowed by the Aqua wizard, which has the
ability to automatically discover and dynamically load new components at
run time. In order to simplify the programmatic approach, we have
deprecated the ``init_args`` API. Component classes no longer have empty
constructors. Rather, we now allow the constructor of each component to
take as parameters all the objects needed for that component to be fully
initialized. For example, this one line constructs and initializes an
instance of Grover's search algorithm:

.. code-block:: python

    algorithm = Grover(oracle)

where ``oracle`` is an instance of the Aqua Oracle interface.

It is also worth noting that, in previous versions of Aqua, a backend
was made available to an algorithm in the form of a string, and it was
the algorithm's responsibility to create an instance of the backend by
interpreting that string. Starting with this release, the Qiskit
ecosystem includes a new element: Qiskit Aer, consisting of a collection
of high-quality, high-performance and highly scalable simulators. Aer
will help us understand the limits of classical processors by
demonstrating to what extent they can mimic quantum computation.
Furthermore, we can use Aer to verify that current and near-future
quantum computers function correctly. Being fully integrated with the
newly released Aer 0.1, Aqua 0.4 allows for an experiment's backend to
be constructed programmatically from the Aer APIs.

Furthermore, we have decoupled the Aqua algorithms from the Terra
backends. An Aqua algorithm is now a pure implementation of a quantum
algorithm, and as such it is orthogonal to the notion of the backend on
which the algorithm-generated circuits will be executed. This decoupling
is reflected by the fact that the construction of a ``QuantumAlgorithm``
object no longer requires setting up the backend. Rather, the backend is
passed as a parameter to the ``run`` method of the ``QuantumAlgorithm`` object
as is, or wrapped in a ``QuantumInstance`` object along with
backend-configuration parameters.

The following program shows how to conduct a quantum programming experiment using
Aqua's improved programmatic interface:

.. code-block:: python

    from qiskit import Aer
    from qiskit_aqua.components.oracles import SAT
    from qiskit_aqua.algorithms import Grover
    sat_cnf = """
    c Example DIMACS 3-sat
    p cnf 3 5
    -1 -2 -3 0
    1 -2 3 0
    1 2 -3 0
    1 -2 -3 0
    -1 2 3 0
    """
    backend = Aer.get_backend('qasm_simulator')
    oracle = SAT(sat_cnf)
    algorithm = Grover(oracle)
    result = algorithm.run(backend)
    print(result["result"])

This program demonstrates how Grover's search algorithm can be used in conjunction
with the Satisfiability (SAT) oracle to compute one of the many possible solutions of a
Conjunctive Normal Form (CNF).

This example emphasizes the use of Aqua's improved programmatic
interface by illustrating how the Grover ``QuantumAlgorithm`` and its
supporting component—-consisting of the SAT ``oracle``, can both be instantiated and
initialized via simple constructor calls. The Aer QASM simulator
backend is passed as a parameter to the ``run`` method of the ``Grover`` ``QuantumAlgorithm``
object, which means that the backend will be executed with default
parameters.

To customize the backend, you can wrap it into a ``QuantumInstance`` object,
and then pass that object to the run method of the ``QuantumAlgorithm``, as
explained above. The ``QuantumInstance`` API allows you to customize
run-time properties of the backend, such as the number of shots, the
maximum number of credits to use, a dictionary with the configuration
settings for the simulator, a dictionary with the initial layout of
qubits in the mapping, and the Terra ``PassManager`` that will handle the
compilation of the circuits. For the full set of options, please refer
to the documentation of the Aqua ``QuantumInstance`` API.

Numerous new notebooks in the
`qiskit/aqua <https://github.com/Qiskit/qiskit-tutorials/tree/master/qiskit/aqua>`__
and
`community/aqua <https://github.com/Qiskit/qiskit-tutorials/tree/master/community/aqua>`__
folders of the `Qiskit
Tutorials <https://github.com/Qiskit/qiskit-tutorials>`__ repository
illustrate how to conduct a quantum-computing experiment
programmatically using the new Aqua APIs.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Transparent Parallelization of Gradient-based Optimizers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aqua comes with a large collection of adaptive algorithms, such as the
`Variational Quantum Eigensolver (VQE) algorithm <https://www.nature.com/articles/ncomms5213>`__,
`Quantum Approximate Optimization
Algorithm (QAOA) <https://arxiv.org/abs/1411.4028>`__, the `Quantum
Support Vector Machine (SVM) Variational
Algorithm <https://arxiv.org/abs/1804.11326>`__ for AI. All these
algorithms interleave quantum and classical computations, making use of
classical optimizers. Aqua includes nine local and five global
optimizers to choose from. By profiling the execution of the adaptive
algorithms, we have detected that a large portion of the execution time
is taken by the optimization phase, which runs classically. Among the
most widely used optimizers are the *gradient-based* ones; these
optimizers attempt to compute the absolute minimum (or maximum) of a
function :math:`f` through its gradient.

Five local optimizers among those integrated into Aqua are
gradient-based: the four local optimizers *Limited-memory
Broyden-Fletcher-Goldfarb-Shanno Bound (L-BFGS-B)*, *Sequential Least SQuares Programming
(SLSQP)*, *Conjugate Gradient (CG)*, and *Truncated Newton (TNC)* from
`SciPy <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html>`__,
as well as `Simultaneous Perturbation Stochastic Approximation
(SPSA) <https://www.jhuapl.edu/SPSA/>`__. Aqua 0.4 contains a
methodology that parallelizes the classical computation of the partial
derivatives in the gradient-based local optimizers listed above. This
parallelization takes place *transparently*, in the sense that Aqua
intercepts the computation of the partial derivatives and parallelizes
it without making any change to the actual source code of the
optimizers.

In order to activate the parallelization mechanism for an adaptive
algorithm included in Aqua, it is sufficient to construct it with
parameter ``batch_mode`` set to ``True``. Our experiments have proven
empirically that parallelizing the process of a gradient-based local
optimizer achieves a 30% speedup in the execution time of an adaptive algorithms on
a simulator.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Multiple-Controlled-NOT Operation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *Multiple-Controlled-NOT (cnx)* operation, as the name suggests, is
a generalization of the quantum operation where one target qubit is
controlled by a number *n* of control qubits for a NOT (`x`) operation.
The multiple-controlled-NOT operation can be used as the building block
for implementing various different quantum algorithms, such as Grover's
search algorithm.

For the different numbers 0, 1, 2, … of controls, we have corresponding
quantum gates ``x``, ``cx``, ``ccx``, ... The first three are basic/well-known
quantum gates. In Aqua, the cnx operation provides support for arbitrary
numbers of controls, in particular, 3 or above.

Currently two different implementation strategies are included: *basic*
and *advanced*. The basic mode employs a textbook implementation, where
a series of ``ccx`` Toffoli gates are linked together in a ``V`` shape to
achieve the desired multiple-controlled-NOT operation. This mode
requires :math:`n-2` ancillary qubits, where :math:`n` is the number of controls. For
the advanced mode, the ``cccx`` and ``ccccx`` operations are achieved without
needing ancillary qubits. Multiple-controlled-NOT operations for higher
number of controls (5 and above) are implemented recursively using these
lower-number-of-control cases.

Aqua's cnx operation can be invoked from a ``QuantumCircuit`` object
using the ``cnx`` API, which expects a list ``q_controls`` of control qubits,
a target qubit ``q_target``, and a list ``q_ancilla`` of ancillary qubits.
An optional keyword
argument ``mode`` can also be passed in to indicate whether the ``'basic'`` or
``'advanced'`` mode is chosen.  If omitted, this argument defaults to ``'basic'``.

^^^^^^^^^^^^^^^^^^^^
Random Distributions
^^^^^^^^^^^^^^^^^^^^

A random distribution is an implementation of a circuit factory. It
provides a way to construct a quantum circuit to prepare a state
corresponding to a random distribution. More precisely, the resulting
state, together with an affine map, can be used to sample from the
considered distribution. The qubits are measured and then mapped to
the desired range using the affine map. Aqua 0.4 introduces random
distributions in the form of the ``RandomDistribution`` pluggable
component, and provides numerous concrete implementations, such as
``BernoulliDistribution``, ``LogNormalDistribution``,
``MultivariateDistribution``, ``MultivariateNormalDistribution``,
``MultivariateUniformDistribution``, ``NormalDistribution``,
``UniformDistribution``, and ``UnivariateDistribution``.

^^^^^^^^^^^^^^^^^^^^
Uncertainty Problems
^^^^^^^^^^^^^^^^^^^^

Uncertainty is present in most realistic applications, and often it is
necessary to evaluate the behavior of a system under uncertain data. For
instance, in finance, it is of interest to evaluate expected value or
risk metrics of financial products that depend on underlying stock
prices, economic factors, or changing interest rates. Classically, such
problems are often evaluated using Monte Carlo simulation. However,
Monte Carlo simulation does not converge very fast, which implies that
large numbers of samples are required to achieve estimations of
reasonable accuracy and confidence. Uncertainty problems can be solved
by the amplitude estimation algorithm, discussed below. Aqua 0.4
introduces the ``UncertaintyProblem`` pluggable component and provides
implementations for several concrete uncertainty problems used in Aqua
Finance, such as ``FixedIncomeExpectedValue``, ``EuropeanCallExpectedValue`` and
``EuropeanCallDelta``.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Amplitude Estimation Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Aqua library of algorithms is fully extensible; new algorithms can
easily be plugged in. Aqua 0.4 includes a new algorithm: *Amplitude
Estimation*, which is a derivative of Quantum Phase Estimation applied
to a particular operator :math:`A`, assumed to operate on :math:`n + 1`
+ 1 qubits (plus possible ancillary qubits). Here, the first *n* qubits
encode the uncertainty (in the form of a random distribution), and the
last qubit, called the *objective qubit*, is used to represent the
normalized objective value as its amplitude. In other words, :math:`A` is
constructed such that the probability of measuring a `1` in the objective
qubit is equal to the value of interest. Amplitude estimation leads to a
quadratic speedup compared to the classical Monte Carlo approach when
solving an uncertainty problem. Thus, millions of classical samples
could be replaced by a few thousand quantum samples.

^^^^^^^^^^^^^^
Qiskit Finance
^^^^^^^^^^^^^^

The Amplitude Estimation algorithm, along with the ``RandomDistribution``
and ``UncertaintyProblem`` components introduced in Aqua 0.4, enriches the
portfolio of Finance problems that can be solved on a quantum computer.
These now include *European Call Option Pricing* (expected value and
delta, using univariate distributions) and *Fixed Income Asset Pricing*
(expected value, using multivariate distributions). New Jupyter
Notebooks illustrating the use of the Amplitude Estimation algorithm to
deal with these new problems are available in the `Qiskit Finance
tutorials
repository <https://github.com/Qiskit/qiskit-tutorials/tree/master/qiskit/aqua/finance>`__.

^^^^^^^^^
Qiskit AI
^^^^^^^^^

Aqua 0.4 introduces two new implementations of the FeatureMap pluggable
component, ``PauliZExpansion`` and ``PauliExpansion``.

The ``PauliZExpansion`` feature map is a generalization of the already
existing ``FirstOrderExpansion`` and ``SecondOrderExpansion`` feature maps,
allowing for the order of expansion *k* to be greater than 2.

The ``PauliExpansion`` feature map generalizes the existing feature maps
even more. Not only does this feature map allows for the order of
expansion *k* to be greater than 2, but it also supports Paulis *I*, *X*
and *Y*, in addition to *Z*.

Furthermore, we have improved both the Support Vector Machine Quantum
Kernel (QSVM Kernel) and Support Vector Machine Quantum Variational
(QSVM Variational) algorithms by allowing a training model to be
serialized to disk and dynamically retrieved in subsequent experiments.

^^^^^^^^^^^^^^^^^^^
Qiskit Optimization
^^^^^^^^^^^^^^^^^^^

In Aqua 0.4, we introduce new Ising models for the following
optimization problems: `exact
cover <https://en.wikipedia.org/wiki/Exact_cover>`__, `set
packing <https://en.wikipedia.org/wiki/Set_packing>`__, `vertex
cover <https://en.wikipedia.org/wiki/Vertex_cover>`__,
`clique <https://en.wikipedia.org/wiki/Clique_problem>`__, and `graph
partition <https://en.wikipedia.org/wiki/Graph_partition>`__. All this
problems are solved with VQE. Jupyter Notebooks illustrating how to use
a quantum computer to solve these problems are available in the `Qiskit
community Optimization tutorials
repository <https://github.com/Qiskit/qiskit-tutorials/tree/master/community/aqua/optimization>`__.
