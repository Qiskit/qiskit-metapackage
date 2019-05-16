.. _Transpiler API Overview:

=======================
Transpiler API Overview
=======================

There are two main ways to use the transpiler:

#. Use the ``transpile()`` function, and specify some desired transpilation
   options, like ``basis_gates``, ``coupling_map``, ``initial_layout`` of
   qubits, or ``optimization_level``.
#. Create your own custom pass manager.
