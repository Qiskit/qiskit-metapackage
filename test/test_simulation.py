# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

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
