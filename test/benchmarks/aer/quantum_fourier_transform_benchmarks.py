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

"""Quantum Fourier Transform benchmark suite"""
# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

from qiskit.compiler import transpile, assemble
from qiskit.providers.aer import QasmSimulator
from .utils import build_qft_circuit, mixed_unitary_noise_model, \
                    reset_noise_model, kraus_noise_model, no_noise


class QuantumFourierTransformQasmSimulatorBenchmarks:
    """
    Benchmarking times for Quantum Fourier Transform with various noise
    configurations:
    - ideal (no noise)
    - mixed state
    - reset
    - kraus

    and different simulator methods

    For each noise model, we want to test various configurations of number of
    qubits

    The methods defined in this class will be executed by ASV framework as many
    times as the combination of all parameters exist in `self.params`, for
    exmaple: self.params = ([1,2,3],[4,5,6]), will run all methdos 9 times:
        time_method(1,4)
        time_method(1,5)
        time_method(1,6)
        time_method(2,4)
        time_method(2,5)
        time_method(2,6)
        time_method(3,4)
        time_method(3,5)
        time_method(3,6)
    """

    def __init__(self):
        self.timeout = 60 * 20
        self.qft_circuits = []
        self.backend = QasmSimulator()
        for num_qubits in (5, 10, 15, 20):
            circ = build_qft_circuit(num_qubits, measure=True)
            circ = transpile(circ, basis_gates=['u1', 'u2', 'u3', 'cx'],
                             optimization_level=0, seed_transpiler=1)
            qobj = assemble(circ, self.backend, shots=1)
            self.qft_circuits.append(qobj)

        self.param_names = ["Quantum Fourier Transform", "Noise Model",
                            "Simulator Method"]

        # This will run every benchmark for one of the combinations we have:
        # bench(qft_circuits, None) => bench(qft_circuits, mixed()) =>
        # bench(qft_circuits, reset) => bench(qft_circuits, kraus())
        self.params = (
            self.qft_circuits, [no_noise(), mixed_unitary_noise_model(),
                                reset_noise_model(), kraus_noise_model()],
            ['statevector', 'density_matrix', 'stabilizer',
             'extended_stabilizer', 'matrix_product_state'])

    def setup(self, qobj, noise_model_wrapper, simulator_method):
        """ Setup env before benchmarks start """

    def time_quantum_fourier_transform(self, qobj, noise_model_wrapper,
                                       simulator_method):
        """ Benchmark QFT """
        backend_options = {
            'method': simulator_method,
            'noise_model': noise_model_wrapper(),
        }
        result = self.backend.run(
            qobj, backend_options=backend_options
        ).result()
        if result.status != 'COMPLETED':
            raise Exception("Simulation failed. Status: " + result.status)

    def peakmem_quantum_fourier_transform(self, qobj, noise_model_wrapper,
                                          simulator_method):
        """ Benchmark QFT """
        backend_options = {
            'method': simulator_method,
            'noise_model': noise_model_wrapper(),
        }
        result = self.backend.run(
            qobj, backend_options=backend_options
        ).result()
        if result.status != 'COMPLETED':
            raise Exception("Simulation failed. Status: " + result.status)
