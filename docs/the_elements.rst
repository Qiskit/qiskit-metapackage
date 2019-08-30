.. _Elements:

###################
The Qiskit Elements
###################

.. _Terra:

=====
Terra
=====

Terra, the ‘earth’ element, is the foundation on which the rest of Qiskit lies.
Terra provides a bedrock for composing quantum programs at the level of circuits and pulses,
to optimize them for the constraints of a particular device, and to manage the execution
of batches of experiments on remote-access devices. Terra defines the interfaces
for a desirable end-user experience, as well as the efficient handling of layers
of optimization, pulse scheduling and backend communication.

Qiskit Terra is organized in six main modules:

1. `Circuit <https://qiskit.org/documentation/apidoc/circuit/circuit.html>`__
   A quantum circuit is a model for quantum computing in which a computation is done by performing a
   sequence of quantum operations (usually gates) on a register of qubits. A quantum circuit usually
   starts with the qubits in the :math:`|0,…,0>` state and these gates evolve the qubits to states
   that cannot be efficiently represented on a
   classical computer. To extract information on the state a quantum circuit must have a measurement
   which maps the outcomes (possible random due to the fundamental nature of quantum systems) to
   classical registers which can be efficiently represented.

2. `Pulse <https://qiskit.org/documentation/apidoc/pulse/pulse.html>`__
   A pulse schedule is set of pulses which are sent to a quantum experiment that are applied to
   a channel (experimental input line). This is a lower level than circuits and requires each gate
   in the circuit to be  represented as a set of pulses. At this leavel the experiments can be
   designed to reduce errors (dynamical decoupling, error mitigation, and optimal pulse shapes).

3. `Transpiler <https://qiskit.org/documentation/apidoc/transpiler/transpiler.html>`__
   A major part of research on quantum computing is working out how to run a quantum
   circuits on real devices.  In these devices, experimental errors and decoherence introduce
   errors during computation. Thus, to obtain a robust implementation it is essential
   to reduce the number of gates and the overall running time of the quantum circuit.
   The transpiler introduces the concept of a pass manager to allow users to explore
   optimization and find better quantum circuits for their given algorithm. We call it a
   transpiler as the end result is still a circuit.

4. `Providers <https://qiskit.org/documentation/apidoc/providers/providers.html>`__
   Once the user has made the circuits to run on the backend they need to have a convenient way of
   working with it. In Terra we do this using four parts:

   #. A `Provider <https://qiskit.org/documentation/api/qiskit.providers.BaseProvider.html>`__
      is an entity that
      provides access to a group of different backends (for example,
      backends available through the `IBM Q Experience <https://quantum-computing.ibm.com>`__).
      It interacts with those backends to, for example,
      find out which ones are available, or retrieve an instance of a particular backend.
   #. `Backend <https://qiskit.org/documentation/api/qiskit.providers.BaseBackend.html>`__
      represent either a simulator or a real
      quantum computer and are responsible for running quantum circuits and returning results.
      They have a run method which takes in a `qobj` as input and returns a `BaseJob` object.
      This object allows asynchronous running of jobs for retrieving results from a backend
      when the job is completed.
   #. `Job <https://qiskit.org/documentation/api/qiskit.providers.BaseJob.html>`__
      instances can be thought of as the
      “ticket” for a submitted job.
      They find out the execution’s state at a given point in time (for example,
      if the job is queued, running, or has failed) and also allow control over the job.
   #. `Result <https://qiskit.org/documentation/api/qiskit.result.Result.html>`__.
      Once the job has finished Terra allows the
      results to be obtained from the remote backends using `result = job.result()`.
      This result object holds the quantum data and the most common way of interacting
      with it is by using `result.get_counts(circuit)`. This method allows the user to get
      the raw counts from the quantum circuit and use them for more analysis with
      quantum information tools provided by Terra.

5. `Quantum Information <https://qiskit.org/documentation/apidoc/quantum_info/quantum_info.html>`__
   To perform more advanced algorithms and analysis of the circuits run on the quantum
   computer, it is
   important to have tools to implement simple quantum information tasks. These include
   methods to both estimate metrics and generate quantum states, operations, and channels.

6. `Visualization <https://qiskit.org/documentation/apidoc/visualization/visualization.html>`__
   In Terra we have many tools to visualize a quantum circuit. This allows a quick inspection of the
   quantum circuit to make sure it is what the user wanted to implement. There is a text, python and
   latex version. Once the circuit has run it is important to be able to view the output. There is a
   simple function (`plot_histogram`) to plot the results from a quantum circuit including an
   interactive version. There is also a function `plot_state` and `plot_bloch_vector` that allow
   the plotting of a quantum state. These functions are usually only used when using the
   `statevector_simulator` backend but can also be used on real data after running state tomography
   experiments (Ignis).

.. _Aer:

===
Aer
===

