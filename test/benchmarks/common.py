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

# pylint: disable=invalid-name,no-member

"""Benchmark utility functions."""
import math
import numpy as np
from qiskit.quantum_info.random import random_unitary
from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit import Reset
from qiskit.quantum_info.synthesis import two_qubit_cnot_decompose
from qiskit.extensions import (IdGate, U1Gate, U2Gate, U3Gate, XGate,
                               YGate, ZGate, HGate, SGate, SdgGate, TGate,
                               TdgGate, RXGate, RYGate, RZGate, CnotGate,
                               CyGate, CzGate, CHGate, CrzGate, Cu1Gate,
                               Cu3Gate, SwapGate, RZZGate,
                               ToffoliGate, FredkinGate)
from qiskit.providers.aer.noise import NoiseModel
from qiskit.providers.aer.noise.errors import depolarizing_error
from qiskit.providers.aer.noise.errors import amplitude_damping_error
from qiskit.providers.aer.noise.errors import thermal_relaxation_error
import qiskit.ignis.verification.randomized_benchmarking as rb


def add_measurements(circuit, qr_or_width):
    """
    Helper function to add measurements operations to the circuit passed
    by parameter.

    Args:
        circuit (QuantumCircuit): The circuit to add parameters to
        qr_or_width (QuantumRegister or int): The QuantumRegister of the
            circuit or the size of the quatum register

    Returns:
        QuantumCircuit: The same input quantum circuit with the added
                        measurements operations at the end of the circuit
    """
    if isinstance(qr_or_width, QuantumRegister):
        cr = ClassicalRegister(qr_or_width.size)
    else:
        cr = qr_or_width
    meas = QuantumCircuit(qr_or_width, cr)
    meas.measure_all()
    return circuit + meas


def build_random_circuit(n_qubits, depth, max_operands=3, measure=False,
                         conditional=False, reset=False, seed=None):
    """Generate random circuit of arbitrary size and form.

    Args:
        n_qubits (int): number of quantum wires
        depth (int): layers of operations (i.e. critical path length)
        max_operands (int): maximum operands of each gate (between 1 and 3)
        measure (bool): if True, measure all qubits at the end
        conditional (bool): if True, insert middle measurements and
            conditionals
        reset (bool): if True, insert middle resets
        seed (int): sets random seed (optional)

    Returns:
        QuantumCircuit: constructed circuit

    Raises:
        Exception: when invalid options given
    """
    if max_operands < 1 or max_operands > 3:
        raise Exception("max_operands must be between 1 and 3")

    one_q_ops = [IdGate, U1Gate, U2Gate, U3Gate, XGate, YGate, ZGate,
                 HGate, SGate, SdgGate, TGate, TdgGate, RXGate, RYGate, RZGate]
    one_param = [U1Gate, RXGate, RYGate, RZGate, RZZGate, Cu1Gate, CrzGate]
    two_param = [U2Gate]
    three_param = [U3Gate, Cu3Gate]
    two_q_ops = [CnotGate, CyGate, CzGate, CHGate, CrzGate,
                 Cu1Gate, Cu3Gate, SwapGate, RZZGate]
    three_q_ops = [ToffoliGate, FredkinGate]

    qr = QuantumRegister(n_qubits, 'q')
    qc = QuantumCircuit(n_qubits)

    if measure or conditional:
        cr = ClassicalRegister(n_qubits, 'c')
        qc.add_register(cr)

    if reset:
        one_q_ops += [Reset]

    if seed is None:
        seed = np.random.randint(0, np.iinfo(np.int32).max)
    rng = np.random.RandomState(seed)

    # apply arbitrary random operations at every depth
    for _ in range(depth):
        # choose either 1, 2, or 3 qubits for the operation
        remaining_qubits = list(range(n_qubits))
        while remaining_qubits:
            max_possible_operands = min(len(remaining_qubits), max_operands)
            num_operands = rng.choice(range(max_possible_operands)) + 1
            rng.shuffle(remaining_qubits)
            operands = remaining_qubits[:num_operands]
            remaining_qubits = [
                q for q in remaining_qubits if q not in operands]
            if num_operands == 1:
                operation = rng.choice(one_q_ops)
            elif num_operands == 2:
                operation = rng.choice(two_q_ops)
            elif num_operands == 3:
                operation = rng.choice(three_q_ops)
            if operation in one_param:
                num_angles = 1
            elif operation in two_param:
                num_angles = 2
            elif operation in three_param:
                num_angles = 3
            else:
                num_angles = 0
            angles = [rng.uniform(0, 2*np.pi) for x in range(num_angles)]
            register_operands = [qr[i] for i in operands]
            op = operation(*angles)

            # with some low probability, condition on classical bit values
            if conditional and rng.choice(range(10)) == 0:
                value = rng.randint(0, np.power(2, n_qubits))
                op.condition = (cr, value)

            qc.append(op, register_operands)

    if measure:
        qc.measure(qr, cr)

    return qc


