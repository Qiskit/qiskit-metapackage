.. _aqua-optimization:

*******************
Qiskit Optimization
*******************

Qiskit Optimization is a set of tools and algorithms
that enable experimenting with optimization problems via quantum computing. Aqua Optimization
is the only end-to-end software stack that translates optimization-specific problems
into inputs for one of the :ref:`quantum-algorithms` in :ref:`aqua-library`,
which in turn uses Qiskit Terra for the actual quantum computation on top a
quantum simulator or a real quantum hardware device.

Qiskit Optimization allows users with different levels of experience to execute optimization
experiments and contribute to the quantum computing optimization software stack.
Users with a pure optimization background or interests can continue to configure
optimization problems without having to learn the details of quantum computing.

----------------------------
Qiskit Optimization Problems
----------------------------

Qiskit Optimization can already be used to experiment with numerous well known optimization
problems, such as:

1. `Stable Set <https://github.com/Qiskit/qiskit-tutorials/blob/master/community/aqua/optimization/stable_set.ipynb>`__
2. `Maximum Cut (Max-Cut) <https://github.com/Qiskit/qiskit-tutorials/blob/master/community/aqua/optimization/max_cut.ipynb>`__
3. `Partition <https://github.com/Qiskit/qiskit-tutorials/blob/master/community/aqua/optimization/partition.ipynb>`__
4. `3 Satisfiability (3-SAT) <https://github.com/Qiskit/qiskit-tutorials/blob/master/community/aqua/optimization/grover.ipynb>`__


--------------------------------
Aqua Algorithms for Optimization
--------------------------------

:ref:`aqua-library` includes numerous algorithms
that can be used to experiment with optimization problems.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
General Quantum Algorithms for Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following quantum algorithms are suitable to optimization problems:
:ref:`vqe`, :ref:`qaoa`, :ref:`qpe`, :ref:`iqpe` and :ref:`grover`.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Classical Reference Algorithms for Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To produce reference values and compare and contrast results during experimentation,
the Aqua library of :ref:`classical-reference-algorithms` includes the
:ref:`exact-eigensolver` and :ref:`cplex` classical algorithms.

-----------------------------------
Contributing to Qiskit Optimization
-----------------------------------

Research and developers interested in :ref:`aqua-extending` with new optimnization-specific
capabilities can take advantage
of the modular architecture of Aqua and easily extend Aqua with more algorithms
and algorithm components, such as new :ref:`oracles` for the :ref:`grover` algorithm,
:ref:`optimizers` and :ref:`variational-forms` for :ref:`vqe`, :ref:`qaoa`, and
:ref:`vqc`, :ref:`iqfts` for :ref:`qpe`, :ref:`initial-states` for
:ref:`variational-forms`, as well as :ref:`feature-maps` and :ref:`multiclass-extensions`
for Support Vector Machine


--------
Examples
--------

The ``optimization`` folder of the `Aqua Tutorials GitHub Repository
<https://github.com/Qiskit/aqua-tutorials>`__ contains numerous
`Jupyter Notebooks <http://jupyter.org/>`__ and sample input data files
explaining how to use Aqua Optimization.

