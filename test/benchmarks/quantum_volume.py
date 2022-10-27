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

# pylint: disable=missing-class-docstring,missing-function-docstring
# pylint: disable=attribute-defined-outside-init

"""Module for estimating quantum volume.
See arXiv:1811.12926 [quant-ph]"""

import numpy as np

from qiskit.compiler import transpile
from qiskit.converters import circuit_to_dag
from qiskit.transpiler import CouplingMap
from qiskit.transpiler.passes import SabreSwap

from .utils import build_qv_model_circuit


class QuantumVolumeBenchmark:
    params = ([1, 2, 3, 5, 8, 14, 20, 27], ['translator', 'synthesis'])
    param_names = ['Number of Qubits', 'Basis Translation Method']
    version = 3

    def setup(self, width, _):
        random_seed = np.random.seed(10)
        self.circuit = build_qv_model_circuit(width, width, random_seed)
        self.coupling_map = [
            [0, 1], [1, 0], [1, 2], [1, 4], [2, 1], [2, 3], [3, 2], [3, 5],
            [4, 1], [4, 7], [5, 3], [5, 8], [6, 7], [7, 4], [7, 6], [7, 10],
            [8, 5], [8, 9], [8, 11], [9, 8], [10, 7], [10, 12], [11, 8],
            [11, 14], [12, 10], [12, 13], [12, 15], [13, 12], [13, 14],
            [14, 11], [14, 13], [14, 16], [15, 12], [15, 18], [16, 14],
            [16, 19], [17, 18], [18, 15], [18, 17], [18, 21], [19, 16],
            [19, 20], [19, 22], [20, 19], [21, 18], [21, 23], [22, 19],
            [22, 25], [23, 21], [23, 24], [24, 23], [24, 25], [25, 22],
            [25, 24], [25, 26], [26, 25]]
        self.basis = ['id', 'rz', 'sx', 'x', 'cx', 'reset']

    def time_ibmq_backend_transpile(self, _, translation):
        transpile(self.circuit,
                  basis_gates=self.basis,
                  coupling_map=self.coupling_map,
                  translation_method=translation,
                  seed_transpiler=20220125)


class LargeQuantumVolumeMappingBenchmark:
    timeout = 600.0  # seconds
    heavy_hex_distance = {115: 7, 409: 13, 1081: 21}
    allowed_sizes = {(115, 100), (115, 10), (409, 10), (1081, 10)}
    n_qubits = sorted({n_qubits for n_qubits, _ in allowed_sizes})
    depths = sorted({depth for _, depth in allowed_sizes})

    params = (n_qubits, depths, ["lookahead", "decay"])
    param_names = ["n_qubits", "depth", "heuristic"]

    def setup(self, n_qubits, depth, _):
        if (n_qubits, depth) not in self.allowed_sizes:
            raise NotImplementedError
        seed = 2022_10_27
        self.dag = circuit_to_dag(build_qv_model_circuit(n_qubits, depth, seed))
        self.coupling = CouplingMap.from_heavy_hex(
            self.heavy_hex_distance[n_qubits]
        )

    def time_sabre_swap(self, _n_qubits, _depth, heuristic):
        pass_ = SabreSwap(self.coupling, heuristic, seed=2022_10_27, trials=1)
        pass_.run(self.dag)

    def track_depth_sabre_swap(self, _n_qubits, _depth, heuristic):
        pass_ = SabreSwap(self.coupling, heuristic, seed=2022_10_27, trials=1)
        return pass_.run(self.dag).depth()

    def track_size_sabre_swap(self, _n_qubits, _depth, heuristic):
        pass_ = SabreSwap(self.coupling, heuristic, seed=2022_10_27, trials=1)
        return pass_.run(self.dag).size()
