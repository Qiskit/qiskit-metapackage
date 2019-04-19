.. _oracles:

=======
Oracles
=======

An oracle is a black box operation used as input to another algorithm.
They tend to encode a function :math:`f:\{0,1\}^n \rightarrow \{0,1\}^m`
where the goal of the algorithm is to determine some property of :math:`f`.

The following quantum oracles are included in Aqua:

-  :ref:`Logic Expression Oracle`
-  :ref:`Truth Table Oracle`
-  :ref:`Custom Circuit Oracle`

.. topic:: Extending the Oracle Library

    Consistent with its unique design, Aqua has a modular and extensible
    architecture. Algorithms and their supporting objects, such as oracles,
    are pluggable modules in Aqua,
    and are able to be used in a plug-and-play fashion, when appropriate.
    For example, The Grover's Search algorithm would be able to take
    any single-valued binary oracles, while the Deutsch Jozsa algorithm
    can work on single-valued oracles that represent constant or balanced
    functions only.

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

.. _logical-expression-oracle:

^^^^^^^^^^^^^^^^^^^^^^^^^
Logical Expression Oracle
^^^^^^^^^^^^^^^^^^^^^^^^^

The Logical Expression Oracle, as its name suggests,
constructs circuits for any arbitrary input logical expressions.
A logical expression is composed of logical operators
``&`` (``AND``), ``|`` (``OR``), ``~`` (``NOT``), and ``^`` (``XOR``),
as well as symbols for literals (variables).
For example, ``'a & b'``, and ``(v[0] | ~v[1]) ^ (~v[2] & v[3])``.
Aqua's logical expression oracle`` relies on the
`PyEda package <https://pyeda.readthedocs.io>`__
to try to parse any input strings, assuming no predetermined formats.

.. code:: python

    expression : str

For convenience, this oracle,
in addition to trying to parse arbitrary logical expressions,
also supports input strings in the `DIMACS CNF
format <http://www.satcompetition.org/2009/format-benchmarks2009.html>`__,
which is the standard format
for specifying SATisfiability (SAT) problem instances
in `Conjunctive Normal Form (CNF)
<https://en.wikipedia.org/wiki/Conjunctive_normal_form>`__,
which is a conjunction of one or more clauses,
where a clause is a disjunction of one or more literals.

The following is an example of a CNF expressed in DIMACS format:

.. code:: text

    c This is an example DIMACS CNF file with 3 satisfying assignments: 1 -2 3, -1 -2 -3, 1 2 -3.
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

An example showing how to use the Grover algorithm on a DIMACS oracle
to search for a satisfying assignment to an SAT problem encoded in DIMACS
is available in the ``optimization`` folder of the
`Qiskit Tutorials GitHub repository
<https://github.com/Qiskit/qiskit-tutorials/tree/master/community/aqua>`__.

Logic expressions, regardless of the input formats,
are parsed and stored as Abstract Syntax Tree (AST) tuples,
from which the corresponding circuits are constructed.
The oracle circuits can then be used with
any oracle-oriented algorithms when appropriate.
For example, an oracle built from a DIMACS input
can be used with the Grover's algorithm to search for
a satisfying assignment to the encoded SAT instance.

.. topic:: Circuit Optimization

   By default,
   Aqua's logical expression oracle would not try to apply any optimization
   when building the circuits. For any ``DIMACS`` input,
   the constructed circuit truthfully recreates each inner disjunctive clauses
   as well as the outermost conjunction; For other arbitrary input expression,
   Aqua only tries to convert it to a CNF or DNF (Disjunctive Normal Form,
   similar to CNF, but with inner conjunctions and a outer disjunction)
   before constructing its circuit.
   This, for example, could be good for educational purposes,
   where a user would like to compare a built circuit against their input
   expression to examine and analyze details.
   However, this oftentimes leads to relatively deep circuits that possibly
   also involve many ancillary qubits.
   Aqua, therefore, provides the option to try to minimize the input
   logical expression before building its circuit.
   The minimization is carried out via `PyEda`,
   which internally uses the `Espresso heuristic logic minimizer
   <https://en.wikipedia.org/wiki/Espresso_heuristic_logic_minimizer>`__.

.. code:: python

   optimization : str = 'off' | 'espresso'

