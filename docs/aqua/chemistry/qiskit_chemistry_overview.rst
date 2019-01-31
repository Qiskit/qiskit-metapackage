.. _aqua-chemistry-overview:

========
Overview
========

Qiskit Chemistry is a set of tools and algorithms that enable experimenting with chemistry problems
via quantum computing. Qiskit Chemistry translates chemistry-specific problems
into inputs for an algorithm from the Aqua :ref:`quantum-algorithms` library,
which in turn uses `Qiskit Terra <https://qiskit.org/terra>`__ for the actual
quantum computation.

Qiskit Chemistry allows users with different levels of experience to execute
chemistry experiments and contribute to the quantum computing chemistry
software stack. Users with pure chemistry background can continue to configure
chemistry problems according to their favorite computational chemistry software
packages, called *drivers*. These users do not need to learn the details of
quantum computing; Qiskit Chemistry translates any chemistry program
configuration entered by those users in one of their favorite drivers into
quantum-specific input. For these to work, the following simple requirements
must be met:

- The driver chosen by the user should be installed on the same system in which
  Qiskit Chemistry is also installed.
- The appropriate software license for that driver must be in place.
- An interface to that driver must be built in Qiskit Chemistry as a ``BaseDriver`` extension
  point.

Currently, Qiskit Chemistry comes with interfaces prebuilt
for the following four computational chemistry software drivers:

1. :ref:`gaussian-16`, a commercial chemistry program
2. :ref:`psi4`, an open-source chemistry program built on Python
3. :ref:`pyscf`, an open-source Python chemistry program
4. :ref:`pyquante`, a pure Python cross-platform open-source chemistry program

Additional chemistry drivers can easily be added via the ``BaseDriver``
extension point. Once an interface for a driver installed in the system has
been implemented, that driver will be automatically loaded at run time
and made available in Qiskit Quantum Chemistry for running experiments.

Once Qiskit Chemistry has been installed, a user can execute chemistry
experiments on a quantum machine by using either the
:ref:`qiskit-chemistry-gui` or :ref:`qiskit-chemistry-command-line` supplied
tools, or the :ref:`qiskit-chemistry-programmable-interface`. Either option
enforces schema-based configuration correctness.

.. topic:: Contributing to Qiskit Chemistry

    Instead of just *accessing* Qiskit Chemistry as a tool to experiment with chemistry problems
    on a quantum machine, a user may decide to *contribute* to Qiskit Chemistry by
    providing new algorithms, algorithm components, input translators, and driver interfaces.
    Algorithms and supporting components may be programmatically added to
    :ref:`aqua-library`, which was designed as an extensible, pluggable
    framework in order to address the needs of research and developers interested in
    :ref:`aqua-extending`.
    Qiskit Chemistry utilizes a similar framework for drivers and the core computation
    performed at the input-translation layer.

    If you would like to contribute to Qiskit Chemistry, please follow the
    Qiskit Chemistry `contribution
    guidelines <https://github.com/Qiskit/qiskit-chemistry/blob/master/.github/CONTRIBUTING.rst>`__.


----------------------------
Modularity and Extensibility
----------------------------

Qiskit Chemistry is built on top of :ref:`aqua-library`.  Just like Aqua,
it is specifically designed to be extensible at each level of the software stack.
This allows different users with different levels of expertise and different scientific
interests to contribute to, and extend, the Qiskit Chemistry software stack at different levels.
In addition to the extension points offered by the underlying Aqua library, Qiskit Chemistry
allows a user to plug in new algorithms and new operators for translating classical inputs
into inputs for quantum algorithms.

~~~~~~~~~~~~~~~~
Input Generation
~~~~~~~~~~~~~~~~

At the application level, Aqua allows for classical computational
software to be used as the quantum application front end.  This module is extensible;
new computational software can be easily plugged in.  Behind the scenes, Aqua lets that
software perform some initial computations classically.  The  results of those computations are
then combined with the problem configuration and translated into input for one or more quantum
algorithms, which invoke the Qiskit code Application Programming Interfaces (APIs) to build,
compile and execute quantum circuits.

The following code is the configuration file, written in Gaussian™ 16, of a molecule of
hydrogen, whose two hydrogen atoms are placed at a distance of :math:`0.735` Å:

.. code::

    # rhf/STO-3G scf(conventional)

    h2 molecule

    0 1
    H   0.0  0.0 -0.3675
    H   0.0  0.0  0.3675

Qiskit Chemistry uses this molecular configuration as an input to the computational
chemistry software --- in the case above, Gaussian 16.  The computational chemistry software
package is executed classically --- not to compute the ground-state energy,
dipole moment, or excited states of the given molecule, since these expensive computations
are delegated to the underlying quantum machine, but only to the extent necessary to compute
some intermediate data which,
combined with the molecular configuration above, can later be used to form the input to the
quantum algorithm in Aqua.  The information that needs to be extracted from the
computational chemistry software is configured when building the interface between
to the computational software package from within Aqua.

