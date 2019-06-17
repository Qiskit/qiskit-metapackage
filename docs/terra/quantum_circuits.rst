======================
Circuits and Registers
======================

The ``QuantumCircuit``, ``QuantumRegister``, and ``ClassicalRegister``
are the main objects for Qiskit Terra. You can create custom circuits,
combine existing circuits, manipulate a circuit's structure,
and index into circuit elements.

The following imports will be used in the examples below.

.. code:: python

    import numpy as np
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
    from qiskit import BasicAer, execute
    from qiskit.quantum_info import Pauli, state_fidelity, basis_state, process_fidelity



------------------
Creating Registers
------------------

Quantum and classical registers are declared using the following:

.. code:: python

    q0 = QuantumRegister(2, 'q0')
    c0 = ClassicalRegister(2, 'c0')
    q1 = QuantumRegister(2, 'q1')
    c1 = ClassicalRegister(2, 'c1')
    q_test = QuantumRegister(2, 'q0')

The name is optional. If not given Qiskit will name it ``qi`` where
``i`` is an integer which will count from 0. The name and size can
be returned using the following:

.. code:: python

    print(q0.name)
    print(q0.size)

.. code-block:: text

    q0
    2

You can test if the register are the same or different.

.. code:: python

    q0==q0

.. code-block:: text

    True

.. code:: python

    q0==q_test

.. code-block:: text

    True

.. code:: python

    q0==q1

.. code-block:: text

    False



-----------------
Creating Circuits
-----------------

Quantum Circuits are made using registers. Either when initiated or by
using the ``add_register`` command.

.. code:: python

    circ = QuantumCircuit(q0, q1)
    circ.x(q0[1])
    circ.x(q1[0])
    circ.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_13_0.png
  :alt: Quantum circuit with 4 qubits, X gates on qubits 1 and 2.

is the same as

.. code:: python

    circ2 = QuantumCircuit()
    circ2.add_register(q0)
    circ2.add_register(q1)
    circ2.x(q0[1])
    circ2.x(q1[0])
    circ2.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_13_0.png
  :alt: Quantum circuit with 4 qubits, X gates on qubits 1 and 2.


.. note::

    The order of registers in the list is the order they are initiated
    or added **not** the tensor product for quantum registers.

.. code:: python

    from copy import deepcopy

    q3 = QuantumRegister(2, 'q3')
    circ3 = deepcopy(circ)
    circ3.add_register(q3)
    circ3.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_15_0.png
  :alt: Quantum circuit with 6 qubits, two sets of labels, and X gates on
    qubits q0_1 and q1_0.


.. note::

    The circuit drawer has the last register added at the bottom and
    if we add a new register it will add it to the bottom of the circuit.

Circuits can also be created without predefined registers. Instead, you can
supply the the number of qubits (required) and the number of classical bits
(optional) to ``QuantumCircuit()``.

.. code:: python

  num_qubits = 3;
  num_bits   = 2;
  qc = QuantumCircuit(num_qubits, num_bits)

With this syntax, registers are created automatically and can be accessed as
properties of the ``QuantumCircuit``.

.. code:: python

  print(qc.qregs)
  print(qc.cregs)

.. code-block:: text

  [QuantumRegister(3, 'q')]
  [ClassicalRegister(2, 'c')]

Qubits and bits can be indexed directly, without indexing into a
``QuantumRegister``. A gate's expected argument types will determine whether an
index refers to a qubit or a bit. For example, ``cx`` expects a qubit followed
by a bit.

.. code:: python

  num_qubits = 2;
  num_bits   = 2;
  bell = QuantumCircuit(2,2)
  bell.h(0)
  bell.cx(0, 1)
  bell.measure([0,1], [0,1])

  bell.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_3.png
  :alt: Quantum circuit with 2 qubits, 2 bits, an H gate on qubit 0, CNOT
    targeting qubit 1 controlled by qubit 0 and measurements on both qubits.

