User Config Files
=================

When using Qiskit Terra there are several aspects of the library where Terra
has opinionated defaults. These defaults are normally in the interest of
supporting the least common demonitator between users. For example, the default
backend for ``qiskit.visualization.circuit_drawer()``/``QuantumCircuit.draw()``
is the text backend. However, depending on your local environment you may want
to change these defaults to something better suited for your use case. This is
what the user config file can be used for. It lets you optionally specify
local defaults for these things


Creating a User Config File
---------------------------

By default the user config file should be located in
``~/.qiskit/settings.conf``. It is a ``.ini`` file that lists any options you'd
like to change the defaults on. Right now there is only one supported option,
``circuit_drawer`` which is used to set the default backend used when running
the circuit drawer.

For example, a ``settings.conf`` file with all the options set would look
like::

    [default]
    circuit_drawer = mpl

In this file when you call the circuit drawer the default output will be
``'mpl'`` instead of ``'text'``. You can use any of the valid circuit drawer
backends as the value for this config, this includes ``text``, ``mpl``,
``latex``, and ``latex_source``. These are the only valid values for the
``circuit_drawer`` field.

Alternative Locations for a User Config File
--------------------------------------------

The default location for the user config file is ``~/.qiskit/settings.conf``
but if you want to store your user config file in a different location you
can specify this with the ``QISKIT_SETTINGS`` environment variable. When
``QISKIT_SETTINGS`` is set Qiskit Terra will try to use the value as the path
to the user config file.
