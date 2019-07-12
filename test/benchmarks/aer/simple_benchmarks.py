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

"""
Airspeed Velocity (ASV) benchmarks suite for simple 1-qubit/2-qubit gates
"""

from qiskit import QiskitError
from qiskit.compiler import assemble
from qiskit.providers.aer import QasmSimulator
from .tools import mixed_unitary_noise_model, \
                   reset_noise_model, kraus_noise_model, no_noise, \
                   simple_cnot_circuit, simple_u3_circuit

# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.


class SimpleU3TimeSuite:
    """
    Benchmark simple circuits with just one U3 gate

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

    For each noise model, we want to test various configurations of number of
    qubits
    """

    def __init__(self):
        self.timeout = 60 * 20
        self.backend = QasmSimulator()
        self.circuits = []
        for i in 5, 10, 15:
            circuit = simple_u3_circuit(i)
            self.circuits.append(assemble(circuit, self.backend, shots=1))

        self.param_names = [
            "Simple u3 circuits", "Noise Model"
        ]
        self.params = (self.circuits, [
            no_noise(),
            mixed_unitary_noise_model(),
            reset_noise_model(),
            kraus_noise_model()
        ])

    def time_simple_u3(self, qobj, noise_model_wrapper):
        """ Benchmark for circuits with a simple u3 gate """
        result = self.backend.run(
            qobj, noise_model=noise_model_wrapper()
        ).result()
        if result.status != 'COMPLETED':
            raise QiskitError("Simulation failed. Status: " + result.status)


class SimpleCxTimeSuite:
    """
    Benchmark simple circuits with just on CX gate

    For each noise model, we want to test various configurations of number of
    qubits
    """

    def __init__(self):
        self.timeout = 60 * 20
        self.backend = QasmSimulator()
        self.circuits = []
        self.param_names = [
            "Simple cnot circuits", "Noise Model"
        ]
        for i in 5, 10, 15:
            circuit = simple_cnot_circuit(i)
            self.circuits.append(assemble(circuit, self.backend, shots=1))
        self.params = (self.circuits, [
            no_noise(),
            mixed_unitary_noise_model(),
            reset_noise_model(),
            kraus_noise_model()
        ])

    def time_simple_cx(self, qobj, noise_model_wrapper):
        """ Benchmark for circuits with a simple cx gate """
        result = self.backend.run(
            qobj, noise_model=noise_model_wrapper()
        ).result()
        if result.status != 'COMPLETED':
            raise QiskitError("Simulation failed. Status: " + result.status)
