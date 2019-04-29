.. _aqua-execution:

=====================================
Configuring and Running an Experiment
=====================================

Aqua supports two types of users:

1. *Practitioners*, who are merely interested in executing Aqua
   as a tool to execute :ref:`quantum-algorithms`.
   These users may not be interested in extending Aqua
   with additional capabilities.  In fact, they may not even be interested
   in learning the details of quantum computing, such as the notions of
   circuits, gates and qubits.  What these users expect
   from quantum computing is the gains in performance and accuracy, and
   the reduction in computational complexity, compared to the use of
   a classical algorithm.  Aqua also provides a library of :ref:`classical-reference-algorithms`
   for generating reference values and comparing and contrasting results during
   experimentation.
2. *Quantum algorithm researchers and developers*, who are interested in extending
   Aqua with new quantum algorithms or algorithm components for more efficient
   and accurate computations.

In this section, we cover the first class of users --- the algorithm practitioners.
Specifically, this section describes how Aqua can be accessed as a
tool for experimenting with the execution of quantum algorithms.

To see how you can extend Aqua with new components,
please refer to `Section ":ref:`aqua-extending`".

---------------
Execution Modes
---------------

Aqua has both a `Graphical User Interface (GUI) <#aqua-gui>`__ and a `command
line tool <#aqua-command-line>`__.  These can be used when experimenting with quantum algorithms.
Both can load and run an `input
file <#aqua-input-file>`__ specifying the the type of problem the experiment is about,
and the quantum
algorithm to be used for the computation, along with the algorithm configuration
and various other options to
customize the experiment.  If you are new to
Aqua, we highly recommend getting started with the GUI.
Aqua can also be accessed
`programmatically <#aqua-programmable-interface>`__ by users interested
in customizing the experiments beyond what the command line and GUI can offer.
Finally, users configuring an Aqua experiment and researchers
intersted in extending Aqua with new components can access
the :ref:`aqua-doc-ui` for quickly inspecting the various components
and their configuration parameters.

.. _aqua-gui:

^^^
GUI
^^^

The GUI provides an easy means to create from scratch, or load
an existing, `input file <#aqua-input-file>`__, and then run that input file to experiment with a
quantum algorithm.
An input file for Aqua is assumed to be in JSON format.  Such a file is created,
edited and saved with schema-based validation of parameter values.

When installing
Aqua via the ``pip install`` command,
a script is created that allows you to start the GUI from the command line,
as follows:

.. code:: sh

   qiskit_aqua_ui

If you cloned Aqua directly from the
`GitHub repository <https://github.com/Qiskit/aqua>`__ instead of using ``pip
install``, then the script above will not be present and the launching command should be instead:

.. code:: sh

   python qiskit_aqua_ui/run

This command must be launched from the root folder of the ``qiskit-aqua`` repository clone.

.. seealso::

    Consult the documentation on the :ref:`aqua-installation` for more details.

.. _aqua-command-line:

^^^^^^^^^^^^
Command Line
^^^^^^^^^^^^

If installed via ``pip install``,
Aqua comes with the following command-line tool:

.. code:: sh

   qiskit_aqua_cmd

If you cloned Aqua from its remote
`GitHub repository <https://github.com/QISKit/aqua>`__
instead of using ``pip install``, then the command-line interface can be executed as follows:

.. code:: sh

   python qiskit_aqua_cmd

from the root folder of the ``qiskit-aqua`` repository clone.

.. seealso::

    Consult the documentation on the :ref:`aqua-installation` for more details.

When invoking Aqua from the command line, an `input file <#aqua-input-file>`__ in
`JavaScript Object Notation (JSON) <https://www.json.org/>`__ format
is expected as a command-line parameter.

.. _aqua-programmable-interface:

^^^^^^^^^^^^^^^^^^^^^^
Programmable Interface
^^^^^^^^^^^^^^^^^^^^^^

Experiments can be run programmatically too. Numerous
examples on how to program an experiment in Aqua
can be found in the ``aqua`` folder of the
`Aqua Tutorials GitHub repository
<https://github.com/QISKit/aqua-tutorials>`__.

It should be noted at this point that Aqua is
designed to be as much declarative as possible.  This is done in order
to simplify the programmatic access to Aqua,
minimize the chances for configuration errors, and help users
who might not interested in writing a lot of code or
learning new Application Programming Interfaces (APIs).