The indexing method above works for ``QuantumCircuit`` objects constructed with
or without predefined ``QuantumRegister`` objects.

For circuits with multiple registers, index ordering will correspond to the
order registers were added to the circuit, and can be verified by inspecting the
circuit's ``qubits`` and ``clbits`` properties.

.. code:: python

  qr1 = QuantumRegister(1, 'q1')
  qr2 = QuantumRegister(1, 'q2')
  cr = ClassicalRegister(2, 'c')
  circuit = QuantumCircuit(qr2, qr1, cr)

  print('Qubit ordering:', circuit.qubits)
  print('Classical bit ordering:', circuit.clbits)

  circuit.h([1,0])
  circuit.measure(1,[0,1])
  circuit.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_4.png
  :alt: Quantum circuit with 2 qubits, 2 bits, a Hadamard gate on each qubit, a
    measurement from q1_0 to both bits.



----------------------
Concatenating Circuits
----------------------

In many situations you may have two circuits that you want to
concatenate together to form a new circuit. This is very useful when one
circuit has no measurements and the final circuit represents a
measurement.

.. code:: python

    meas = QuantumCircuit(q0, q1, c0, c1)
    meas.measure(q0, c0)
    meas.measure(q1, c1)

    qc = circ + meas

    qc.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_18_0.png
  :alt: Quantum circuit with 4 qubits and 4 bits, two sets of labels, X gates on
    qubits q0_1 and q1_0, measurements off all qubits recorded to all bits in a
    one to one fashion.

.. code:: python

    meas2 = QuantumCircuit()
    meas2.add_register(q0)
    meas2.add_register(q1)
    meas2.add_register(c0)
    meas2.add_register(c1)
    meas2.measure(q0, c0)
    meas2.measure(q1, c1)

    qc2 = circ2 + meas2

    qc2.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_19_0.png
  :alt: Quantum circuit with 4 qubits and 4 bits, two sets of labels, X gates on
    qubits q0_1 and q1_0, measurements off all qubits recorded to all bits in a
    one to one fashion.

.. code:: python

    circ4 = QuantumCircuit(q1)
    circ4.x(q1)
    circ4.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_20_0.png
  :alt: Quantum circuit with 2 qubits, each with an X gate.

.. code:: python

    circ5 = QuantumCircuit(q3)
    circ5.h(q3)
    circ5.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_21_0.png
  :alt: Quantum circuit with 2 qubits, each with an H gate.

The new register is added to the circuit:

.. code:: python

    (circ4+circ5).draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_23_0.png
  :alt: Quantum circuit with 4 qubits, an X gate on each of the first two, an H
    gate of each of the last two.

We have also overloaded ``+=`` to the ``QuantumCircuit`` object:

.. code:: python

    circ4 += circ5
    circ4.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_25_0.png
  :alt: Quantum circuit with 4 qubits, an X gate on each of the first two, an H
    gate of each of the last two.


Examining Circuit Results
-------------------------

In the circuit output, the most significant bit (MSB) is to the left and
the least significant bit (LSB) is to the right (i.e. we follow the
regular computer science little endian ordering). In this example:

.. code:: python

    circ.draw(output='mpl')

.. image:: ../images/figures/quantum_circuits_27_0.png
  :alt: Quantum circuit with 4 qubits, an X gate on the second and third qubits.

qqubit register :math:`Q_0` is prepared in the state :math:`|10\rangle`
and :math:`Q_1` is in the state :math:`|01\rangle` giving a total state
:math:`|0110\rangle` (:math:`Q1\otimes Q0`).

.. note::

    The tensor order in Qiskit goes as :math:`Q_n \otimes .. Q_1 \otimes Q_0`

That is the four qubit statevector of length 16 with the 6th element
(``int('0110',2)=6``) being one. Note the element count starts from
zero.

.. code:: python

    backend_sim = BasicAer.get_backend('statevector_simulator')
    result = execute(circ, backend_sim).result()
    state = result.get_statevector(circ)
    print(state)


