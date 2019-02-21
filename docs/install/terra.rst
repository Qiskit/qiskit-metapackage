.. _install-terra-source:

Installing Qiskit Terra from Source
===================================
In what follows, we assume that you have downloaded the Qiskit Terra source files into
a local folder called ``qiskit-terra``.

Setup with an Environment
-------------------------

The simplest way is to use environments via `Anaconda <https://www.anaconda.com/distribution/>`_:

.. code:: sh

    conda create -y -n QiskitDevenv python=3
    source activate QiskitDevenv

For the python code, we need some libraries that can be installed in this way:

.. code:: sh

    cd qiskit-terra
    pip install -r requirements.txt
    pip install -r requirements-dev.txt

Installing from source requires that you have a c++ compiler on your system that supports
c++-11.  On most Linux platforms, the necessary GCC compiler is already installed.  Under
Apple OSX, the default clang compiler can be installed via XCode, or running

.. code:: sh

    $ xcode-select --install

in the terminal.  On Windows, you are required to have Visual Studio version 2015 or 2017
installed.  Make sure to select the options for installing the c++ compiler.

Once a compiler is installed, the necessary modules are built by calling:

.. code:: sh

    $ python setup.py build_ext --inplace

To get the examples working try

.. code:: sh

    $ pip install -e .

and then you can run them with

.. code:: sh

    $ python examples/python/using_qiskit_terra_level_0.py

If you would like to install qiskit-terra onto your system, then call:

.. code:: sh

    $ python setup.py install

We recommend that after setting up Terra you set up Aer to get more advanced simulators.
