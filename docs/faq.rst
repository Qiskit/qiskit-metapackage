==========================
Frequently Asked Questions
==========================

* How should I cite Qiskit in my research?

  * Please cite it as per the included `BibTeX file
    <https://raw.githubusercontent.com/Qiskit/qiskit/master/Qiskit.bib>`_.

|

* Why do I receive the error message ``AttributeError: 'str' object has no
  attribute 'configuration'`` when I try to execute or compile a circuit on a
  backend?

  * The backend parameter of these two functions takes in a ``BaseBackend`` type,
    which can be returned by calling one of these methods:

    For simulators:

    .. code:: python

      Aer.get_backend('<backend_name>')

    For real devices:

    .. code:: python

      IBMQ.get_backend('<backend_name>')

    For example, if you want to run a job on the ``'ibmqx4'`` backend, the
    following code would throw the error message:

    .. code:: python

      job = execute(circuit, backend='ibmqx4', shots=100)

    Instead, the code should be written as

    .. code:: python

      my_backend = IBMQ.get_backend('ibmqx4')
      job = execute(circuit, backend=my_backend, shots=100)

|

* Why do I receive the error message ``Error: Instance of QuantumCircuit has no
  member`` when adding gates to a circuit?

  * This is a pylint error, which is a Linter for Python. Linters analyze
    code for potential errors, and they throw errors when they find
    potentially erroneous code. However, this error should not prevent your
    code from compiling or running, so there is no need to worry. The error
    message can be disabled by adding the following line above the code that
    is causing the error:

    .. code:: python

      #pylint: disable=no-member

|

* Why do my results from real devices differ from my results from the simulator?

  * The simulator runs jobs as though is was in an ideal environment; one
    without noise or decoherence. However, when jobs are run on the real devices
    there is noise from the environment and decoherence, which causes the qubits
    to behave differently than what is intended.

|

* Why do I receive the error message ``No Module 'qiskit'`` when using Jupyter
  Notebook?

  * If you have done ``pip install qiskit`` and set up your virtual environment in
    Anaconda, then you may experience this error when you are running a tutorial
    in Jupyter Notebook. If you have not yet installed Qiskit and/or set up your
    virtual environment, you can follow the steps
    `here <https://qiskit.org/documentation/install.html#install>`__.

    |

    The error is caused when trying to import the Qiskit package in an
    environment where Qiskit is not installed. If you launched Jupyter Notebook
    from the Anaconda-Navigator, it is possible that Jupyter Notebook is being
    run in the base (root) environment, instead of in your virtual
    environment. To change environments in the Anaconda-Navigator, click the
    dropdown arrow next to **Applications on** in the top left corner. There you
    should see all of the virtual environments within Anaconda, and you can
    select the environment where you have Qiskit installed and launch Jupyter
    Notebook from there.
