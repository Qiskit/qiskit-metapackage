###############
Release History
###############

*************
Release Notes
*************

======================
Qiskit Chemistry 0.4.0
======================

In the `Qiskit <https://qiskit.org/>`__ ecosystem,
`Aqua <https://qiskit.org/aqua>`__ is the
`element <https://medium.com/qiskit/qiskit-and-its-fundamental-elements-bcd7ead80492>`__
that encompasses cross-domain quantum algorithms and applications
running on `Noisy Intermediate-Scale Quantum
(NISQ) <https://arxiv.org/abs/1801.00862>`__ computers. Aqua is an
open-source library completely written in Python and specifically
designed to be modular and extensible at multiple levels. Currently,
Aqua supports four applications, in domains that have long been
identified as potential areas for quantum computing: Chemistry,
Artificial Intelligence (AI), Optimization, and Finance.

In this release of Qiskit Chemistry,
we have added the following new features :

- Compatibility with Aqua 0.4
- Compatibility with Terra 0.7
- Compatibility with Aer 0.1
- Programmatic APIs for algorithms and components -- each component can now be instantiated and
  initialized via a single (non-empty) constructor call ``QuantumInstance`` API for
  algorithm/backend decoupling -- ``QuantumInstance`` encapsulates a backend and its settings
- Updated documentation and Jupyter Notebooks illustrating the new programmatic APIs
- ``HartreeFock`` component of pluggable type ``InitialState`` moved from Qiskit Aqua to Qiskit
  Chemistry registers itself at installation time as Aqua algorithmic components for use at run
  time
- ``UCCSD`` component of pluggable type ``VariationalForm`` moved from Qiskit Aqua to Qiskit
  Chemistry registers itself at installation time as Aqua algorithmic components for use at run
  time
- Z-matrix support for the PySCF & PyQuante classical computational chemistry drivers

--------------------------------------------------
Compatibility with Aqua 0.4, Terra 0.7 and Aer 0.1
--------------------------------------------------

Qiskit Chemistry 0.4 is fully compatible with Qiskit Aqua, 0.4,
Qiskit Terra, 0.7, and the newly released Qiskit Aer 0.1. This allows you to
install and execute Qiskit Chemistry in the same Python environment as all the other
Qiskit elements and components.

Specifically, Qiskit Chemistry can now use the enhanced programmatic APIs
from Qiskit Aqua 0.4 along with the algorithm/backend decoupling logic.

The following Qiskit Chemistry program shows how to conduct a chemistry experiment using
Aqua's improved programmatic interface:

.. code-block:: python

    from qiskit_chemistry import FermionicOperator
    from qiskit_chemistry.drivers import PySCFDriver, UnitsType

    # Use PySCF, a classical computational chemistry software package, to compute the one-body and two-body integrals in
    # molecular-orbital basis, necessary to form the Fermionic operator
    driver = PySCFDriver(atom='H .0 .0 .0; H .0 .0 0.735',
                        unit=UnitsType.ANGSTROM,
                        basis='sto3g')
    molecule = driver.run()
    num_particles = molecule.num_alpha + molecule.num_beta
    num_spin_orbitals = molecule.num_orbitals * 2

    # Build the qubit operator, which is the input to the VQE algorithm in Aqua
    ferOp = FermionicOperator(h1=molecule.one_body_integrals, h2=molecule.two_body_integrals)
    map_type = 'PARITY'
    qubitOp = ferOp.mapping(map_type)
    qubitOp = qubitOp.two_qubit_reduced_operator(num_particles)
    num_qubits = qubitOp.num_qubits

    # set the backend for the quantum computation
    from qiskit import Aer
    backend = Aer.get_backend('statevector_simulator')

    # setup a classical optimizer for VQE
    from qiskit_aqua.components.optimizers import L_BFGS_B
    optimizer = L_BFGS_B()

    # setup the initial state for the variational form
    from qiskit_chemistry.aqua_extensions.components.initial_states import HartreeFock
    init_state = HartreeFock(num_qubits, num_spin_orbitals, num_particles)

    # setup the variational form for VQE
    from qiskit_aqua.components.variational_forms import RYRZ
    var_form = RYRZ(num_qubits, initial_state=init_state)

    # setup and run VQE
    from qiskit_aqua.algorithms import VQE
    algorithm = VQE(qubitOp, var_form, optimizer)
    result = algorithm.run(backend)
    print(result['energy'])

Specifically, the program above uses a quantum computer to calculate
the ground state energy of molecular Hydrogen, H2, where the two atoms
are configured to be at a distance of 0.735 angstroms. The molecular
configuration input is generated using
`PySCF <https://sunqm.github.io/pyscf/>`__, a standard classical
computational chemistry software package. First, Aqua transparently
executes PySCF, and extracts from it the one- and two-body
molecular-orbital integrals; an inexpensive operation that scales well
classically and does not require the use of a quantum computer. These
integrals are then used to create a quantum fermionic-operator
representation of the molecule. In this specific example, we use a
parity mapping to generate a qubit operator from the fermionic one, with
a unique precision-preserving optimization that allows for two qubits to
be tapered off; a reduction in complexity that is particularly
advantageous for NISQ computers. The qubit operator is then passed as an
input to the `Variational Quantum Eigensolver
(VQE) <https://www.nature.com/articles/ncomms5213>`__ algorithm,
instantiated with a `Limited-memory Broyden-Fletcher-Goldfarb-Shanno
Bound
(L-BFGS-B) <http://www.ece.northwestern.edu/~nocedal/PSfiles/limited-memory.ps.gz>`__
classical optimizer and the `RyRz variational
form <https://qiskit.org/documentation/aqua/variational_forms.html#ryrz>`__.
The `Hartree-Fock
state <https://qiskit.org/documentation/aqua/initial_states.html#id2>`__
is utilized to initialize the variational form.

