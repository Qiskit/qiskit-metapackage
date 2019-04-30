.. _aqua-ai:

******************************
Qiskit Artificial Intelligence
******************************

Qiskit Artificial Intelligence (AI) is a set of tools and algorithms
that enable experimenting with AI problems via quantum computing. Aqua AI
is the only end-to-end software stack that translates AI-specific problems
into inputs for one of the :ref:`quantum-algorithms` in :ref:`aqua-library`,
which in turn uses Qiskit Terra for the actual quantum computation on top a
quantum simulator or a real quantum hardware device.

Qiskit AI allows users with different levels of experience to execute AI
experiments and contribute to the quantum computing AI software stack.
Users with a pure AI background or interests can continue to configure AI problems
without having to learn the details of quantum computing.

---------------------
Applicable Algorithms
---------------------

There are numerous algorithms from :ref:`aqua-library` that can be applied
to AI problems.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AI-specific Quantum Algorithms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aqua AI comes with two quantum Support Vector Machine (SVM) algorithms
already integrated into the Aqua library:

1. The :ref:`qsvm` algorithm applies to classification problems that
   require a feature map for which computing the kernel is not efficient
   classically. This means that the required computational resources are
   expected to scale exponentially with the size of the problem.
   QSVM uses a Quantum processor to solve this problem by a direct
   estimation of the kernel in the feature space. The method used falls in
   the category of what is called *supervised learning*, consisting of a
   *training phase* (where the kernel is calculated and the support vectors
   obtained) and a *test or classification phase* (where new labelless data
   is classified according to the solution found in the training phase).

2. The :ref:`vqc` algorithm also applies to
   classification problems that require a feature map for which computing
   the kernel is not efficient classically. SVM Variational uses the variational
   method to solve such problems in a quantum processor.  Specifically, it optimizes
   a parameterized quantum circuit to provide a solution that cleanly
   separates the data.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
General Quantum Algorithms for AI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Other quantum algorithms available in Aqua
that can be used to experiment with AI problems
include :ref:`vqe`, :ref:`qaoa`, :ref:`qpe`, :ref:`iqpe` and :ref:`grover`.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Classical Reference Algorithms for AI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To produce reference values and compare and contrast results during experimentation,
the Aqua library of :ref:`classical-reference-algorithms` also includes the
:ref:`avm-rbf-kernel` classical algorithm.

-------------------------
Contributing to Qiskit AI
-------------------------

Research and developers interested in :ref:`aqua-extending` with new AI-specific
capabilities can take advantage
of the modular architecture of Aqua and easily extend Aqua with more algorithms
and algorithm components, such as new :ref:`oracles` for the :ref:`grover` algorithm,
:ref:`optimizers` and :ref:`variational-forms` for :ref:`vqe`, :ref:`qaoa`, and
:ref:`vqc`, :ref:`iqfts` for :ref:`qpe`, :ref:`initial-states` for
:ref:`variational-forms`, as well as :ref:`feature-maps` and
:ref:`multiclass-extensions` for Support Vector Machine
(SVM) algorithms, such as :ref:`vqc` and :ref:`qsvm`.


--------
Examples
--------

The ``artificial_intelligence`` folder of the `Aqua Tutorials GitHub Repository
<https://github.com/Qiskit/aqua-tutorials>`__ contains numerous
`Jupyter Notebooks <http://jupyter.org/>`__ and input data files
explaining how to use Aqua AI.
