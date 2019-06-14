


Tools for Monitoring Backends and Jobs
======================================

In this section, we will learn how to monitor the status of jobs
submitted to devices and simulators (collectively called backends), as
well as discover how to easily query backend details and view the
collective state of all the backends available to you.

Loading the Monitoring Tools
----------------------------

First, let us load the default qiskit routines, and register our IBMQ
credentials.

.. code:: python

    from qiskit import *
    IBMQ.load_accounts(hub=None)

Functions for monitoring jobs and backends are here:

.. code:: python

    from qiskit.tools.monitor import job_monitor, backend_monitor, backend_overview

Tracking Job Status
-------------------

Many times a job(s) submitted to the IBM Q network can take a long time
to process, e.g. jobs with many circuits and/or shots, or may have to
wait in queue for other users. In situations such as these, it is
beneficial to have a way of monitoring the progress of a job, or several
jobs at once. As of Qiskit ``0.6+`` it is possible to monitor the status
of a job in a Jupyter notebook, and also in a Python script (version
``0.7+``).

Lets see how to make use of these tools.

Monitoring the status of a single job
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lets build a simple Bell circuit, submit it to a device, and then
monitor its status.

.. code:: python

    q = QuantumRegister(2)
    c = ClassicalRegister(2)
    qc = QuantumCircuit(q, c)

    qc.h(q[0])
    qc.cx(q[0], q[1])
    qc.measure(q, c);

Lets grab the least busy backend

.. code:: python

    from qiskit.providers.ibmq import least_busy
    backend = least_busy(IBMQ.backends(filters=lambda x: not x.configuration().simulator))
    backend.name()




.. code-block:: text

    'ibmq_16_melbourne'



Monitor the job using ``job_monitor`` in blocking-mode (i.e. using the
same thread as the Python interpreter)

.. code:: python

    job1 = execute(qc, backend)
    job_monitor(job1)


.. code-block:: text

    Job Status: job has successfully run


It is also possible to monitor the job using ``job_monitor`` in
async-mode (Jupyter notebooks only). The job will be monitored in a
separate thread, allowing you to continue to work in the notebook. For
details see: `Jupyter tools for Monitoring jobs and
backends <../../../../../qiskit-tutorials/blob/master/qiskit/jupyter/jupyter_backend_tools.ipynb>`__

Changing the interval of status updating
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the interval at which the job status is checked is every two
seconds. However, the user is free to change this using the ``interval``
keyword argument in ``job_monitor``

.. code:: python

    job2 = execute(qc, backend)
    job_monitor(job2, interval=5)


.. code-block:: text

    Job Status: job has successfully run


Backend Details
---------------

So far we have been executing our jobs on a backend, but we have
explored the backends in any detail. For example, we have found the
least busy backend, but do not know if this is the best backend with
respect to gate errors, topology etc. It is possible to get detailed
information for a single backend by calling ``backend_monitor``:

.. code:: python

    backend_monitor(backend)


