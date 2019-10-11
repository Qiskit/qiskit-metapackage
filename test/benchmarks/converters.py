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

from .utils import random_circuit


class ConverterBenchmarks:
    params = ([1, 2, 5, 8, 14, 20, 32, 53], [8, 128, 2048, 8192])
    param_names = ['n_qubits', 'depth']
    timeout = 600

    def setup(self, n_qubits, depth):
        seed = 42
        if n_qubits >= 20:
            if depth >= 2048:
                raise NotImplementedError
        elif n_qubits == 14:
            if depth > 2048:
                raise NotImplementedError
        self.qc = random_circuit(n_qubits, depth, measure=True,
                                 conditional=True, seed=seed)
        self.dag = converters.circuit_to_dag(self.qc)
        self.qasm = qasm.Qasm(data=self.qc.qasm()).parse()

    def time_circuit_to_dag(self, *_):
        converters.circuit_to_dag(self.qc)

    def time_circuit_to_instruction(self, *_):
        converters.circuit_to_instruction(self.qc)

    def time_dag_to_circuit(self, *_):
        converters.dag_to_circuit(self.dag)

    def time_ast_to_circuit(self, *_):
        converters.ast_to_dag(self.qasm)
