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
from qiskit.providers.basicaer import QasmSimulatorPy
from .utils import build_quantum_volume_kak_circuit

try:
    from qiskit.compiler import transpile
except ImportError:
    from qiskit.transpiler import transpile


class QuantumVolumeBenchmark:
    params = ([1, 2, 3, 5, 8, 13, 14], [1, 2, 3, 5, 8, 13, 21, 34])
    param_names = ['width', 'depth']
    version = 2
    timeout = 600

    def setup(self, width, depth):
        random_seed = np.random.seed(10)
        self.circuit = build_quantum_volume_kak_circuit(
            width, depth, random_seed
        )
        self.sim_backend = QasmSimulatorPy()

    def time_simulator_transpile(self, _, __):
        transpile(self.circuit, self.sim_backend)

    def time_ibmq_backend_transpile(self, _, __):
        # Run with ibmq_16_melbourne configuration
        coupling_map = [[1, 0], [1, 2], [2, 3], [4, 3], [4, 10], [5, 4],
                        [5, 6], [5, 9], [6, 8], [7, 8], [9, 8], [9, 10],
                        [11, 3], [11, 10], [11, 12], [12, 2], [13, 1],
                        [13, 12]]

        transpile(self.circuit,
                  basis_gates=['u1', 'u2', 'u3', 'cx', 'id'],
                  coupling_map=coupling_map)