There is
nothing preventing a user from accessing the Aqua APIs and
programming an experiment step by step, but a  more direct way to access Aqua programmatically
is by obtaining a JSON algorithm input file, such as one of those
available in the ``aqua/input_files`` subfolder of the
`Aqua Tutorials GitHub repository <https://github.com/QISKit/aqua-tutorials>`__.
Such files can be constructed manually, but a much more intuitive way to automatically
construct one of these input files is
via Aqua domain-specific applications.  For example,
the :ref:`aqua-chemistry-command-line`
and :ref:`aqua-chemistry-gui`
have options to serialize the input to the quantum algorithm for future reuse.
The JSON file can then be pasted into a Python program and modified according to the
needs of the developer, before invoking the ``run_algorithm`` API in ``qiskit_aqua``.
This technique can be used, for example, to compare the results of two different algorithms.

.. _aqua-doc-ui:

^^^^^^^^^^^^^^^^
Documentation UI
^^^^^^^^^^^^^^^^

Aqua is a modular and extensible software framework, supporting two types of endusers:
those who want to simply use Aqua as a tool to execute experiments, and those interested in
extending Aqua with new components.  Users in either of these categories may find it useful
to access the Aqua documentation UI, which shows all the pluggable components along with
the schemas for their parameters.

If installed via ``pip install``,
Aqua comes with the following command-line tool
to launch the Aqua documentation UI:

.. code:: sh

   qiskit_aqua_browser

If you cloned Aqua from its remote
`GitHub repository <https://github.com/QISKit/aqua>`__
instead of using ``pip install``, then the
Aqua documentation UI can be launched as follows:

.. code:: sh

   python qiskit_aqua_ui/browser

from the root folder of the ``qiskit-aqua`` repository clone.

.. _aqua-input-file:

----------
Input File
----------

An input file is used to define an Aqua problem,
and includes the input to the
quantum algorithm
as well as configuration information for
the underlying quantum system.
Specific configuration parameter values can be supplied to
explicitly control the processing and the quantum algorithm used for
the computation, instead of using defaulted values when none are
supplied.

The format for the input file is `JavaScript Object Notation (JSON) <https://www.json.org/>`__.
This allows for schema-based
configuration-input correctness validation.  While it is certainly possible to
generate a JSON input file manually, Aqua allows for a simple way
for automatically generating such a JSON input file from the execution
of a domain-specific application.

For example, the Aqua Chemistry `command-line tool
:ref:`aqua-chemistry-command-line`
and :ref:`aqua-chemistry-gui`
both allow for automatically serializing the input to the quantum algorithm
as a JSON :ref:`input-file-for-direct-algorithm-invocation`.
Serializing the input to the quantum algorithm is useful in many scenarios
because the contents of one of such JSON files are domain- and problem-independent:

- Users can share JSON files among each other in order to compare and contrast
  their experimental results at the algorithm level, for example to compare
  results obtained by passing the same input to different algorithms, or
  to different implementations of the same algorithm, regardless of the domain
  in which those inputs were generated (chemistry, artificial intelligence, optimization, etc.)
  or the problem that the user was trying to solve.
- People performing research on quantum algorithms may be interested in having
  access to a number of such JSON files in order to test and refine the design and
  implementation of an algorithm, irrespective of the domain in which those JSON files were
  generated or the problem that the user was trying to solve.
- Repeating a domain-specific experiment in which the values of the input parameters remain
  the same, and the only difference is in the configuration of the quantum algorithm and its
  supporting components becomes much more efficient because the user can choose to
  restart any new experiment directly at the algorithm level, thereby bypassing the
  data extraction from the driver, and the translation of that data into input to a
  quantum algorithm.

A number of sample JSON input files for Aqua are available in the
``aqua/input_files``
subfolder of the `Aqua Tutorials GitHub repository <https://github.com/QISKit/aqua-tutorials>`__.

An input file comprises the following main sections, although not all
mandatory:

^^^^^^^^^^^^^
``"problem"``
^^^^^^^^^^^^^

In Aqua,
a *problem* specifies the type of experiment being run.  Configuring the problem is essential
because it determines which algorithms are suitable for the specific experiment.
Aqua comes with a set of predefined problems.
This set is extensible: new problems can be added,
just like new algorithms can be plugged in to solve existing problems in a different way,
or to solve new problems.

Currently, a problem can be configured by assigning a ``str`` value to the ``"name"`` parameter:

.. code:: python

    "name" = "energy" | "excited_states" | "ising" | "dynamics" | "search" | "classification"