.. code-block:: text

    ibmq_16_melbourne
    =================
    Configuration
    -------------
        n_qubits: 14
        operational: True
        status_msg: active
        pending_jobs: 0
        basis_gates: ['u1', 'u2', 'u3', 'cx', 'id']
        local: False
        simulator: False
        max_shots: 8192
        description: 14 qubit device
        max_experiments: 75
        online_date: 2018-11-06T05:00:00+00:00
        url: None
        backend_version: 1.0.0
        credits_required: True
        memory: False
        conditional: False
        open_pulse: False
        sample_name: albatross
        coupling_map: [[1, 0], [1, 2], [2, 3], [4, 3], [4, 10], [5, 4], [5, 6], [5, 9], [6, 8], [7, 8], [9, 8], [9, 10], [11, 3], [11, 10], [11, 12], [12, 2], [13, 1], [13, 12]]
        n_registers: 1
        backend_name: ibmq_16_melbourne
        allow_q_object: True

    Qubits [Name / Freq / T1 / T2 / U1 err / U2 err / U3 err / Readout err]
    -----------------------------------------------------------------------
        Q0 / 5.10005 GHz / 67.38168 µs / 20.8927 µs / 0.0 / 0.00157 / 0.00313 / 0.0447
        Q1 / 5.23867 GHz / 38.11844 µs / 72.55859 µs / 0.0 / 0.00556 / 0.01111 / 0.0397
        Q2 / 5.03294 GHz / 45.8347 µs / 96.1172 µs / 0.0 / 0.00311 / 0.00622 / 0.0731
        Q3 / 4.89617 GHz / 89.39497 µs / 84.33097 µs / 0.0 / 0.00101 / 0.00202 / 0.0618
        Q4 / 5.02726 GHz / 53.93443 µs / 35.28576 µs / 0.0 / 0.00156 / 0.00313 / 0.0335
        Q5 / 5.06715 GHz / 24.14202 µs / 45.93013 µs / 0.0 / 0.00209 / 0.00418 / 0.0402
        Q6 / 4.92381 GHz / 64.313 µs / 46.5611 µs / 0.0 / 0.00158 / 0.00317 / 0.1202
        Q7 / 4.97447 GHz / 47.12427 µs / 80.09072 µs / 0.0 / 0.0019 / 0.00381 / 0.1033
        Q8 / 4.73979 GHz / 59.53633 µs / 76.3004 µs / 0.0 / 0.00239 / 0.00477 / 0.0579
        Q9 / 4.96337 GHz / 45.71424 µs / 75.46827 µs / 0.0 / 0.00397 / 0.00794 / 0.1086
        Q10 / 4.94505 GHz / 55.13212 µs / 56.69945 µs / 0.0 / 0.00185 / 0.0037 / 0.065
        Q11 / 5.00527 GHz / 61.25009 µs / 101.05622 µs / 0.0 / 0.00181 / 0.00362 / 0.0816
        Q12 / 4.76015 GHz / 96.01526 µs / 143.34551 µs / 0.0 / 0.00332 / 0.00663 / 0.1608
        Q13 / 4.96847 GHz / 22.97295 µs / 39.88249 µs / 0.0 / 0.00524 / 0.01047 / 0.0493

    Multi-Qubit Gates [Name / Type / Gate Error]
    --------------------------------------------
        CX1_0 / cx / 0.04706
        CX1_2 / cx / 0.04913
        CX2_3 / cx / 0.04437
        CX4_3 / cx / 0.03565
        CX4_10 / cx / 0.04076
        CX5_4 / cx / 0.04962
        CX5_6 / cx / 0.05647
        CX5_9 / cx / 0.04919
        CX6_8 / cx / 0.04215
        CX7_8 / cx / 0.03156
        CX9_8 / cx / 0.04416
        CX9_10 / cx / 0.0493
        CX11_3 / cx / 0.02672
        CX11_10 / cx / 0.03757
        CX11_12 / cx / 0.03782
        CX12_2 / cx / 0.07713
        CX13_1 / cx / 0.15178
        CX13_12 / cx / 0.03901


Or, if we are interested in a higher-level view of all the backends
available to us, then we can use ``backend_overview()``

.. code:: python

    backend_overview()


.. code-block:: text

    ibmq_16_melbourne           ibmqx4
    -----------------           ------
    Num. Qubits:  14            Num. Qubits:  5
    Pending Jobs: 0             Pending Jobs: 40
    Least busy:   True          Least busy:   False
    Operational:  True          Operational:  True
    Avg. T1:      55.1          Avg. T1:      50.9
    Avg. T2:      69.6          Avg. T2:      25.3





There are also Jupyter magic equivalents that give more detailed
information, as demonstrated here: `Jupyter tools for Monitoring jobs
and backends
<../../../../../qiskit-tutorials/blob/master/qiskit/jupyter/jupyter_backend_tools.ipynb>`__
