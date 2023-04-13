"""Test url_redirects.py."""

from pathlib import Path
from unittest import TestCase

from docs.url_redirects import _redirects_for_aer


class CustomExtensionsTest(TestCase):
    """Test url_redirects.py."""

    def test_redirects_for_aer(self) -> None:
        """Test _redirects_for_aer()."""

        result = _redirects_for_aer()
        num_lines_aer_sources = len(
            Path("docs/aer_sources.txt").read_text(encoding="utf-8").splitlines()
        )
        self.assertEqual(len(result), num_lines_aer_sources * 2)

        # Spot check some redirects.
        self.assertEqual(
            result["stubs/qiskit.providers.aer.AerError.html"],
            "https://qiskit.org/documentation/aer/stubs/qiskit_aer.AerError.html",
        )
        self.assertEqual(
            result["stubs/qiskit_aer.AerError.html"],
            "https://qiskit.org/documentation/aer/stubs/qiskit_aer.AerError.html",
        )
        self.assertEqual(
            result["stubs/qiskit.providers.aer.library.SaveAmplitudes.is_parameterized.html"],
            (
                "https://qiskit.org/documentation/aer/"
                "stubs/qiskit_aer.library.SaveAmplitudes.is_parameterized.html"
            ),
        )
        self.assertEqual(
            result["stubs/qiskit_aer.library.SaveAmplitudes.is_parameterized.html"],
            (
                "https://qiskit.org/documentation/aer/stubs/"
                "qiskit_aer.library.SaveAmplitudes.is_parameterized.html"
            ),
        )

        # Extensions should redirect to the general Aer docs,
        # since the API was removed.
        self.assertEqual(
            result["stubs/qiskit.providers.aer.extensions.Snapshot.html"],
            "https://qiskit.org/documentation/aer",
        )
        self.assertEqual(
            result["stubs/qiskit.providers.aer.extensions.Snapshot.html"],
            "https://qiskit.org/documentation/aer",
        )
