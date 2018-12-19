# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""Tests for Aer simulation"""

import qiskit

from .base import QiskitTestCase


class TestAerSimulation(QiskitTestCase):
    """Tests for Aer simulation"""

    def test_execute_in_aer(self):
        """Test executing a circuit in an Aer simulator"""
        qr = qiskit.QuantumRegister(1)
        cr = qiskit.ClassicalRegister(1)
        circuit = qiskit.QuantumCircuit(qr, cr)
        circuit.h(qr[0])
        circuit.measure(qr, cr)

        backend = qiskit.Aer.get_backend('qasm_simulator')
        shots = 2000
        results = qiskit.execute(circuit, backend, shots=shots).result()
        self.assertDictAlmostEqual({'0': 1000, '1': 1000},
                                   results.get_counts(),
                                   delta=100)
