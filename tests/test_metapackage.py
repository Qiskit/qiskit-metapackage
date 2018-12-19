# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import qiskit

from .base import TestCase


class TestMetaPackage(TestCase):

    def test_Aer_import_works(self):
        self.assertIsNotNone(qiskit.Aer)
