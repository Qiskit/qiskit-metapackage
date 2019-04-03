========
Overview
========

----------------------------
Modularity and Extensibility
----------------------------

Aqua is a library of quantum algorithms specifically designed in order to be modular and extensible
at multiple levels.
This allows different users with different levels of experience and scientific interests
to contribute to, and extend, the Aqua software stack at different levels.

^^^^^^^^^^^^^^^^
Input Generation
^^^^^^^^^^^^^^^^

At the application level, Aqua allows for classical computational
software to be used as the quantum application front end.  This module is extensible;
new computational software can be easily plugged in.  Behind the scenes, Aqua lets that
software perform some initial computations classically.  The  results of those computations
are then combined with the problem
configuration and translated into input for one or more quantum algorithms, which invoke
the `Qiskit Terra <https://Qiskit.org/terra>`__ code APIs to build, compile and execute quantum circuits.

^^^^^^^^^^^^^^^^^
Input Translation
^^^^^^^^^^^^^^^^^

The problem configuration and (if present) the additional intermediate data
obtained from the classical execution of the computational software are
combined to form the input to the quantum system.  This phase, known as *translation*,
is also extensible.  Practitioners interested in providing more efficient
translation operators may do so by extending this layer of the Aqua software
stack with their own translation operator implementation.

^^^^^^^^^^^^^^^^^^
Quantum Algorithms
^^^^^^^^^^^^^^^^^^

Quantum algorithm researchers and developers can experiment with the algorithms already included
in Aqua, or contribute their own algorithms via the pluggable interface exposed
by Aqua.  In addition to plain quantum algorithms, Aqua offers a vast set
of supporting components, such as variational forms, local and global optimizers, initial states,
Quantum Fourier Transforms (QFTs) and Grover oracles.  These components are also extensible
via pluggable interfaces.

--------------
Novel Features
--------------

In addition to its modularity and extensibility, ability to span across multiple
domains, and top-to-bottom completeness from classical computational software to
quantum hardware, compared to other quantum software stacks, Aqua presents numerous unique
advantages in terms of usability, functionality, and configuration-correctness enforcement.

^^^^^^^^^^^^^^^
User Experience
^^^^^^^^^^^^^^^

Allowing classical computational software at the frontend has its own important advantages.
In fact, at the top of the Aqua software stack are industry-domain experts, who are most likely
very familiar with existing
computational software specific to their own domains.  These practitioners are probably interested
in experimenting with the benefits of quantum computing in terms of performance, accuracy
and reduction of computational complexity, but at the same time they might be
unwilling to learn about the underlying quantum infrastructure. Ideally,
such practitioners would like to use the computational software they are
familiar with as a front end to the quantum computing system,
without having to learn a new quantum programming
language or new APIs.  It is also
likely that such practitioners may have collected, over time, numerous
problem configurations, corresponding to various experiments. Aqua has been designed to accept those
configuration files  with no modifications, and
without requiring a practitioner experienced in a particular domain to
have to learn a quantum programming language. This approach has a clear advantage in terms
of usability.

^^^^^^^^^^^^^
Functionality
^^^^^^^^^^^^^

If Aqua had been designed to interpose a quantum programming language
or new APIs between the user and the classical computational software, it would not have been able
to fully exploit all the features of the underlying classical computational software unless
those features had been exposed at the higher programming-language or API level.  In other
words, in order to drive the classical execution of any interfaced computational
software to the most precise computation of the intermediate data needed to form
the quantum input, the advanced features of that software would have had to be configurable
through Aqua. Given the intention for Aqua to have an extensible interface capable of accepting
any classical computational software, the insertion of a quantum-specific programming language or
API would have been not only a usability obstacle, but also a functionality-limiting factor.
The ability of Aqua to directly interface classical computational software allows that software
to compute the intermediate data needed to form the quantum input at its highest level of precision.

^^^^^^^^^^^^^^^^^^^^^^^^^
Configuration Correctness
^^^^^^^^^^^^^^^^^^^^^^^^^

Aqua offers another unique feature. Given that Aqua
allows traditional software to be executed on a quantum system,
configuring an experiment in a particular domain may require a hybrid
configuration that involves both domain- and quantum-specific
configuration parameters whose values cannot be assigned in isolation from each other.
The chances of introducing configuration
errors, making typos, or selecting incompatible configuration parameters
are very high, especially for people who are expert in a given domain
but new to the realm of quantum computing. To address such issues, in
Aqua the problem-specific and
quantum-specific configuration data is dynamically verified for
correctness so that the combination of classical and quantum inputs is
resilient to configuration errors. Very importantly, configuration
correctness is dynamically enforced even for components that are
dynamically discovered and loaded.

.. include:: CONTRIBUTORS.rst

-------
License
-------

This project uses the `Apache License Version 2.0 software
license <https://www.apache.org/licenses/LICENSE-2.0>`__.
