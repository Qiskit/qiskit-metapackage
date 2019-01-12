The Qiskit Roadmap 2019
=======================

With a very successful r0.7 release behind us, now is a good time to look towards the future. 
We are going to look out 12 months to establish a set of goals we want to work 
towards. When planning, we typically look at potential work from the perspective 
of the elements. 

Qiskit Terra
------------

In 2018 we worked on formalizing the backends and user flow in Qiskit Terra. The 
basic Idea is as follows: the user designs a quantum circuit and then, through a set of
transpiler passes, rewrites the circuit to run on different backends with
different optimizations. We also introduced the concept of a *provider*,
whose role is to supply backends for the user to run quantum circuits on.
The provider API we have defined at version one supplies a set of
schemas to verify that the provider and its backends are Terra-compatible.

In 2019, we have many extensions planed. These include:

- **Extending the passes in the transpiler.** The goal here is to be more efficient in
  circuit depth as well as adding passes that find approximate circuits and resource estimations. 

- **Circuit Foundry and Circuit API.** This has the goal of making sure that a
  user can easily build complex circuits from operations. Some of these include 
  adding controls and power to operations and inserting unitary matrices directly. 

- **OpenPulse.** Now that OpenPulse is defined, and the IBM Q provider can accept
  it, we plan to build out the pulse features. These will include a
  scheduler and tools for building experiments out of pulses. Also included will 
  be tools for mapping between experiments with gates (QASM) to experiments with Pulses. 

Qiskit Aer
----------

The first version of Qiskit Aer was released at the end of 2018. It included C++
implementations of Qasm, statevector, and unitary simulators. These are the core to
Qiskit Aer and replace the simulators that existed in Terra. The QASM simulator includes
a customizable general (Kraus) noise model, and all simulators are include CPU parallelization
through the OpenMP library.

In 2019, Aer will be extended in many ways:

- **Optimizations.** We are going to start profiling the simulators and work on making
  them faster. This will include automatic settings for backend configuration and 
  OpenMP parallelization configuration based on the input Qobj and available hardware.
- **Additional simulator backends.** We will include several approximate simulator backends
  that are more efficient for specific subclasses of circuits, such as the
  T-gate simulator, which works on Clifford and T gates (with low T-depth), and a stabilizer
  simulator,  which works just on Clifford gates.
- **Noise approximations.** We plan to add noise approximation tools to mapping general (Kraus)
  noise models to approximate noise model that may be implemented on an approximate backends
  (for example only mixed Clifford and reset errors in the noise model).
 
Qiskit Ignis
------------

This year, we are going to release the first version of Qiskit Ignis. The goal of
Ignis is to develop as set of tools for characterization of errors, 
improving gates, and enhancing computing 
in the presence of noise. Such examples are optimal control, dynamical 
decoupling, and error mitigation.

In 2019 the first release will include 

- Tools for quantum state tomography

- Tools for quantum process tomography

- Tools for randomize benchmarking over different groups

- Tools for optimal control, such as pulse shaping

- Tools for dynamical decoupling 

- Tools using randomization to improve circuits in the presence of noise

- Tools for error mitigation to make quantum chemistry experiments work better

Qiskit Aqua
-----------

Aqua is an open-source library of quantum algorithms and applications, introduced in June 2018.
As a library of quantum algorithms, Aqua comes with a rich set of quantum algorithms of
general applicability—such as VQE, QAOA, Grover's Search, Amplitude Estimation and
Phase Estimation—and domain-specific algorithms-such as the Support Vector Machine (SVM)
Quantum Kernel and Variational algorithms, suitable for supervised learning.  In addition,
Aqua include algorithm-supporting components, such as optimizars, variational forms, oracles,
Quantum Fourier Transforms, feature maps, and multiclass classification extensions.
As a framework for quantum applications, Aqua provides support for Chemistry (released as the
Qiskit Chemistry component), as well as Artificial Intelligence (AI), Optimization and
Finance.  Aqua is extensible across multiple domains, and has been designed and structured as a
framework that allows researchers to contribute their own implementations of new algorithms and
algorithm-supporting components.

Over the course of 2019, we are planning to enrich Aqua as follows:

- We will include several new quantum algorithms,
  such as Deutsch-Jozsa, Simon's, Bernstein-Vazirani, and
  Harrow, Hassidim, and Lloyd (HHL)
- We will improve the performance of quantum algorithms on top of both
  simulators and real hardware
- We will provide better support for execution on real quantum hardware
- We will increase the set of problems supported by the AI, Optimization and Finance
  applications of Aqua

Qiskit Chemistry
~~~~~~~~~~~~~~~~
Qiskit Chemistry is the first end-to-end software stack that enables experimenting with
chemistry problems on near-term quantum computers. It translates chemistry-specific problems
defined via classical drivers into inputs for Aqua algorithms.
It is modular and extensible, and allows users with different levels of experience to execute
chemistry experiments and contribute to the quantum computing chemistry software stack.
Qiskit Chemistry continues to be the most advanced quantum chemistry application available,
with support for the computation of a molecule's ground state energy and dipole moment, and
with the inclusion of numerous chemistry-specific algorithmic components/

In 2019, we are planning to enrich Qiskit Chemistry as follows:

- Improved scalability to support the simulation of
  larger molecules and/or the use of more sophisticated basis sets
- Enhanced support for the execution of chemistry experiments on real hardware
- Support for new chemistry problems, such as the computation of a molecule's excited states

Summary
-------

These are examples of just some of the work we will be focusing on in the next 12 months. 
We will continuously adapt the plan based on feedback. Please follow along and let us
know what you think!