.. code-block:: text

    [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 1.+0.j 0.+0.j 0.+0.j 0.+0.j
     0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]


To check the fidelity of this state with the ``basis_state`` in Qiskit
Terra you can use:

.. code:: python

    state_fidelity(basis_state('0110', 4), state)




.. code-block:: text

    1.0



We can also use Qiskit Terra to make the unitary operator representing
the circuit (provided there are no measurements). This will be a
:math:`16\times16` matrix equal to
:math:`I\otimes X\otimes X\otimes I`. To check this is correct we can
use the ``Pauli`` class and the ``process_fidelity`` function.

.. code:: python

    backend_sim = BasicAer.get_backend('unitary_simulator')
    result = execute(circ, backend_sim).result()
    unitary = result.get_unitary(circ)
    process_fidelity(Pauli(label='IXXI').to_matrix(), unitary)




.. code-block:: text

    1.0



To map the information of the quantum state to the classial world we
have to use the example with measurements ``qc``:

.. code:: python

    qc.draw(output='mpl')




.. image:: ../images/figures/quantum_circuits_35_0.png
  :alt: Quantum circuit with 4 qubits and 4 bits, an X gate on the second and
    third qubits, measurements on all qubits recorded on all bits in a one to
    one fashion.



This will map the quantum state to the classical world and since the
state has no superpositions it will be deterministic and equal to
``'01 10'``. Here a space is used to separate the registers.

.. code:: python

    backend_sim = BasicAer.get_backend('qasm_simulator')
    result = execute(qc, backend_sim).result()
    counts = result.get_counts(qc)
    print(counts)


.. code-block:: text

    {'01 10': 1024}


To show that it does not matter how you add the registers we run the
same as above on the second example circuit:

.. code:: python

    backend_sim = BasicAer.get_backend('statevector_simulator')
    result = execute(circ2, backend_sim).result()
    states = result.get_statevector(circ2)

    backend_sim = BasicAer.get_backend('qasm_simulator')
    result = execute(qc2, backend_sim).result()
    counts = result.get_counts(qc2)

    backend_sim = BasicAer.get_backend('unitary_simulator')
    result = execute(circ2, backend_sim).result()
    unitary = result.get_unitary(circ2)

.. code:: python

    print(counts)


.. code-block:: text

    {'01 10': 1024}


.. code:: python

    state_fidelity(basis_state('0110', 4), state)




.. code-block:: text

    1.0



.. code:: python

    process_fidelity(Pauli(label='IXXI').to_matrix(), unitary)




.. code-block:: text

    1.0



Determining Circuit Resources
-----------------------------

A ``QuantumCircuit`` object provides methods for inquiring its resource
use. This includes the number of qubits, operations, and a few other
things.

.. code:: python

    q = QuantumRegister(6)
    circuit = QuantumCircuit(q)
    circuit.h(q[0])
    circuit.ccx(q[0], q[1], q[2])
    circuit.cx(q[1], q[3])
    circuit.x(q)
    circuit.h(q[2])
    circuit.h(q[3])
    circuit.draw(output='mpl')




.. image:: ../images/figures/quantum_circuits_44_0.png
  :alt: Quantum circuit with 6 qubits, 8 single qubit gates, a controlled not
    gate, and a Toffoli gate.


.. code:: python

    # total number of operations in the circuit. no unrolling is done.
    circuit.size()




.. code-block:: text

    11



.. code:: python

    # depth of circuit (number of ops on the critical path)
    circuit.depth()




.. code-block:: text

    5



.. code:: python

    # number of qubits in the circuit
    circuit.width()




.. code-block:: text

    6



.. code:: python

    # a breakdown of operations by type
    circuit.count_ops()




.. code-block:: text

    {'h': 3, 'ccx': 1, 'cx': 1, 'x': 6}



.. code:: python

    # number of unentangled subcircuits in this circuit.
    # each subcircuit can in principle be executed on a different quantum processor!
    circuit.num_tensor_factors()




.. code-block:: text

    3
