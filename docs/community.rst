Community Extensions
====================

Qiskit has been designed with modularity in mind. It is extensible in many
different ways; on the page, we highlight the ways in which the Qiskit community
has engaged with Qiskit and developed extensions and packages on top of it.

Backend Providers
-----------------

The Qiskit base provider is an entity that provides access to a group
of different backends (for example, backends available through IBM Q).
It interacts with those backends to do many things: find out which ones
are available, retrieve an instance of a particular backend, get backend
properties and configurations, and handling running and working with jobs.

Additional providers
~~~~~~~~~~~~~~~~~~~~

- **Decision diagram-based quantum simulator**

    - **Organization:** Johannes Kepler University, Linz, Austria (Alwin
      Zulehner and Robert Wille)
    - **Description:** A local provider which allows Qiskit to use decision
      diagram-based quantum simulation
    - **Qiskit Version:** 0.7
    - **More info:**  `Webpage at JKU <http://iic.jku.at/eda/research/
      quantum_simulation>`__, `Medium Blog <https://medium.com/qiskit/classical-simulators-for-quantum-computers-4b994dad4fa2>`_ and `Github Repo <https://
      github.com/Qiskit/qiskit-jku-provider>`__

- **Quantum Inspire**

    - **Organization:** QuTech-Delft
    - **Description:** A provider for the Quantum Inspire backend
    - **Qiskit Version:** 0.7
    - **More info:** `Medium Blog
      <https://medium.com/qiskit/quantum-inspire-and-qiskit-f1be608f8955>`__
      and `Github <https://github.com/QuTech-Delft/quantuminspire>`__.



Circuit Optimization
--------------------

Circuit optimization is at the heart of making quantum computing feasible on actual hardware.
A central component of Qiskit is the transpiler, which is a framework for manipulating
quantum circuits according to certain transformations (known as transpiler passes). The transpiler
enables users to create customized sets of passes, orchestrated by a pass manager, to transform
the circuit according to the rules specified by the passes. In addition, the transpiler architecture
is designed for modularity and extensibility, enabling Qiskit users to write their own passes,
use them in the pass manager, and combine them with existing passes. In this way,
the transpiler architecture opens up the door for research into aggressive optimization
of quantum circuits.


Additional passes
~~~~~~~~~~~~~~~~~
- **t|ket〉 optimization & routing pass**

    - **Organization:** Cambridge Quantum Computing
    - **Description:** Transpiler pass for circuit optimization and mapping
      to backend using CQC's t|ket〉compiler.
    - **Qiskit Version:** 0.7
    - **More info:** `Tutorial Notebook <https://github.com/Qiskit/qiskit-tutorials/
      blob/master/community/aqua/chemistry/QSE_pytket.ipynb>`_  and `Github <https://
      github.com/CQCL/pytket>`_.

Tools
-----

Extending Qiskit with new tools and functionality is an important part
of building a community. These tools can be new visualizations, slack integration,
Juypter extensions and much more.

Additional Tools
~~~~~~~~~~~~~~~~
* **OpenControls library**

    - **Organization:** Q-CTRL
    - **Description:** Library of quantum control pulses derived from the open literature.
    - **Qiskit Version:** 0.7
    - **More info:**  `Github <https://github.com/qctrl/python-open-controls>`__
      and `Q-CTRL website <https://q-ctrl.com/products/open-controls/>`_
