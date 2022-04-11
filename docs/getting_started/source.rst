.. _install-from-source:

######################
Installing from source
######################

Installing the elements from source allows you to access the most recently
updated version of Qiskit instead of using the version in the Python Package
Index (PyPI) repository. This will give you the ability to inspect and extend
the latest version of the Qiskit code more efficiently.

When installing the elements and components from source, by default their
``development`` version (which corresponds to the ``master`` git branch) will
be used, as opposed to the ``stable`` version (which contains the same codebase
as the published ``pip`` packages). Since the ``development`` versions of an
element or component usually include new features and changes, they generally
require using the ``development`` version of the rest of the items as well.

.. note::

   The Terra and Aer packages both require compilers to build from source
   before you can install.  Most other Qiskit-family packages do not require
   a compiler.

Installing elements from source requires the following order of installation to
prevent installing versions of elements that may be lower than those desired if the
``pip`` version is behind the source versions:

#. :ref:`qiskit-terra <install-qiskit-terra>`
#. :ref:`qiskit-aer <install-qiskit-aer>`
#. :ref:`qiskit-ignis <install-qiskit-ignis>`
#. :ref:`qiskit-ibmq-provider <install-qiskit-ibmq-provider>`
   (if you want to connect to the IBM Quantum devices or online
   simulator)

To work with several components and elements simultaneously, use the following
steps for each element.

.. note::

   Due to the use of namespace packaging in Python, care must be taken in how you
   install packages. If you're planning to install any element from source, do not
   use the ``qiskit`` meta-package. Also, follow this guide and use a separate virtual
   environment for development. If you do choose to mix an existing installation
   with your development, refer to
   https://github.com/pypa/sample-namespace-packages/blob/master/table.md
   for the set of combinations of installation methods that work together.

Set up the Virtual Development Environment
==========================================

.. code-block:: sh

   conda create -y -n QiskitDevenv python=3
   conda activate QiskitDevenv


.. _install-qiskit-terra:

Qiskit Terra
============

Installing from source requires that you have the Rust compiler on your system.
To install the Rust compiler the recommended path is to use rustup, which is
a cross-platform Rust installer. To use rustup you can go to:

https://rustup.rs/

which will provide instructions for how to install rust on your platform.
Besides rustup there are
`other installation methods <https://forge.rust-lang.org/infra/other-installation-methods.html>`__ available too.

Once the Rust compiler is installed, you are ready to install Qiskit Terra.

1. Clone the Terra repository.

   .. code:: sh

      git clone https://github.com/Qiskit/qiskit-terra.git

2. Cloning the repository creates a local folder called ``qiskit-terra``.

   .. code:: sh

      cd qiskit-terra

3. If you want to run tests or linting checks, install the developer requirements.

   .. code:: sh

      pip install -c constraints.txt -r requirements-dev.txt

4. Install ``qiskit-terra``.

   .. code:: sh

      pip install .

If you want to install it in editable mode, meaning that code changes to the
project don't require a reinstall to be applied, you can do this with:

.. code:: sh

   pip install -e .

Installing in editable mode will build the compiled extensions in debug mode
without optimizations. This will affect the runtime performance of the compiled
code. If you'd like to use editable mode and build the compiled code in release
with optimizations enabled you can run:

.. code:: sh

   python setup.py build_rust --release --inplace

after you run pip and that will rebuild the binary in release mode.

If you are working on Rust code in Qiskit you will need to rebuild the extension
code every time you make a local change. ``pip install -e .`` will only build
the Rust extension when it's called, so any local changes you make to the Rust
code after running pip will not be reflected in the installed package unless
you rebuild the extension. You can leverage the above ``build_rust`` command to
do this (with or without ``--release`` based on whether you want to build in
debug mode or release mode).

You can then run the code examples after installing Terra. You can
run an example script with the following command.

.. code:: sh

   python examples/python/using_qiskit_terra_level_0.py


