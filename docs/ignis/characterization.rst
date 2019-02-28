
Characterization
================

Ignis provides a set of tools to characterize specific aspects
of the quantum device and the gates, generically, circuits
and analysis tools to extract single characterization parameters.

Coherence
---------

The coherence tools look at measuring |T1| and |T2|. 

Generating Coherence Circuits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To generate coherence circuits, call the functions ``t1_circuits``, ``t2_circuits``, and ``t2star_circuits``. The circuits contain blocks of identity gates. Block sizes differ for different circuits, resulting in differences in the execution times of the circuits.

The |T1| circuits consist merely of identity gates. Specify the qubits to measure, as well as the block sizes and execution time of a single identity gate. Here is a usage example for ``t1_circuit``:

.. code:: python

    circs, xdata = t1_circuits(num_of_gates=[10, 20, 30], 
                               gate_time=0.1, 
                               qubits=[0, 2])

The function returns a list of circuits (objects of type ``QuantumCircuit``), and a list of delay times. The delay times are multiplications of the number of identity gates in the circuits with the time per gate.

|TS| circuits consist of one Hadamard gate, one block of identity gates, a phase gate, and an additional Hadamard gate. You can control the phase gate by setting the number of oscillations. Example:

.. code:: python

    circs, xdata, osc_frec = t2star_circuits(num_of_gates=[5, 10], 
                                             gate_time=0.4,
                                             qubits=[1],
                                             nosc=3)

Note an additional return parameter - the number of oscillation frequency.

``t2_circuits`` follow the CPMG protocol. Specify the number of echoes, and whether to alternate the echo between X and Y.

.. code:: python

    circs, xdata, osc_frec = t2star_circuits(num_of_gates=[100, 500, 1000], 
                                             gate_time=0.3,
                                             qubits=[2, 1],
                                             n_echos=4,
					     phase_alt_echo=True)

.. |T1| replace:: T\ :subscript:`1`
.. |T2| replace:: T\ :subscript:`2`
.. |TS| replace:: T\ :subscript:`2`\ :superscript:`*`



