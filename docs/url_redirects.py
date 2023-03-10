# This code is part of Qiskit.
#
# (C) Copyright IBM 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Redirects of old pages to new pages.

See https://documatt.gitlab.io/sphinx-reredirects/usage.html for how this works.
"""

from pathlib import Path
from typing import Dict


def determine_redirects() -> Dict[str, str]:
    return {
        "install": "getting_started.html",
        **_redirects_for_tutorials(),
        **_redirects_for_aer(),
    }


_optimization_tutorials = [
    '1_quadratic_program',
    '2_converters_for_quadratic_programs',
    '3_minimum_eigen_optimizer',
    '4_grover_optimizer',
    '5_admm_optimizer',
    '6_examples_max_cut_and_tsp',
    '7_examples_vehicle_routing',
    '8_cvar_optimization',
    'index.html'
]

_finance_tutorials = [
    '01_portfolio_optimization',
    '02_portfolio_diversification',
    '03_european_call_option_pricing',
    '04_european_put_option_pricing',
    '05_bull_spread_pricing',
    '06_basket_option_pricing',
    '07_asian_barrier_spread_pricing',
    '08_fixed_income_pricing',
    '09_credit_risk_analysis',
    '10_qgan_option_pricing',
    '11_time_series',
    'index'
]

_chemistry_tutorials = [
    '01_electronic_structure',
    '02_vibronic_structure',
    '03_ground_state_solvers',
    '04_excited_states_solvers',
    '05_Sampling_potential_energy_surfaces',
    '06_calculating_thermodynamic_observables',
    'index'
]

_ml_tutorials = [
    '01_qsvm_classification',
    '02_qsvm_multiclass',
    '03_vqc',
    '04_qgans_for_loading_random_distributions',
    'index'
]

_dynamics_tutorials = [
    "09_pulse_simulator_duffing_model",
    "10_pulse_simulator_backend_model",
]

_experiments_tutorials = [
    "1_hamiltonian_and_gate_characterization",
    "2_relaxation_and_decoherence",
    "3_measurement_error_mitigation",
    "4_randomized_benchmarking",
    "5_quantum_volume",
    "6_repetition_code",
    "7_accreditation",
    "8_tomography",
    "9_entanglement_verification",
    "index",
]


def _redirects_for_tutorials() -> Dict[str, str]:
    result = {}
    for tutorial in _optimization_tutorials:
        result[
            'tutorials/optimization/%s' % tutorial] = "https://qiskit.org/documentation/optimization/tutorials/index.html"
    for tutorial in _finance_tutorials:
        result[
            'tutorials/finance/%s' % tutorial] = "https://qiskit.org/documentation/finance/tutorials/index.html"
    for tutorial in _chemistry_tutorials:
        result[
            "tutorials/chemistry/%s" % tutorial] = "https://qiskit.org/documentation/nature/tutorials/index.html"
    for tutorial in _ml_tutorials:
        result[
            "tutorials/machine_learning/%s" % tutorial] = "https://qiskit.org/documentation/machine-learning/tutorials/index.html"
    for tutorial in _dynamics_tutorials:
        result[
            "tutorials/circuits_advanced/%s" % tutorial] = "https://qiskit.org/documentation/dynamics/tutorials/index.html"
    for tutorial in _experiments_tutorials:
        result[
            "tutorials/noise/%s" % tutorial] = "https://qiskit.org/documentation/experiments/tutorials/index.html"
    return result


def _redirects_for_aer() -> Dict[str, str]:
    """Set up URL redirects for Aer.

    We've gone through two migrations with Aer:

        1) From `qiskit.org/documentation/stubs/qiskit.providers.aer` to
           `qiskit.org/documentation/stubs/qiskit_aer`.
        2) From `qiskit.org/documentation/stubs/qiskit_aer` to
          `qiskit.org/documentation/aer/stubs/qiskit_aer`.
    """
    result = {}
    original_sources = (Path(__file__).parent / "aer_sources.txt").read_text()
    for original_provider_html_file_path in original_sources.splitlines():
        qiskit_aer_html_file_path = original_provider_html_file_path.replace(
            "qiskit.providers.aer", "qiskit_aer"
        )
        new_url = (
            "https://qiskit.org/documentation/aer"
            if ".extensions." in original_provider_html_file_path
            else f"https://qiskit.org/documentation/aer/{qiskit_aer_html_file_path}"
        )
        result.update(
            {
                original_provider_html_file_path: new_url,
                qiskit_aer_html_file_path: new_url,
            }
        )
    return result