def build_quantum_volume_circuit(width, depth, seed=None, measure=False):
    """
    The model circuits consist of layers of Haar random
    elements of SU(4) applied between corresponding pairs
    of qubits in a random bipartition.
    """
    np.random.seed(seed)
    circuit = QuantumCircuit(width)
    # For each layer
    for _ in range(depth):
        # Generate uniformly random permutation Pj of [0...n-1]
        perm = np.random.permutation(width)
        # For each pair p in Pj, generate Haar random SU(4)
        for k in range(int(np.floor(width/2))):
            U = random_unitary(4)
            pair = int(perm[2*k]), int(perm[2*k+1])
            circuit.append(U, [pair[0], pair[1]])

    if measure is True:
        circuit = add_measurements(circuit, width)

    return circuit


def build_ripple_adder_circuit(size):
    """
    Builds a ripple adder of a given size.
    """
    n = size
    a = QuantumRegister(n, "a")
    b = QuantumRegister(n, "b")
    cin = QuantumRegister(1, "cin")
    cout = QuantumRegister(1, "cout")
    ans = ClassicalRegister(n+1, "ans")
    qc = QuantumCircuit(a, b, cin, cout, ans, name="rippleadd")

    def majority(p, a, b, c):
        """Majority gate."""
        p.cx(c, b)
        p.cx(c, a)
        p.ccx(a, b, c)

    def unmajority(p, a, b, c):
        """Unmajoritygate."""
        p.ccx(a, b, c)
        p.cx(c, a)
        p.cx(a, b)

    # Build a temporary subcircuitthat adds a to b,
    # storing the result in b
    adder_subcircuit = QuantumCircuit(cin, a, b, cout)
    majority(adder_subcircuit, cin[0], b[0], a[0])
    for j in range(n - 1):
        majority(adder_subcircuit, a[j], b[j + 1], a[j + 1])

    adder_subcircuit.cx(a[n - 1], cout[0])

    for j in reversed(range(n - 1)):
        unmajority(adder_subcircuit, a[j], b[j + 1], a[j + 1])
        unmajority(adder_subcircuit, cin[0], b[0], a[0])

    # Set the inputs to the adder
    qc.x(a[0])  # Set input a = 0...0001
    qc.x(b)   # Set input b = 1...1111
    # Apply the adder
    qc += adder_subcircuit

    # Measure the output register in the computational basis
    for j in range(n):
        qc.measure(b[j], ans[j])
    qc.measure(cout[0], ans[n])

    return qc


class NoiseWithDescription:
    """
    This is just a wrapper for adding a descriptive text to the noise model
    so ASV can print this text in its reports
    """
    def __init__(self, noise_model, description):
        self._noise_model = noise_model
        self._description = description

    def __repr__(self):
        return self._description

    def __call__(self):
        return self._noise_model


def no_noise():
    """ No noise at all """
    return NoiseWithDescription(None, "No Noise")


def mixed_unitary_noise_model():
    """Return test rest mixed unitary noise model"""
    noise_model = NoiseModel()
    error1 = depolarizing_error(0.1, 1)
    noise_model.add_all_qubit_quantum_error(error1, ['u1', 'u2', 'u3'])
    error2 = depolarizing_error(0.1, 2)
    noise_model.add_all_qubit_quantum_error(error2, ['cx'])
    return NoiseWithDescription(noise_model, "Mixed Unitary Noise")


def reset_noise_model():
    """Return test reset noise model"""
    noise_model = NoiseModel()
    error1 = thermal_relaxation_error(50, 50, 0.1)
    noise_model.add_all_qubit_quantum_error(error1, ['u1', 'u2', 'u3'])
    error2 = error1.tensor(error1)
    noise_model.add_all_qubit_quantum_error(error2, ['cx'])
    return NoiseWithDescription(noise_model, "Reset Noise")


def kraus_noise_model():
    """Return test Kraus noise model"""
    noise_model = NoiseModel()
    error1 = amplitude_damping_error(0.1)
    noise_model.add_all_qubit_quantum_error(error1, ['u1', 'u2', 'u3'])
    error2 = error1.tensor(error1)
    noise_model.add_all_qubit_quantum_error(error2, ['cx'])
    return NoiseWithDescription(noise_model, "Kraus Noise")


