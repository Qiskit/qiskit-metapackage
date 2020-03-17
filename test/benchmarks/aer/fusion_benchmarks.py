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

# pylint: disable=no-member,invalid-name,missing-docstring
"""Gate Fusion benchmark suite"""

from qiskit import QuantumRegister
from qiskit.compiler import assemble
from qiskit.providers.aer import QasmSimulator
from ..utils import build_qft_circuit, build_quantum_volume_kak_circuit


class QuantumFourierTransformBenchmarks:
    """ QFT benchmark with/without gate fusion optimization enabled """
    def __init__(self):
        self.timeout = 60 * 20
        self.backend = QasmSimulator()
        num_qubits = [5, 10, 15, 20, 25]
        self.circuit = {}
        for num_qubit in num_qubits:
            for use_cu1 in [True, False]:
                qr = QuantumRegister(num_qubit, "qr")
                circuit = build_qft_circuit(
                    qr,
                    use_cu1,
                    measure=True
                )
                self.circuit[(num_qubit, use_cu1)] = assemble(
                    circuit,
                    self.backend,
                    shots=1
                )
        self.param_names = ["Quantum Fourier Transform", "Fusion Activated",
                            "Use cu1 gate"]
        self.params = (num_qubits, [True, False], [True, False])

    def time_quantum_fourier_transform(self, num_qubit, fusion_enable,
                                       use_cu1):
        """ Benchmark QFT """
        result = self.backend.run(
            self.circuit[(num_qubit, use_cu1)],
            backend_options={'fusion_enable': fusion_enable}
        ).result()
        if result.status != 'COMPLETED':
            raise Exception("Simulation failed. Status: " + result.status)


class RandomFusionBenchmarks:
    """
    Quantum Volume KAK variant with/without gate fusion optimization enabled
    """
    def __init__(self):
        self.timeout = 60 * 20
        self.backend = QasmSimulator()
        self.param_names = ["Number of Qubits", "Fusion Activated"]
        self.params = ([5, 10, 15, 20, 25], [True, False])

    def time_random_transform(self, num_qubits, fusion_enable):
        circ = build_quantum_volume_kak_circuit(num_qubits, num_qubits, 1)
        qobj = assemble(circ)
        result = self.backend.run(
            qobj,
            backend_options={'fusion_enable': fusion_enable}
        ).result()
        if result.status != 'COMPLETED':
            raise Exception("Simulation failed. Status: " + result.status)