As shown above, ``"energy"``, ``"excited_states"``, ``"ising"``, ``"dynamics"``,
``"search"``, and ``"classification"`` are currently
the only values accepted for ``"name"``, corresponding to the computation of
*energy*, *excited states*, *Ising models*, *dynamics of evolution*, *search* and
*Support Vector Machine (SVM) classification*, respectively.
New problems, disambiguated by their
``"name"`` parameter, can be programmatically
added to Aqua via the
``AlgorithmInput`` Application Programming Interface (API), and each quantum or classical
Aqua algorithm should programmatically list the problems it is suitable for
in its JSON schema, embedded into
the class implementing the ``QuantumAlgorithm`` interface.

Aspects of the computation may include use of random numbers. For instance, the
:ref:`vqe`
is coded to use a random initial point if the variational form does not supply any
preference based on the initial state and if the
user does not explicitly supply an initial point.
In this case, each run of VQE, for what would otherwise be a constant problem,
can produce a different result, causing non-determinism and the inability to replicate
the same result across different runs with
identical configurations. Even though the final values obtained after multiple
executions of VQE might be numerically indistinguishable,
the number of evaluations may differ across different runs.
To enable repeatable experiments, with the exact same outcome, a *random seed* can be set,
thereby forcing the same pseudo-random numbers to
be generated every time the experiment is run:

.. code:: python

    "random_seed" : int

The default value for this parameter is ``None``.

^^^^^^^^^^^
``"input"``
^^^^^^^^^^^

This section allows the user to specify the input to the Aqua algorithm.
Such input is expected to be a qubit operator, expressed as the value of the
``"qubit_op"`` parameter, for problems of type energy, excited states, Ising models and
dynamics of evolution.  For problems of type SVM classification, the input consists
of a *training dataset* (a map linking each label to a list of data points),
a *test dataset* (also a map linking each label to a list of data points), and
the list of data points on which to apply classification.
These are specified as the values of the parameters
``"training_datasets"``, ``"test_datasets"``, and ``"datapoints"``, respectively.
The ``"input"`` section is disabled for problems of type search; for such problems,
the input specification depends on the particular
oracle chosen for the :ref:`grover` algorithm.
Currently, Aqua provides an implementation of the satisfiability (SAT) oracle,
which takes as input a SAT problem in
`DIMACS CNF format <http://www.satcompetition.org/2009/format-benchmarks2009.html>`__
expressed as the value of the ``"cnf"`` parameter,
and constructs the corresponding quantum circuit.

^^^^^^^^^^^^^^^
``"algorithm"``
^^^^^^^^^^^^^^^

This is an optional section that allows the user to specify which of the
:ref:`quantum-algorithms`
will be used for the experiment.
To compute reference values, Aqua also offers a library of
:ref:`classical-reference-algorithms`.
In the ``"algorithm"`` section, algorithms are disambiguated using the
declarative names
by which Aqua recognizes them, based on the JSON schema
each algorithm must provide according to the Aqua ``QuantumAlgorithm`` API.
The declarative name is specified as the ``"name"`` parameter in the ``"algorithm"`` section.
The default value for the ``"name"`` parameter is ``"VQE"``, corresponding
to the :ref:`vqe`
algorithm.

An algorithm typically comes with a set of configuration parameters.
For each of them, a default value is provided according to the Aqua
``QuantumAlgorithm`` API.

Furthermore, according to each algorithm, additional sections
may become relevant to optionally
configure that algorithm's components.  For example, variational algorithms,
such as VQE, allow the user to choose and configure an
optimizer and a
variational form from the :ref:`optimizers` and :ref:`variational-forms` libraries, respectively,
:ref:`qpe`
can be configured with one of the
:ref:`iqfts`,
and :ref:`grover` comes with the option
to specify an oracle from the :ref:`oracles` library.
The Aqua documentation on :ref:`quantum-algorithms`
explains how to configure each algorithm and any of the pluggable entities it may use.

Here is an example in which the algorithm VQE is selected along with the
:ref:`L-BFGS-B`
optimizer and the :ref:`ryrz` variational form:

.. code:: json

    "algorithm": {
        "initial_point": null,
        "name": "VQE",
        "operator_mode": "matrix"
    },

    "optimizer": {
        "factr": 10,
        "iprint": -1,
        "maxfun": 1000,
        "name": "L_BFGS_B"
    },

    "variational_form": {
        "depth": 3,
        "entanglement": "full",
        "entangler_map": null,
        "name": "RYRZ"
    }

^^^^^^^^^^^^^
``"backend"``
^^^^^^^^^^^^^

Aqua allows for configuring the *backend*, which is the quantum machine
on which a quantum experiment will be run.
This configuration requires specifying
the `Qiskit Terra <https://www.qiskit.org/terra>`__ quantum computational
provider and backend to be used for computation, which is done by assigning a ``str`` value to
the ``"provider"`` and ``"name"`` parameters of the ``"backend"`` section:

