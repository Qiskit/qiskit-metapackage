DAGCircuit
==========

.. currentmodule:: qiskit.dagcircuit

.. autoclass:: DAGCircuit
   :show-inheritance:

   .. rubric:: Attributes Summary

   .. autosummary::

      ~DAGCircuit.multi_graph
      ~DAGCircuit.node_counter

   .. rubric:: Methods Summary

   .. autosummary::

      ~DAGCircuit.add_creg
      ~DAGCircuit.add_qreg
      ~DAGCircuit.ancestors
      ~DAGCircuit.apply_operation_back
      ~DAGCircuit.apply_operation_front
      ~DAGCircuit.bfs_successors
      ~DAGCircuit.clbits
      ~DAGCircuit.collect_runs
      ~DAGCircuit.compose_back
      ~DAGCircuit.compose_front
      ~DAGCircuit.count_ops
      ~DAGCircuit.depth
      ~DAGCircuit.descendants
      ~DAGCircuit.edges
      ~DAGCircuit.extend_back
      ~DAGCircuit.gate_nodes
      ~DAGCircuit.get_2q_nodes
      ~DAGCircuit.get_3q_or_more_nodes
      ~DAGCircuit.get_bits
      ~DAGCircuit.get_gate_nodes
      ~DAGCircuit.get_named_nodes
      ~DAGCircuit.get_op_nodes
      ~DAGCircuit.get_qubits
      ~DAGCircuit.layers
      ~DAGCircuit.multigraph_layers
      ~DAGCircuit.named_nodes
      ~DAGCircuit.node
      ~DAGCircuit.nodes
      ~DAGCircuit.nodes_on_wire
      ~DAGCircuit.num_cbits
      ~DAGCircuit.num_tensor_factors
      ~DAGCircuit.op_nodes
      ~DAGCircuit.predecessors
      ~DAGCircuit.properties
      ~DAGCircuit.qasm
      ~DAGCircuit.quantum_predecessors
      ~DAGCircuit.quantum_successors
      ~DAGCircuit.qubits
      ~DAGCircuit.remove_all_ops_named
      ~DAGCircuit.remove_ancestors_of
      ~DAGCircuit.remove_descendants_of
      ~DAGCircuit.remove_nonancestors_of
      ~DAGCircuit.remove_nondescendants_of
      ~DAGCircuit.remove_op_node
      ~DAGCircuit.rename_register
      ~DAGCircuit.serial_layers
      ~DAGCircuit.size
      ~DAGCircuit.substitute_node_with_dag
      ~DAGCircuit.successors
      ~DAGCircuit.threeQ_or_more_gates
      ~DAGCircuit.to_networkx
      ~DAGCircuit.topological_nodes
      ~DAGCircuit.topological_op_nodes
      ~DAGCircuit.twoQ_gates
      ~DAGCircuit.width

   .. rubric:: Attributes Documentation

   .. autoattribute:: multi_graph
   .. autoattribute:: node_counter

   .. rubric:: Methods Documentation

   .. automethod:: add_creg
   .. automethod:: add_qreg
   .. automethod:: ancestors
   .. automethod:: apply_operation_back
   .. automethod:: apply_operation_front
   .. automethod:: bfs_successors
   .. automethod:: clbits
   .. automethod:: collect_runs
   .. automethod:: compose_back
   .. automethod:: compose_front
   .. automethod:: count_ops
   .. automethod:: depth
   .. automethod:: descendants
   .. automethod:: edges
   .. automethod:: extend_back
   .. automethod:: gate_nodes
   .. automethod:: get_2q_nodes
   .. automethod:: get_3q_or_more_nodes
   .. automethod:: get_bits
   .. automethod:: get_gate_nodes
   .. automethod:: get_named_nodes
   .. automethod:: get_op_nodes
   .. automethod:: get_qubits
   .. automethod:: layers
   .. automethod:: multigraph_layers
   .. automethod:: named_nodes
   .. automethod:: node
   .. automethod:: nodes
   .. automethod:: nodes_on_wire
   .. automethod:: num_cbits
   .. automethod:: num_tensor_factors
   .. automethod:: op_nodes
   .. automethod:: predecessors
   .. automethod:: properties
   .. automethod:: qasm
   .. automethod:: quantum_predecessors
   .. automethod:: quantum_successors
   .. automethod:: qubits
   .. automethod:: remove_all_ops_named
   .. automethod:: remove_ancestors_of
   .. automethod:: remove_descendants_of
   .. automethod:: remove_nonancestors_of
   .. automethod:: remove_nondescendants_of
   .. automethod:: remove_op_node
   .. automethod:: rename_register
   .. automethod:: serial_layers
   .. automethod:: size
   .. automethod:: substitute_node_with_dag
   .. automethod:: successors
   .. automethod:: threeQ_or_more_gates
   .. automethod:: to_networkx
   .. automethod:: topological_nodes
   .. automethod:: topological_op_nodes
   .. automethod:: twoQ_gates
   .. automethod:: width
