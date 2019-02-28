
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


Analyzing the results
~~~~~~~~~~~~~~~~~~~~~

Execute the device on the generated circuits. Analysis is done by classes ``T1Fitter``, ``T2Fitter``, and ``T2StarFitter``, all inheriting from class ``BaseCoherenceFitter``. 

Assuming that the device is affected by |T1| errors and state preparation and mesaurement (SPAM) errors, the rate of excited state population after time t is expected to be close to f(t)=a*e^{-t/T1}+c, for unknown parameters a, c, and |T1|. The execution results provide a finite set of data points (t, g(t)), where g(t) is close to f(t). The |T1| fitter assigns values to a, c, and |T1|, which minimize the distance between f(t) and g(t).

The fit is done already at the constructor of |T1|. When you create a ``T1Fitter`` object, you provide the information from the execution:
[ code snippet of a call to T1Fitter constructor ]

Once the object has been created, you can query it using a set of functions and properties that are available in ``BaseCoherenceFitters``. In particular, function ``time()`` of T1Fitter gives the estimated |T1|. Also important are the properties ``params`` and ``params_err`, which provide the full fitting parameters (including the coefficients a and c) and their errors. Function ``plot`` plots the fitting function with the calculated parameters, together with the experimental data points.

[Example]

Simlarly, for |T2| and |TS|, the ground state population is expected to behave like ... and ..., respectively. Use ``T2Fitter`` and ``T2StarFitter`` in the same way as ``T1Fitter``.



.. |T1| replace:: T\ :subscript:`1`
.. |T2| replace:: T\ :subscript:`2`
.. |TS| replace:: T\ :subscript:`2`\ :superscript:`*`