Aer, the ‘air’ element, permeates all Qiskit elements. To really speed up development of
quantum computers we need better simulators, emulators and debuggers. Aer helps us understand
the limits of classical processors by demonstrating to what extent they can mimic quantum
computation. Furthermore, we can use Aer to verify that current and near-future quantum
computers function correctly. This can be done by stretching the limits of simulation,
and by simulating the effects of realistic noise on the computation.

Aer provides a high performance simulator framework for quantum circuits using
the Qiskit software stack. It contains optimized C++ simulator backends for executing
circuits compiled in Terra. Aer also provides tools for constructing highly
configurable noise models for performing realistic noisy simulations of the errors that
occur during execution on real devices.

Qiskit Aer includes three high performance simulator backends:

`Qasm Simulator <https://qiskit.org/documentation/api/qiskit.providers.aer.backends.QasmSimulator.html>`__
   Allows ideal and noisy multi-shot execution of qiskit circuits and returns counts or memory.
   There are multiple methods that can be used that simulate different cirucits more efficiently.
   These inlude:

   #. *statevector* - Uses a dense statevector simulation.
   #. *stabilizer* - Uses a Clifford stabilizer state simulator that is only valid
      for Clifford circuits and noise models.
   #. *extended_stabilizer* - Uses an approximate simulator that decomposes circuits
      into stabilizer state terms, the number of which grows with the number of
      non-Clifford gates.
   #. *matrix_product_state* - Uses a Matrix Product State (MPS) simulator.

`Statevector Simulator <https://qiskit.org/documentation/api/qiskit.providers.aer.backends.StatevectorSimulator.html>`__
   Allows ideal single-shot execution of qiskit circuits and returns the final
   statevector of the simulator after application.

`Unitary Simulator <https://qiskit.org/documentation/api/qiskit.providers.aer.backends.UnitarySimulator.html>`__
   Allows ideal single-shot execution of qiskit circuits and
   returns the final unitary matrix of the circuit itself. Note that the circuit
   cannot contain measure or reset operations for this backend.


.. _Ignis:

=====
Ignis
=====

Ignis, the ‘fire’ element, is dedicated to fighting noise and errors and to forging a
new path. This includes better characterization of errors, improving gates, and
computing in the presence of noise. Ignis is meant for those who want to design
quantum error correction codes, or who wish to study ways to characterize errors
through methods such as tomography, or even to find a better way for using gates
by exploring dynamical decoupling and optimal control.

Ignis provides code for users to easily generate circuits for specific
experiments given a minimal set of user input parameters. Ignis code contains
three fundamental building blocks:

**Circuits**
 The circuits module provides the code to generate the list of circuits
 for a particular Ignis experiment based on a minimal set of user
 parameters. These are then run on Terra or Aer.
**Fitters**
 The results of an Ignis experiment are passed to the Fitters module where
 they are analyzed and fit according to the physics model describing
 the experiment. Fitters can plot the data plus fit and output a list
 of parameters.
**Filters**
 For certain Ignis experiments, the fitters can output a Filter object.
 Filters can be used to mitigate errors in other experiments using the
 calibration results of an Ignis experiment.

Qiskit Ignis is organized into three types of experiments that can be
performed:


`Characterization <https://qiskit.org/documentation/apidoc/ignis/characterization/characterization.html>`__
  Characterization experiments are designed to measure parameters in the
  system such as noise parameters (T1, T2-star, T2), Hamiltonian parameters such
  as the ZZ interaction rate and control errors in the gates.

`Verification <https://qiskit.org/documentation/apidoc/ignis/verification/verification.html>`__
  Verification experiments are designed to verify gate and small
  circuit performance. Verification includes state and process tomography,
  quantum volume and randomized benchmarking (RB). These experiments provide
  the information to determine performance metrics such as the gate fidelity.

`Mitigation <https://qiskit.org/documentation/apidoc/ignis/mitigation/mitigation.html>`__
  Mitigation experiments run calibration circuits that are analyzed to
  generate mitigation routines that can be applied to arbitrary sets of results
  run on the same backend. Ignis code will generate a list of circuits that
  run calibration measurements. The results of these measurements will be
  processed by a Fitter and will output a Filter than can be used to apply
  mitigation to other results.


.. _Aqua:

====
Aqua
====

Aqua, the ‘water’ element, is the element of life. To make quantum computing live up to its
expectations,
we need to find real-world applications. Aqua is where algorithms for quantum computers
are built. These algorithms can be used to build applications for quantum computing.
Aqua is accessible to domain experts in chemistry, optimization, finance and AI, who
want to explore the benefits of using quantum computers as accelerators for specific
computational tasks.

Problems that may benefit from the power of quantum computing
have been identified in numerous
domains, such as Chemistry, Artificial Intelligence (AI), Optimization
and Finance. Quantum computing, however, requires very specialized skills.
To address the needs of the vast population of practitioners who want to use and
contribute to quantum computing at various levels of the software stack, we have
created Qiskit Aqua.
