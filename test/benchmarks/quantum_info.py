# -*- coding: utf-8 -*

# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
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

import random
from qiskit.quantum_info import random_clifford, Clifford, \
    decompose_clifford, random_pauli, Pauli, SparsePauliOp
from qiskit.quantum_info.operators.symplectic.random import random_pauli_list
from qiskit.quantum_info import random_cnotdihedral, CNOTDihedral
import numpy as np


class RandomCliffordBench:
    params = ['1,3000', '2,2500', '3,2000', '4,1500', '5,1000', '6,700']
    param_names = ['nqubits,length']

    def time_random_clifford(self, nqubits_length):
        (nqubits, length) = map(int, nqubits_length.split(','))
        for _ in range(length):
            random_clifford(nqubits)


class CliffordComposeBench:
    params = ['1,7000', '2,5000', '3,5000', '4,2500', '5,2000']
    param_names = ['nqubits,length']

    def setup(self, nqubits_length):
        (nqubits, length) = map(int, nqubits_length.split(','))
        self.random_clifford = \
            [random_clifford(nqubits) for _ in range(length)]

    def time_compose(self, nqubits_length):
        (nqubits, length) = map(int, nqubits_length.split(','))
        clifford = Clifford(np.eye(2 * nqubits))
        for i in range(length):
            clifford.compose(self.random_clifford[i])


class CliffordDecomposeBench:
    params = ['1,1000', '2,500', '3,100', '4,50', '5,10']
    param_names = ['nqubits,length']

    def setup(self, nqubits_length):
        (nqubits, length) = map(int, nqubits_length.split(','))
        self.random_clifford = \
            [random_clifford(nqubits) for _ in range(length)]

    def time_decompose(self, nqubits_length):
        length = int(nqubits_length.split(',')[1])
        for i in range(length):
            decompose_clifford(self.random_clifford[i])


class RandomCnotDihedralBench:
    params = ['1,2000', '2,1500', '3,1200', '4,1000', '5,800', '6,700']
    param_names = ['nqubits,length']

    def time_random_cnotdihedral(self, nqubits_length):
        (nqubits, length) = map(int, nqubits_length.split(','))
        for _ in range(length):
            random_cnotdihedral(nqubits)


class CnotDihedralComposeBench:
    params = ['1,1500', '2,400', '3,100', '4,40', '5,10']
    param_names = ['nqubits,length']

    def setup(self, nqubits_length):
        (nqubits, length) = map(int, nqubits_length.split(','))
        self.random_cnotdihedral = \
            [random_cnotdihedral(nqubits) for _ in range(length)]

    def time_compose(self, nqubits_length):
        (nqubits, length) = map(int, nqubits_length.split(','))
        cxdihedral = CNOTDihedral(num_qubits=nqubits)
        for i in range(length):
            cxdihedral.compose(self.random_cnotdihedral[i])


class PauliBench:
    params = [100, 200, 300, 400, 500]

    def time_basic_ops(self, nqubits):
        iterations = 200
        for _ in range(0, iterations):
            p1 = random_pauli(nqubits, True)
            p2 = random_pauli(nqubits, True)

            p1.compose(p2)
            p1.evolve(p2)  # by another Pauli, so by composition
            p1.commutes(p2)
            p1.to_instruction()

    def time_conversions(self, nqubits):
        iterations = 200
        for _ in range(0, iterations):
            p = random_pauli(nqubits, True)
            label = p.to_label()
            Pauli(label).to_instruction()

    def time_evolve_by_clifford(self, nqubits):
        iterations = 20
        for _ in range(0, iterations):
            p1 = random_pauli(nqubits, True)
            c1 = random_clifford(nqubits)
            p1.evolve(c1)
    time_evolve_by_clifford.params = [10]


class PauliListBench:
    params = [100, 200, 300, 400, 500]

    def time_basic_ops(self, nqubits):
        length = 500

        pl1 = random_pauli_list(num_qubits=nqubits, size=length, phase=True)
        pl2 = random_pauli_list(num_qubits=nqubits, size=length, phase=True)

        pl1.commutes(pl2)
        pl1.commutes_with_all(pl2)
        pl1.argsort()
        pl1.compose(pl2)
        pl1.group_qubit_wise_commuting()  # exercise retworkx-based code

    def time_basic_op_with_qargs(self, nqubits):
        length = 500
        half_qubits = int(nqubits/2)

        pl1 = random_pauli_list(num_qubits=nqubits, size=length, phase=True)
        pl2 = random_pauli_list(num_qubits=half_qubits, size=length,
                                phase=True)

        qargs = [random.randint(0, nqubits - 1) for _ in range(half_qubits)]
        pl1.commutes(pl2, qargs)
        pl1.compose(pl2, qargs)

    def time_evolve_by_clifford(self, nqubits):
        length = 100

        pl1 = random_pauli_list(num_qubits=nqubits, size=length, phase=True)
        c1 = random_clifford(nqubits)
        pl1.evolve(c1)
    time_evolve_by_clifford.params = [20]


class SparsePauliOpBench:
    params = [50, 100, 150, 200]

    def time_basic_ops(self, nqubits):
        length = 100

        p1 = SparsePauliOp(
            random_pauli_list(num_qubits=nqubits, size=length, phase=True))
        p2 = SparsePauliOp(
            random_pauli_list(num_qubits=nqubits, size=length, phase=True))

        p1.compose(p2)
        p1.tensor(p2)
        p1.simplify()

    def time_conversion(self, nqubits):
        length = 50
        p1 = SparsePauliOp(
            random_pauli_list(num_qubits=nqubits, size=length, phase=True))

        p1.to_list()
        p1.to_operator()
        p1.to_matrix()
    time_conversion.params = [2, 4, 6, 8, 10]
