# -*- coding: utf-8 -*-

# Copyright 2018 IBM RESEARCH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

# pylint: disable=no-member,invalid-name,missing-docstring,no-name-in-module
# pylint: disable=attribute-defined-outside-init,unsubscriptable-object

"""Module for estimating quantum volume.
See arXiv:1811.12926 [quant-ph]"""

import numpy as np

from qiskit.circuit import QuantumCircuit, QuantumRegister
from qiskit.compiler import transpile
from qiskit.quantum_info.random import random_unitary
from qiskit.providers.basicaer import QasmSimulatorPy
from qiskit.test.mock import FakeMelbourne


def build_model_circuit(width, depth, seed=None):
    """
    The model circuits consist of layers of Haar random
    elements of SU(4) applied between corresponding pairs
    of qubits in a random bipartition.
    """
    np.random.seed(seed)
    circuit = QuantumCircuit(width)
    # For each layer
    for j in range(depth):
        # Generate uniformly random permutation Pj of [0...n-1]
        perm = np.random.permutation(width)
        # For each pair p in Pj, generate Haar random SU(4)
        for k in range(int(np.floor(width/2))):
            U = random_unitary(4)
            pair = int(perm[2*k]), int(perm[2*k+1])
            circuit.append(U, [pair[0], pair[1]])
    return circuit


class QuantumVolumeBenchmark:
    params = ([1, 2, 3, 5, 8, 13, 14], [1, 2, 3, 5, 8, 13, 21, 34])
    param_names = ['width', 'depth']
    timeout = 600

    def setup(self, width, depth):
        random_seed = np.random.seed(10)
        self.circuit = build_model_circuit(
            width=width, depth=depth, seed=random_seed)
        self.sim_backend = QasmSimulatorPy()

    def time_simulator_transpile(self, _, __):
        transpile(self.circuit, self.sim_backend)

    def time_ibmq_backend_transpile(self, _, __):
        # Run with ibmq_16_melbourne configuration
        backend = FakeMelbourne()
        transpile(self.circuit,
                  basis_gates=['u1', 'u2', 'u3', 'cx', 'id'],
                  coupling_map=backend.coupling_map)