def build_qft_circuit(num_qubits, circuit=None, use_cu1=True, measure=False):
    """Create quantum fourier transform circuit on quantum register qreg."""
    qreg = QuantumRegister(num_qubits, "qr")
    if circuit is None:
        circuit = QuantumCircuit(qreg, name="qft")

    n = len(qreg)

    for i in range(n):
        for j in range(i):
            theta = math.pi/float(2**(i-j))
            if use_cu1 is True:
                circuit.cu1(theta, qreg[i], qreg[j])
            else:
                circuit.u1(theta/2, qreg[i])
                circuit.cx(qreg[i], qreg[j])
                circuit.u1(-theta/2, qreg[j])
                circuit.cx(qreg[i], qreg[j])
                circuit.u1(theta/2, qreg[j])
        circuit.h(qreg[i])

    if measure is True:
        circuit = add_measurements(circuit, qreg)

    return circuit


def build_simple_u3_circuit(num_qubits, measure=True):
    """Creates a simple circuit composed by u3 gates, with measurements or not
    at the end of each qubit.

    Args:
        num_qubits (int): Number of qubits
        measure (bool): Add measurements at the end of each qubit

    Returns:
        QuantumCircuit: The simple quantum circuit
    """
    qr = QuantumRegister(num_qubits)
    circuit = QuantumCircuit(qr)
    for i in range(num_qubits):
        circuit.u3(1.1, 2.2, 3.3, qr[i])

    if measure:
        circuit = add_measurements(circuit, qr)
    return circuit


def build_simple_cnot_circuit(num_qubits, measure=True):
    """Creates a simple circuit composed by cnot gates, with measurements or
    not at the end of each qubit.

    Args:
        num_qubits (int): Number of qubits
        measure (bool): Add measurements at the end of each qubit

    Returns:
        QuantumCircuit: The simple quantum circuit
    """
    qr = QuantumRegister(num_qubits)
    circuit = QuantumCircuit(qr)
    for i in range(num_qubits):
        # for the last qubit, we exchange control and target qubits
        target_qubit = i + 1 if num_qubits - 1 > i else i - 1
        circuit.cx(qr[i], qr[target_qubit])

    if measure:
        circuit = add_measurements(circuit, qr)
    return circuit


def build_randomized_benchmark_circuit(nseeds=1, length_vector=None,
                                       rb_pattern=None, length_multiplier=1,
                                       seed_offset=0, align_cliffs=False,
                                       seed=None):
    """
    Randomized Benchmarking sequences.
    """
    if not seed:
        np.random.seed(10)
    else:
        np.random.seed(seed)
    rb_opts = {}
    rb_opts['nseeds'] = nseeds
    rb_opts['length_vector'] = length_vector
    rb_opts['rb_pattern'] = rb_pattern
    rb_opts['length_multiplier'] = length_multiplier
    rb_opts['seed_offset'] = seed_offset
    rb_opts['align_cliffs'] = align_cliffs

    # Generate the sequences
    try:
        rb_circs, _ = rb.randomized_benchmarking_seq(**rb_opts)
    except OSError:
        skip_msg = ('Skipping tests because '
                    'tables are missing')
        raise NotImplementedError(skip_msg)
    all_circuits = []
    for seq in rb_circs:
        all_circuits += seq
    return all_circuits


def build_quantum_volume_kak_circuit(width, depth, seed=None):
    """Create quantum volume model circuit on quantum register qreg of given
    depth (default depth is equal to width) and random seed.
    The model circuits consist of layers of Haar random
    elements of U(4) applied between corresponding pairs
    of qubits in a random bipartition.
    """
    qreg = QuantumRegister(width)
    depth = depth or width

    np.random.seed(seed)
    circuit = QuantumCircuit(qreg, name="Qvolume: %s by %s, seed: %s" %
                             (width, depth, seed))

    for _ in range(depth):
        # Generate uniformly random permutation Pj of [0...n-1]
        perm = np.random.permutation(width)

        # For each pair p in Pj, generate Haar random U(4)
        # Decompose each U(4) into CNOT + SU(2)
        for k in range(width // 2):
            U = random_unitary(4, seed).data
            for gate in two_qubit_cnot_decompose(U):
                qs = [qreg[int(perm[2 * k + i.index])] for i in gate[1]]
                pars = gate[0].params
                name = gate[0].name
                if name == "cx":
                    circuit.cx(qs[0], qs[1])
                elif name == "u1":
                    circuit.u1(pars[0], qs[0])
                elif name == "u2":
                    circuit.u2(*pars[:2], qs[0])
                elif name == "u3":
                    circuit.u3(*pars[:3], qs[0])
                elif name == "id":
                    pass  # do nothing
                else:
                    raise Exception("Unexpected gate name: %s" % name)
    return circuit
