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

""" Some __repr__ hooks for beauty-printing reports """

from qiskit.qobj import Qobj
from qiskit.providers.aer.noise import NoiseModel


def qobj_repr_hook(self):
    """ This is needed for ASV to beauty-printing reports """
    return "Num. qubits: {0}".format(self.config.n_qubits)


Qobj.__repr__ = qobj_repr_hook


def noise_model_repr_hook(self):
    """ This is needed for ASV to beauty-printing reports """
    return self.__class__.__name__.replace("_", " ").capitalize()


NoiseModel.__repr__ = noise_model_repr_hook
