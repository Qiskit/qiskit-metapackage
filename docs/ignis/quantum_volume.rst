
Quantum Volume
==========================

Quantum volume (QV) is a method to provide a holistic device benchmark as
described in "Validating quantum computers
using randomized model circuits" (https://arxiv.org/abs/1811.12926).
The basic idea is to generate many random sequences, run them on a
device and see if the results pass an outcome threshold.

To use the Qiskit Ignis quantum volume (QV) module, import it with

.. code:: python

    import qiskit.ignis.verification.quantum_volume as qv

Generating QV Sequences
-----------------------

In order to generate the QV sequences ``qv_circs``, which is a list of lists of
quantum volume circuits, run

.. code:: python

    qv_circs, qv_circs_nomeas = qv.qv_circuits(
        qubit_lists,
        ntrials,
        qr,
        cr)

The parameters given to this function are:

* ``qubit_lists``: list of list of qubit subsets to generate volume circuits for
  (each volume circuit will be depth equal to the number of qubits in the subset)
* ``ntrials``: Number of random circuits to create for each subset
* ``qr``: QuantumRegister
* ``cr``: ClassicalRegister

This function returns:

* ``qv_circs``: a list of lists of circuits for the QV sequences (separate list
  for each trial)
* ``qv_circs_nomeas``: the same circuits with no ``measure`` operations. These are
  for passing to the statevector simulator (the QV algorithm requires this)


Analyzing Results
-----------------

The first step is to execute the circuits on an ideal statevector simulator.

.. code:: python

    backend = qiskit.Aer.get_backend('statevector_simulator')
    ideal_results = []
    for trial in range(ntrials):
        ideal_results.append(qiskit.execute(qv_circs_nomeas[trial],
                            backend=backend).result())

Next, you can execute the qv circuit either using Qiskit Aer
Simulator (with some noise model) or using IBMQ provider, and obtain a list of
results ``result_list`` for the QV sequences.

.. code:: python

    result_list = [] # Output results
    for trial in range(ntrials):
        # Executing each QV sequence
        job = qiskit.execute(
            qv_circs[trial],
            backend=backend,
            basis_gates=basis_gates,
            shots=shots,
            noise_model=noise_model)
        result_list.append(job.result())

To analyze the results we add to a quantum volume fitter

.. code:: python

    qvfit = qv.QVFitter(qubit_lists=qubit_lists,
                        statevector_result=ideal_results,
                        backend_result=result_list)

Results can be added to an existing fitter as

.. code:: python

    qvfit.add_data(more_results)

The number of trials in the fitter is based on the number of added results. To
compute the data run:

.. code:: python

    qvfit.calc_data()
    qvfit.calc_statistics()

These steps are performed automatically when data is added (unless ``rerun_fit``
is set to ``False`` in ``add_data()``).

The quantum volume success or failure is given as:

.. code:: python

    qvfit.qv_success()

which for each subset of qubits returns whether the mean heavy output of the circuits
are greater than 2/3 with a confidence greater than 0.975 (as defined in the paper).
