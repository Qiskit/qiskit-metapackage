# -*- coding: utf-8 -*

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import os

import qiskit


class TranspilerBenchSuite:

    def _build_cx_circuit(self):
        if self.local_qasm_simulator is None:
            qp = qiskit.QuantumProgram()
            cx_register = qp.create_quantum_register('qr', 2)
            cx_circuit = qp.create_circuit("cx_circuit", [cx_register])
            cx_circuit.h(cx_register[0])
            cx_circuit.h(cx_register[0])
            cx_circuit.cx(cx_register[0], cx_register[1])
            cx_circuit.cx(cx_register[0], cx_register[1])
            cx_circuit.cx(cx_register[0], cx_register[1])
            cx_circuit.cx(cx_register[0], cx_register[1])
            return qp
        else:
            cx_register = qiskit.QuantumRegister(2)
            cx_circuit = qiskit.QuantumCircuit(cx_register)
            cx_circuit.h(cx_register[0])
            cx_circuit.h(cx_register[0])
            cx_circuit.cx(cx_register[0], cx_register[1])
            cx_circuit.cx(cx_register[0], cx_register[1])
            cx_circuit.cx(cx_register[0], cx_register[1])
            cx_circuit.cx(cx_register[0], cx_register[1])
            return cx_circuit

    def _build_single_gate_circuit(self):
        if self.local_qasm_simulator is None:
            qp = qiskit.QuantumProgram()
            single_register = qp.create_quantum_register('qr', 1)
            single_gate_circuit = qp.create_circuit('single_gate',
                                                    [single_register])
            single_gate_circuit.h(single_register[0])
            return qp
        else:
            single_register = qiskit.QuantumRegister(1)
            single_gate_circuit = qiskit.QuantumCircuit(single_register)
            single_gate_circuit.h(single_register[0])
            return single_gate_circuit

    def setup(self):
        version_parts = qiskit.__version__.split('.')

        if version_parts[0] == '0' and int(version_parts[1]) < 5:
            self.local_qasm_simulator = None
        elif hasattr(qiskit, 'Aer'):
            self.local_qasm_simulator = qiskit.Aer.get_backend(
                'qasm_simulator')
        elif hasattr(qiskit, 'get_backend'):
                self.local_qasm_simulator = qiskit.get_backend(
                    'local_qasm_simulator')
        else:
            self.local_qasm_simulator = qiskit.BasicAer.get_backend(
                "qasm_simulator")
        self.single_gate_circuit = self._build_single_gate_circuit()
        self.cx_circuit = self._build_cx_circuit()
        self.qasm_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'qasm'))
        pea_3_pi_8_path = os.path.join(self.qasm_path, 'pea_3_pi_8.qasm')
        large_qasm_path = os.path.join(self.qasm_path, 'test_eoh_qasm.qasm')

        if hasattr(qiskit, 'load_qasm_file'):
#            self.pea_3_pi_8 = qiskit.load_qasm_file(pea_3_pi_8_path)
            self.large_qasm = qiskit.load_qasm_file(large_qasm_path)
        elif version_parts[0] == '0' and int(version_parts[1]) < 5:
#            self.pea_3_pi_8 = qiskit.QuantumProgram()
#            self.pea_3_pi_8.load_qasm_file(pea_3_pi_8_path,
#                                           name='pea_3_pi_8')
            self.large_qasm = qiskit.QuantumProgram()
            self.large_qasm.load_qasm_file(large_qasm_path,
                                           name='large_qasm')
        else:
#            self.pea_3_pi_8 = qiskit.QuantumCircuit.from_qasm_file(
#                pea_3_pi_8_path)
            self.large_qasm = qiskit.QuantumCircuit.from_qasm_file(
                large_qasm_path)

    def time_single_gate_transpile(self):
        if self.local_qasm_simulator is None:
            self.single_gate_circuit.compile('single_gate')
        else:
            qiskit.compile(self.single_gate_circuit, self.local_qasm_simulator)

    def time_cx_transpile(self):
        if self.local_qasm_simulator is None:
            self.cx_circuit.compile('cx_circuit')
        else:
            qiskit.compile(self.cx_circuit, self.local_qasm_simulator)

#    def time_pea_3_pi_8(self):
#        if self.local_qasm_simulator is None:
#            self.pea_3_pi_8.compile('pea_3_pi_8')
#        else:
#            qiskit.compile(self.pea_3_pi_8, self.local_qasm_simulator)

    def time_transpile_from_large_qasm(self):
        if self.local_qasm_simulator is None:
            self.large_qasm.compile('large_qasm')
        else:
            qiskit.compile(self.large_qasm, self.local_qasm_simulator)
