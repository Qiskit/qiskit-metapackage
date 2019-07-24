===========
Resources
===========

The following are links to certain tutorials:

`Introducing the Transpiler <https://github.com/Qiskit/qiskit-tutorials/blob/master/qiskit/terra/using_the_transpiler.ipynb>`_
  This tutorial introduces the Qiskit transpiler and walks through some
  examples of circuit transformations using transpiler passes.

`Writing a Transpiler Pass <https://github.com/Qiskit/qiskit-tutorials/blob/master/qiskit/terra/writing_a_transpiler_pass.ipynb>`_
  This tutorial shows how to develop a simple transpiler pass. To do so,
  we first introduce the internal representation of quantum circuits in Qiskit,
  in the form of a Directed Acyclic Graph or DAG. Then, we illustrate a simple
  swap mapper pass, which transforms an input circuit to be compatible with a
  limited-connectivity quantum device.

The following are other related information:

`Qiskit Compiler and the Look-Ahead Swap Mapper <https://www.youtube.com/watch?v=hidQGlKl_-E>`_
  *Video (11:02)*

`Validating quantum computers using randomized model circuits <https://arxiv.org/abs/1811.12926>`_
  | *Research article*
  | All circuits for the simulations in Tables III and IV were compiled using
  | the standard Qiskit Terra transpiler.

`CQCL/pytket <https://github.com/CQCL/pytket>`_
  | *Github repository*
  | Transpiler pass for circuit optimization and mapping to backends using CQC’s
  | t|ket〉compiler.
