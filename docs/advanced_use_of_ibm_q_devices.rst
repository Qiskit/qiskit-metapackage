.. _advanced_use_of_ibm_q_devices_label:

Advanced Use of IBM Q Devices
=============================

.. note::

    This documentation describes access to the IBM Q devices using API version 2.0 and higher,
    which is available in Qiskit 0.11+.

In Qiskit we have an interface for backends and jobs that is useful for running quantum circuits
and/or pulse schedules and extending to third-party backends. In this section, we will review the
core components of Qiskit’s base backend framework, using the IBM Q account as an example.

The interface has four parts: the account, the provider, the backend, and the job:

-  account: Gives access to one or more 'providers' based on account permissions.
-  provider: Provides access to quantum devices and simulators, collectively called 'backends',
   and additional services tailored to a specific backend instance.
-  backend: A quantum device or simulator capable of running quantum circuits or pulse schedules.
-  job: A local reference to a collection of quantum circuits or pulse schedules submitted to a
   given backend.

The Account
------------

The Qiskit ``IBMQ`` account object is the local reference for accessing your IBM Q account,
and all of the providers, backends, etc, that are available to you.

The ``IBMQ`` account has functions for handling administrative tasks. The credentials can
be saved to disk, or used in a session and never saved.

-  ``enable_account(TOKEN)``: Enable your account in the current session
-  ``save_account(TOKEN)``: Save your account to disk for future use.
-  ``load_account()``: Load account using stored credentials.
-  ``disable_account()``: Disable your account in the current session.
-  ``active_account()``: List the account currently in the session.
-  ``stored_account()``: List the account stored to disk.
-  ``delete_account())``: Delete the saved account from disk.

In order to access quantum devices, simulators, or other services, you
must specify the source of these items by selecting a provider.  To see all
the providers available:

.. code:: python

    from qiskit import IBMQ

    IBMQ.load_account() # Load account from disk
    IBMQ.providers()    # List all available providers


.. code-block:: text

    [<AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>,
     <AccountProvider for IBMQ(hub='ibm-q-perf', group='performance', project='default-params')>]

where we have assumed that the user has stored their IBMQ account information
locally ahead of time using ``IBMQ.save_account(TOKEN)``.

The above example shows two different providers.  All ``IBMQ`` providers are specified
by a ``hub``, ``group``, and ``project``.  The provider given by
``hub='ibm-q', group='open', project='main'`` is the provider that gives access to the
public IBM Q devices available to all IQX users.  The second is an example of
a provider that is only unlocked for a specific set of users.  Members of the IBM Q network
may see one or more providers (with names different than those shown above) depending on the
access level granted to them.

To access a given provider one should use the ``get_provider()`` method of the ``IBMQ``
account, filtering by ``hub``, ``group``, or ``project``:

.. code:: python

    IBMQ.get_providers(hub='ibm-q')


.. code-block:: text

    <AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>


.. code:: python

    IBMQ.get_providers(project='default-params')

.. code-block:: text

    <AccountProvider for IBMQ(hub='ibm-q-perf', group='performance', project='default-params')>

Finally, as a convenience, calling ``IBMQ.load_account()`` or ``IBMQ.enable_account()`` will
return the default public provider instance
``<AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>``.


The Provider
------------

Providers accessed via the ``IBMQ`` account provide access to a group of
different backends (for example, backends available through the IBM Q
Experience or IBM Q Network quantum cloud services).

A provider inherits from ``BaseProvider`` and implements the methods:

-  ``backends()``: returns all backend objects known to the provider.
-  ``get_backend(NAME)``: returns the named backend.

Using the public provider instance from above:

.. code:: python

    provider = IBMQ.get_providers(hub='ibm-q')
    provider.backends()


