.. _executing_quantum_programs:

==========================
Executing Quantum Programs
==========================

The general workflow for executing a quantum program is as follows:

1. Build your circuit
2. Choose your **backend**
3. Execute your circuit on your backend, returning a **job** object
4. Access the **result** from the job object via ``job.result()``

A **backend** represents either a simulator or a real quantum computer,
responsible for running quantum circuits and returning results.

**Job** instances can be thought of as the “ticket” for a submitted job. They
find out the execution’s state at a given point in time (for example, if the
job is queued, running, or has failed) and also allow control over the
execution.

Once a job has finished, Qiskit Terra allows the **results** to be obtained from
the remote backends using ``result = job.result()``. This result object holds
the quantum data and the most common way of interacting with it is by using
``result.get_counts(circuit)``. This method gets the raw counts from the quantum
circuit to use them for more analysis with quantum information tools provided by
Terra.

Each of the common backends are demonstrated in the subsequent sections using
the quantum circuit built as follows:

.. code-block:: python

    import numpy as np
    from qiskit import *
    %matplotlib inline

    # Create a Quantum Register with 2 qubits.
    q = QuantumRegister(2)

    # Create a Quantum Circuit acting on the q register
    circ = QuantumCircuit(q)

    # Add a H gate on qubit 0
    circ.h(q[0])

    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1
    circ.cx(q[0], q[1])

    # Plot the circuit
    circ.draw(output='mpl')




.. image:: /images/figures/executing_quantum_programs_0.png
   :alt: Quantum circuit creating a Bell state.


-----------------------------------
Simulating Circuits with Qiskit Aer
-----------------------------------

~~~~~~~~~~~~~~~~~~~~~
Statevector Simulator
~~~~~~~~~~~~~~~~~~~~~

The most common backend in Qiskit Aer is the ``statevector_simulator``. This
simulator returns the quantum state which is a complex vector of dimensions
:math:`2^n` where :math:`n` is the number of qubits (so be careful using this as
it will quickly get too large to run on your machine).

.. note::

  When representing the state of a multi-qubit system, the tensor order used in
  Qiskit is different than that use in most physics textbooks. Suppose there are
  :math:`n` qubits, and qubit :math:`j` is labeled as :math:`Q_j`. In most
  textbooks (such as Nielsen and Chuang’s “Quantum Computation and
  Information”), the basis vectors for the :math:`n`-qubit state space would be
  labeled as :math:`Q_0 ⊗ Q_1 ⊗⋯⊗ Q_n`. **This is not the ordering used by
  Qiskit!** Instead, Qiskit uses an ordering in which the :math:`n^{th}` qubit
  is on the left side of the tesnsor product, so that the basis vectors are
  labeled as :math:`Q_n ⊗⋯⊗ Q_1 ⊗ Q_0`. For example, if qubit zero is in state
  0, qubit 1 is in state 0, and qubit 2 is in state 1, Qiskit would represent
  this state as :math:`|100\rangle`, whereas most physics textbooks would
  represent it as :math:`|001\rangle`. This difference in labeling affects the
  way multi-qubit operations are represented as matrices. For example, Qiskit
  represents a controlled-X (:math:`C_X`) operation with qubit 0 being the
  control and qubit 1 being the target as

  .. math::
     C_X = \begin{bmatrix}
      1 & 0 & 0 & 0 \\
      0 & 0 & 0 & 1 \\
      0 & 0 & 1 & 0 \\
      0 & 1 & 0 & 0
      \end{bmatrix}

To run the above circuit using the statevector simulator, first you need to
import Aer and then set the backend to ``statevector_simulator``.

.. code-block:: python

    # Import Aer
    from qiskit import Aer

    # Run the quantum circuit on a statevector simulator backend
    backend = Aer.get_backend('statevector_simulator')

Now we have chosen the backend it’s time to compile and run the quantum circuit.
In Qiskit we provide the ``execute`` function for this. ``execute`` returns a
``job`` object that encapsulates information about the job submitted to the
backend.

.. code-block:: python

    # Create a Quantum Program for execution
    job = execute(circ, backend)

When you run a program, a job object is made that has the following two useful
methods: ``job.status()`` and ``job.result()`` which return the status of the
job and a result object respectively.

.. note::

  Jobs run asynchronously but when the result method is called it switches to
  synchronous and waits for it to finish before moving on to another task.

.. code-block:: python

    result = job.result()

The results object contains the data and Qiskit provides the method
``result.get_statevector(circ)`` to return the state vector for the quantum
circuit.

.. code-block:: python

    outputstate = result.get_statevector(circ, decimals=3)
    print(outputstate)


.. code-block:: text

    [0.707+0.j 0.   +0.j 0.   +0.j 0.707+0.j]


Qiskit also provides a visualization toolbox to allow you to view these results.

Below, we use the visualization function to plot the real and imaginary
components of the state vector.

.. code-block:: python

    from qiskit.visualization import plot_state_city
    plot_state_city(outputstate)




