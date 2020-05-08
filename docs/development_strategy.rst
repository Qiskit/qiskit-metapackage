Development Strategy
********************

Roadmap
=======

We are going to look out 12 months to establish a set of goals we want to work
towards. When planning, we typically look at potential work from the perspective
of the elements.

Qiskit Terra
------------

In 2018 we worked on formalizing the backends and user flow in Qiskit Terra. The
basic idea is as follows: the user designs a quantum circuit and then, through a set of
transpiler passes, rewrites the circuit to run on different backends with
different optimizations. We also introduced the concept of a *provider*,
whose role is to supply backends for the user to run quantum circuits on.
The provider API we have defined at version one supplies a set of
schemas to verify that the provider and its backends are Terra-compatible.

In 2019, we have many extensions planned. These include:

- **Add passes to the transpiler.** The goal here is to be more efficient in
  circuit depth as well as adding passes that find approximate circuits and resource estimations.

- **Introduce a circuit foundry and circuit API.** This has the goal of making sure that a
  user can easily build complex circuits from operations. Some of these include
  adding controls and power to operations, and inserting unitary matrices directly.

- **Provide an API for OpenPulse.** Now that OpenPulse is defined, and the IBM Quantum
  provider can accept it, we plan to build out the pulse features. These will include a
  scheduler and tools for building experiments out of pulses. Also included will
  be tools for mapping between experiments with gates (QASM) to experiments with pulses.

Qiskit Aer
----------

The first release of Qiskit Aer was made available at the end of 2018. It included C++
implementations of QASM, statevector, and unitary simulators. These are the core to
Qiskit Aer, and replace the simulators that existed in Terra. The QASM simulator includes
a customizable general (Kraus) noise model, and all simulators include CPU parallelization
through the OpenMP library.

In 2019, Aer will be extended in many ways:

- **Optimize simulators.** We are going to start profiling the simulators and work on making
  them faster. This will include automatic settings for backend configuration and
  OpenMP parallelization configuration based on the input Qobj and available hardware.
- **Develop additional simulator backends.** We will include several approximate simulator backends
  that are more efficient for specific subclasses of circuits, such as the
  T-gate simulator, which works on Clifford and T gates (with low T-depth), and a stabilizer
  simulator,  which works just on Clifford gates.
- **Add noise approximation tools.** We plan to add noise approximation tools to mapping
  general (Kraus) noise models to approximate noise model that may be implemented on
  an approximate backends (for example only mixed Clifford and reset errors in the noise model).

Qiskit Ignis
------------

This year, we are going to release the first version of Qiskit Ignis. The goal of
Ignis is to be a set of tools for characterization of errors,
improving gates, and enhancing computation
in the presence of noise. Examples of these tools include optimal control, dynamical
decoupling, and error mitigation.

In 2019, Ignis will include tools for:

- quantum state/process tomography

- randomized benchmarking over different groups

- optimal control (e.g., pulse shaping)

- dynamical decoupling

- circuit randomization

- error mitigation (to improve results for quantum chemistry experiments)

Qiskit Aqua
-----------

Aqua is an open-source library of quantum algorithms and applications, introduced in June 2018.
As a library of quantum algorithms, Aqua comes with a rich set of quantum algorithms of
general applicability—such as VQE, QAOA, Grover's Search, Amplitude Estimation and
Phase Estimation—and domain-specific algorithms-such as the Support Vector Machine (SVM)
Quantum Kernel and Variational algorithms, suitable for supervised learning.  In addition,
Aqua includes algorithm-supporting components, such as optimizers, variational forms, oracles,
Quantum Fourier Transforms, feature maps, multiclass classification extension algorithms,
uncertainty problems, and random distributions.
As a framework for quantum applications, Aqua provides support for Chemistry (released separately
as the Qiskit Chemistry component), as well as Artificial Intelligence (AI), Optimization and
Finance.  Aqua is extensible across multiple domains, and has been designed and structured as a
framework that allows researchers to contribute their own implementations of new algorithms and
algorithm-supporting components.