.. code-block:: text

    [<IBMQSimulator('ibmq_qasm_simulator') from IBMQ(hub='ibm-q', group='open', project='main')>,
     <IBMQBackend('ibmqx4') from IBMQ(hub='ibm-q', group='open', project='main')>,
     <IBMQBackend('ibmqx2') from IBMQ(hub='ibm-q', group='open', project='main')>,
     <IBMQBackend('ibmq_16_melbourne') from IBMQ(hub='ibm-q', group='open', project='main')>]

Selecting a backend is done by name using the ``get_backend(NAME)`` method:

.. code:: python

    backend = IBMQ.get_backend('ibmq_16_melbourne')


Filtering the backends
^^^^^^^^^^^^^^^^^^^^^^

You may also optionally filter the set of returned backends, by passing
arguments that query the backend’s ``configuration`` or ``status`` or
``properties``. The filters are passed by conditions and, for more
general filters, you can make advanced functions using the lambda
function.

As a first example lets return only those backends that are real quantum
devices, and that are currently operational:

.. code:: python

    provider.backends(simulator=False, operational=True)


.. code-block:: text

    [<IBMQBackend('ibmqx4') from IBMQ(hub='ibm-q', group='open', project='main')>,
    <IBMQBackend('ibmqx2') from IBMQ(hub='ibm-q', group='open', project='main')>,
    <IBMQBackend('ibmq_16_melbourne') from IBMQ(hub='ibm-q', group='open', project='main')>]



Or, only those backends that are real devices, have more than 10 , and
are operational

.. code:: python

    provider.backends(filters=lambda x: x.configuration().n_qubits >= 10 and
                  not x.configuration().simulator and x.status().operational==True)


.. code-block:: text

    [<IBMQBackend('ibmq_16_melbourne') from IBMQ(hub='ibm-q', group='open', project='main')>]



Filter: show the least busy device (in terms of the number of jobs pending in the
queue)

.. code:: python

    from qiskit.providers.ibmq import least_busy

    small_devices = providers.backends(filters=lambda x: x.configuration().n_qubits == 5 and
                                       not x.configuration().simulator)
    least_busy(small_devices)


.. code-block:: text

    <IBMQBackend('ibmqx4') from IBMQ(hub='ibm-q', group='open', project='main')>


The above filters can be combined as desired.


The Backend
-----------

Backends represent either a simulator or a real quantum computer, and
are responsible for running quantum circuits and/or pulse schedules and
returning results. They have a ``run`` method which takes in a ``qobj``
as input, which is a quantum object and the result of the compilation process,
and returns a ``BaseJob`` object. This object allows asynchronous running of
jobs for retrieving results from a backend when the job is completed.

At a minimum, backends use the following methods, inherited from
``BaseBackend``:

-  ``provider`` - Returns the provider of the backend
-  ``name()`` - Returns the name of the backend.
-  ``status()`` - Returns the current status of the backend.
-  ``configuration()`` - Returns the backend's configuration.
-  ``properties()`` -Returns the backend properties.
-  ``run(QOBJ, **kwargs)`` - Runs a qobj on the backend.

For remote backends they must support the additional

-  ``jobs()`` - Returns a list of previous jobs executed on this backend
   through the current provider instance.
-  ``retrieve_job()`` - returns a job by a job_id.

On a per device basis, the following commands may be supported:

-  ``defaults()`` - Gives a data structure of typical default
   parameters.
-  ``schema()`` - gets a schema for the backend

There are some IBM Q backend only attributes:

-  ``hub`` - The IBMQ hub for this backend.
-  ``group`` - The IBMQ group for this backend.
-  ``project`` - The IBMQ project for this backend.

.. code:: python

    backend = least_busy(small_devices)

Let’s start with the ``backend.provider()``, which returns a provider
object

.. code:: python

    backend.provider()

.. code-block:: text

    <AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>



Next is the ``name()``, which returns the name of the backend

.. code:: python

    backend.name()


.. code-block:: text

    'ibmq_16_melbourne'



Next let’s look at the ``status()``:


.. code:: python

    backend.status()