.. image:: /images/figures/executing_quantum_programs_1.png
  :alt: 3D bar charts of the real and imaginary parts of the state vector.



~~~~~~~~~~~~~~~~~
Unitary Simulator
~~~~~~~~~~~~~~~~~

Qiskit Aer also includes a ``unitary_simulator`` that works provided all the
elements in the circuit are unitary operations. This backend calculates the
:math:`2^n × 2^n` matrix representing the gates in the quantum circuit.

.. code-block:: python

    # Run the quantum circuit on a unitary simulator backend
    backend = Aer.get_backend('unitary_simulator')
    job = execute(circ, backend)
    result = job.result()

    # Show the results
    print(result.get_unitary(circ, decimals=3))


.. code-block:: text

    [[ 0.707+0.j  0.707+0.j  0.   +0.j  0.   +0.j]
     [ 0.   +0.j  0.   +0.j  0.707+0.j -0.707+0.j]
     [ 0.   +0.j  0.   +0.j  0.707+0.j  0.707+0.j]
     [ 0.707+0.j -0.707+0.j  0.   +0.j  0.   +0.j]]



~~~~~~~~~~~~~~~~~~
OpenQASM Simulator
~~~~~~~~~~~~~~~~~~

The simulators above are useful because they provide information about the state
output by the ideal circuit and the matrix representation of the circuit.
However, a real experiment terminates by measuring each qubit (usually in the
computational :math:`|0\rangle`, :math:`|1\rangle` basis). Without measurement,
we cannot gain information about the state. Measurements cause the quantum
system to collapse into classical bits.

For example, suppose we make independent measurements on each qubit of the
two-qubit Bell state

.. math:: |\psi\rangle = \left(|00\rangle+|11\rangle\right)/\sqrt{2}.

and let :math:`x_1x_0` denote the bitstring that results. Recall that, under the
qubit labeling used by Qiskit, :math:`x_1` would correspond to the outcome on
qubit 1 and :math:`x_0` to the outcome on qubit 0.

.. note::

    This representation of the bitstring puts the most significant bit (MSB) on
    the left, and the least significant bit (LSB) on the right. This is the
    standard ordering of binary bitstrings. We order the qubits in the same way,
    which is why Qiskit uses a non-standard tensor product order.

The probability of obtaining outcome :math:`x_1x_0` is given by

.. math:: Pr(x_1x_0) = |\langle{x_1x_0|\psi}\rangle|^2

By explicit computation, we see there are only two bitstrings that will occur:
:math:`00` and :math:`11`. If the bitstring :math:`00` is obtained, the state of
the qubits is :math:`|00\rangle`, and if the bitstring is :math:`11`, the qubits
are left in the state :math:`|11\rangle`. The probability of obtaining
:math:`00` or :math:`11` is the same; namely, 1/2:

.. math:: Pr(00) = |\langle00|\psi\rangle|^2 = \frac{1}{2}

.. math:: Pr(11) = |\langle11|\psi\rangle|^2 = \frac{1}{2}

To simulate a circuit that includes measurement, we need to add measurements to
the original circuit above, and use a different Aer backend.

.. code-block:: python

    # Create a Classical Register with 3 bits.
    c = ClassicalRegister(2, 'c')
    # Create a Quantum Circuit
    meas = QuantumCircuit(q, c)
    meas.barrier(q)
    # map the quantum measurement to the classical bits
    meas.measure(q,c)

    # The Qiskit circuit object supports composition using
    # the addition operator.
    qc = circ+meas

    #drawing the circuit
    qc.draw(output='mpl')




.. image:: /images/figures/executing_quantum_programs_2.png
  :alt: Quantum circuit with measurements.



This circuit adds a classical register, and two measurements that are used to
map the outcome of qubits to the classical bits.

To simulate this circuit, we use the ``qasm_simulator`` in Qiskit Aer. Each run
of this circuit will yield either the bitstring :math:`00` or :math:`11`. To
build up statistics about the distribution of the bitstrings (to, e.g., estimate
:math:`Pr(00)`), we need to repeat the circuit many times. The number of times
the circuit is repeated can be specified in the ``execute`` function, via the
``shots`` keyword.

.. code-block:: python

    # Use Aer's qasm_simulator
    backend_sim = Aer.get_backend('qasm_simulator')

    # Execute the circuit on the qasm simulator.
    # We've set the number of repeats of the circuit
    # to be 1024, which is the default.
    job_sim = execute(qc, backend_sim, shots=1024)

    # Grab the results from the job.
    result_sim = job_sim.result()

Once you have a result object, you can access the counts via the function
``get_counts(circuit)``. This gives you the aggregated binary outcomes of the
circuit you submitted.

.. code-block:: python

    counts = result_sim.get_counts(qc)
    print(counts)


.. code-block:: text

    {'11': 531, '00': 493}


