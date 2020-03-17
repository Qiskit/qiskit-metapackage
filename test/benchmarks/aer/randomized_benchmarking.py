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

# pylint: disable=no-member,invalid-name,missing-docstring,no-name-in-module
# pylint: disable=attribute-defined-outside-init,unsubscriptable-object

import numpy as np

from qiskit import assemble
from qiskit import transpile
from qiskit import Aer
from ..utils import build_randomized_benchmark_circuit, kraus_noise_model, \
                    no_noise, mixed_unitary_noise_model, reset_noise_model


class RandomizedBenchmarkingQasmSimBenchmarks:
    # parameters for RB (1&2 qubits):
    params = ([[[0]], [[0, 1]], [[0, 2], [1]]],
              ['statevector', 'density_matrix', 'stabilizer',
               'extended_stabilizer', 'matrix_product_state'],
              [no_noise(), mixed_unitary_noise_model(), reset_noise_model(),
               kraus_noise_model()])
    param_names = ['rb_pattern', 'simulator_method', 'noise_model']
    version = '0.2.0'
    timeout = 600

    def setup(self, rb_pattern, _, __):
        length_vector = np.arange(1, 200, 4)
        nseeds = 1
        self.seed = 10
        self.circuits = build_randomized_benchmark_circuit(
            nseeds=nseeds,
            length_vector=length_vector,
            rb_pattern=rb_pattern,
            seed=self.seed
        )
        self.sim_backend = Aer.get_backend('qasm_simulator')
        trans_circ = transpile(self.circuits, backend=self.sim_backend,
                               seed_transpiler=self.seed)
        self.qobj = assemble(trans_circ, backend=self.sim_backend)

    def time_run_rb_circuit(self, _, simulator_method, noise_model):
        backend_options = {
            'method': simulator_method,
            'noise_model': noise_model(),
        }
        job = self.sim_backend.run(self.qobj,
                                   backend_options=backend_options)
        job.result()

    def peakmem_run_rb_circuit(self, _, simulator_method, noise_model):
        backend_options = {
            'method': simulator_method,
            'noise_model': noise_model(),
        }
        job = self.sim_backend.run(self.qobj,
                                   backend_options=backend_options)
        job.result()