.. code-block:: text

    BackendStatus(backend_name='ibmq_16_melbourne', backend_version='1.0.0', operational=True, pending_jobs=5, status_msg='active')


Here we see the name of the backend, the software version it is running,
along with its operational status, number of jobs pending in the backends queue,
and a more detailed status message.


The next is ``configuration()``

.. code:: python

    backend.configuration()


.. code-block:: text

    QasmBackendConfiguration(allow_q_circuit=False, allow_q_object=True, backend_name='ibmq_16_melbourne', backend_version='1.0.0', basis_gates=['u1', 'u2', 'u3', 'cx', 'id'], conditional=False, coupling_map=[[1, 0], [1, 2], [2, 3], [4, 3], [4, 10], [5, 4], [5, 6], [5, 9], [6, 8], [7, 8], [9, 8], [9, 10], [11, 3], [11, 10], [11, 12], [12, 2], [13, 1], [13, 12]], credits_required=True, description='14 qubit device', gates=[GateConfig(coupling_map=[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]], name='id', parameters=[], qasm_def='gate id q { U(0,0,0) q; }'), GateConfig(coupling_map=[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]], name='u1', parameters=['lambda'], qasm_def='gate u1(lambda) q { U(0,0,lambda) q; }'), GateConfig(coupling_map=[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]], name='u2', parameters=['phi', 'lambda'], qasm_def='gate u2(phi,lambda) q { U(pi/2,phi,lambda) q; }'), GateConfig(coupling_map=[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]], name='u3', parameters=['theta', 'phi', 'lambda'], qasm_def='u3(theta,phi,lambda) q { U(theta,phi,lambda) q; }'), GateConfig(coupling_map=[[1, 0], [1, 2], [2, 3], [4, 3], [4, 10], [5, 4], [5, 6], [5, 9], [6, 8], [7, 8], [9, 8], [9, 10], [11, 3], [11, 10], [11, 12], [12, 2], [13, 1], [13, 12]], name='cx', parameters=[], qasm_def='gate cx q1,q2 { CX q1,q2; }')], local=False, max_experiments=75, max_shots=8192, memory=False, n_qubits=14, n_registers=1, online_date=datetime.datetime(2018, 11, 6, 5, 0, tzinfo=tzutc()), open_pulse=False, sample_name='albatross', simulator=False, url='None')


The next is ``properties()`` method

.. code:: python

    backend.properties()


