# -*- coding: utf-8 -*

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=missing-docstring,invalid-name,no-member
# pylint: disable=attribute-defined-outside-init
# pylint: disable=no-name-in-module,import-error

from qiskit.circuit import QuantumRegister, Gate
from qiskit.dagcircuit import DAGCircuit

class DAGCircuitApplyOperationBench:
    params = ([1, 5, 10, 50, 100],
              [0, 1, 10, 100, 1000],
              [1, 2, 5, 10])
    param_names = ['num_dag_qubits', 'num_op_gates', 'num_op_qubits']

    def setup(self, num_dag_qubits, num_op_gates, num_op_qubits):
        if num_op_qubits > num_dag_qubits:
            raise NotImplementedError

        self.qr = QuantumRegister(num_dag_qubits)
        self.dag = DAGCircuit()
        self.dag.add_qreg(self.qr)

        oneq_op = Gate('oneq', 1, [])
        for i in range(num_op_gates):
            self.dag.apply_operation_back(oneq_op, [self.qr[i % num_dag_qubits]])
        self.test_op = Gate('test', num_op_qubits, [])

    def time_apply_operation_back(self, _, __, num_op_qubits):
        self.dag.apply_operation_back(
            self.test_op,
            self.qr[:num_op_qubits]
        )

class DAGCircuitSubstituteNodeWithDAGBench:
    params = ([1, 5, 10, 20, 50, 100],
              [1, 10, 100, 1000])
    param_names = ['node_width', 'num_dag_gates']

    def setup(self, node_width, num_dag_gates):
        dag_width = 120
        self.qr = QuantumRegister(dag_width, 'q')
        self.dag = DAGCircuit()
        self.dag.add_qreg(self.qr)

        oneq_op = Gate('oneq', 1, [])
        twoq_op = Gate('twoq', 2, [])

        # Build DAG with alternating 1Q/2Q gates, with target op in the middle.
        for i in range(0, dag_width, 3):
            self.dag.apply_operation_back(oneq_op, self.qr[i:i+1])
            self.dag.apply_operation_back(twoq_op, self.qr[i+1:i+3])

        target_op = Gate('target', node_width, [])
        self.target_node = self.dag.apply_operation_back(target_op, self.qr[:node_width])

        for i in range(0, dag_width, 3):
            self.dag.apply_operation_back(oneq_op, self.qr[i:i+1])
            self.dag.apply_operation_back(twoq_op, self.qr[i+1:i+3])

        # Input DAG with alternating 1Q/2Q gates.
        self.input_dag = DAGCircuit()
        input_qr = QuantumRegister(node_width, 'input_reg')
        self.input_dag.add_qreg(input_qr)

        for i in range(0, num_dag_gates, 3):
            self.input_dag.apply_operation_back(
                oneq_op, [input_qr[i % node_width]])

            self.input_dag.apply_operation_back(
                twoq_op, input_qr[(i + 1) % node_width
                                  :(i + 3) % node_width])

        # substitute_node_with_dag will remove target_node from the dag, so we
        # need a clean dag for each iteration of the benchmark.
        from copy import deepcopy
        self.dags = [deepcopy(self.dag) for _ in range(200)]
        self.i = 0

    def time_substitute_node_with_dag(self, _, __):
        self.dags[self.i].substitute_node_with_dag(self.target_node, self.input_dag)
        self.i += 1

    # N.B. In my testing, this did not work (so smaller benchmarks would fail
    # with an IndexError). Maybe this is an ASV bug?
    time_substitute_node_with_dag.number = 200
