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
    decompose_clifford, random_pauli, Pauli, PauliList
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
    def time_basic_ops(self):
        nqubits = 500
        iterations = 300
        for _ in range(0, iterations):
            p1 = random_pauli(nqubits, True)
            # Going through a different initialization path
            p2 = Pauli(random_pauli(nqubits, True).to_label())

            p1.compose(p2)
            p1.evolve(p2)  # by another Pauli, so by composition
            p1.commutes(p2)
            p1.anticommutes(p2)
            p1.to_instruction()

    def time_evolve_by_clifford(self):
        nqubits = 20
        iterations = 10
        for _ in range(0, iterations):
            p1 = random_pauli(nqubits, True)
            c1 = random_clifford(nqubits)
            p1.evolve(c1)


class PauliListBench:
    def time_basic_ops(self):
        nqubits = 500
        length = 500

        pl1 = PauliList([random_pauli(nqubits, True)
                         for _ in range(0, length)])
        pl2 = PauliList(
            [random_pauli(nqubits, True).to_label() for _ in range(0, length)])

        pl1.commutes(pl2)
        pl1.commutes_with_all(pl2)
        pl1.argsort()
        pl1.compose(pl2)

    def time_basic_op_with_qargs(self):
        length = 500
        nqubits = 1000
        half_qubits = int(nqubits/2)

        pl1 = PauliList([random_pauli(nqubits, True)
                         for _ in range(0, length)])
        pl2 = PauliList(
            [random_pauli(half_qubits, True) for _ in range(0, length)])

        qargs = [random.randint(0, nqubits - 1) for _ in range(half_qubits)]
        pl1.commutes(pl2, qargs)
        pl1.compose(pl2, qargs)

    def time_evolve_by_clifford(self):
        nqubits = 20
        length = 100

        pl1 = PauliList([random_pauli(nqubits, True)
                         for _ in range(0, length)])
        c1 = random_clifford(nqubits)
        pl1.evolve(c1)