.. code-block:: text

    BackendProperties(backend_name='ibmq_16_melbourne', backend_version='1.0.0', gates=[Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[0]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.001570601788269732)], qubits=[0]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.003141203576539464)], qubits=[0]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[1]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.008715080370287898)], qubits=[1]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.017430160740575795)], qubits=[1]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[2]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.003657501402404062)], qubits=[2]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.007315002804808124)], qubits=[2]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[3]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0018890962135893474)], qubits=[3]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.003778192427178695)], qubits=[3]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[4]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0035559285003328167)], qubits=[4]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.007111857000665633)], qubits=[4]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[5]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0022386896355628405)], qubits=[5]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.004477379271125681)], qubits=[5]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[6]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0018895452926070977)], qubits=[6]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0037790905852141954)], qubits=[6]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[7]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.001562544550278655)], qubits=[7]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.00312508910055731)], qubits=[7]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[8]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.002479153434522041)], qubits=[8]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.004958306869044082)], qubits=[8]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[9]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0029654467868943657)], qubits=[9]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.005930893573788731)], qubits=[9]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[10]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0013039171445604625)], qubits=[10]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.002607834289120925)], qubits=[10]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[11]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0013983817590772496)], qubits=[11]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.002796763518154499)], qubits=[11]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[12]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0031078121194844655)], qubits=[12]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.006215624238968931)], qubits=[12]), Gate(gate='u1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.0)], qubits=[13]), Gate(gate='u2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.005660930994786095)], qubits=[13]), Gate(gate='u3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 6, 22, 35, tzinfo=tzutc()), name='gate_error', unit='', value=0.01132186198957219)], qubits=[13]), Gate(gate='cx', name='CX1_0', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 20, 20, tzinfo=tzutc()), name='gate_error', unit='', value=0.045740852071565447)], qubits=[1, 0]), Gate(gate='cx', name='CX1_2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='gate_error', unit='', value=0.0858374161782575)], qubits=[1, 2]), Gate(gate='cx', name='CX2_3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 23, 34, tzinfo=tzutc()), name='gate_error', unit='', value=0.06373088324946385)], qubits=[2, 3]), Gate(gate='cx', name='CX4_3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 26, 49, tzinfo=tzutc()), name='gate_error', unit='', value=0.03688104993550978)], qubits=[4, 3]), Gate(gate='cx', name='CX4_10', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 30, tzinfo=tzutc()), name='gate_error', unit='', value=0.05357986992525404)], qubits=[4, 10]), Gate(gate='cx', name='CX5_4', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 33, 14, tzinfo=tzutc()), name='gate_error', unit='', value=0.06650537876375073)], qubits=[5, 4]), Gate(gate='cx', name='CX5_6', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 36, 34, tzinfo=tzutc()), name='gate_error', unit='', value=0.04965815672774171)], qubits=[5, 6]), Gate(gate='cx', name='CX5_9', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 40, 24, tzinfo=tzutc()), name='gate_error', unit='', value=0.053128149203371305)], qubits=[5, 9]), Gate(gate='cx', name='CX6_8', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 43, 49, tzinfo=tzutc()), name='gate_error', unit='', value=0.036278771746848154)], qubits=[6, 8]), Gate(gate='cx', name='CX7_8', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 47, 16, tzinfo=tzutc()), name='gate_error', unit='', value=0.03307615597398114)], qubits=[7, 8]), Gate(gate='cx', name='CX9_8', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 50, 26, tzinfo=tzutc()), name='gate_error', unit='', value=0.04082495337788555)], qubits=[9, 8]), Gate(gate='cx', name='CX9_10', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 54, 27, tzinfo=tzutc()), name='gate_error', unit='', value=0.04442146739711669)], qubits=[9, 10]), Gate(gate='cx', name='CX11_3', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 8, 4, 14, tzinfo=tzutc()), name='gate_error', unit='', value=0.04886767166678935)], qubits=[11, 3]), Gate(gate='cx', name='CX11_10', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 7, 57, 50, tzinfo=tzutc()), name='gate_error', unit='', value=0.03543129679135215)], qubits=[11, 10]), Gate(gate='cx', name='CX11_12', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 8, 1, 4, tzinfo=tzutc()), name='gate_error', unit='', value=0.05927055914890103)], qubits=[11, 12]), Gate(gate='cx', name='CX12_2', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 8, 7, 29, tzinfo=tzutc()), name='gate_error', unit='', value=0.11226039126452647)], qubits=[12, 2]), Gate(gate='cx', name='CX13_1', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 8, 12, 8, tzinfo=tzutc()), name='gate_error', unit='', value=0.1279557204157135)], qubits=[13, 1]), Gate(gate='cx', name='CX13_12', parameters=[Nduv(date=datetime.datetime(2019, 7, 19, 8, 16, 7, tzinfo=tzutc()), name='gate_error', unit='', value=0.052689052030127914)], qubits=[13, 12])], general=[], last_update_date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), qubits=[[Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=76.79227555986287), Nduv(date=datetime.datetime(2019, 7, 19, 6, 18, 42, tzinfo=tzutc()), name='T2', unit='µs', value=24.116040513979055), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=5.100097173606134), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.025399999999999978)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=55.409066888970266), Nduv(date=datetime.datetime(2019, 7, 19, 6, 19, 43, tzinfo=tzutc()), name='T2', unit='µs', value=94.43728841410335), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=5.2386110863104465), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.07180000000000009)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=50.521956266319215), Nduv(date=datetime.datetime(2019, 7, 19, 6, 20, 42, tzinfo=tzutc()), name='T2', unit='µs', value=82.88747539554133), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=5.032629096197071), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.07230000000000003)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=70.22351500869209), Nduv(date=datetime.datetime(2019, 7, 19, 6, 21, 42, tzinfo=tzutc()), name='T2', unit='µs', value=61.11098069764448), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=4.896205369707648), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.0595)], [Nduv(date=datetime.datetime(2019, 7, 18, 6, 27, 24, tzinfo=tzutc()), name='T1', unit='µs', value=49.254369270572425), Nduv(date=datetime.datetime(2019, 7, 19, 6, 18, 42, tzinfo=tzutc()), name='T2', unit='µs', value=14.434181519378738), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=5.028370622843613), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.047800000000000065)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=23.275031085884514), Nduv(date=datetime.datetime(2019, 7, 19, 6, 19, 43, tzinfo=tzutc()), name='T2', unit='µs', value=49.21642747583066), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=5.06718706742364), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.059599999999999986)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=61.45084084697073), Nduv(date=datetime.datetime(2019, 7, 19, 6, 20, 42, tzinfo=tzutc()), name='T2', unit='µs', value=78.1629688631431), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=4.923902084183442), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.048799999999999955)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=47.88578036667165), Nduv(date=datetime.datetime(2019, 7, 19, 6, 21, 42, tzinfo=tzutc()), name='T2', unit='µs', value=77.57411285221376), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=4.974592665321239), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.05699999999999994)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=52.1077299749745), Nduv(date=datetime.datetime(2019, 7, 19, 6, 18, 42, tzinfo=tzutc()), name='T2', unit='µs', value=95.58512361131682), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=4.739556168567215), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.04069999999999996)], [Nduv(date=datetime.datetime(2019, 7, 18, 6, 27, 24, tzinfo=tzutc()), name='T1', unit='µs', value=46.45477114414843), Nduv(date=datetime.datetime(2019, 7, 19, 6, 20, 42, tzinfo=tzutc()), name='T2', unit='µs', value=53.1906035654724), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=4.96341864859716), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.05030000000000001)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=40.99452808851492), Nduv(date=datetime.datetime(2019, 7, 19, 6, 19, 43, tzinfo=tzutc()), name='T2', unit='µs', value=57.446823863062804), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=4.9450638633226776), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.058699999999999974)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=53.32345170589069), Nduv(date=datetime.datetime(2019, 7, 19, 6, 20, 42, tzinfo=tzutc()), name='T2', unit='µs', value=95.94073783089142), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=5.004998659157227), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.026799999999999935)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=65.66165564720977), Nduv(date=datetime.datetime(2019, 7, 19, 6, 19, 43, tzinfo=tzutc()), name='T2', unit='µs', value=109.72244978184753), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=4.760049758926836), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.04600000000000004)], [Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 29, tzinfo=tzutc()), name='T1', unit='µs', value=19.08344673433371), Nduv(date=datetime.datetime(2019, 7, 19, 6, 18, 42, tzinfo=tzutc()), name='T2', unit='µs', value=35.14960752601085), Nduv(date=datetime.datetime(2019, 7, 19, 8, 19, 57, tzinfo=tzutc()), name='frequency', unit='GHz', value=4.96849476694589), Nduv(date=datetime.datetime(2019, 7, 19, 6, 17, 3, tzinfo=tzutc()), name='readout_error', unit='', value=0.0726)]])


