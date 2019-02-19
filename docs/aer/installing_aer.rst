*********************
Installing Qiskit Aer
*********************

Install from PyPI
=================

**Install With the Rest of Qiskit**

Qiskit packages are published on the Python Package Index. The preferred tool for installing packages from *PyPI* is **pip**. This tool is provided with all modern versions of Python.

On Linux or MacOS, you should open your terminal and run the following command.
::

  $ pip install qiskit

On Windows, you should open *Command Prompt* (``⊞Win-r`` and type **cmd**) and run the same command.
::

  C:\> pip install qiskit

Installation from *PyPI* also allows you to install the latest development release. You will not generally need (or want) to do this, but it can be useful if you see a possible bug in the latest stable release. To do this, use the ``--pre flag``.
::

  $ pip install --pre qiskit

**Install Without the Rest of Qiskit**
::

  $ pip install qiskit-aer

**Upgrade Without the Rest of Qiskit**
::

  $ pip install --upgrade qiskit-aer

Install from Source
===================

.. note::
  The following are prerequisites for all operating systems

We recommend using Python virtual environments to cleanly separate Qiskit from other applications and improve your experience.

The simplest way to use environments is by using **Anaconda**
::

  $ conda create -y -n QiskitDevEnv python=3
  $ source activate QiskitDevEnv

Clone the Qiskit Aer repo via **git**.
::

  $ git clone https://github.com/Qiskit/qiskit-aer

Most of the required dependencies can be installed via **pip**, using the ``requirements-dev.txt`` file, eg:
::

  $ cd qiskit-aer
  $ pip install -r requirements-dev.txt


Linux
=====

Qiskit is supported on Ubuntu >= 16.04. To get most of the necessary compilers and libraries , install the ``build-essential`` package by running
::

  $ sudo apt install build-essential

Although the **BLAS** and **LAPACK** library implementations included in the ``build-essential`` package are sufficient to build all of the Aer simulators, we recommend using **OpenBLAS**, which you can install by running
::

  $ sudo apt install libopenblas-dev

There are two ways of building Aer simulators, depending on your goal:

#. Build a Terra compatible add-on;
#. Build a standalone executable.

**Terra Add-on**

For the former, we just need to call the ``setup.py`` script:
::

  qiskit-aer$ python ./setup.py bdist_wheel

We are using **scikit-build** as a substitute for **setuptools**. This is basically the glue between **setuptools** and **CMake**, so there are various options to pass variables to **CMake**, and the underlying build system (depending on your platform). The way to pass variables is:
::

  qiskit-aer$ python ./setup.py bdist_wheel -- -DCMAKE_VARIABLE=Values -- -Makefile_Flag

So a real example could be:
::

  qiskit-aer$ python ./setup.py bdist_wheel -- -j8

This is setting the **CMake** variable ``STATIC_LINKING`` to value ``True`` so **CMake** will try to create an statically linked **cython** library, and is passing ``-j8`` flag to the underlaying build system, which in this case is Makefile, telling it that we want to build in parallel, using 8 processes.

**Standalone Executable**

If we want to build a standalone executable, we have to use **CMake** directly. The preferred way **CMake** is meant to be used, is by setting up an "out of source" build. So in order to build our standalone executable, we have to follow these steps:
::

  qiskit-aer$ mkdir out
  qiskit-aer$ cd out
  qiskit-aer/out$ cmake ..
  qiskit-aer/out$ cmake --build . --config Release -- -j4

Once built, you will have your standalone executable into the ``Release/`` or ``Debug/`` directory (depending on the type of building chosen with the ``--config`` option):
::

  qiskit-aer/out$ cd Release
  qiskit-aer/outRelease/$ ls
  aer_simulator_cpp



macOS
=====

There are various methods depending on the compiler we want to use. If we want to use the **Clang** compiler, we need to install an extra library for supporting **OpenMP**: **libomp**. The **CMake** build system will warn you otherwise. To install it manually, run:
::

  $ brew install libomp

We recommend installing **OpenBLAS**, which is our default choice:
::

  $ brew install openblas

The **CMake** build system will search for other **BLAS** implementation alternatives if **OpenBLAS** is not installed in the system.

You further need to have **Xcode Command Line Tools** installed on macOS:
::

  $ xcode-select --install

There are two ways of building Aer simulators, depending on your goal:

#. Build a Terra compatible add-on;
#. Build a standalone executable.

**Terra Add-on**

For the former, we just need to call the ``setup.py`` script:
::

  qiskit-aer$ python ./setup.py bdist_wheel

We are using **scikit-build** as a substitute for **setuptools**. This is basically the glue between **setuptools** and **CMake**, so there are various options to pass variables to **CMake**, and the underlying build system (depending on your platform). The way to pass variables is:
::

  qiskit-aer$ python ./setup.py bdist_wheel -- -DCMAKE_VARIABLE=Values -- -Makefile_Flag

So a real example could be:
::

  qiskit-aer$ python ./setup.py bdist_wheel -- -j8

This is setting the **CMake** variable ``STATIC_LINKING`` to value ``True`` so **CMake** will try to create an statically linked **cython** library, and is passing ``-j8`` flag to the underlaying build system, which in this case is Makefile, telling it that we want to build in parallel, using 8 processes.

.. note::

  You may need to turn off static linking and specify your platform name, e.g.:

::

  qiskit-aer$ python ./setup.py bdist_wheel --plat-name macosx-10.9-x86_64 -- -DSTATIC_LINKING=False -- -j8

After this command is executed successfully, we will have a wheel package into the ``dist/`` directory, so next step is installing it:
::

  qiskit-aer/$ cd dist
  qiskit-aer/dist$ pip install qiskit_aer-<...>.whl

**Standalone Executable**

If we want to build a standalone executable, we have to use **CMake** directly. The preferred way **CMake** is meant to be used, is by setting up an "out of source" build. So in order to build our standalone executable, we have to follow these steps:
::

  qiskit-aer$ mkdir out
  qiskit-aer$ cd out
  qiskit-aer/out$ cmake ..
  qiskit-aer/out$ cmake --build . --config Release -- -j4

Once built, you will have your standalone executable into the ``Release/`` or ``Debug/`` directory (depending on the type of building chosen with the ``--config`` option):
::

  qiskit-aer/out$ cd Release
  qiskit-aer/outRelease/$ ls
  aer_simulator_cpp



Windows
=======

On Windows, you must have **Anaconda3** installed. We recommend also installing **Visual Studio 2017** (Community Edition). **Anaconda3** is required when searching for an **OpenBLAS** implementation. If **CMake** can't find a suitable implementation installed, it will take the **BLAS** library from the **Anaconda3** environment.