Over the course of 2019, we are planning to enrich Aqua as follows:

- We will include several new quantum algorithms,
  such as Deutsch-Jozsa, Simon's, Bernstein-Vazirani, and
  Harrow, Hassidim, and Lloyd (HHL).
- We will improve the performance of quantum algorithms on top of both
  simulators and real hardware.
- We will provide better support for execution on real quantum hardware.
- We will increase the set of problems supported by the AI, Optimization and Finance
  applications of Aqua.

Summary
-------

These are examples of just some of the work we will be focusing on in the next 12 months.
We will continuously adapt the plan based on feedback. Please follow along and let us
know what you think!

.. _versioning_strategy:

Versioning
==========

The Qiskit project is made up of several elements each performing different
functionality. Each is independently useful and can be used on their own,
but for convenience we provide this repository and meta-package to provide
a single entrypoint to install all the elements at once. This is to simplify
the install process and provide a unified interface to end users. However,
because each Qiskit element has it's own releases and versions some care is
needed when dealing with versions between the different repositories. This
document outlines the guidelines for dealing with versions and releases of
both Qiskit elements and the meta-package.

For the rest of this guide the standard Semantic Versioning nomenclature will
be used of: ``Major.Minor.Patch`` to refer to the different components of a
version number. For example, if the version number was ``0.7.1``, then the major
version is ``0``, the minor version ``7``, and the patch version ``1``.


Meta-package Version
--------------------

The Qiskit meta-package version is an independent value that is determined by
the releases of each of the elements being tracked. Each time we push a release
to a tracked component (or add an element) the meta-package requirements, and
version will need to be updated and a new release published. The timing should
be coordinated with the release of elements to ensure that the meta-package
releases track with element releases.

Adding New Elements
^^^^^^^^^^^^^^^^^^^

When a new Qiskit element is being added to the meta-package requirements, we
need to increase the **Minor** version of the meta-package.

For example, if the meta-package is tracking 2 elements ``qiskit-aer`` and
``qiskit-terra`` and it's version is ``0.7.4``. Then we release a new element
``qiskit-ignis`` that we intend to also have included in the meta-package. When
we add the new element to the meta-package we increase the version to
``0.8.0``.


Patch Version Increases
^^^^^^^^^^^^^^^^^^^^^^^

When any Qiskit element that is being already tracked by the meta-package
releases a patch version to fix bugs in a release we need also bump the
requirement in the setup.py and then increase the patch version of the
meta-package.

For example, if the meta-package is tracking 3 elements ``qiskit-terra==0.8.1``,
``qiskit-aer==0.2.1``, and ``qiskit-ignis==0.1.4`` with the current version
``0.9.6``. When qiskit-terra release a new patch version to fix a bug ``0.8.2``
the meta-package will also need to increase it's patch version and release,
becoming ``0.9.7``.

Additionally, there are occasionally packaging or other bugs in the
meta-package itself that need to be fixed by pushing new releases. When those
are encountered we should increase the patch version to differentiate it from
the broken release. Do **not** delete the broken or any old releases from pypi
in any situation, instead just increase the patch version and upload a new
release.


Minor Version Increases
^^^^^^^^^^^^^^^^^^^^^^^

Besides adding a new element to the meta-package the minor version of the
meta-package should also be increased anytime a minor version is increased in
a tracked element.

For example, if the meta-package is tracking 2 elements ``qiskit-terra==0.7.0``
and ``qiskit-aer==0.1.1`` and the current version is ``0.7.5``. When the
``qiskit-aer`` element releases ``0.2.0`` then we need to increase the
meta-package version to be ``0.8.0`` to correspond to the new release.


Major Version Increases
^^^^^^^^^^^^^^^^^^^^^^^

