# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""The qiskit package re-exports the most common and useful interfaces from
terra and aer."""

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from qiskit.terra.circuit import QuantumCircuit
from qiskit.terra.circuit import QuantumRegister
from qiskit.terra.circuit import ClassicalRegister
from qiskit.terra import Aer
from qiskit.terra import IBMQ
from qiskit.terra import QiskitError
from qiskit.terra.tools.compiler import compile
from qiskit.terra.tools.compiler import execute
