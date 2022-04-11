#############
Start locally
#############

Qiskit supports Python 3.7 or later. However, both Python and Qiskit are
evolving ecosystems, and sometimes when new releases occur in one or the other,
there can be problems with compatibility.

We recommend installing `Anaconda <https://www.anaconda.com/download/>`__, a
cross-platform Python distribution for scientific computing. Jupyter,
included in Anaconda, is recommended for interacting with Qiskit.

We recommend using Python virtual environments to cleanly separate Qiskit from
other applications and improve your experience.

The simplest way to use environments is by using the ``conda`` command,
included with Anaconda. A Conda environment allows you to specify a specific
version of Python and set of libraries. Open a terminal window in the directory
where you want to work.

It is preferred that you use the Anaconda prompt installed with Anaconda.
All you have to do is create a virtual environment inside Anaconda and activate the environment.
These commands can be run in the Anaconda prompt irrespective of Windows or Linux machine.

Create a minimal environment with only Python installed in it.

.. code:: sh

    conda create -n ENV_NAME python=3

Activate your new environment.

.. code:: sh

    conda activate ENV_NAME


Next, install the Qiskit package.

.. code:: sh

    pip install qiskit

If the packages were installed correctly, you can run ``conda list`` to see the active
packages in your virtual environment.

If you intend to use visualization functionality or Jupyter notebooks it is
recommended to install Qiskit with the extra ``visualization`` support:

.. code:: sh

    pip install qiskit[visualization]

It is worth pointing out that if you're a zsh user (which is the default shell on newer
versions of macOS), you'll need to put ``qiskit[visualization]`` in quotes:

.. code:: sh

    pip install 'qiskit[visualization]'
