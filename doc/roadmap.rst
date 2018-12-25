The Qiskit Roadmap 2019
=======================

With a very successful r0.7 release behind us, now is a good time to look towards the future. 
We are going to look out 12 months to establish a set of goals we want to work 
towards. When planning, we typically look at potential work from the perspective 
of the elements. 

Qiskit Terra
------------

In 2018 we worked on formalizing the backends and user flow in Qiskit Terra. The 
basic Idea is the user designs a quantum circuit and then by using a set of 
transpiler passes rewrites the circuit to run on different backends with 
different optimizations. We also introduced the concept of a provider 
which role is to supply backends for the user to run quantum circuits on.  
The provider API we have defined at version one and provided a set of 
schemas to verify that the provider and its backends are Terra compatible. 

In 2019 we have many extensions planed. These include:

- Extending the passes in the transpiler. The goal here is to be more 
efficient in circuit depth as well as adding passes that find approximate 
circuits and resource estimations. 

- Circuit Foundry and Circuit API. This has the goal of making sure that 
user can easily build complex circuits from operations. Some of these include 
adding controls and power to operations and inserting unitary matrices directly. 

- OpenPulse. Now that OpenPulse is defined, and the IBM Q provider can accept
it in this year we plan to build out the pulse features. These will include a 
scheduler and tools for building experiments out of pulses. Also included will 
be tools for mapping between experiments with gates (QASM) to experiments with Pulses. 

Qiskit Aer
----------

The first version of Qiskit Aer came out this year. It included in the first 
release a qasm simulator, statevector simulator, and a unitary simulator. 
These are the core to Qiskit Aer and replace the simulators that existed 
in Terra. They are faster and more feature complete. We also released noise 
into the QASM simulator. This noise considers what we are calling noise type 
1 and allows us to add ....

In 2019 Aer will be extended in many ways. 

- We are going to start profiling the simulators and work on making them faster. 

- We are going to extend the noise features to noise of type 2. 

- Adding approximate simulators that are more efficient such as the 
t-gate simulator (works on Clifford and T gates) and a stabilizer simulator 
(works just on Clifford gates)
 
Qiskit Ignis
------------

This year we are going to release the first version of Qiskit ignis. The goal of 
Ignis is to develop as set of tools for characterization of errors, 
improving gates, and enhancing computing 
in the presence of noise. Such examples are optimal control, dynamical 
decoupling, and error mitigation.

In 2019 the first release will include 

- Tools for quantum state tomography

- Tools for quantum process tomography

- Tools for randomize benchmarking over different groups. 

- Tools for optimal control such as pulse shaping. 

- Tools for dynamical decoupling 

- Tools using randomization to improve circuits in the presence of noise. 

- Tools for error mitigation to make quantum chemistry experiments work better. 

Qiskit Aqua
-----------


Summary
-------

These are examples of just some of the work we will be focusing on in the next 12 months. 
We will continuously adapt the plan based on feedback. Please follow along and let us
know what you think!

