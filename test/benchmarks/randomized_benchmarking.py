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

"""Module for estimating randomized benchmarking."""

import numpy as np
import qiskit.ignis.verification.randomized_benchmarking as rb
from qiskit.providers.basicaer import QasmSimulatorPy

try:
    from qiskit.compiler import transpile
except ImportError:
    from qiskit.transpiler import transpile


def build_rb_circuit(nq, nseeds=1, length_vector=None,
                     rb_pattern=None, length_multiplier=1,
                     seed_offset=0, align_cliffs=False, seed=None):
    """
    Randomized Benchmarking sequences.
    """
    np.random.seed(seed)
    rb_opts = {}
    rb_opts['nseeds'] = nseeds
    rb_opts['length_vector'] = length_vector
    rb_opts['rb_pattern'] = rb_pattern
    rb_opts['length_multiplier'] = length_multiplier
    rb_opts['seed_offset'] = seed_offset
    rb_opts['align_cliffs'] = align_cliffs

    # Generate the sequences
    try:
        rb_circs, _ = rb.randomized_benchmarking_seq(**rb_opts)
    except OSError:
        skip_msg = ('Skipping tests for %s qubits because '
                    'tables are missing' % str(nq))
        print(skip_msg)
    return rb_circs


class RandomizedBenchmarkingBenchmark:
    # parameters for RB (1&2 qubits):
    params = ([1, 2, 3], [1, 5, 10],
              [[[0]], [[0, 1]], [[0, 2], [1]]],
              [[1], [1], [1, 3]],
              [np.arange(1, 200, 4), np.arange(1, 500, 10)])
    param_names = ['nq', 'nseeds', 'rb_pattern',
                   'length_multiplier', 'length_vector']
    versions = 2
    timeout = 600

    def setup(self, nq, nseeds, length_vector, rb_pattern,
              length_multiplier):
        random_seed = np.random.seed(10)
        self.circuit = build_rb_circuit(nq=nq, nseeds=nseeds,
                                        length_vector=length_vector,
                                        rb_pattern=rb_pattern,
                                        length_multiplier=length_multiplier,
                                        seed=random_seed)

        self.sim_backend = QasmSimulatorPy()

    def time_simulator_transpile(self, _, __, ___, ____, _____):
        transpile(self.circuit, self.sim_backend)

    def time_ibmq_backend_transpile(self, _, __, ___, ____, _____):
        # Run with ibmq_16_melbourne configuration
        coupling_map = [[1, 0], [1, 2], [2, 3], [4, 3], [4, 10], [5, 4],
                        [5, 6], [5, 9], [6, 8], [7, 8], [9, 8], [9, 10],
                        [11, 3], [11, 10], [11, 12], [12, 2], [13, 1],
                        [13, 12]]

        transpile(self.circuit,
                  basis_gates=['u1', 'u2', 'u3', 'cx', 'id'],
                  coupling_map=coupling_map)