The intermediate data extracted from the classical computational software consists
of the following:

1. One- and two-body integrals in Molecular Orbital (MO) basis
2. Dipole integrals
3. Molecular orbital coefficients
4. :ref:`hartree-fock` energy
5. Nuclear repulsion energy

Once extracted, the structure of this intermediate data is independent of the
computational chemistry software that was used to compute it.  However,
the level of accuracy of such data does depend on the computational chemistry software;
more elaborate software packages are more likely to produce more accurate data.

Qiskit Chemistry offers the option to serialize this data in a binary format known as
`Hierarchical Data Format 5 (HDF5) <https://support.hdfgroup.org/HDF5/>`__.
This is done to enable future reuse of previously computed
input data.  This feature also enables researchers to exchange
input data among each other --- which turns out to be particularly useful to researchers who may
not have particular computational chemistry drivers installed on their computers.  HDF5 is
configured as a prebuilt driver in Qiskit Chemistry because it allows for chemistry input to
be passed into the computation.

~~~~~~~~~~~~~~~~~
Input Translation
~~~~~~~~~~~~~~~~~

The problem configuration and the additional intermediate data
obtained from the classical execution of one of computational chemistry drivers are
combined and then transformed to form the input to the quantum system.  This phase, known as
*translation*, is also extensible.  Practitioners interested in providing more efficient
translation operators may do so by extending this layer of the Aqua software
stack with their own implementation of the ``ChemistryOperator`` class.

In the reference implementation provided by Qiskit Chemistry, the translation phase
takes the input generated by the classical execution of the computational chemistry driver
and generates first a fermionic operator, and from this a qubit operator, which becomes
the input to one of the quantum algorithms in Aqua.

--------------
Novel Features
--------------

Qiskit Chemistry present some unique advantages
in terms of usability, functionality, and configuration-correctness enforcement.

~~~~~~~~~~~~~~~
User Experience
~~~~~~~~~~~~~~~

Allowing classical computational chemistry software at the front end has its own important
advantages. In fact, at the top of the Qiskit Chemistry software stack are chemists
who are most likely very familiar with existing computational chemistry software.  These
practitioners  may be interested in experimenting with the benefits of quantum computing
in terms of performance, accuracy and reduction of computational complexity, but at the
same time they might be unwilling to learn about the underlying quantum infrastructure.
Ideally, such practitioners would like to use a computational chemistry driver they are
used to as a front end to the quantum computing system, without having to learn a new quantum
programming language of new APIs.  It is also likely that such practitioners may have collected,
over time, numerous chemistry problem configurations, corresponding to various experiments.
Qiskit Chemistry is designed to accept those configuration files  with no modifications, and
without requiring a chemist to have to learn a quantum programming language. This approach has
a clear advantage in terms of usability.

~~~~~~~~~~~~~
Functionality
~~~~~~~~~~~~~

If Qiskit Chemistry had been designed to interpose a quantum programming language
or new APIs between the user and the classical computational chemistry software drivers,
it would not have been able to
fully exploit all the features of those drivers unless all such features
had been exposed by the higher programming-language or API.  In other words, in order to drive
the classical execution of any interfaced computational chemistry driver
to perform the most precise computation of the intermediate data needed to form
the quantum input, the advanced features of that driver would have had to be configurable through
Aqua Chemistry.  The ability of  Aqua to directly interface classical computational software
allows that software to compute the intermediate data needed to form the quantum input at its
highest level of precision.

To better illustrate this point, consider the ability of popular computational chemistry
:ref:`drivers`, such as :ref:`gaussian-16`, :ref:`psi4` and :ref:`pyscf` --- all interfaced by
Qiskit Chemistry --- to accept the configuration of a molecule where different atoms are
represented in different basis sets, as opposed to having to necessarily impose one single basis
set for all the atoms.  As an example, the following code snippet, written in the PSI4 language,
individually configures the basis sets for the atoms of a molecule of benzene, whose chemical
formula is :math:`C_6H_6`, indicating the fact that the molecule comprises six atoms of carbon
and six of hydrogen:

.. code::

    basis {
       assign DZ
       assign C 3-21G
       assign H1 STO-3G
       assign C1 STO-3G
    }

Here, the chemist has chosen to use basis DZ for all atoms via the first assignment. The second
assignment overwrites such statement for all six carbon atoms, which will be represented via the
3-21G basis set.  The third statement assigns basis set STO-3G to one particular hydrogen atom ---
the one with index 1 --- while all the other five hydrogen atoms keep basis set DZ. Finally, the
last statement assigns basis set STO-3G to the one carbon atom with index 1, leaving the remaining
five carbon atoms with basis set 3-21G as per the second assignment.

Qiskit Chemistry would have no problem supporting this fine-grained basis set specification, since
it allows the computational chemistry drivers to be the front end to the system, with no additional
layer on top of them.  Conversely, other systems that have chosen to interpose a new programming
language or new APIs in front of the computational drivers currently do not support the assignment
of different basis sets to different atoms in the same molecules.  In order to support
such advanced, fine-grained configurations, those systems will have to support the APIs for the
different basis sets to be specified, and map them to all of the underlying drivers.