.. _install-qiskit-aer:

Qiskit Aer
==========

1. Clone the Aer repository.

   .. code:: sh

      git clone https://github.com/Qiskit/qiskit-aer

2. Install build requirements.

   .. code:: sh

      pip install cmake scikit-build

After this, the steps to install Aer depend on which operating system you are
using. Since Aer is a compiled C++ program with a Python interface, there are
non-Python dependencies for building the Aer binary which can't be installed
universally depending on operating system.

.. tabbed:: Linux

   3. Install compiler requirements.

      Building Aer requires a C++ compiler and development headers.

      If you're using Fedora or an equivalent Linux distribution,
      install using:

      .. code:: sh

         dnf install @development-tools

      For Ubuntu/Debian install it using:

      .. code:: sh

         apt-get install build-essential

   4. Install OpenBLAS development headers.

      If you're using Fedora or an equivalent Linux distribution,
      install using:

      .. code:: sh

         dnf install openblas-devel

      For Ubuntu/Debian install it using:

      .. code:: sh

         apt-get install libopenblas-dev


.. tabbed:: macOS


   3. Install dependencies.

      To use the `Clang <https://clang.llvm.org/>`__ compiler on macOS, you need to install
      an extra library for supporting `OpenMP <https://www.openmp.org/>`__.  You can use `brew <https://brew.sh/>`__
      to install this and other dependencies.

      .. code:: sh

         brew install libomp

   4. Then install a BLAS implementation; `OpenBLAS <https://www.openblas.net/>`__
      is the default choice.

      .. code:: sh

         brew install openblas

      Next, install ``Xcode Command Line Tools``.

      .. code:: sh

         xcode-select --install

.. tabbed:: Windows

   On Windows you need to use `Anaconda3 <https://www.anaconda.com/distribution/#windows>`__
   or `Miniconda3 <https://docs.conda.io/en/latest/miniconda.html>`__ to install all the
   dependencies.

   3. Install compiler requirements.

      .. code:: sh

         conda install --update-deps vs2017_win-64 vs2017_win-32 msvc_runtime

   4. Install binary and build dependencies.

      .. code:: sh

         conda install --update-deps -c conda-forge -y openblas cmake


5. Build and install qiskit-aer directly

   If you have pip <19.0.0 installed and your environment doesn't require a
   custom build, run:

   .. code:: sh

      cd qiskit-aer
      pip install .

   This will both build the binaries and install Aer.

   Alternatively, if you have a newer pip installed, or have some custom requirement,
   you can build a Python wheel manually.

   .. code:: sh

      cd qiskit-aer
      python ./setup.py bdist_wheel

   If you need to set a custom option during the wheel build, refer to
   :ref:`aer_wheel_build_options`.

   After you build the Python wheel, it will be stored in the ``dist/`` dir in the
   Aer repository. The exact version will depend

   .. code:: sh

      cd dist
      pip install qiskit_aer-*.whl

   The exact filename of the output wheel file depends on the current version of
   Aer under development.

.. _aer_wheel_build_options:

Custom options during wheel builds
----------------------------------

The Aer build system uses `scikit-build <https://scikit-build.readthedocs.io/en/latest/index.html>`__
to run the compilation when building it with the Python interface. It acts as an interface for
`setuptools <https://setuptools.readthedocs.io/en/latest/>`__ to call `CMake <https://cmake.org/>`__
and compile the binaries for your local system.

Due to the complexity of compiling the binaries, you may need to pass options
to a certain part of the build process. The way to pass variables is:

.. code:: sh

   python setup.py bdist_wheel [skbuild_opts] [-- [cmake_opts] [-- build_tool_opts]]

where the elements within square brackets `[]` are optional, and
``skbuild_opts``, ``cmake_opts``, ``build_tool_opts`` are to be replaced by
flags of your choice. A list of *CMake* options is available here:
https://cmake.org/cmake/help/v3.6/manual/cmake.1.html#options. For
example, you could run something like:

