.. _oracles:

=======
Oracles
=======

An oracle is a black box operation used as input to another algorithm.
They tend to encode a function :math:`f:\{0,1\}^n \rightarrow \{0,1\}^m`
where the goal of the algorithm is to determine some property of :math:`f`.

The following quantum oracles are included in Aqua:

-  :ref:`SATisfiability Grover Oracle`
-  :ref:`Deutsch-Jozsa Oracle`
-  :ref:`Bernstein-Vazirani Oracle`
-  :ref:`Simon Oracle`

.. topic:: Extending the Oracle Library

    Consistent with its unique design, Aqua has a modular and extensible
    architecture. Algorithms and their supporting objects, such as oracles
    for Grover's Search Algorithm, are pluggable modules in Aqua.

    New oracles are typically installed in the ``qiskit_aqua/components/oracles``
    folder and derive from the ``Oracle`` class. Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new components can register
    themselves as Aqua extensions and be dynamically discovered at run time
    independent of their location in the file system. This is done in order to
    encourage researchers and developers interested in :ref:`aqua-extending` to
    extend the Aqua framework with their novel research contributions.

.. seealso::

    :ref:`aqua-extending` provides more details on how to extend Aqua with new
    components.

.. note::

    Each of the quantum oracles is created to be used with their respective
    :ref:`quantum-algorithms`. 


