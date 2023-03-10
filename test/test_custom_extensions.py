from pathlib import Path
from unittest import TestCase

from docs.custom_extensions import determine_redirects_for_aer


class CustomExtensionsTest(TestCase):
    def test_determine_redirects_for_aer(self) -> None:
        result = determine_redirects_for_aer()
        num_lines_aer_sources = len(Path("docs/aer_sources.txt").read_text().splitlines())
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
            "https://qiskit.org/documentation/aer/stubs/qiskit_aer.library.SaveAmplitudes.is_parameterized.html",
        )
        self.assertEqual(
            result["stubs/qiskit_aer.library.SaveAmplitudes.is_parameterized.html"],
            "https://qiskit.org/documentation/aer/stubs/qiskit_aer.library.SaveAmplitudes.is_parameterized.html",
        )
