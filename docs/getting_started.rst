:orphan:

###############
Getting started
###############

Installation
============

Let's get started using Qiskit!  The first thing to do is choose how you're
going to run and install the packages.  There are three main ways to do this:

.. toctree::
   :maxdepth: 2

   getting_started/local
   getting_started/cloud
   getting_started/source


Platform Support
================

Qiskit strives to support as many platforms as possible, but due to limitations
in available testing resources and platform availability, not all platforms
can be supported. Platform support for Qiskit is broken into 3 tiers with different
levels of support for each tier. For platforms outside these, Qiskit is probably
still installable, but it's not tested and you will have to build Qiskit (and likely
Qiskit's dependencies) from source.

Additionally, Qiskit only supports CPython. Running with other Python
interpreters isn't currently supported.

Tier 1
------

Tier 1 supported platforms are fully tested upstream as part of the development
processes to ensure any proposed change will function correctly. Pre-compiled
binaries are built, tested, and published to PyPI as part of the release process.
These platforms are expected to be installable with just a functioning Python
environment as all dependencies are available on these platforms.

Tier 1 platforms are currently:

 * Linux x86_64 (distributions compatible with the
   `manylinux 2014 <https://www.python.org/dev/peps/pep-0599/>`__
   packaging specification.
 * macOS x86_64 (10.9 or newer)
 * Windows 64 bit

Tier 2
------

Tier 2 platforms are not tested upstream as part of development process. However,
pre-compiled binaries are built, tested, and published to PyPI as part of the
release process and these packages can be expected to be installed with just a
functioning Python environment.

Tier 2 platforms are currently:

 * Linux i686 (distributions compatible with the
   `manylinux 2014 <https://www.python.org/dev/peps/pep-0599/>`__ packaging
   specification) for Python < 3.10
 * Windows 32 bit for Python < 3.10
 * Linux aarch64 (distributions compatible with the
   `manylinux 2014 <https://www.python.org/dev/peps/pep-0599/>`__ packaging
   specification)

Tier 3
------

Tier 3 platforms are not tested upstream as part of the development process.  Pre-compiled
binaries are built and published to PyPI as part of the release process, with no
testing at all. They may not be installable with just a functioning Python
environment and may require a C/C++ compiler or additional programs to build
dependencies from source as part of the installation process. Support for these
platforms are best effort only.

Tier 3 platforms are currently:

 * Linux i686 (distributions compatible with the
   `manylinux 2014 <https://www.python.org/dev/peps/pep-0599/>`__ packaging
   specification) for Python >= 3.10
 * Windows 32 bit for Python >= 3.10
 * macOS arm64 (10.15 or newer)

Ready to get going?...
======================

.. raw:: html

   <div class="tutorials-callout-container">
      <div class="row">

.. customcalloutitem::
   :description: Learn how to build, execute, and post-process quantum circuits with Qiskit.
   :header: Qiskit from the ground up
   :button_link:  intro_tutorial1.html
   :button_text: Start learning Qiskit


.. customcalloutitem::
   :description: Find out how to leverage Qiskit for everything from single-circuits to full quantum application development.
   :header: Dive into the tutorials
   :button_link:  tutorials.html
   :button_text: Qiskit tutorials

.. raw:: html

   </div>
