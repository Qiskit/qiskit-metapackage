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

from qiskit.compiler import transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from .backends.fake_melbourne import FakeMelbourne
import numpy as np
from math import sqrt

# funtion get_grover_circuit
# input:
#     n number of qubit
# return:
#     Grover's Circuit
def get_grover_circuit(n):
    qr = QuantumRegister(n+1) # n qubits with ancilla
    cr = ClassicalRegister(n)
    q = QuantumCircuit(qr,cr)
    q.h(range(n))
    q.barrier(range(n+1))

    # multicontrol preparing
    mct_control = [qr[0]]
    mcz_control = [qr[0]]
    for x in range(1,n):
        mct_control.append(qr[x])
        mcz_control.append(qr[x])
    mcz_control.pop()

    ## marking the target state  |11...1> and amplification
    for x in range( int(sqrt(2 ** n))):
    # put the x gate to the prefer state here
    # in the case that you didn't put anything default case with be |11...1>
    #====== end ========================
        q.mct(mct_control,qr[n],None, mode='noancilla')
    #============== same as the previous section ===========
    #=======================================================
        q.barrier(range(n+1))
    #===== amplification part =============================
        q.h(range(n))
        q.x(range(n))
        q.barrier(range(n+1))
        q.mcrz(np.pi,mcz_control,qr[n-1])
        q.barrier(range(n+1))
        q.x(range(n))
        q.h(range(n))
        q.barrier(range(n+1))
    return q


class GroverBenchmarks:
    params = ([0, 1, 2, 3],[2,3,4,5])
    param_names = ['op_level','n_qubits']
    timeout = 1800 #timeout for benchmarking

    def setup(self, _, n_qubits):
        self.backend = FakeMelbourne()
        self.circuit = get_grover_circuit(n_qubits)

    def time_optimize_level(self, op_level,_): #optimize with
        transpile(self.circuit,self.backend,optimization_level=op_level)