To see your last 5 jobs ran on the backend use the ``jobs()`` method of
that backend

.. code:: python

    for ran_job in backend.jobs(limit=5):
        print(str(ran_job.job_id()) + " " + str(ran_job.status()))


.. code-block:: text

    5d2de07868f1450019050c17 JobStatus.DONE
    5d2cf4c3ab759a0019f9418a JobStatus.DONE
    5d2cf4c11f1f6d00182d15ee JobStatus.DONE
    5d2cf4c0499a6c0018fe5066 JobStatus.DONE
    5d2cf1d168f1450019050be1 JobStatus.DONE


A job can be retrieved using ``retrieve_job(job_id())`` method

.. code:: python

    job = backend.retrieve_job(ran_job.job_id())



The Job
-------

Job instances can be thought of as the “ticket” for a submitted job.
They find out the execution’s state at a given point in time (for
example, if the job is queued, running, or has failed), and also allow
control over the job. They have the following methods:

-  ``status()`` - returns the status of the job.
-  ``backend()`` - returns the backend the job was run on.
-  ``job_id()`` - gets the job_id.
-  ``cancel()`` - cancels the job.
-  ``result()`` - gets the results from the circuit run.

IBM Q only functions include:

-  ``creation_date()`` - gives the date at which the job was created.
-  ``queue_position()`` - gives the position of the job in the queue.
-  ``error_message()`` - gives the error message of failed jobs.

