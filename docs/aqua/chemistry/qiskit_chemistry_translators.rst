.. _translators:

===========
Translators
===========

The translation layer in Qiskit Chemistry maps high-level classically generated input
to a qubit operator, which becomes the input to one of Aqua's :ref:`quantum-algorithms`.
As part of this layer, Qiskit Chemistry offers three qubit mapping functions.

.. _jordan-wigner:

-------------
Jordan-Wigner
-------------
The `Jordan-Wigner transformation <https://rd.springer.com/article/10.1007%2FBF01331938>`__,
maps spin operators onto fermionic creation and annihilation operators.
It was proposed by Ernst Pascual Jordan and Eugene Paul Wigner
for one-dimensional lattice models,
but now two-dimensional analogues of the transformation have also been created.
The Jordan–Wigner transformation is often used to exactly solve 1D spin-chains
by transforming the spin operators to fermionic operators and then diagonalizing
in the fermionic basis.

.. _parity:

------
Parity
------

The `parity-mapping transformation <https://arxiv.org/abs/1701.08213>`__.
optimizes encodings of fermionic many-body systems by qubits
in the presence of symmetries.
Such encodings eliminate redundant degrees of freedom in a way that preserves
a simple structure of the system Hamiltonian enabling quantum simulations with fewer qubits.

.. _bravyi-kitaev:

-------------
Bravyi-Kitaev
-------------

Also known as *binary-tree-based qubit mapping*, the `Bravyi-Kitaev transformation
<https://www.sciencedirect.com/science/article/pii/S0003491602962548>`__
is a method of mapping the occupation state of a
fermionic system onto qubits. This transformation maps the Hamiltonian of :math:`n`
interacting fermions to an :math:`\mathcal{O}(\log n)`
local Hamiltonian of :math:`n` qubits.
This is an improvement in locality over the Jordan–Wigner transformation, which results
in an :math:`\mathcal{O}(n)` local qubit Hamiltonian.
The Bravyi–Kitaev transformation was proposed by Sergey B. Bravyi and Alexei Yu. Kitaev.

.. _bravyi-kitaev-superfast:

-----------------------
Bravyi-Kitaev Superfast
-----------------------

Bravyi Kitaev Superfast (BKSF) algorithm `<https://aip.scitation.org/doi/10.1063/1.5019371>` is a mapping from fermionic operators to qubit operators. BKSF algorithm defines an abstract model where the fermionic modes are mapped to vertices of an interaction graph. The edges of the graph correspond to the interaction between the modes. The graph can be constructed from the Hamiltonian. The simulation is done by putting qubits on the edges of the graph. Each fermionic operator costs :math:`\mathcal{O}(d)` qubit operations, where :math:`d` is the degree of the interaction graph. Nonetheless, the number of qubits required are more than the number of fermionic modes.
The BKSF was proposed by Kanav Setia and James D. Whitfield.