The major version is different from the other version number components. Unlike
the other version number components, which are updated in lock step with each
tracked element, the major version is only increased when all tracked versions
are bumped (at least before ``1.0.0``). Right now all the elements still have
a major version number component of ``0`` and until each tracked element in the
meta-repository is marked as stable by bumping the major version to be ``>=1``
then the meta-package version should not increase the major version.

The behavior of the major version number component tracking after when all the
elements are at >=1.0.0 has not been decided yet.


Qiskit Element Requirement Tracking
-----------------------------------

While not strictly related to the meta-package and Qiskit versioning how we
track the element versions in the meta-package's requirements list is
important. Each element listed in the setup.py should be pinned to a single
version. This means that each version of Qiskit should only install a single
version for each tracked element. For example, the requirements list at any
given point should look something like::

  requirements = [
      "qiskit_terra==0.7.0",
      "qiskit-aer==0.1.1",
  ]

This is to aid in debugging, but also make tracking the versions across
multiple elements more transparent.

It is also worth pointing out that the order we install the elements is
critically important too. ``pip`` does not have a real dependency solver which
means the installation order matters. So if there are overlapping requirements
versions between elements or dependencies between elements we need to ensure
that the order in the requirements list installs everything as expected. If the
order needs to be change for some install time incompatibility it should be
noted clearly.


Module Status
=============

Qiskit is developing so fast that is it is hard to keep all different parts
of the API supported for various versions. We do our best and we use
the rule that for one minor version update, for example 0.6 to 0.7,
we will keep the API working with a deprecated warning. Please don’t
ignore these warnings. Sometimes there are cases in which this can’t
be done and for these in the release history we will outline these in
great details.

This being said as we work towards Qiskit 1.0 there are some modules
that have become stable and the table below is our attempt to label them



Modules
-------

+------------------------+------------+------------------------------------+
| Name                   | status     | Note                               |
+========================+============+====================================+
| assembler              | stable     | completed in version 0.9           |
+------------------------+------------+------------------------------------+
| circuit                | unstable   |                                    |
+------------------------+------------+------------------------------------+
| compiler               | stable     |  completed in version 0.9          |
+------------------------+------------+------------------------------------+
| converters             | unstable   |                                    |
+------------------------+------------+------------------------------------+
| dagcircuit             | remove     | will be part of circuits           |
+------------------------+------------+------------------------------------+
| extensions             | remove     | will be part of circuits           |
+------------------------+------------+------------------------------------+
| ignis.characterization |            |                                    |
+------------------------+------------+------------------------------------+
| ignis.mitigation       |            |                                    |
+------------------------+------------+------------------------------------+
| ignis.characterization |            |                                    |
+------------------------+------------+------------------------------------+
| providers              | stable     | completed in version 0.7           |
+------------------------+------------+------------------------------------+
| pulse                  | unstable   |                                    |
+------------------------+------------+------------------------------------+
| qasm                   | remove     | passer location to be determined   |
+------------------------+------------+------------------------------------+
| qobj                   | remove     | moved into the provider            |
+------------------------+------------+------------------------------------+
| quantum_info           | unstable   |                                    |
+------------------------+------------+------------------------------------+
| result                 | remove     | moved into the provider            |
+------------------------+------------+------------------------------------+
| schemas                | stable     | completed in version 0.7           |
+------------------------+------------+------------------------------------+
| tests                  | unstable   |                                    |
+------------------------+------------+------------------------------------+
| tools                  | unstable   | various elements to be removed     |
+------------------------+------------+------------------------------------+
| transpiler             | stable     | completed in version 0.9           |
+------------------------+------------+------------------------------------+
| validation             | stable     | completed in version 0.7           |
+------------------------+------------+------------------------------------+
| visualization          | stable     | completed in version 0.9           |
+------------------------+------------+------------------------------------+

Providers
---------

There are three providers that come with the default installation of Qiskit

Basic Aer Provider
^^^^^^^^^^^^^^^^^^

This provider simulates ideal quantum circuits and has three backends.
As Aer becomes more stable and can work on any operating system this
provider will be removed.

