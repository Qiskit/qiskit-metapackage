.. _qc-intro:

===============================
Quantum computing in a nutshell
===============================

Introduction
============

Quantum computing represents a new paradigm in computation that utilizes the fundamental
principles of quantum mechanics to perform calculations.  If you are reading this then you 
have undoubtedly heard that the promise of quantum computation lies in the possibility of
efficiently performing a handful of tasks such as prime factorization and quantum simulation;
computations that at size are beyond the capabilities of even the largest of classical computers.

The power of quantum computing rests on two cornerstones of quantum mechanics, 
:ref:`superposition <qc-intro-superposition>` and 
:ref:`entanglement <qc-intro-entanglement>` that highlight the wave- and particle-like aspects
of quantum computation, respectively.


.. _qc-intro-superposition:

Superposition
~~~~~~~~~~~~~

Like a classical computer, a quantum computer operates on bits.  However, while classical bits can
only be found in the states 0 and 1, a quantum bit, or qubit, can represent the values 0 and 1, 
or linear combinations of both.  These linear combinations are known as **superpositions** 
(or superposition states) and allow for representing, and processing, exponentially many
logical states at once.

To see how this resource is utilized in quantum computation we first turn toward a classical
analog: noise cancellation.  Noise cancellation, as done in noise cancelling headphones for example,
is performed by utilizing the principle of superposition to reduce the amplitude of unwanted noise by
generating a tone of approximately the same frequency and amplitude, but out of phase by a value of
:math:`\pi` (or any other odd integer of :math:`\pi`). 

.. figure:: images/noise_cancel.png
   :scale: 40 %
   :align: center

   Approximate cancellation of a noise signal by a tone of nearly equal amplitude
   and offset by a phase of :math:`\sim \pi`.
   

As shown above, when the phase difference is close to an odd multiple of :math:`\pi`, the superposition
of the two waves results in a output that is significantly reduced compared to the original.  The result 
is the signal of interest unincumbered by noise.
Although this processing is done by digital circuits, the amplitude and phase are continuous variables
that can never be matched perfectly, resulting in incomplete correction.

A general computation on a quantum computer proceeds in very much the same way as noise cancellation.
To begin, one prepares a superposition of all possible computation states.  This is then used as an input
to a **quantum circuit** that selectively interferes the components of the superposition according to a 
prescribed algorithm, with the output yielding the solution to the computation.

.. figure:: images/quantum_interference.png
   :align: center

   Quantum computation as an interference generation process.

.. _qc-intro-entanglement:

Entanglement
~~~~~~~~~~~~

The second principle of quantum mechanics that quantum computation can utilize is the
phenomena of **entanglement**.  Entanglement refers to states of more than one qubit 
(or particles in general) in which the combined state of the qubits contains more
information than the qubits do independently.  The overwhelming majority of multi-qubit quantum states
are entangled, and represent a valuable resource.  For example, entangled states between qubits can 
be used for quantum teleportation (quantum circuit below), where a shared entangled state of
two qubits can be manipulated to transfer information from one qubit to another, regardless of
the relative physical proximity of the qubits.


.. figure:: images/teleportation.png
   :align: center

   Quantum state teleportation circuit.

Entangled states as natural states of quantum systems are also of importance in disciplines such as
quantum chemistry and quantum simulation where the solution(s) often 
take the form of highly-entangled multi-qubit states.