.. code:: python

    "provider" : string
    "name" : string

The value of the ``"provider"`` parameter indicates the full name of a class derived from
``"BaseProvider"`` or global variable pointing to a instance of this class.
The value of the ``"name"`` parameter indicates either a real-hardware
quantum computer or a quantum simulator accessed from the provider.
Terra comes with two predefined providers: ``"qiskit.BasicAer"`` and  ``"qiskit.IBMQ"``.
By installing ``"qiskit-aer"``, the ``"qiskit.Aer"`` provider gets included too.
Each provider has its own set of simulators and ``"qiskit.IBMQ"`` gives access to real-hardware
quantum computer or simulators in the cloud.
For the ``"qiskit.IBMQ"`` provider, you need to configure it with a token and possibly url proxies.
The Aqua `GUI <#aqua-gui>` greatly simplifies it via a user friendly interface,
accessible through the **Preferences...** menu item.
Otherwise you need to configure programmatically using Qiskit Terra <https://www.qiskit.org/terra>` apis.

.. topic:: Backend Configuration: Quantum vs. Classical Algorithms

    Although Aqua is mostly a library of
    :ref:`quantum-algorithms`,
    it also includes a number of
    :ref:`classical-reference-algorithms`
    which can be selected to generate reference values
    and compare and contrast results in quantum research experimentation.
    Since a classical algorithm runs on a classical computer,
    no backend should be configured when a classical algorithm
    is selected in the ``"algorithm"`` section.
    Accordingly, the Aqua `GUI <#aqua-gui>`__ will automatically
    disable the ``"backend"`` configuration section
    whenever a non-quantum algorithm is selected.

Configuring the backend to use by a quantum algorithm
requires setting the following parameters too:

-  The number of repetitions of each circuit to be used for sampling:

   .. code:: python

        "shots" : int

   This parameter applies, in particular to the local QASM simulator and any real quantum device.
   The default value is ``1024``.

-  A ``bool`` value indicating whether or not the circuit should undergo optimization:

   .. code:: python

        "skip_transpiler" : bool

   The default value is ``False``.  If ``"skip_transpiler"`` is set to ``True``, then
   QISKit will not perform circuit translation. If Aqua has been configured
   to run an experiment with a quantum algorithm that uses only basis gates,
   then no translation of the circuit into basis gates is required.
   Only in such cases is it safe to skip circuit translation.
   Skipping the translation phase when only basis gates are used may improve overall performance,
   especially when many circuits are used repeatedly, as it is the case with the VQE algorithm.

   .. warning::

       Use caution when setting ``"skip_transpiler"`` to ``True``
       as if the quantum algorithm does not restrict itself to the set of basis
       gates supported by the backend, then the circuit will fail to run.

-  An optional list can be supplied to setup the backend's coupling map:

   .. code:: python

       "coupling_map" : list

   This is a Python list consisting of the directed edges, each edge ([A, B]) points qubit A can connect to qubit B.  Configuring it is optional; the default value is ``None``.
   The following is an example of such a list that can be used:

   .. code:: python

      "coupling_map": [[0, 1], [0, 2], [1, 2], [3, 2], [3, 4], [4, 2]]

-  An optional string can be supplied to the basis gates:

   .. code:: python

       "basis_gates" : string

   This is a Python string consisting of basis gates, where are separated by comma.  Configuring it is optional; the default value is ``None``.
   ``None`` denotes using the basis gates in the selected backend. The following is an example of such a dictionary that can be used:

   .. code:: python

      "basis_gates": "u1,u2,u3,cx,id"

-  An optional dictionary can be supplied to assign the qubit mapping:

   .. code:: python

       "initial_layout" : dictionary

   This is a Python dictionary consisting of the mapping qubits from the codes to
   the backend. Configuring it is optional; the default value is ``None``.
   The following is an example of such a dictionary that can be used:

   .. code:: python

      "initial_layout": {('qr', 0): ('q', 1), ('qr', 1): ('q', 0)}


-  The maximum number of credits used per quantum job:

   .. code:: python

        "max_credits" : int

   This parameter applies, in particular to any real quantum device.
   The default value is ``10``.


-  The waiting time of a result submitted to any real quantum device:

   .. code:: python

        "timeout" : float or None

   This parameter applies, in particular to any real quantum device.
   The default value is ``None``.


-  The query period of the job submitted to any real quantum device:

   .. code:: python

        "wait" : float

   This parameter applies, in particular to any real quantum device.
   The default value is ``5.0``.

