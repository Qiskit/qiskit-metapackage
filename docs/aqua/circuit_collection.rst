.. _circuit-collection:

===============================================================================================
A Collection of Circuits and Gates for Building Higher Level Circuits, Components and Algorithm
===============================================================================================

Aqua provides easy access to a collection of commonly used
:ref:`collection-circuits` and :ref:`collection-gates`
to be used as the building blocks for various components, algorithms and applications.
The gates can be enabled by corresponding imports from ``qiskit.aqua.circuits.gates``
and then directly invoked from ``QuantumCircuit`` objects.
The circuits can be accessed by importing corresponding classes from ``qiskit.aqua.circuits``.

.. _collection-gates:

-----
Gates
-----

The following gates are part of the collection:

- :ref:`mct`
- :ref:`rpt`
- :ref:`mcmt`
- :ref:`ch-gate`
- :ref:`cry-gate`
- :ref:`mcr-gates`
- :ref:`mcu1-gate`
- :ref:`logical-gates`

.. _mct:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Multiple-Control Toffoli (MCT) Gate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *Multiple-Control Toffoli (mct)* gate, as the name suggests, is
a generalization of the traditional Toffoli gate s.t. one target qubit is
controlled by an arbitrary number of control qubits for a NOT (`x`) operation.
The MCT gate can be used as the building block
for implementing various different quantum algorithms, such as Grover's search.

For the different numbers 0, 1, 2, … of controls, we have corresponding
quantum gates ``x``, ``cx``, ``ccx``, ... The first three are basic/well-known
quantum gates. In Aqua, ``mct`` provides support for arbitrary
numbers of controls, in particular, 3 or above.

Currently four different implementation strategies are included: *basic*,
*basic-dirty-ancilla*, *advanced*, and *noancilla*.
The basic mode employs a textbook
implementation, where a series of ``ccx`` Toffoli gates are linked
together in a ``V`` shape to achieve the desired Multiple-Control Toffoli
operation. This mode requires :math:`n-2` ancillary qubits, where
:math:`n` is the number of controls.
The basic-dirty-ancilla mode is the same as the basic mode
except that it allows using dirty ancillary qubits,
whereas the basic mode requires clean ancillae.
For the advanced mode, the ``cccx``
and ``ccccx`` operations are achieved without needing ancillary
qubits. Multiple-Control Toffoli operations for higher
number of controls (5 and above) are implemented recursively using these
lower-number-of-control cases. For the noancilla mode, no ancillary
qubits are needed even for higher number of controls. This uses a
technique of spliting multiple-control Toffoli operations, which is
efficient up to 8 controls but gets inefficient in the number of required
basic gates for values above. This technique relies on ``mcu1``, see
:ref:`mcu1 gate <mcu1-gate>` for more information.

Aqua's MCT gate can be invoked from a ``QuantumCircuit`` object
using the ``mct`` API, which expects a list ``q_controls`` of control qubits,
a target qubit ``q_target``, and a list ``q_ancilla`` of ancillary qubits.
An optional keyword argument ``mode`` can also be passed in to indicate
whether the ``'basic'``, ``'basic-dirty-ancilla'``, ``'advanced'``,
or ``'noancilla'`` mode is chosen.
If omitted, this argument defaults to ``'basic'``.


.. _rpt:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Relative-Phase Toffoli Gates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toffoli gates are helpful in implementing various other quantum circuits,
including the Multiple-Control Toffoli gates discussed above.
However, the usage of Toffoli gates might incur high costs in terms of circuit depth
depending on the particular implementations selected.
One approach that has been studied to mitigate this problem
is the use of Toffoli gates *up to a relative phase*,
for example, as discussed in `this paper <https://arxiv.org/abs/1508.03273>`__.
In Aqua, two such Relative-Phase Toffoli gates are provided,
the 2-Control ``rccx`` and the 3-Control ``rcccx``.
Upon import, both can be directly invoked from QuantumCircuit objects
similar to the traditional Toffoli ``ccx`` gate.


.. _mcmt:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Multiple-Control Multiple-Target (MCMT) Gate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *Multiple-Control Multiple-Target (mcmt)* Gate, as the name suggests,
allows to generalize a single-control, single-target gate (such as `cz`) to
support multiple control qubits and multiple target qubits.
In other words, the single-control gate passed as argument is applied to all
the target qubits if all the control qubits are active.

