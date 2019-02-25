Community Extensions
====================

Qiskit has been designed with modularity in mind. It is extensible in many
different ways and it is important to us to highlight the community projects

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

    - **Organization:** Alwin Zulehner and Robert Wille
      from Johannes Kepler University, Linz, Austria
    - **Description:** A local provider which allows Qiskit to use decision
      diagram-based quantum simulation
    - **Qiskit Version:** 0.7
    - **More info:**  `Webpage at JKU <http://iic.jku.at/eda/research/
      quantum_simulation>`_, `Medium Blog <blah>`_ and `Github Repo <https://
      github.com/Qiskit/qiskit-jku-provider>`_


Circuit Optimization
--------------------

Circuit optimization is at the heart of making quantum computing. A central
component of Qiskit is the transpiler, which is designed for modularity
and extensibility. The goal is to be able to easily write new circuit
transformations (known as transpiler passes) and combine them with other
existing passes. In this way, the transpiler opens up the door for research
into aggressive optimization of quantum circuits.


Additional passes
~~~~~~~~~~~~~~~~~


Tools
-----

Extending Qiskit with new tools and functionality is an important part
of building a community. These tools can be new visualizations, slack integration,
Juypter extensions and much more.

Additional Tools
~~~~~~~~~~~~~~~~