Aer Provider
^^^^^^^^^^^^

This is a more advance simulator that is written in C++. It runs faster than Basic Aer
and also allows you to add noise to your circuits. This allow you to explore what
happens to your circuits for realistic
models of the experiments and design experiments that might be more resilient
to the noise in today’s quantum computers.

IBM Quantum Provider
^^^^^^^^^^^^^^^^^^^^

This provider gives you access to real experiments. You will need an IBM Quantum Experience
account to use it.  It also has an online HPC simulator that can be used. It is a
hosted version of the Aer Provider.


Community Extensions
====================

Qiskit has been designed with modularity in mind. It is extensible in many
different ways; on the page, we highlight the ways in which the Qiskit community
has engaged with Qiskit and developed extensions and packages on top of it.

Providers
---------

The Qiskit base provider is an entity that provides access to a group
of different backends (for example, backends available through IBM Quantum).
It interacts with those backends to do many things: find out which ones
are available, retrieve an instance of a particular backend, get backend
properties and configurations, and handling running and working with jobs.

Additional providers
^^^^^^^^^^^^^^^^^^^^

- **Decision diagram-based quantum simulator**

  | - **Organization:** Johannes Kepler University, Linz, Austria (Alwin
      Zulehner and Robert Wille)
  | - **Description:** A local provider which allows Qiskit to use decision
      diagram-based quantum simulation
  | - **Qiskit Version:** 0.7
  | - **More info:**  `Webpage at JKU <http://iic.jku.at/eda/research/quantum_simulation>`__,
    `Medium Blog <https://medium.com/qiskit/classical-simulators-for-quantum-computers-4b994dad4fa2>`__
    and `GitHub Repo <https://github.com/Qiskit/qiskit-jku-provider>`__

- **Quantum Inspire**

  | - **Organization:** QuTech-Delft
  | - **Description:** A provider for the Quantum Inspire backend
  | - **Qiskit Version:** 0.7
  | - **More info:** `Medium Blog <https://medium.com/qiskit/quantum-inspire-and-qiskit-f1be608f8955>`__
    and `GitHub <https://github.com/QuTech-Delft/quantuminspire>`__.


Transpiler
----------

Circuit optimization is at the heart of making quantum computing feasible on actual hardware.
A central component of Qiskit is the transpiler, which is a framework for manipulating
quantum circuits according to certain transformations (known as transpiler passes). The transpiler
enables users to create customized sets of passes, orchestrated by a pass manager, to transform
the circuit according to the rules specified by the passes. In addition, the transpiler architecture
is designed for modularity and extensibility, enabling Qiskit users to write their own passes,
use them in the pass manager, and combine them with existing passes. In this way,
the transpiler architecture opens up the door for research into aggressive optimization
of quantum circuits.


Additional passes
^^^^^^^^^^^^^^^^^

- **t|ket〉 optimization & routing pass**

  | - **Organization:** Cambridge Quantum Computing
  | - **Description:** Transpiler pass for circuit optimization and mapping
      to backend using CQC's t|ket〉compiler.
  | - **Qiskit Version:** 0.7
  | - **More info:** `Tutorial Notebook <https://github.com/Qiskit/qiskit-tutorials/blob/master/community/aqua/chemistry/QSE_pytket.ipynb>`__
    and `GitHub <https://github.com/CQCL/pytket>`__.

Tools
-----

Extending Qiskit with new tools and functionality is an important part
of building a community. These tools can be new visualizations, slack integration,
Jupyter extensions and much more.

Additional Tools
^^^^^^^^^^^^^^^^
* **OpenControls library**

  | - **Organization:** Q-CTRL
  | - **Description:** Library of quantum control pulses derived from the open literature.
  | - **Qiskit Version:** 0.7
  | - **More info:**  `GitHub <https://github.com/qctrl/python-open-controls>`__
    and `Q-CTRL website <https://q-ctrl.com/products/open-controls/>`__
