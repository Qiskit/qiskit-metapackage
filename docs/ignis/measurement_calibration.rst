
Measurement Calibration
=======================

The measurement calibration is used to mitigate measurement errors.
The main idea is to prepare all :math:`2^n` basis input states and compute the
probability of measuring counts in the other basis states.
From these calibrations, we can correct the average results of another experiment
of interest.

In order to use Qiskit Ignis Measurement Calibration module,
one should import the following libraries:

.. code:: python

    import qiskit
    from qiskit import QuantumRegister, QuantumCircuit, ClassicalRegister
    from qiskit.ignis.mitigation.measurement import
                                            (measurement_calibration,
                                            MeasurementFitter)

In order to simulate noise using Qiskit Aer device noise module,
one should additionally import the following libraries:

.. code:: python

    from qiskit import Aer
    from qiskit.providers.aer import noise


Generating Measurement Calibration Circuits
-------------------------------------------

Assume that we would like to  generate a calibration matrix for
the 3 qubits Q2, Q3 and Q4 in a 5-qubit Quantum Register [Q0,Q1,Q2,Q3,Q4].
Since we have 3 qubits, there are :math:`2^3=8` possible quantum states.

.. code:: python

    qr = qiskit.QuantumRegister(5)
    # Compute a list of measurement calibration circuits.
    # Each circuit creates a basis state
    meas_calibs, state_labels = measurement_calibration
    (qubit_list=[2,3,4], qr=qr, circlabel='mcal')
    # Print the state labels
    print (state_labels)

.. code:: python

    # State labels (for the 3 qubits)
    ['000', '001', '010', '011', '100', '101', '110', '111']

If we do not apply any noise, then the calibration matrix is expected to be
the :math:`8 \times 8` identity matrix.

.. code:: python

    # Run the calibration circuits (without noise)
    backend = qiskit.Aer.get_backend('qasm_simulator')
    qobj = qiskit.compile(meas_calibs, backend=backend, shots=1000)
    job = backend.run(qobj)
    cal_results = job.result()

    # Compute a calibration matrix
    meas_fitter = MeasurementFitter(cal_results, state_labels,
                                    circlabel='mcal')
    print(meas_fitter.cal_matrix)

.. code:: python

    # Calibration matrix without noise is the identity matrix
    [[1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0]
     [0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0]
     [0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0]
     [0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0]
     [0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0]
     [0.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0]
     [0.0 0.0 0.0 0.0 0.0 0.0 1.0 0.0]
     [0.0 0.0 0.0 0.0 0.0 0.0 0.0 1.0]]


Assume that we apply some noise model from Qiskit Aer to these qubits,
then the calibration matrix will have most of its mass on the main diagonal,
with some additional 'noise'.

.. code:: python

    # Generate a noise model for the qubits
    noise_model = noise.NoiseModel()
    for qi in range(5):
        read_err = noise.errors.readout_error.ReadoutError
                                            ([[0.9, 0.1],[0.25,0.75]])
        noise_model.add_readout_error(read_err, [qi])

    # Run the calibration circuits (with the noise model)
    backend = qiskit.Aer.get_backend('qasm_simulator')
    qobj = qiskit.compile(meas_calibs, backend=backend, shots=1000)
    job = backend.run(qobj, noise_model=noise_model)
    cal_results = job.result()

    # Compute a calibration matrix
    meas_fitter = MeasurementFitter(cal_results, state_labels,
                                    circlabel='mcal')
    print(meas_fitter.cal_matrix)

.. code:: python

    # Calibration matrix with noise
    [[0.74  0.209 0.203 0.049 0.219 0.06  0.058 0.022]
     [0.071 0.605 0.025 0.17  0.023 0.16  0.007 0.049]
     [0.077 0.012 0.613 0.167 0.018 0.006 0.162 0.043]
     [0.008 0.088 0.055 0.519 0.002 0.021 0.02  0.127]
     [0.081 0.027 0.02  0.005 0.586 0.166 0.166 0.05 ]
     [0.012 0.051 0.005 0.02  0.071 0.511 0.011 0.147]
     [0.008 0.004 0.077 0.014 0.074 0.02  0.512 0.149]
     [0.003 0.004 0.002 0.056 0.007 0.056 0.064 0.413]]

Analyzing the Results
---------------------
We would like to compute the total measurement fidelity,
and the measurement fidelity for a specific qubit, for example, Q0.

Since the on-diagonal elements of the calibration matrix are the
probabilities of measuring state 'x' given preparation of state
'x', then the trace of this matrix is the average assignment fidelity.

.. code:: python

    # What is the measurement fidelity?
    print("Average Measurement Fidelity: %f"
        % meas_fitter.readout_fidelity())

    # What is the measurement fidelity of Q0?
    print("Average Measurement Fidelity of Q0: %f"
        % meas_fitter.readout_fidelity(
        label_list = [['000','001','010','011'],['100','101','110','111']]))

.. code:: python

    Average Measurement Fidelity: 0.562375
    Average Measurement Fidelity of Q0: 0.826750

Applying the Calibration
------------------------

We now perform another experiment and correct the measured results.
As an example, we start with the 3-qubit GHZ state.

.. code:: python

    # Make a 3Q GHZ state
    cr = ClassicalRegister(3)
    ghz = QuantumCircuit(qr, cr)
    ghz.h(qr[2])
    ghz.cx(qr[2], qr[3])
    ghz.cx(qr[3], qr[4])
    ghz.measure(qr[2],cr[0])
    ghz.measure(qr[3],cr[1])
    ghz.measure(qr[4],cr[2])

    # Run the calibration circuits (with the noise model above)
    qobj = qiskit.compile([ghz], backend=backend, shots=1000)
    job = backend.run(qobj, noise_model=noise_model)
    results = job.result()

We now compute the results without any error mitigation and with the
mitigation, namely after applying the calibration matrix to
the results.

There are two fitting methods for applying thr calibration
(if none method is defined, then 'least_squares' is used).
The first method is 'pseudo_inverse', which is a direct inversion of
the calibration matrix,
and the second is 'least_squares', which constrained to have
physical probabilities.

.. code:: python

    # Results without mitigation
    raw_counts = results.get_counts()
    print("Results without mitigation:", raw_counts)

    # Results with mitigation:
    # Apply the calibration matrix to results
    mitigated_results = meas_fitter.apply(results, method='least_squares')
    mitigated_counts = mitigated_results.get_counts(0)
    print("Results with mitigation:", mitigated_counts)

.. code:: python

    Results without mitigation:
    {'000': 181, '001': 83, '010': 59, '011': 65,
    '100': 101, '101': 48, '110': 72, '111': 391}

    Results with mitigation:
    {'000': 420.866934, '001': 2.1002, '011': 1.30314,
    '100': 53.0165, '110': 13.1834, '111': 509.5296}