This example emphasizes the use of Aqua's improved programmatic
interface by illustrating how the VQE ``QuantumAlgorithm``, along with its
supporting components—-consisting of the L-BFGS-B ``Optimizer``, RyRz
``VariationalForm``, and Hartree-Fock ``InitialState``-—are all instantiated and
initialized via simple constructor calls. The Aer statevector simulator
backend is passed as a parameter to the run method of the VQE algorithm
object, which means that the backend will be executed with default
parameters.

To customize the backend, you can wrap it into a ``QuantumInstance`` object,
and then pass that object to the run method of the ``QuantumAlgorithm``, as
explained above. The ``QuantumInstance`` API allows you to customize
run-time properties of the backend, such as the number of shots, the
maximum number of credits to use, a dictionary with the configuration
settings for the simulator, a dictionary with the initial layout of
qubits in the mapping, and the Terra ``PassManager`` that will handle the
compilation of the circuits. For the full set of options, please refer
to the documentation of the Aqua ``QuantumInstance`` API.

Numerous new Qiskit Chemistry notebooks in the
`qiskit/aqua <https://github.com/Qiskit/qiskit-tutorials/tree/master/qiskit/aqua>`__
and
`community/aqua <https://github.com/Qiskit/qiskit-tutorials/tree/master/community/aqua>`__
folders of the `Qiskit
Tutorials <https://github.com/Qiskit/qiskit-tutorials>`__ repository
illustrate how to conduct a quantum-computing experiment
programmatically using the new Aqua APIs.

-----------------------------------------
Chemistry-Specific Algorithmic Components
-----------------------------------------

The support of Aqua for Chemistry continues to be very advanced. Aqua
now features a new mechanism allowing pluggable components to register
themselves to Aqua even without being part of the original Aqua
installation package or installation directory. A component that has
registered itself to Aqua is dynamically loaded and made available at
run time to any program executed on top of Aqua. Taking advantage of
this feature, we have remodeled the boundary between Qiskit Aqua and its
Chemistry application. For example, the code for the `Unitary Coupled
Cluster Singles and Doubles
(UCCSD) <https://arxiv.org/abs/1805.04340>`__ variational form and
Hartree-Fock initial state has been made part of the Qiskit Chemistry
project to reflect the fact that these components are chemistry-specific
and unlikely to make sense in any non-chemistry setting.
The programming example above shows how to import and use the ``HartreeFock``
``InitialState`` from Qiskit Chemistry (as opposed to importing it from
Qiskit Aqua as was done in previous versions).

---------------------------------------
Z-matrix Support for PySCF and PyQuante
---------------------------------------

We have also improved the way molecular configurations are input into
Qiskit Chemistry. Specifically, Qiskit Chemistry interfaces four
classical computational-chemistry software packages: `Gaussian™
16, <http://gaussian.com/gaussian16/>`__
`PSI4, <http://www.psicode.org/>`__
`PySCF <https://github.com/sunqm/pyscf>`__ and
`PyQuante <https://github.com/rpmuller/pyquante2/>`__. Qiskit Chemistry
is unique in the fact that it allows the end user to configure chemistry
experiments using these classical software packages as the front end,
without imposing any new programming language of APIs. Qiskit Chemistry
then executes these software packages classically to compute some
preliminary data necessary to form the input to the underlying quantum
algorithms in Aqua. Directly exposing to the end user classical
computational software input parameters maximizes the functionality
available to the underlying quantum algorithms. In this release, we have
unified some advanced configuration features across the various drivers
currently supported by Qiskit Chemistry. For example, while all the
supported drivers allow the user to configure a molecule's geometry by
specifying the *x*, *y* and *z* coordinates of each atom in the
molecule, only Gaussian™ 16 and PSI4 allow the end user to enter a
molecule's configuration in
`Z-matrix <https://en.wikipedia.org/wiki/Z-matrix_%28chemistry%29>`__
format, which consists of describing each atom in a molecule in terms of
its atomic number, bond length, bond angle, and *dihedral angle* (the
angle between planes through two sets of three atoms having two atoms in
common). A Z-matrix configuration assigns the second atom of a molecule along the *z*
axis from the first atom, which is assumed to be at the origin. This
representation is very intuitive and convenient, especially when the
position and orientation in space of a molecule are irrelevant. Starting
from V0.4, Qiskit Chemistry allows the configuration of a molecule to be
entered in Z-matrix format even when the user has chosen PySCF or
PyQuante as the classical computational chemistry software driver
interfaced by Qiskit Chemistry. Qiskit Chemistry uses the APIs of the underlying
drivers to transparently convert any Z-matrix configuration entered by the user to the
corresponding Cartesian coordinates.  Molecules with a linear segment of 3 connected
atoms or more are not yet covered by this new feature.
