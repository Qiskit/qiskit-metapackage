# -*- coding: utf-8 -*-

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

# pylint: disable=no-member,invalid-name,missing-docstring,no-name-in-module
# pylint: disable=attribute-defined-outside-init,unsubscriptable-object

import os

from qiskit import QuantumCircuit
from qiskit.compiler import transpile


class TranspilerQualitativeBench:
    params = ([0, 1, 2, 3],
              [None, "sabre"])
    param_names = ["optimization level", "routing/layout method"]
    timeout = 600

    # pylint: disable=unused-argument
    def setup(self, optimization_level, routing_method):
        self.rochester_coupling_map = [
            [0, 5],
            [0, 1],
            [1, 2],
            [1, 0],
            [2, 3],
            [2, 1],
            [3, 4],
            [3, 2],
            [4, 6],
            [4, 3],
            [5, 9],
            [5, 0],
            [6, 13],
            [6, 4],
            [7, 16],
            [7, 8],
            [8, 9],
            [8, 7],
            [9, 10],
            [9, 8],
            [9, 5],
            [10, 11],
            [10, 9],
            [11, 17],
            [11, 12],
            [11, 10],
            [12, 13],
            [12, 11],
            [13, 14],
            [13, 12],
            [13, 6],
            [14, 15],
            [14, 13],
            [15, 18],
            [15, 14],
            [16, 19],
            [16, 7],
            [17, 23],
            [17, 11],
            [18, 27],
            [18, 15],
            [19, 20],
            [19, 16],
            [20, 21],
            [20, 19],
            [21, 28],
            [21, 22],
            [21, 20],
            [22, 23],
            [22, 21],
            [23, 24],
            [23, 22],
            [23, 17],
            [24, 25],
            [24, 23],
            [25, 29],
            [25, 26],
            [25, 24],
            [26, 27],
            [26, 25],
            [27, 26],
            [27, 18],
            [28, 32],
            [28, 21],
            [29, 36],
            [29, 25],
            [30, 39],
            [30, 31],
            [31, 32],
            [31, 30],
            [32, 33],
            [32, 31],
            [32, 28],
            [33, 34],
            [33, 32],
            [34, 40],
            [34, 35],
            [34, 33],
            [35, 36],
            [35, 34],
            [36, 37],
            [36, 35],
            [36, 29],
            [37, 38],
            [37, 36],
            [38, 41],
            [38, 37],
            [39, 42],
            [39, 30],
            [40, 46],
            [40, 34],
            [41, 50],
            [41, 38],
            [42, 43],
            [42, 39],
            [43, 44],
            [43, 42],
            [44, 51],
            [44, 45],
            [44, 43],
            [45, 46],
            [45, 44],
            [46, 47],
            [46, 45],
            [46, 40],
            [47, 48],
            [47, 46],
            [48, 52],
            [48, 49],
            [48, 47],
            [49, 50],
            [49, 48],
            [50, 49],
            [50, 41],
            [51, 44],
            [52, 48]]

        self.tokyo_coupling_map = [
            [0, 1], [1, 2], [2, 3], [3, 4],
            [0, 5], [1, 6], [1, 7], [2, 6], [2, 7], [3, 8], [3, 9], [4, 8],
            [4, 9], [5, 6], [6, 7], [7, 8], [8, 9], [5, 10], [5, 11], [6, 10],
            [6, 11], [7, 12], [7, 13], [8, 12], [8, 13], [9, 14], [10, 11],
            [11, 12], [12, 13], [13, 14], [10, 15], [11, 16], [11, 17],
            [12, 16], [12, 17], [13, 18], [13, 19], [14, 18], [14, 19],
            [15, 16], [16, 17], [17, 18], [18, 19]
        ]
        self.sycamore_coupling_map = [
            [0, 6], [1, 6], [1, 7], [2, 7], [2, 8], [3, 8], [3, 9], [4, 9],
            [4, 10], [5, 10], [5, 11], [6, 12], [6, 13], [7, 13], [7, 14],
            [8, 14], [8, 15], [9, 15], [9, 16], [10, 16], [10, 17], [11, 17],
            [12, 18], [13, 18], [13, 19], [14, 19], [14, 20], [15, 20],
            [15, 21], [16, 21], [16, 22], [17, 22], [17, 23], [18, 24],
            [18, 25], [19, 25], [19, 26], [20, 26], [20, 27], [21, 27],
            [21, 28], [22, 28], [22, 29], [23, 29], [24, 30], [25, 30],
            [25, 31], [26, 31], [26, 32], [27, 32], [27, 33], [28, 33],
            [28, 34], [29, 34], [29, 35], [30, 36], [30, 37], [31, 37],
            [31, 38], [32, 38], [32, 39], [33, 39], [33, 40], [34, 40],
            [34, 41], [35, 41], [36, 42], [37, 42], [37, 43], [38, 43],
            [38, 44], [39, 44], [39, 45], [40, 45], [40, 46], [41, 46],
            [41, 47], [42, 48], [42, 49], [43, 49], [43, 50], [44, 50],
            [44, 51], [45, 51], [45, 52], [46, 52], [46, 53], [47, 53]
        ]
        self.basis_gates = ["id", "rz", "sx", "x", "cx"]
        self.qasm_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "qasm"))

        self.bigd = QuantumCircuit.from_qasm_file(
            os.path.join(self.qasm_path, "20QBT_45CYC_.0D1_.1D2_3.qasm"))
        self.bss = QuantumCircuit.from_qasm_file(
            os.path.join(self.qasm_path, "53QBT_100CYC_QSE_3.qasm"))
        self.bntf = QuantumCircuit.from_qasm_file(
            os.path.join(self.qasm_path, "54QBT_25CYC_QSE_3.qasm"))

    def track_depth_bntf_optimal_depth_25(self, optimization_level,
                                          routing_method):
        return transpile(self.bntf, coupling_map=self.sycamore_coupling_map,
                         basis_gates=self.basis_gates,
                         routing_method=routing_method,
                         layout_method=routing_method,
                         optimization_level=optimization_level,
                         seed_transpiler=0).depth()

    def track_depth_bss_optimal_depth_100(self, optimization_level,
                                          routing_method):
        return transpile(self.bss, coupling_map=self.rochester_coupling_map,
                         basis_gates=self.basis_gates,
                         routing_method=routing_method,
                         layout_method=routing_method,
                         optimization_level=optimization_level,
                         seed_transpiler=0).depth()

    def track_depth_bigd_optimal_depth_45(self, optimization_level,
                                          routing_method):
        return transpile(self.bigd, coupling_map=self.tokyo_coupling_map,
                         basis_gates=self.basis_gates,
                         routing_method=routing_method,
                         layout_method=routing_method,
                         optimization_level=optimization_level,
                         seed_transpiler=0).depth()

    def time_transpile_bntf(self, optimization_level, routing_method):
        transpile(self.bntf, coupling_map=self.sycamore_coupling_map,
                  basis_gates=self.basis_gates,
                  routing_method=routing_method,
                  layout_method=routing_method,
                  optimization_level=optimization_level,
                  seed_transpiler=0).depth()

    def time_transpile_bss(self, optimization_level, routing_method):
        transpile(self.bss, coupling_map=self.rochester_coupling_map,
                  basis_gates=self.basis_gates,
                  routing_method=routing_method,
                  layout_method=routing_method,
                  optimization_level=optimization_level,
                  seed_transpiler=0).depth()

    def time_transpile_bigd(self, optimization_level, routing_method):
        transpile(self.bigd, coupling_map=self.tokyo_coupling_map,
                  basis_gates=self.basis_gates,
                  routing_method=routing_method,
                  layout_method=routing_method,
                  optimization_level=optimization_level,
                  seed_transpiler=0).depth()
