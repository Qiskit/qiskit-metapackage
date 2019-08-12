.. _aqua-chemistry:

****************
Qiskit Chemistry
****************

Qiskit Chemistry is the only end-to-end quantum software stack that allows for mapping high-level
classical chemistry computational software problems all the way down to a quantum machine (a
simulator or a real quantum device).

Qiskit Chemistry is a set of tools and algorithms that enable experimenting with chemistry problems
via quantum computing. Qiskit Chemistry translates chemistry-specific problems
into inputs for an algorithm from the Aqua :ref:`quantum-algorithms` library,
which in turn uses `Qiskit Terra <https://qiskit.org/terra>`__ for the actual
quantum computation. Qiskit Chemistry supports both closed-shell and open-shell molecules
in conjunction with chemistry driver computations using RHF, ROHF or UHF methods.

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

.. toctree::
   :maxdepth: 3
   :hidden:

   Installation and Setup <qiskit_chemistry_installation>
   Drivers <qiskit_chemistry_drivers>
   Translators <qiskit_chemistry_translators>
   Configuring and Running an Experiment <qiskit_chemistry_execution>
   Contributing to Qiskit Chemistry <qiskit_chemistry_extending>
   Qiskit Chemistry SDK Reference <../../autodoc/qiskit_chemistry>
   Release history <release_history>

.. include:: qiskit_chemistry_features.rst
.. include:: qiskit_chemistry_license.rst
