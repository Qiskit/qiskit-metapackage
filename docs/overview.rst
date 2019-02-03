Overview
========

Qiskit is an open-source framework for working with 
noisy quantum computers
at the level of pulses, circuits, and algorithms.

Certainly, a central goal of Qiskit is to build a software stack 
that makes it easy for anyone to use quantum computers. However, Qiskit also aims 
to facilitate research on the most important open issues facing quantum computation today.

Qiskit allows the user to easily design experiments and run them on simulators and real
quantum computers. 

Qiskit consists of four foundational elements:  Terra (the code foundation, 
for composing quantum programs at the level of circuits and pulses), 
Aqua (for building algorithms and applications), Ignis (for addressing noise 
and errors), and Aer (for accelerating development via simulators,
emulators and debuggers).


Qiskit Elements 
---------------

.. image:: images/qiskit_elements.png


Qiskit Terra
^^^^^^^^^^^^

Terra , the ‘earth’ element, is the foundation on which the rest of Qiskit lies. 
Terra provides a bedrock for composing quantum programs at the level of circuits and pulses, 
to optimize them for the constraints of a particular device, and to manage the execution 
of batches of experiments on remote-access devices. Terra defines the interfaces 
for a desirable end-user experience, as well as the efficient handling of layers 
of optimization, pulse scheduling and backend communication.

Qiskit Aer
^^^^^^^^^^

Aer, the ‘air’ element, permeates all Qiskit elements. To really speed up development 
of quantum computers we need better simulators, emulators and debuggers.  Aer will help
us understand the limits of classical processors by demonstrating to what extent they 
can mimic quantum computation. Furthermore, we can use Aer to verify that current 
and near-future quantum computers function correctly. This can be done by stretching 
the limits of simulation, and by simulating the effects of realistic noise on 
the computation.

Qiskit Ignis
^^^^^^^^^^^^

Ignis, the ‘fire’ element, is dedicated to fighting noise and errors and to forging 
a new path. This includes better characterization of errors, improving gates, and computing 
in the presence of noise. Ignis is meant for those who want to design quantum error 
correction codes, or who wish to study ways to characterize errors through methods 
such as tomography, or even to find a better way for using gates by exploring 
dynamical decoupling and optimal control. 

Qiskit Aqua
^^^^^^^^^^^

Aqua, the ‘water’ element, is the element of life. To make quantum computing live up 
to its expectations, we need to find real-world applications. Aqua is where algorithms 
for NISQ computers are built. These algorithms can be used to build applications 
for quantum computing. Aqua is accessible to domain experts in chemistry, optimization 
or AI, who want to explore the benefits of using quantum computers as accelerators 
for specific computational tasks, without needing to worry about how to translate 
the problem into the language of quantum machines.

Qiskit Components 
-----------------

The components of Qiskit extend the functionality. 

Qiskit Chemistry
^^^^^^^^^^^^^^^^

Qiskit Chemistry extends the Aqua element to allow the user to work easier
with quantum computing for quantum chemistry problem. Is a set of tools, algorithms
and software to use for quantum chemistry research. Qiskit Chemistry comes with
interfaces prebuilt for the following four computational chemistry software drivers:
Gaussian™ 16 (a commercial chemistry program), PSI4 (an open-source chemistry program
built on Python), PySCF (an open-source Python chemistry program), and PyQuante
(a pure Python cross-platform open-source chemistry program).