The kind of gate to apply can be passed as a parameter and should be a single
control gate already defined for a ``QuantumCircuit`` object (such as
``QuantumCircuit.cz`` or ``QuantumCircuit.ch``).

Currently, just one implementation strategy is implemented: *basic*. It
employs almost the same strategy adopted for the basic mode of `mct`:
multiple Toffoli gates are chained together to get the logical `AND` of
all the control qubits on a single ancilla qubit, which is then used as the
control of the single-control gate function.

This mode requires :math:`n-1` ancillary qubits, where :math:`n` is the
number of controls. Compare this with ``mct`` mode which uses :math:`n-2`
ancillary qubits for the same strategy. The difference is due to the fact
that in ``mct`` the chain ends with a single ``ccx`` writing on the target
qubit, while in ``mcmt`` the chain ends with the ``ccx`` writing on an
ancillary qubit, which is then used as the control qubit of the single-control
gate function.

Aqua's mcmt operation can be invoked from a ``QuantumCircuit`` object
using the ``mcmt`` API, which expects a list ``q_controls`` of control qubits,
a list ``q_targets`` of target qubits, a list ``q_ancilla`` of ancillary qubits
that must be off and are promised to be off after the function call, and a
function ``single_control_gate_fun`` which is the generic function to
apply to the ``q_targets`` qubits. An optional keyword argument ``mode`` can
also be passed in to indicate the mode, but at the moment only the ``'basic'``
mode is supported. If omitted, this argument defaults to ``'basic'``.


.. _ch-gate:

^^^^^^^^^^^^^^^^^^^^^^^^
Controlled-Hadamard Gate
^^^^^^^^^^^^^^^^^^^^^^^^

The controlled-Hadamard, or ``ch``, gate is already provided by Terra,
but it uses two ``cx`` gates in its implementation.
Aqua's ``ch`` gate only uses a single ``cx`` and is thus more efficient.
Upon import, Aqua's ``ch`` will automatically replace Terra's ``ch`` with no
invocation difference.


.. _cry-gate:

^^^^^^^^^^^^^^^^^^
Controlled-RY Gate
^^^^^^^^^^^^^^^^^^

The controlled-RY, or ``cry``, gate takes as input a rotation angle as well as the
control and target qubits.
Upon import, Aqua's ``cry`` can be directly invoked from QuantumCircuit objects.


.. _mcr-gates:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Multiple-Control Rotation (MCRX, MCRY, MCRZ) Gates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *Multiple-Control Rotation (mcrx, mcry, mcrz)* gates, implements
rotations around X-, Y-, and Z-axis on a single target qubit with an
arbitrary number of control qubits. The MCR operations take one rotation
angle as input parameter. The ``mcry`` gate supports two modes of
operation: *basic* and *noancilla*. Mode *basic* takes an
additional ancillary register to perform the rotation. See :ref:`mct
gate <mct>` for more information. In mode *noancilla* no ancillary
qubits are needed. This is the standard mode for ``mcrx`` and ``mcrz``
gates. It is efficiently implemented by using a grey code sequence for up
to 8 control qubits. For larger number of controls this implementation
gets very inefficient.

Aqua's ``mcrx``, ``mcry``, and ``mcrz`` operations can be invoked from a
``QuantumCircuit`` object and expect a list ``control_qubits`` of control
qubits and a target qubit ``target_qubit`` as well as an angle ``theta``
for the ``mcrx`` and ``mcry`` operation or ``lam`` for the ``mcrz``
operation.


.. _mcu1-gate:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Multiple-Control U1 (MCU1) Gate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *Multiple-Control Rotation (mcu1)* gate, implements a U1 (`u1`)
rotation (phase rotation) on a single target qubit with an arbitrary number
of control qubits. The MCU1 operation takes one rotation angle as input
parameter. No ancillary qubits are needed. It is efficiently implemented
by using a grey code sequence for up to 8 control qubits. For larger
number of controls this implementation gets very inefficient.

Aqua's ``mcu1`` operation can be invoked from a ``QuantumCircuit``
object and expect a list ``control_qubits`` of control qubits and a target
qubit ``target_qubit`` as well as an angle ``lam``.


