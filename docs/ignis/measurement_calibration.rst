
Measurement Calibration
=======================

The measurement calibration is used to mitigate measurement errors.
The main idea is to prepare all :math:`2^n` basis input states and compute the
probability of measuring counts in the other basis states.
From these calibrations, it is possible to correct the average results
of another experiment of interest.

To use Qiskit Ignis Measurement Calibration module, import it with

.. code:: python

    from qiskit.ignis.mitigation.measurement import (complete_measurement_calibration,
                                                     CompleteMeasFitter, MeasurementFilter)

Generating Measurement Calibration Circuits
-------------------------------------------

The goal is to generate a list of measurement calibration circuits for the full
Hilbert space. Each circuit creates a basis state.
If there are :math:`n` qubits, then you get :math:`2^n` calibration circuits.

The following function returns
a list **cal_circuits** of QuantumCircuit objects containing the calibration circuits,
and a list **state_labels** of the calibration state labels.

.. code:: python

    cal_circuits, state_labels =
    complete_measurement_calibration(qubit_list, qr, cr, circlabel)


The input to this function can be given in one of the following three forms:

- **qubit_list:** A list of qubits to perform the measurement correction on, or:
- **qr (QuantumRegister):** A quantum register, or:
- **cr (ClassicalRegister):** A classical register.

In addition, you can provide a string **circlabel**, which is added at
the beginning of the circuit names for unique identification.

For example, for a 5-qubit QuantumRegister, use

.. code:: python

    cal_circuits, state_labels = complete_measurement_calibration(
                                qiskit.QuantumRegister(5))

Now, you can execute the calibration circuits either using
Qiskit Aer Simulator (with some noise model) or using IBMQ provider.


.. code:: python

    job = qiskit.execute(cal_circuits)
    cal_results = job.results()

Analyzing the Results
---------------------

After you run the calibration circuits and obtain the results **cal_results**,
you can compute the calibration matrix
(this matrix will be ordered according to the state_labels).

.. code:: python

    meas_fitter = CompleteMeasFitter(cal_results, state_labels, circlabel)
    print(meas_fitter.cal_matrix)


To compute the measurement fidelity, use

.. code:: python

    fidelity = meas_fitter.readout_fidelity(label_list)

If **label_list** is None, then it returns the average assignment fidelity
of a single state. Otherwise it returns the assignment fidelity
to be in any one of these states averaged over the second index.


Applying the Calibration
------------------------

If you now perform another experiment using another circuits **my_circuits**
and obtain the results **my_results**, for example

.. code:: python

    my_job = qiskit.execute(my_circuits)
    my_results = my_job.results()


then you can compute the mitigated results **mitigated_results**

.. code:: python

    # Results without mitigation
    raw_counts = my_results.get_counts()

    # Get the filter object
    meas_filter = meas_fitter.filter

    # Results with mitigation
    mitigated_results = meas_filter.apply(my_results, method)
    mitigated_counts = mitigated_results.get_counts(0)

The raw data to be corrected can be given in a number of forms:

- Form1: A counts dictionary from results.get_counts,
- Form2: A list of counts of length=len(state_labels),
- Form3: A list of counts of length=M*len(state_labels) where M is an integer
  (e.g. for use with the tomography data),
- Form4: A qiskit Result (e.g. my_results as above).

There are two fitting methods for applying the calibration:

- **method='pseudo_inverse'**, which is a direct inversion of the calibration matrix.
- **method='least_squares'**, which constrained to have physical probabilities

If none method is defined, then 'least_squares' is used.



