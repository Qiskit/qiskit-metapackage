# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""Tests for metapackage"""

import qiskit

from .base import QiskitTestCase


class TestMetaPackage(QiskitTestCase):
    """Tests for metapackage"""

    def test_aer_import_works(self):
        """Test importing Aer"""
        self.assertIsNotNone(qiskit.Aer)