.. _logical-gates:

^^^^^^^^^^^^^^^^^^^^^
Boolean Logical Gates
^^^^^^^^^^^^^^^^^^^^^

Aqua also provides the logical *AND* and *OR* gates to mirror the corresponding classic
logical operations.
*OR* gates are converted to *AND* gates using De Morgan's Law.
*AND* gates are implemented using :ref:`mct gate <mct>`.

The ``AND`` and ``OR`` gates can be invoked from a ``QuantumCircuit`` object.
They both expect a ``qr_variables`` register holding the variable qubits,
a ``qb_target`` qubit for holding the result,
a ``qr_ancillae`` register to use as ancilla,
an optional ``flags`` list of ``+1``, ``0``, or ``-1`` values
indicating the signs or omissions of the variable qubits,
and an optional ``mct_mode`` flag for specifying the mode to use for ``mct``.


.. _collection-circuits:

--------
Circuits
--------

The following circuits are part of the collection:

- :ref:`logical-circuits`
- :ref:`fourier-transform-circuits`
- :ref:`statevector_circuit`


.. _logical-circuits:

^^^^^^^^^^^^^^^^^^^^^^^^
Boolean Logical Circuits
^^^^^^^^^^^^^^^^^^^^^^^^

Aqua provides a simple set of tools for constructing circuits
from simple Boolean logical expressions.
Currently three types of expressions are supported:
Conjunctive Normal Forms (``CNF``), Disjunctive Normal Forms (``DNF``), and
Exclusive Sum of Products (``ESOP``).
They are also used internally by Aqua for constructing various :ref:`oracles`.
For initialization of each of the three types of objects,
the corresponding logical expression
can be specified as a tuple corresponding to the Abstract Syntax Tree (AST)
of the desired expression,
where each literal's absolute value indicates a variable,
and a negative sign indicates the negation of the corresponding variable.
The logical operations represented by the inner and outer lists
depend on the particular type (CNF, DNF, or ESOP) of objects being created.
For example, below is the AST for a simple CNF expression:

.. code:: python

  ('and',
    ('or', ('lit', 1), ('lit', -2)),
    ('or', ('lit', -1), ('lit', 2)))

The ``CNF``, ``DNF``, and ``ESOP`` objects, upon the aforementioned AST initialization,
can generate their corresponding circuits from the API call ``construct_circuit``,
which takes a ``circuit`` object to extend from,
a ``variable_register`` for holding the variables of the logic expression,
a ``clause_register`` for holding the intermediate results of all clauses of the expression,
an ``output_register`` for holding the result,
an ``ancillary_register`` for all other ancillae,
and an ``mct_mode`` flag for specifying the mode to use for ``mct``.
All these arguments are optional can will be properly handled if omitted.


.. _fourier-transform-circuits:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Quantum Fourier Transform Circuits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quantum Fourier Transform is another technique commonly used in quantum algorithms,
for example, Phase Estimation and the Shor's factoring algorithm.
The ``FourierTransformCircuits`` class in Aqua's ``circuits`` library
is capable of constructing, for any specified number ``num_qubits`` of qubits,
both the normal quantum Fourier transform (qft) circuits
and the *inverse* quantum Fourier transform (iqft) circuits,
as can be specified by the ``inverse`` Boolean flag.
For each, an ``approximation_degree`` can also be specified
to build the approximation circuits with the desired approximation degree.

Besides being directly exposed as circuits,
``qft`` and ``iqft`` are also accessible as Aqua's pluggable ``components``.
More detailed discussion on quantum Fourier transform can be found at
:ref:`iqfts`.


.. _statevector_circuit:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Arbitrary State Vector Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The circuit library also includes the ability to construct circuits from arbitrary
state vectors, via the ``StateVectorCircuit`` class,
which can be initialized using any arbitrary input state vector.
The ``construct_circuit`` method,
which takes optional ``circuit`` and ``register`` parameters,
can then build the corresponding circuit
using the basis ``u1``, ``u2``, ``u3``, ``cx``, and ``id`` gates.
This functionality is also exposed via
the ``CUSTOM`` mode of Aqua's ``InitialState`` pluggable component,
which is detailed at :ref:`custom-initial-states`.