Fine-grained basis-set specification is only one example of the functionality of
the computational chemistry drivers directly exposed by Qiskit Chemistry.  Another --- perhaps
even more important --- example has to do with the :ref:`hartree-fock` wave function,
which is computed by the underlying driver and allows for the computation of the one-
and two-body MO integrals, which in turn are used to determine
the full Configuration Interaction (CI) wave function and the :ref:`uccsd`
wave function, among other things.  Computational chemistry software drivers
expose configuration parameters to make the computation of the
Hartree-Fock wave function converge, should the default parameter values fail.
Qiskit Chemistry has no problem supporting such advanced configuration parameters,
which would be passed directly into the configuration file as an input to the underlying driver.
Conversely, solutions that have chosen to interpose a new programming language or new APIs between
the user and the underlying drivers currently do not support customizing the parameters for
facilitating the convergence of the computation of the Hartree-Fock wave function.  In order for
these alternative solutions to allow for this type of customization, the parameters would have to
be exposed through the programming language or the APIs.  As a result, such alternative solutions
may not be able to get the integrals that need to be used in the full CI or UCCSD calculations.

Let us consider yet another example illustrating why a direct use of the classical computational
chemistry software is superior to the choice of interposing a new programming language or API
between the user and the driver.  It has been `demonstrated <https://arxiv.org/abs/1701.08213>`__
that taking into account a molecule's spatial symmetries
can be used to reduce the number of qubits necessary to model that molecule and compute its energy
properties.  Computational chemistry software packages allow for configuring spatial symmetries
in their input files.  Thus, Qiskit Chemistry can immediately take direct advantage of such feature
exposed by the underlying computational software packages and obtain from those packages
intermediate data that is already optimized with respect to the symmetries configured by the user.
As a result, energy computations performed by Qiskit Chemistry require fewer qubits when
a spatial symmetries are present in a molecule.
Conversely, other solutions that interpose a new programming language or APIs fail to expose
this configuration feature to their users unless an ad-hoc symmetry API is constructed, which must
then be mapped to all the underlying software packages interfaced by those solutions.  To make
things more complicated, for any new software package that is interfaced by those solutions, that
symmetry API will have to be programmatically mapped to the package's symmetry
configuration feature.

In essence, interposing a new language or new APIs between the user and the underlying
classical drivers severely limits the functionality of the whole system, unless the new
language or APIs interfacing the drivers match the union of all the configuration parameters
of all the possible computational drivers that are currently supported by the system, or
that will be supported in the future.

~~~~~~~~~~~~~~~~~~~~~~~~~
Configuration Correctness
~~~~~~~~~~~~~~~~~~~~~~~~~

Qiskit Chemistry offers another unique feature. Given that Qiskit Chemistry
allows traditional software to be executed on a quantum system,
configuring a chemistry experiment definitely requires setting up a hybrid
configuration, which involves configuring both chemistry- and quantum-specific
parameters. The chances of introducing configuration
errors, making typos, or selecting incompatible configuration parameters
are very high, especially for people who are expert in chemistry
but new to the realm of quantum computing.

For example, the number of qubits necessary to compute the ground-state energy or a molecule
depends on the number of spin orbitals of that molecule.  The total number of qubits may
be reduced by applying various optimization techniques, such as the novel parity-map-based
precision-preserving two-qubit reduction.  Further reductions may be achieved with various
approximations, such as the freezing of the core and the virtual-orbital removal.  The number
of qubits to allocate to solve a particular problem should be computed by the system and not
exposed as a configuration parameter.  Letting the user configure the number of qubits can
easily lead to a configuration parameter mismatch.

Another scenario in which a user could misconfigure a problem would involve the
user associating algorithm components (such as optimizers and trial functions
for quantum variational algorithms) to algorithms that do not support such components.

To address such issues, in
Aqua the problem-specific configuration information and the
quantum-specific configuration information are verified for correctness both at configuration
time and at run time, so that the combination of classical and quantum inputs is
resilient to configuration errors. Very importantly, configuration
correctness is dynamically enforced even for components that are
dynamically discovered and loaded.


-------
License
-------

This project uses the `Apache License Version 2.0 software
license <https://www.apache.org/licenses/LICENSE-2.0>`__.

Some code supplied by Qiskit Chemistry for interfacing
to external chemistry :ref:`drivers` has additional licensing:

-  The :ref:`gaussian-16`
   driver
   contains work licensed under the `Gaussian Open-Source Public
   License <https://github.com/Qiskit/qiskit-chemistry/blob/master/qiskit_chemistry/drivers/gaussiand/gauopen/LICENSE.txt>`__.

-  The :ref:`pyquante`
   driver
   contains work licensed under the `modified BSD
   license <https://github.com/Qiskit/qiskit-chemistry/blob/master/qiskit_chemistry/drivers/pyquanted/LICENSE.txt>`__.

