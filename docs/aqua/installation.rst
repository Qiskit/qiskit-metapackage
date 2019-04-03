.. _aqua-installation:

===========================
Aqua Installation and Setup
===========================

Aqua can be used as a tool to execute `quantum algorithms <#quantum-algorithms.html>`__.
With the appropriate input, a quantum algorithm will run on top of the underlying
`Terra <https://qiskit.org/terra>`__
platform, which will generate, compile and execute a circuit modeling the input problem.
Aqua can also be used as the foundation for domain-specific applications, such as
:ref:`aqua-chemistry`, :ref:`aqua-ai` and :ref:`aqua-optimization`.
This section describes how to install and setup Aqua based on the user's goals.

------------
Dependencies
------------

At least `Python 3.5 or
later <https://www.python.org/downloads/>`__ is needed to use
Aqua. In addition, `Jupyter
Notebook <https://jupyter.readthedocs.io/en/latest/install.html>`__ is
recommended for interacting with the tutorials. For this reason, we
recommend installing the `Anaconda
3 <https://www.anaconda.com/download/>`__ Python distribution, as it
comes with all of these dependencies pre-installed.

.. seealso::
    Since Aqua is built upon `Terra <https://qiskit.org/terra>`__,
    you are encouraged to look over the
    `Terra
    installation and setup instructions <https://qiskit.org/documentation/install.html>`__.

------------
Installation
------------

The best way to install Aqua when the goal is to use it as a tool or as a library
of quantum algorithms is via the `pip <https://pip.pypa.io/en/stable/>`__  package management system:

.. code:: sh

    pip install qiskit_aqua

pip will handle all dependencies automatically and you will always
install the latest (and well-tested) release version.

A different class of users --- namely, quantum researchers and developers --- might be more
interested in exploring the source code of Aqua and :ref:`aqua-extending` by providing
new components, such as :ref:`quantum-algorithms`, :ref:`optimizers`, :ref:`variational-forms`,
:ref:`iqfts`, :ref:`oracles` and :ref:`initial-states`.
The best way to install Aqua when the goal is to extend its capabilities is by cloning
the `Aqua repository <https://github.com/Qiskit/aqua>`__.

.. note::

    We recommend using `Python virtual environments <https://docs.python.org/3/tutorial/venv.html>`__
    to cleanly separate Qiskit from other applications and improve your experience.
