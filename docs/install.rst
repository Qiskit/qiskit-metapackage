Qiskit Installation and setup
=============================


Dependencies
------------

To use Qiskit  you'll need to have installed at least
`Python 3.5 or later <https://www.python.org/downloads/>`__.
`Jupyter Notebooks <https://jupyter.readthedocs.io/en/latest/install.html>`__
is also recommended for interacting with
`tutorials`_.

For this reason we recommend installing `Anaconda 3 <https://www.anaconda.com/download/>`__
python distribution, which already comes with all these dependencies pre-installed.

Windows users also need to install VC++ runtime components. We recommend one of the following links.

- `Microsoft Visual C++ Redistributable for Visual Studio 2017 <https://go.microsoft.com/fwlink/?LinkId=746572>`__
- `Microsoft Visual C++ Redistributable for Visual Studio 2015 <https://www.microsoft.com/en-US/download/details.aspx?id=48145>`__


Installation with environment
-----------------------------

.. note::

    We recommend using `Python virtual environments <https://docs.python.org/3/tutorial/venv.html>`__
    to cleanly separate Qiskit from other applications and improve your experience.


The simplest way to use environments is by using Anaconda

.. code:: sh

     conda create -y -n Qiskitenv python=3
     activate Qiskitenv


The recommended way to install Qiskit is by using the PIP (Python
package manager) tool:

.. code:: sh

    pip install qiskit

This will install the latest stable release, along with all the dependencies.


Install with visualization dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are optional dependencies that are required to use all the visualization
functions included in Qiskit. You can install these at the same time by
running:

.. code:: sh

   pip install qiskit[visualization]

which will install qiskit and all the visualization dependencies.


Setup a standalone version
^^^^^^^^^^^^^^^^^^^^^^^^^^

The best way to install Qiskit when the goal is to extend its capabilities is by cloning
the individual repositories 

- `Terra repository <https://github.com/Qiskit/qiskit-terra>`__.
- `Aer repository <https://github.com/Qiskit/qiskit-aer>`__.
- `Aqua repository <https://github.com/Qiskit/qiskit-aqua>`__.
- `Chemistry repository <https://github.com/Qiskit/qiskit-chemistry>`__.

and following the standalone install instructions in these repositories.


Configure your API token and IBMQ credentials
---------------------------------------------

-  Create an `IBM Q <https://quantumexperience.ng.bluemix.net>`__ account if
   you haven't already done so
-  Get an API token from the IBM Q website under “My
   Account” > “Advanced”


Automatically loading credentials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The credentials for accessing the IBM Q quantum devices can be loaded
automatically, thus streamlining the set up of the IBM Q 
authentication.  You can set or store your API credentials once after installation, 
and when you want to use them, you can simply run:

.. code:: python

    from qiskit import IBMQ

    IBMQ.load_accounts()

This ``IBMQ.load_accounts()`` call performs the automatic loading of the
credentials from several sources (if needed), and authenticates against IBM Q, 
making the online devices available to your program. Please use one of the following
methods for storing the credentials before calling the automatic registration:


Store API credentials locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For most users, storing your API credentials is the most convenient approach.
Your information is stored locally in a configuration file called `qiskitrc`,
and once stored, you can use the credentials without explicitly passing them
to your program.

To store your information, simply run:

.. code:: python

    from qiskit import IBMQ

    IBMQ.save_account('MY_API_TOKEN')


where `MY_API_TOKEN` should be replaced with your token.

If you are on the IBM Q network, you must also pass the `url` 
argument found on your q-console account page to `IBMQ.save_account()`,
along with any other additional information required (e.g. proxy information):

.. code:: python

    from qiskit import IBMQ

    IBMQ.save_account('MY_API_TOKEN', url='https://...')



Manually loading credentials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In more complex scenarios or for users that need finer control over multiple
accounts, one can pass the API token, and the other parameters, directly to the 
``IBMQ.enable_account()`` function, that will ignore the automatic
loading of the credentials and use the arguments directly. For example:

.. code:: python

    from qiskit import IBMQ

    IBMQ.enable_account('MY_API_TOKEN', url='https://my.url')

will authenticate using ``MY_API_TOKEN`` and the specified URL,
regardless of the configuration stored in the config file, the environment
variables, or the ``Qconfig.py`` file, if any.

Manually loading from a ``Qconfig.py`` file can also be done:

.. code:: python

    from qiskit import IBMQ
    import Qconfig

    IBMQ.enable_account(Qconfig.APIToken, **Qconfig.config)


Please refer to the ``qiskit.IBMQ`` documentation for more information about
using multiple credentials.


Troubleshooting
---------------

The installation steps described on this document assume familiarity with the
Python environment on your setup (for example, standard Python, ``virtualenv``
or Anaconda). Please consult the relevant documentation for instructions
tailored to your environment.

Depending on the system and setup, appending "sudo -H" before the
``pip install`` command could be needed:

.. code:: sh

    pip install -U --no-cache-dir qiskit



.. _tutorials: https://github.com/Qiskit/qiskit-tutorial
