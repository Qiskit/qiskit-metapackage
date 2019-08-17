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

Qiskit Terra is organized in the qiskit-terra `repo <https://github.com/Qiskit/qiskit-terra>`__.
Python example programs can be found in the `examples <https://github.com/Qiskit/qiskit-terra/tree/master/examples>`__
directory, and test scripts are located in the `test <https://github.com/Qiskit/qiskit-terra/tree/master/test>`__ directory.
The `qiskit <https://github.com/Qiskit/qiskit-terra/tree/master/qiskit>`__ directory is the main module of Terra. This
module has six main parts.

**Quantum Circuits**
   A quantum circuit is a model for quantum computing in which a computation is done by performing a
   sequence of quantum operations (usually gates) on a register of qubits. A quantum circuit usually
   starts with the qubits in the :math:`|0,…,0>` state (Terra assumes this unless otherwise
   specified) and these gates evolve the qubits to states
   that cannot be efficiently represented on a
   classical computer. To extract information on the state a quantum circuit must have a measurement
   which maps the outcomes (possible random due to the fundamental nature of quantum systems) to
   classical registers which can be efficiently represented.

**Transpiler**
   A major part of research on quantum computing is working out how to run a quantum
   circuits on real devices.  In these devices, experimental errors and decoherence introduce
   errors during computation. Thus, to obtain a robust implementation it is essential
   to reduce the number of gates and the overall running time of the quantum circuit.
   The transpiler introduces the concept of a pass manager to allow users to explore
   optimization and find better quantum circuits for their given algorithm. We call it a
   transpiler as the end result is still a circuit.

**Tools**
   This directory contains tools that make working with Terra simpler. It contains functions that
   allow the user to execute quantum circuits and not worry about the optimization for a given
   backend. It also contains a compiler which uses the transpiler
   to map an array of quantum circuits
   to a `qobj` (quantum object) which can then be run on a backend. The `qobj` is a convenient
   representation (currently JSON) of the data that can be easily sent to the remote backends.
   It also has functions for monitoring jobs, backends, and parallelization of transpilation tasks.

**Backends and Results**
   Once the user has made the `qobj` to run on the backend they need to have a convenient way of
   working with it. In Terra we do this using three parts:

   #. A *Provider* is an entity that provides access to a group of different backends (for example,
      backends available through the `IBM Q <https://www.research.ibm.com/ibm-q/technology/devices/>`__).
      It interacts with those backends to, for example,
      find out which ones are available, or retrieve an instance of a particular backend.
   #. *Backends* represent either a simulator or a real quantum computer and are responsible
      for running quantum circuits and returning results. They have a run method which takes in a
      `qobj` as input and returns a `BaseJob` object. This object allows asynchronous running of
      jobs for retrieving results from a backend when the job is completed.
   #. *Job* instances can be thought of as the “ticket” for a submitted job.
      They find out the execution’s state at a given point in time (for example,
      if the job is queued, running, or has failed) and also allow control over the job.

   Once the job has finished Terra allows the results to be obtained from the remote backends
   using `result = job.result()`.  This result object holds the quantum data and the most
   common way of interacting with it is by using `result.get_counts(circuit)`. This method allows
   the user to get the raw counts from the quantum circuit and use them for more analysis with
   quantum inofrmation tools provided by Terra.

**Quantum Information**
   To perform more advanced algorithms and analysis of the circuits run on the quantum
   computer, it is
   important to have tools to implement simple quantum information tasks. These include
   methods to both estimate metrics and generate quantum states, operations, and channels.

**Visualization Tools**
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

Qiskit Aer provides a high performance simulator framework for quantum circuits using
the Qiskit software stack. It contains optimized C++ simulator backends for executing
circuits compiled in Qiskit Terra. Aer also provides tools for constructing highly
configurable noise models for performing realistic noisy simulations of the errors that
occur during execution on real devices.


.. _Ignis:

=====
Ignis
=====

A framework for characterizing and mitigating noise in
quantum circuits and devices.

.. image:: images/figures/ignis_overview.png
  :alt: Schematic of the Ignis framework.

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

Qiskit Ignis is organized in this `repo <https://github.com/Qiskit/qiskit-ignis>`__.
The Ignis repository is grouped into the types of experiments that can be
performed:


`Characterization <https://github.com/Qiskit/qiskit-ignis/tree/master/qiskit/ignis/characterization>`__
  Characterization experiments are designed to measure parameters in the
  system such as noise parameters (T1, T2-star, T2), Hamiltonian parameters such
  as the ZZ interaction rate and control errors in the gates.

`Verification <https://github.com/Qiskit/qiskit-ignis/tree/master/qiskit/ignis/verification>`__
  Verification experiments are designed to verify gate and small
  circuit performance. Verification includes state and process tomography,
  quantum volume and randomized benchmarking (RB). These experiments provide
  the information to determine performance metrics such as the gate fidelity.

`Mitigation <https://github.com/Qiskit/qiskit-ignis/tree/master/qiskit/ignis/mitigation>`__
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

Problems that may benefit from the power of quantum computing
have been identified in numerous
domains, such as Chemistry, Artificial Intelligence (AI), Optimization
and Finance. Quantum computing, however, requires very specialized skills.
To address the needs of the vast population of practitioners who want to use and
contribute to quantum computing at various levels of the software stack, we have
created :ref:`aqua-library` that can be invoked directly or via domain-specific computational
applications:
:ref:`aqua-chemistry`, :ref:`aqua-ai`, :ref:`aqua-optimization` and
:ref:`aqua-finance`.
Finally, :ref:`aqua-tutorials` is a companion library of notebooks, input files and sample code
which are available from the
`Qiskit Tutorials GitHub repository <https://github.com/Qiskit/qiskit-tutorials>`__.

.. toctree::
  :maxdepth: 1
  :hidden:

  aqua/library
  aqua/chemistry/qiskit_chemistry
  aqua/ai/qiskit_ai
  aqua/optimization/qiskit_optimization
  aqua/finance/qiskit_finance
  aqua/tutorials/aqua_tutorials
  aqua/release_history