Let’s start with the ``status()``. This returns the job status and a
message

.. code:: python

    job.status()


.. code-block:: text

    <JobStatus.DONE: 'job has successfully run'>


To get a backend object from the job use the ``backend()`` method

.. code:: python

    backend_temp = job.backend()
    backend_temp


.. code-block:: text

    <IBMQBackend('ibmq_16_melbourne') from IBMQ(hub='ibm-q', group='open', project='main')>


To get the job_id use the ``job_id()`` method

.. code:: python

    job.job_id()


.. code-block:: text

    '5c1a2e4228983e0059e42862'


To get the result from the job use the ``result()`` method

.. code:: python

    result = job.result()
    counts = result.get_counts()
    print(counts)


.. code-block:: text

    {'01': 89, '10': 87, '11': 454, '00': 394}


If you want to check the creation date use ``creation_date()``

.. code:: python

    job.creation_date()


.. code-block:: text

    '2018-12-19T11:40:50.890Z'


Let’s make an active example

.. code:: python

    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
    from qiskit import compile

.. code:: python

    qr = QuantumRegister(3)
    cr = ClassicalRegister(3)
    circuit = QuantumCircuit(qr, cr)
    circuit.x(qr[0])
    circuit.x(qr[1])
    circuit.ccx(qr[0], qr[1], qr[2])
    circuit.cx(qr[0], qr[1])
    circuit.measure(qr, cr)


.. code-block:: text

    <qiskit.circuit.instructionset.InstructionSet at 0xa16872080>


To execute this circuit on the backend use the ``execute`` function. It
will internally transpile the circuit to run on the given backend, send it
to the device, and return the corresponding job instance.

.. code:: python

    job = execute(circuit, backend=backend, shots=1024)

The status of this job can be checked with the ``status()`` method

.. code:: python

    job.status()

.. code-block:: text

    <JobStatus.INITIALIZING: 'job is being initialized'>



If you made a mistake and need to cancel the job use the ``cancel()``
method.

.. code:: python

    job.cancel()


.. code-block:: text

    True


The ``status()`` will show that the job cancelled.

.. code:: python

    job.status()


.. code-block:: text

    <JobStatus.CANCELLED: 'job has been cancelled'>

If the job status is ``<JobStatus.QUEUED: 'job is queued'>`` then the queue
position is available from the  ``queue_position()`` method.

.. code:: python

    result = job.queue_position()


.. code-block:: text

    4

There is also built-in functionality for automatically monitoring a job:

.. code:: python

    from qiskit.tools.monitor import job_monitor
    job_monitor(job)
    result = job.result()


.. code-block:: text

    Job Status: job is queued (6)

If a job is successful, ``<JobStatus.DONE: 'job has successfully run'>``, the
``result()`` method of a job retrieves the results of a computation from
which the requested information can be retrieved.

.. code:: python

    counts = job.result().get_counts()
    print(counts)


.. code-block:: text

    {'001': 270, '000': 76, '100': 47, '011': 131, '010': 71, '101': 143, '110': 58, '111': 228}
