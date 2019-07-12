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

"""Quantum Voluming benchmark suite"""
# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

from qiskit import QiskitError
from qiskit.compiler import transpile, assemble
from qiskit.providers.aer import QasmSimulator
from .tools import quantum_volume_circuit, mixed_unitary_noise_model, \
                   reset_noise_model, kraus_noise_model, no_noise


class QuantumVolumeTimeSuite:
    """
    Benchmarking times for Quantum Volume with various noise configurations
    - ideal (no noise)
    - mixed state
    - reset
    - kraus

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
        self.qv_circuits = []
        self.backend = QasmSimulator()
        for num_qubits in (5, 10, 15):
            for depth in (10, ):
                # We want always the same seed, as we want always the same
                # circuits for the same value pairs of qubits and depth
                circ = quantum_volume_circuit(num_qubits, depth, seed=1)
                circ = transpile(circ, basis_gates=['u1', 'u2', 'u3', 'cx'],
                                 optimization_level=0, seed_transpiler=1)
                qobj = assemble(circ, self.backend, shots=1)
                self.qv_circuits.append(qobj)
        self.param_names = ["Quantum Volume", "Noise Model"]

        # This will run every benchmark for one of the combinations we have:
        # bench(qv_circuits, None) => bench(qv_circuits, mixed()) =>
        # bench(qv_circuits, reset) => bench(qv_circuits, kraus())
        self.params = (self.qv_circuits, [
            no_noise(),
            mixed_unitary_noise_model(),
            reset_noise_model(),
            kraus_noise_model()
        ])

    def setup(self, qobj, noise_model_wrapper):
        """ Setup enviornment before running the tests """

    def time_quantum_volume(self, qobj, noise_model_wrapper):
        """ Benchmark for quantum volume """
        result = self.backend.run(
            qobj, noise_model=noise_model_wrapper()
        ).result()
        if result.status != 'COMPLETED':
            raise QiskitError("Simulation failed. Status: " + result.status)
