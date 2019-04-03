
Find the Unitary Matrix for a Circuit
=====================================

Introduction
------------

This tutorial shows how to use Qiskit Aer™ to find the unitary matrix of
quantum circuits.

UnitarySimulator
----------------

The ``UnitarySimulator`` constructs the unitary matrix for a Qiskit
``QuantumCircuit`` by applying each gate matrix to an identity matrix.
The circuit may only contain *gates*, if it contains *resets* or
*measure* operations an exception will be raised.

Import the ``UnitarySimulator``.

.. code:: python

    import numpy as np

    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    from qiskit import Aer, execute

    from qiskit.providers.aer import UnitarySimulator

Simulating a quantum circuit unitary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this example we will return the unitary matrix corresponding to the
previous examples circuit which prepares a bell state.

.. code:: python

    # Construct an empty quantum circuit
    qr = QuantumRegister(2)
    circ = QuantumCircuit(qr)
    circ.h(qr[0])
    circ.cx(qr[0], qr[1])

    # Select the UnitarySimulator from the Aer provider
    simulator = Aer.get_backend('unitary_simulator')

    # Execute and get counts
    result = execute(circ, simulator).result()
    unitary = result.get_unitary(circ)
    print("Circuit unitary:\n", unitary)


.. parsed-literal::

    Circuit unitary:
     [[ 0.70710678+0.j  0.70710678+0.j  0.        +0.j  0.        +0.j]
     [ 0.        +0.j  0.        +0.j  0.70710678+0.j -0.70710678+0.j]
     [ 0.        +0.j  0.        +0.j  0.70710678+0.j  0.70710678+0.j]
     [ 0.70710678+0.j -0.70710678+0.j  0.        +0.j  0.        +0.j]]


Setting a custom initial unitary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

we may also set an initial state for the ``UnitarySimulator``, however
this state is an initial *unitary matrix* :math:`U_i`, not a
statevector. In this case the return unitary will be :math:`U.U_i` given
by applying the circuit unitary to the initial unitary matrix.

**Note:** \* The initial unitary must be a valid unitary matrix
:math:`U^\dagger.U =\mathbb{1}`. If not an exception will be raised. \*
If a Qobj contains multiple experiments, the initial unitary must be the
correct size fo *all* experiments in the Qobj, otherwise an exception
will be raised.

Let us consider preparing the output unitary of the previous circuit as
the initial state for the simulator:

.. code:: python

    # Construct an empty quantum circuit
    qr = QuantumRegister(2)
    circ = QuantumCircuit(qr)
    circ.iden(qr)

    # Set the initial unitary
    opts = {"initial_unitary": np.array([[ 1,  1,  0,  0],
                                         [ 0,  0,  1, -1],
                                         [ 0,  0,  1,  1],
                                         [ 1, -1,  0,  0]] / np.sqrt(2))}

    # Select the UnitarySimulator from the Aer provider
    simulator = Aer.get_backend('unitary_simulator')

    # Execute and get counts
    result = execute(circ, simulator, backend_options=opts).result()
    unitary = result.get_unitary(circ)
    unitary = result.get_unitary(circ)
    print("Initial Unitary:\n", unitary)


.. parsed-literal::

    Initial Unitary:
     [[ 0.70710678+0.j  0.70710678+0.j  0.        +0.j  0.        +0.j]
     [ 0.        +0.j  0.        +0.j  0.70710678+0.j -0.70710678+0.j]
     [ 0.        +0.j  0.        +0.j  0.70710678+0.j  0.70710678+0.j]
     [ 0.70710678+0.j -0.70710678+0.j  0.        +0.j  0.        +0.j]]