.. code:: sh

   python setup.py bdist_wheel -- -- -j8

This is passing the flag `-j8` to the underlying build system (which in this
case is `Automake <https://www.gnu.org/software/automake/>`__), telling it that you want
to build in parallel using 8 processes.

For example, a common use case for these flags on linux is to specify a
specific version of the C++ compiler to use (normally if the default is too
old):

.. code:: sh

   python setup.py bdist_wheel -- -DCMAKE_CXX_COMPILER=g++-7

which will tell CMake to use the g++-7 command instead of the default g++ when
compiling Aer.

Another common use case for this, depending on your environment, is that you may
need to specify your platform name and turn off static linking.

.. code:: sh

   python setup.py bdist_wheel --plat-name macosx-10.9-x86_64 \
   -- -DSTATIC_LINKING=False -- -j8

Here ``--plat-name`` is a flag to setuptools, to specify the platform name to
use in the package metadata, ``-DSTATIC_LINKING`` is a flag for using CMake
to disable static linking, and ``-j8`` is a flag for using Automake to use
8 processes for compilation.

A list of common options depending on platform are:

+--------+------------+--------------------------+---------------------------------------------+
|Platform| Tool       | Option                   | Use Case                                    |
+========+============+==========================+=============================================+
| All    | Automake   | ``-j``                   | Followed by a number, sets the number of    |
|        |            |                          | processes to use for compilation.           |
+--------+------------+--------------------------+---------------------------------------------+
| Linux  | CMake      | ``-DCMAKE_CXX_COMPILER`` | Used to specify a specific C++ compiler;    |
|        |            |                          | this is often needed if your default g++ is |
|        |            |                          | too old.                                    |
+--------+------------+--------------------------+---------------------------------------------+
| OSX    | setuptools | ``--plat-name``          | Used to specify the platform name in the    |
|        |            |                          | output Python package.                      |
+--------+------------+--------------------------+---------------------------------------------+
| OSX    | CMake      | ``-DSTATIC_LINKING``     | Used to specify whether or not              |
|        |            |                          | static linking should be used.              |
+--------+------------+--------------------------+---------------------------------------------+

.. note::

    Some of these options are not platform-specific. These particular platforms are listed
    because they are commonly used in the environment. Refer to the
    tool documentation for more information.

.. _install-qiskit-ignis:

Qiskit Ignis
============

1. Clone the Ignis repository.

   .. code:: sh

      git clone https://github.com/Qiskit/qiskit-ignis.git

2. Cloning the repository creates a local directory called ``qiskit-ignis``.

   .. code:: sh

      cd qiskit-ignis

3. If you want to run tests or linting checks, install the developer requirements.
   This is not required to install or use the qiskit-ignis package when installing
   from source.

   .. code:: sh

      pip install -c constraints.txt -r requirements-dev.txt

4. Install Ignis.

   .. code:: sh

      pip install .

If you want to install it in editable mode, meaning that code changes to the
project don't require a reinstall to be applied:

.. code:: sh

    pip install -e .

.. _install-qiskit-ibmq-provider:

IBM Quantum Provider
====================

1. Clone the qiskit-ibmq-provider repository.

   .. code:: sh

      git clone https://github.com/Qiskit/qiskit-ibmq-provider.git

2. Cloning the repository creates a local directory called ``qiskit-ibmq-provider``.

   .. code:: sh

      cd qiskit-ibmq-provider

3. If you want to run tests or linting checks, install the developer requirements.
   This is not required to install or use the qiskit-ibmq-provider package when
   installing from source.

   .. code:: sh

      pip install -c constraints.txt -r requirements-dev.txt

4. Install qiskit-ibmq-provider.

   .. code:: sh

      pip install .

If you want to install it in editable mode, meaning that code changes to the
project don't require a reinstall to be applied:
