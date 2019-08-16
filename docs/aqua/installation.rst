.. _aqua-installation:

===========================
Installing Qiskit Aqua
===========================

Aqua can be used as a tool to execute `quantum algorithms <#quantum-algorithms.html>`__.
With the appropriate input, a quantum algorithm will run on top of the underlying
`Terra <https://qiskit.org/terra>`__
platform, which will compile and execute circuits from Aqua modeling the input problem.
Aqua can also be used as the foundation for domain-specific applications, such as
:ref:`aqua-chemistry`, :ref:`aqua-finance`, :ref:`aqua-ai` and :ref:`aqua-optimization`.
This section describes how to install and setup Aqua.

------------
Installation
------------

The best way to install Aqua, when the goal is to use it as a tool or as a library
of quantum algorithms, is via the `pip <https://pip.pypa.io/en/stable/>`__
package management system. Qiskit provides a meta-package that installs the set of
Qiskit Elements, including Qiskit Aqua and its domain code for Chemistry, Finance, AI
and Optimization.

Please see :doc:`/install` for detailed installation instructions

---------------------------------
Installing Qiskit-Aqua Standalone
---------------------------------

While we recommend following the prior installation section above, it is possible
to install Qiskit Aqua directly, which will also install its dependencies such
as Qiskit-Terra and Qiskit-Ignis, but it will not install other optional aspects such as
qiskit-aer and qiskit-ibmq-provider.

.. code:: sh

    pip install qiskit-aqua

pip will handle all dependencies automatically and you will always
install the latest (and well-tested) release version.

----------------------
Installing from Source
----------------------

A different class of users --- namely, quantum researchers and developers --- might be more
interested in exploring the source code of Aqua and :ref:`aqua-extending` by providing
new components, such as :ref:`quantum-algorithms`, :ref:`optimizers`, :ref:`variational-forms`,
:ref:`iqfts`, :ref:`oracles` and :ref:`initial-states`.

If you want to explore the code more directly and experiment with it, and even contribute
to the Qiskit community by developing and contributing code then you should work with
clones of the master branches of the Qiskit repositories. For detailed instructions on how
to do this see :ref:`Build Qiskit packages from source <install_install_from_source_label>`.
