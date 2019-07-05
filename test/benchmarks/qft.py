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

import math

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import Aer

try:
    from qiskit.compiler import transpile, assemble
except ImportError:
    from qiskit.transpiler import transpile
    from qiskit.converters import circuits_to_qobj as assemble


def build_model_circuit(qreg, creg, circuit=None):
    """Create quantum fourier transform circuit on quantum register qreg."""
    if circuit is None:
        circuit = QuantumCircuit(qreg, creg, name="qft")

    n = len(qreg)

    for i in range(n):
        for j in range(i):
            circuit.cu1(math.pi/float(2**(i-j)), qreg[i], qreg[j])
        circuit.h(qreg[i])
    circuit.measure(qreg, creg)

    return circuit


class QftTranspileBench:
    params = [1, 2, 3, 5, 8, 13, 14, 20, 24]

    def setup(self, n):
        qr = QuantumRegister(n)
        cr = ClassicalRegister(n)
        self.circuit = build_model_circuit(qr, cr)
        self.sim_backend = Aer.get_backend('qasm_simulator')
        new_circ = transpile(self.circuit, self.sim_backend)
        self.qobj = assemble(new_circ, backend_name=self.sim_backend.name(), shots=1000)

    def time_simulator_transpile(self, _):
        transpile(self.circuit, self.sim_backend)

    def time_coupling_map_transpile(self, _):
        # Run with ibmq_poughkeepsie configuration, modified with an extra row to make 25 qubits
        coupling_map = [[0, 1], [0, 5], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4],
                [4, 3], [4, 9], [5, 0], [5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8],
                [7, 12], [8, 7], [8, 9], [9, 4], [9, 8], [9, 14], [10, 5], [10, 11], [10, 15],
                [11, 10], [11, 12], [12, 7], [12, 11], [12, 13], [13, 12], [13, 14], [14, 9],
                [14, 13], [14, 19], [15, 10], [15, 16], [15, 20], [16, 15], [16, 17], [17, 16],
                [17, 18], [18, 17], [18, 19], [19, 14], [19, 18], [19, 24], [20, 15], [20, 21],
                [21, 20], [21, 22], [22, 17], [22, 21], [22, 23], [23, 22], [23, 24],
                [24, 19], [24, 23]]
        transpile(self.circuit,
                  basis_gates=['u1', 'u2', 'u3', 'cx', 'id'],
                  coupling_map=coupling_map)

    def time_qasm_simulator_ideal(self, _):
        self.sim_backend.run(self.qobj).result()
