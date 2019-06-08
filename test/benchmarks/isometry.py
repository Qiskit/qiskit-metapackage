# -*- coding: utf-8 -*

# Copyright 2019, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# pylint: disable=missing-docstring,invalid-name,no-member
# pylint: disable=attribute-defined-outside-init

from qiskit import QuantumRegister, QuantumCircuit
from qiskit.compiler import transpile
from qiskit.quantum_info.random import random_unitary


class IsometryTranspileBench:
    params = ([0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
    param_names = ['number of input qubits', 'number of output qubits']

    def setup(self, m, n):
        iso = random_unitary(2 ** n).data[:, 0:2 ** m]
        if len(iso.shape) == 1:
            iso = iso.reshape((len(iso), 1))
        q = QuantumRegister(n)
        qc = QuantumCircuit(q)
        qc.iso(iso, q[:m], q[m:])
        self.circuit = qc

    def time_simulator_transpile(self, *unused):
        transpile(self.circuit, basis_gates=['u1', 'u3', 'u2', 'cx'])

    def track_gate_counts(self, *unused):
        circuit = transpiler.transpile(self.circuit, self.sim_backend)
        return circuit.count_ops()

