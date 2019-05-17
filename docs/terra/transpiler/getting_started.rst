===================================
Getting Started with the Transpiler
===================================

.. contents::

The Qiskit **transpiler** is a circuit rewriting framework. The term *transpiler*
was coined to evoke much of the meaning of the term *compiler*, but to allow a
distinction between (1) circuit-level analysis and transformations, as compared
to (2) a larger translation from high-level applications (potentially many
circuits, with classical control flow between them) down to the level of machine
pulses. We refer to (1) as *transpilation* and reserve the term *compilation*
for (2).

You can use the transpiler to reduce the number of gates and qubits of a circuit
in order to increase the fidelity of executions to do the most with the limited
quantum resources available today.



---------
Tutorials
---------

`Introducing the Transpiler`_
  This tutorial introduces the Qiskit transpiler and walks through some
  examples of circuit transformations using transpiler passes.

`Writing a Transpiler Pass`_
  This tutorial shows how to develop a simple transpiler pass. To do so,
  we first introduce the internal representation of quantum circuits in Qiskit,
  in the form of a Directed Acyclic Graph or DAG. Then, we illustrate a simple
  swap mapper pass, which transforms an input circuit to be compatible with a
  limited-connectivity quantum device.

.. _Introducing the Transpiler: https://github.com/Qiskit/qiskit-tutorials/blob/
   master/qiskit/terra/using_the_transpiler.ipynb

.. _Writing a Transpiler Pass: https://github.com/Qiskit/qiskit-tutorials/blob/
   master/qiskit/terra/writing_a_transpiler_pass.ipynb


-------------------
About Transpilation
-------------------

:ref:`Transpiler API Overview`
  The big picture.

:ref:`Transpiler Passes`
  What is a transpiler pass?

:ref:`Pass Managers`
  What is a pass manager?

-------------------
Related information
-------------------

`Qiskit Compiler and the Look-Ahead Swap Mapper`_
  *Video (11:02)*

`Validating quantum computers using randomized model circuits`_
  | *Research article*
  | All circuits for the simulations in Tables III and IV were compiled using
  | the standard Qiskit Terra transpiler.

`CQCL/pytket`_
  | *Github repository*
  | Transpiler pass for circuit optimization and mapping to backends using CQC’s
  | t|ket〉compiler.


.. _Qiskit Compiler and the Look-Ahead Swap Mapper: https://www.youtube.com/
   watch?v=hidQGlKl_-E

.. _Validating quantum computers using randomized model circuits : https://
   arxiv.org/abs/1811.12926

.. _CQCL/pytket: https://github.com/CQCL/pytket