Currently, only the ``'espresso'`` optimization mode is supported by
the logical expression oracle. When omitted, it will default to ``off``,
indicating no optimization.

Internally, the logical expression oracle relies heavily on ``mct``,
the Multiple-Control Toffoli operation, for circuit constructions.
Aqua includes three different modes for ``mct``, namely
``'basic'``, ``'advanced'``, and ``'noancilla'``:

.. code:: python

    mct_mode : str = 'basic' | 'advanced' | 'noancilla'

More information on ``mct`` and its three modes can be found at :ref:`mct`.

.. topic:: Declarative Name

   When referring to the logical expression oracle declaratively inside Aqua,
   its code ``name``, by which Aqua dynamically discovers and loads it, is
   ``LogicExpressionOracle``.


.. _truth-table-oracle:

^^^^^^^^^^^^^^^^^^
Truth Table Oracle
^^^^^^^^^^^^^^^^^^

Besides logical expressions,
another common way of specifying boolean functions is using truth tables,
which is basically an exhaustive mapping
from input binary bit-strings of length :math:`n`
to corresponding output bit-strings of length :math:`m`.
For example,
the following is a simple truth table that corresponds to
the ``XOR`` of two variables:

=====  =====  =============
   Inputs        Output
------------  -------------
``A``  ``B``  ``A xor B``
=====  =====  =============
  0      0       0
  0      1       1
  1      0       1
  1      1       0
=====  =====  =============

In this case :math:`n=2`, and :math:`m=1`.
Oftentimes, for brevity, the input bit-strings are omitted
because they can be easily derived for any given :math:`n`.
So to completely specify a truth table,
we only need a Length-2 :sup:`n` bit-string for each of the :math:`m` outputs.
In the above example, a single bit-string ``'0110'`` would suffice.
Besides ``'0'`` and ``'1'``, one can also use ``'x'`` in the output string to
indicate ``'do-not-care'`` entries.
For example, ``'101x'`` specifies a truth table
(again :math:`n=2` and :math:`m=1`)
for which the output upon input ``'11'`` doesn't matter.
Aqua's truth table oracle takes either a single string
or a list of equal-length strings for truth table specifications.

.. code:: python

    bitmaps : str | [str]

Regarding circuit optimization and mct usages,
the truth table oracle is similar to the logical expression oracle.
So the parameters ``optimization`` and ``mct_mode`` can also be supplied here.
One difference is that,
unlike the logical expression oracle who builds circuits out of CNF or DNF,
the truth table oracle uses Exclusive Sum of Products (ESOP),
which is similar to DNF,
with the only difference being the outermost operation being ``XOR``
as opposed to a disjunction.
Because of this difference,
an implicant-based method is used here for circuit optimization:
First, the
`Quine-McCluskey algorithm
<https://en.wikipedia.org/wiki/Quine-McCluskey_algorithm>`__
is used to find all prime implicants
of the input truth table; then an
`Exact Cover <https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X>`__
is found among all prime implicants and truth table onset row entries.
The exact cover is then used to build the corresponding oracle circuit.

.. code:: python

    optimization : str = 'off' | 'qm-dlx'

Currently, the only optimization mode supported by
the truth table oracle is ``'qm-dlx'``,
which stands for Quine-McCluskey with Dancing Links (Knuth's Algorithm X).
When omitted, it will default to ``off``, indicating no optimization.

.. topic:: Declarative Name

   When referring to the Truth Table Oracle declaratively inside Aqua,
   its code ``name``, by which Aqua dynamically discovers and loads it, is
   ``TruthTableOracle``.


.. _custom-circuit-oracle:

^^^^^^^^^^^^^^^^^^^^^
Custom Circuit Oracle
^^^^^^^^^^^^^^^^^^^^^

This class is provided for easy creation of oracles using custom circuits.
It is geared towards programmatically experimenting with oracles,
where a user would directly provide a ``QuantumCircuit`` object
corresponding to the intended oracle function,
together with the various ``QuantumRegister`` objects involved.

.. code:: python

    variable_register : QuantumRegister = The register holding the variables

    output_register : QuantumRegister = The register holding the output(s)

    ancillary_register : QuantumRegister = The optional register holding ancillae

    circuit: QuantumCircuit = The actual circuit for the oracle function
