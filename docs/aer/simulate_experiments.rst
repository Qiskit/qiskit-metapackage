
Simulating an Experiment
========================

Introduction
------------

This tutorial shows how to use Qiskit Aer™ to simulate execution of
quantum circuits and return the measurement outcomes for the experiment.

QasmSimulator
-------------

The ``QasmSimulator`` backend is designed to mimic an actual device. It
executes a Qiskit ``QuantumCircuit`` and returns a count dictionary
containing the final values of any classical registers in the circuit.
The circuit may contain *gates* *measure*, *reset*, *conditionals*, and
other advanced simulator options.

Import the ``QasmSimulator``.

.. code:: python

    import numpy as np

    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    from qiskit import Aer, execute
    from qiskit.tools.visualization import plot_histogram

    from qiskit.providers.aer import QasmSimulator

Simulating a quantum circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The basic operation executes a quantum circuit and returns a counts
dictionary of measurement outcomes. Here we execute a simple circuit
that prepares a 2-qubit Bell-state
:math:`|\psi\rangle = \frac{1}{2}(|0,0\rangle + |1,1 \rangle)` and
measures both qubits.

Construct the quantum circuit.

.. code:: python

    qr = QuantumRegister(2, 'qr')
    cr = ClassicalRegister(2, 'cr')
    circ = QuantumCircuit(qr, cr)
    circ.h(qr[0])
    circ.cx(qr[0], qr[1])
    circ.measure(qr, cr)




.. code-block:: text

    <qiskit.circuit.instructionset.InstructionSet at 0xa24190cf8>



Select the QasmSimulator from the Aer provider.

.. code:: python

    simulator = Aer.get_backend('qasm_simulator')

Execute the simulation, get counts, and plot the result.

.. code:: python

    result = execute(circ, simulator).result()
    counts = result.get_counts(circ)
    plot_histogram(counts, title='Bell-State counts')




.. image:: ../images/figures/simulate_experiments_10_0.png



Returning measurements outcomes for each shot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``QasmSimulator`` also supports returning a list of measurement
outcomes for each individual shot. This is enabled by setting the
keyword argument ``memory=True`` in the ``compile`` or ``execute``
function.

.. code:: python

    # Construct quantum circuit
    qr = QuantumRegister(2, 'qr')
    cr = ClassicalRegister(2, 'cr')
    circ = QuantumCircuit(qr, cr)
    circ.h(qr[0])
    circ.cx(qr[0], qr[1])
    circ.measure(qr, cr)

    # Select the QasmSimulator from the Aer provider
    simulator = Aer.get_backend('qasm_simulator')

    # Execute and get memory
    result = execute(circ, simulator, shots=10, memory=True).result()
    memory = result.get_memory(circ)
    print(memory)


.. code-block:: text

    ['11', '11', '00', '11', '11', '00', '00', '00', '11', '11']


Starting simulation with a custom initial state
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``QasmSimulator`` allows setting a custom initial statevector for
the simulation. This means that all experiments in a Qobj will be
executed starting in a state :math:`|\psi\rangle` rather than the all
zero state :math:`|0,0,..0\rangle`. The custom state may be set using
the ``backend_options`` keyword argument for ``execute``, or the Aer
backend ``run`` method.

**Note:** \* The initial statevector must be a valid quantum state
:math:`|\langle\psi|\psi\rangle|=1`. If not an exception will be raised.
\* If a Qobj contains multiple circuits, the initial statevector must be
the correct size for *all* experiments in the Qobj, otherwise an
exception will be raised.

We now demonstate this functionality be executing an empty circuit, but
setting the simulator to be initialized in the the final Bell-state of
the previous example:

.. code:: python

    # Construct an empty quantum circuit
    qr = QuantumRegister(2)
    cr = ClassicalRegister(2)
    circ = QuantumCircuit(qr, cr)
    circ.measure(qr, cr)

    # Set the initial state
    opts = {"initial_statevector": np.array([1, 0, 0, 1] / np.sqrt(2))}

    # Select the QasmSimulator from the Aer provider
    simulator = Aer.get_backend('qasm_simulator')

    # Execute and get counts
    result = execute(circ, simulator, backend_options=opts).result()
    counts = result.get_counts(circ)
    plot_histogram(counts, title="Bell initial statevector")




.. image:: ../images/figures/simulate_experiments_14_0.png