.. _sat:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SATisfiability Grover Oracle (SAT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`grover` is a well known quantum algorithm for searching through
unstructured collections of records for particular targets with quadratic
speedup compared to classical algorithms.

Given an input :math:`x` in set :math:`X` of :math:`N` elements
:math:`X=\{x_1,x_2,\ldots,x_N\}`, the Grover oracle implements the
boolean function :math:`f : X \rightarrow \{0,1\}`, such that
:math:`f(x^*)=1` for :math:`x^* \in X` and :math:`0` otherwise.

Currently, Aqua provides the SATisfiability (SAT) oracle implementation,
which takes as input an SAT problem specified as a formula in
`Conjunctive Normal Form (CNF) <https://en.wikipedia.org/wiki/Conjunctive_normal_form>`__
and searches for solutions to that problem. A CNF is a conjunction of one or
more clauses, where a clause is a disjunction of one or more literals:

.. code:: python

    cnf : str

The Aqua SAT oracle implementation expects a CNF to be a ``str`` value assigned
to the ``cnf`` parameter.  The value must be encoded in
`DIMACS CNF
format <http://www.satcompetition.org/2009/format-benchmarks2009.html>`__.
Once it receives a CNF as an input, the SAT oracle constructs the corresponding
quantum search circuit for Grover's Search Algorithm to operate upon.

Internally, SAT relies on ``mct``, the Multiple-Control Toffoli operation, for
circuit construction. Aqua includes three different modes for ``mct``, namely
``'basic'``, ``'advanced'``, and ``'noancilla'``:

.. code:: python

    mct_mode : str = 'basic' | 'advanced' | 'noancilla'

More information on ``mct`` and its three modes can be found at :ref:`mct`.

The following is an example of a CNF expressed in DIMACS CNF format:

.. code::

    c This is an example DIMACS 3-sat file with 3 satisfying solutions: 1 -2 3, -1 -2 -3, 1 2 -3.
    p cnf 3 5
    -1 -2 -3 0
    1 -2 3 0
    1 2 -3 0
    1 -2 -3 0
    -1 2 3 0

The first line, following the ``c`` character, is a comment. The second line
specifies that the CNF is over three boolean variables --- let us call them
:math:`x_1, x_2, x_3`, and contains five clauses.  The five clauses, listed
afterwards, are implicitly joined by the logical ``AND`` operator, 
:math:`\land`, while the variables in each clause, represented by their 
indices, are implicitly disjoined by the logical ``OR`` operator, :math:`lor`.
The :math:`-` symbol preceding a boolean variable index corresponds to the
logical ``NOT`` operator, :math:`lnot`.  Character ``0`` marks the end of each
clause.  Essentially, the code above corresponds to the following CNF:
:math:`(\lnot x_1 \lor \lnot x_2 \lor \lnot x_3) 
\land (x_1 \lor \lnot x_2 \lor x_3) 
\land (x_1 \lor x_2 \lor \lnot x_3) 
\land (x_1 \lor \lnot x_2 \lor \lnot x_3) 
\land (\lnot x_1 \lor x_2 \lor x_3)`.

Examples showing how to use the Grover algorithm in conjunction with the SAT
oracles to search for solutions to SAT problems are available in the
``optimization`` folder of the `Qiskit Tutorials GitHub repository 
<https://github.com/Qiskit/qiskit-tutorials/tree/master/community/aqua>`__.

.. topic:: Declarative Name

   When referring to the SAT oracle declaratively inside Aqua, its code
   ``name``, by which Aqua dynamically discovers and loads it, is ``SAT``.

.. _djoracle:

^^^^^^^^^^^^^^^^^^^^
Deutsch-Jozsa Oracle
^^^^^^^^^^^^^^^^^^^^

The Deutsch-Jozsa oracle implements a function
:math:`f:\{0,1\}^n \rightarrow \{0,1\}`.
The function must be either balanced (0 for half the ouputs and 1 for the
other half) or constant (0 for all outputs or 1 for all outputs).

The oracle takes as a dictionary as input that contains the bitmap of
:math:`f(x)` on all length :math:`n` bitstrings.

.. code:: python

    bitmap : {}

The following is an example of a bitmap dictionary representing a balanced
3-bit function:

.. code:: python

    {'000': '1', '001': '1', '010': '1', '011': '1',
     '100': '0', '101': '0', '110': '0', '111': '0'}

.. topic:: Declarative Name

   When referring to the Deutsch-Jozsa oracle declaratively inside Aqua, its
   code ``name``, by which Aqua dynamically discovers and loads it, is
   ``DeutschJozsaOracle``.


.. _bvoracle:

^^^^^^^^^^^^^^^^^^^^^^^^^
Bernstein-Vazirani Oracle
^^^^^^^^^^^^^^^^^^^^^^^^^

The Bernstein-Vazirani oracle implements a function
:math:`f:\{0,1\}^n \rightarrow \{0,1\}`,
such that :math:`f(x)=s \cdot x (\bmod 2)` for some :math:`s \in \{0,1\}^n`.

The oracle takes as a dictionary as input that contains the bitmap of
:math:`f(x)` on all length :math:`n` bitstrings.

.. code:: python

    bitmap : {}

The following is an example of a bitmap dictionary representing a 3-bit
function where :math:`s = 101`:

.. code:: python

    {'000': '0', '001': '1', '010': '0', '011': '1',
     '100': '1', '101': '0', '110': '1', '111': '0'}

.. topic:: Declarative Name

   When referring to the Bernstein-Vazirani oracle declaratively inside Aqua,
   its code ``name``, by which Aqua dynamically discovers and loads it, is
   ``BernsteinVaziraniOracle``.

.. _simonoracle:

^^^^^^^^^^^^^^^^^^^^^^^^^
Simon Oracle
^^^^^^^^^^^^^^^^^^^^^^^^^

The Simon oracle implements a function
:math:`f:\{0,1\}^n \rightarrow \{0,1\}^n`, such that either:

1. :math:`f` is one-to-one (a permuation), or
2. :math:`f` is two-to-one where
   :math:`f(\mathbf{x}) = f(\mathbf{y})
   \Leftrightarrow \mathbf{y} \oplus \mathbf{x} = \mathbf{s}`.

Note that (1) is a special case of (2) with :math:`\mathbf{s} = \mathbf{0}`.

The oracle takes as a dictionary as input that contains the bitmap of
:math:`f(x)` on all length :math:`n` bitstrings.

.. code:: python

    bitmap : {}

The following is an example of a bitmap dictionary representing a 3-bit
function where :math:`s = 110`:

.. code:: python

    {'000': '101', '001': '010', '010': '000', '011': '110',
     '100': '000', '101': '110', '110': '101', '111': '010'}

.. topic:: Declarative Name

   When referring to the Simon oracle declaratively inside Aqua, its code
   ``name``, by which Aqua dynamically discovers and loads it, is
   ``SimonOracle``.
