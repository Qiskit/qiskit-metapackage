=================
Rewiring Circuits
=================

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

.. toctree::
   :maxdepth: 1
   :hidden:

   About Transpilation <about/index>
   Resources <resources>
