.. _aqua-finance:

**************
Qiskit Finance
**************

Qiskit Finance is a set of tools and algorithms
that enable experimenting with financial analysis and optimization problems
via quantum computing. Aqua Finance
is the only end-to-end software stack that translates finance-specific problems
into inputs for one of the :ref:`quantum-algorithms` in :ref:`aqua-library`,
which in turn uses Qiskit Terra for the actual quantum computation on top a
quantum simulator or a real quantum hardware device.

Qiskit Finance allows users with different levels of experience to execute financial analysis and
optimization experiments and contribute to the quantum computing finance software stack.
Users with a pure finance background or interests can continue to configure
financial analysis and optimization problems without having to learn the details of the
underlying quantum computing system.

-----------------------
Qiskit Finance Problems
-----------------------

Aqua Finance can already be used to experiment with financial analysis and optimization problems,
such as risk analysis and
`portfolio optimization <https://github.com/Qiskit/aqua-tutorials/blob/master/finance/portfolio_optimization.ipynb>`__.

------------------------------
Contributing to Qiskit Finance
------------------------------

Research and developers interested in :ref:`aqua-extending` with new finance-specific
capabilities can take advantage
of the modular architecture of Aqua and easily extend Aqua with more algorithms
and algorithm components, such as new :ref:`oracles` for the :ref:`grover` algorithm,
:ref:`optimizers` and :ref:`variational-forms` for :ref:`vqe`, :ref:`qaoa`, and
:ref:`vqc`, :ref:`iqfts` for :ref:`qpe`, :ref:`initial-states` for
:ref:`variational-forms`, as well as :ref:`feature-maps` and :ref:`multiclass-extensions`
for Support Vector Machine (SVM) algorithms, such as :ref:`vqc` and
:ref:`qsvm`.


--------
Examples
--------

The ``finance`` folder of the `Aqua Tutorials GitHub Repository
<https://github.com/Qiskit/aqua-tutorials>`__ contains
`Jupyter Notebooks <http://jupyter.org/>`__ and sample input data files
explaining how to use Aqua Finance.

