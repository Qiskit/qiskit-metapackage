# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=no-member,invalid-name,missing-docstring,no-name-in-module
# pylint: disable=attribute-defined-outside-init,unsubscriptable-object

import os

from qiskit import QuantumCircuit
from qiskit import converters
from qiskit import qasm


class ConverterBenchmarks:

    def setup(self):
        self.qasm_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'qasm'))
        large_qasm_path = os.path.join(self.qasm_path, 'test_eoh_qasm.qasm')
        self.large_qasm = QuantumCircuit.from_qasm_file(large_qasm_path)
        self.large_qasm_dag = converters.circuit_to_dag(self.large_qasm)
        self.large_qasm_ast = qasm.Qasm(large_qasm_path).parse()

    def time_circuit_to_dag(self):
        converters.circuit_to_dag(self.large_qasm)

    def time_circuit_to_instruction(self):
        converters.circuit_to_instruction(self.large_qasm)

    def time_dag_to_circuit(self):
        converters.dag_to_circuit(self.large_qasm_dag)

    def time_ast_to_circuit(self):
        converters.ast_to_dag(self.large_qasm_ast)