Approximately 50 percent of the time the output bitstring is :math:`00`. Qiskit
also provides a function ``plot_histogram`` which allows you to view the
outcomes.

.. code-block:: python

    from qiskit.visualization import plot_histogram
    plot_histogram(counts)




.. image:: /images/figures/executing_quantum_programs_3.png
  :alt: Histogram showing nearly equal probabilities of measuring 00 and 11
   states.


---------------------------------
Running Circuits on IBM Q Devices
---------------------------------

To facilitate access to real quantum computing hardware, we have provided a
simple API interface. To follow along with this section, first be sure to set up
an IBM Q account as explained in the :ref:`install_access_ibm_q_devices_label`
section of the Qiskit installation instructions.

Load your IBM Q account credentials by calling

.. code-block:: python

    from qiskit import IBMQ
    IBMQ.load_accounts()

Once your account has been loaded, you can view the list of devices available to you.

.. code-block:: python

    print("Available backends:")
    IBMQ.backends()


.. code-block:: text

    Available backends:

.. code-block:: text

    [<IBMQBackend('ibmqx4') from IBMQ()>,
     <IBMQBackend('ibmqx2') from IBMQ()>,
     <IBMQBackend('ibmq_16_melbourne') from IBMQ()>,
     <IBMQSimulator('ibmq_qasm_simulator') from IBMQ()>]



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running Circuits on Real Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Today’s quantum information processors are small and noisy, but are advancing
at a fast pace. They provide a great opportunity to explore what noisy quantum
computers can do.

The IBM Q provider uses a queue to allocate the devices to users. We now choose
a device with the least busy queue which can support our program (has at least 3
qubits).

.. code-block:: python

    from qiskit.providers.ibmq import least_busy

    large_enough_devices = IBMQ.backends(filters=lambda x: x.configuration().n_qubits > 3 and not x.configuration().simulator)
    backend = least_busy(large_enough_devices)
    print("The best backend is " + backend.name())


.. code-block:: text

    The best backend is ibmqx2


To run the circuit on the backend, we need to specify the number of shots and
the number of credits we are willing to spend to run the circuit. Then, we
execute the circuit on the backend using the ``execute`` function.

.. code-block:: python

    from qiskit.tools.monitor import job_monitor
    # Number of shots to run the program (experiment);
    # maximum is 8192 shots.
    shots = 1024
    # Maximum number of credits to spend on executions.
    max_credits = 3

    job_exp = execute(qc, backend, shots=shots, max_credits=max_credits)
    job_monitor(job_exp)


.. code-block:: text

    Job Status: job has successfully run


``job_exp`` has a ``.result()`` method that lets us get the results from running
our circuit.

.. note::

   When the ``.result()`` method is called, the code block will wait
   until the job has finished before releasing the cell.

.. code-block:: python

    result_exp = job_exp.result()

Like before, the counts from the execution can be obtained using
``get_counts(qc)``

.. code-block:: python

    counts_exp = result_exp.get_counts(qc)
    plot_histogram([counts_exp,counts])




.. image:: /images/figures/executing_quantum_programs_4.png
  :alt: Histogram of simulated and real device results for the 2 qubit Bell
   state.


~~~~~~~~~~~~~~~~~~~~~~~~~~
Simulating Circuits on HPC
~~~~~~~~~~~~~~~~~~~~~~~~~~

The IBM Q provider also comes with a remote optimized simulator called
``ibmq_qasm_simulator``. This remote simulator is capable of simulating up to 32
qubits. It can be used the same way as the remote real backends.

.. code-block:: python

    backend_hpc = IBMQ.get_backend('ibmq_qasm_simulator', hub=None)

.. code-block:: python

    # Number of shots to run the program (experiment);
    # maximum is 8192 shots.
    shots = 1024

    # Maximum number of credits to spend on executions.
    max_credits = 3

    job_hpc = execute(qc, backend_hpc, shots=shots, max_credits=max_credits)

.. code-block:: python

    result_hpc = job_hpc.result()

.. code-block:: python

    counts_hpc = result_hpc.get_counts(qc)
    plot_histogram(counts_hpc)




.. image:: /images/figures/executing_quantum_programs_5.png
  :alt: Histogram showing nearly equal probabilities of the 00 and 11 states.



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Retrieving a Previously Run Job
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your experiment takes longer to run then you have time to wait around, or if
you simply want to retrieve old jobs back, the IBM Q backends allow you to do
that. First you would need to note your job’s ID:

.. code-block:: python

    jobID = job_exp.job_id()

    print('JOB ID: {}'.format(jobID))


.. code-block:: text

    JOB ID: 5cdecd8b5a005800724fea07


Given a job ID, that job object can be later reconstructed from the backend
using ``retrieve_job``:

.. code-block:: python

    job_get=backend.retrieve_job(jobID)

and then the results can be obtained from the new job object.

.. code-block:: python

    job_get.result().get_counts(qc)

.. code-block:: text

    {'11': 339, '10': 174, '00': 339, '01': 172}
