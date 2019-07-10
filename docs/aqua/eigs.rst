.. _eigs:

===========
Eigenvalues
===========

Aqua bundles methods to find Eigenvalues of a given matrix, such as
:ref:`eigsqpe_component` in the Eigs library. Rather than being used as a
standalone algorithm, the members of the library are to be used in a larger
algorithm such as :ref:`HHL`. The following methods are available

 * :ref:`eigsqpe_component`: Given a matrix and a linear combination of its
   eigenstates, *QPE* prepares the Eigenvalues on a specified output register.

.. topic:: Extending the Eigs Library

    Consistent with its unique  design, Aqua has a modular and extensible
    architecture. Algorithms and their supporting objects, such as optimizers
    for quantum variational algorithms, are pluggable modules in Aqua. New
    eigenvalue solvers are typically installed in the
    ``qiskit/aqua/components/eigs`` folder and derive from the
    ``Eigenvalues`` class.  Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new Eigenvalue estimator can
    register themselves as Aqua extensions and be dynamically discovered at
    run time independent of their location in the file system. This is done
    in order to encourage researchers and developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research
    contributions.


.. seealso::

    Section :ref:`aqua-extending` provides more
    details on how to extend Aqua with new components.


.. _eigsqpe_component:

-------
EigsQPE
-------
This Eigenvalue solver component is directly based on the QPE quantum
algorithm in Aqua :ref:`qpe`. Some changes have been made to support negative
eigenvalues and use it in a larger quantum algorithm (e.g. :ref:`hhl`).

.. seealso::

    Section :ref:`qpe` provides more
    details on the QPE algorithm.

In addition to requiring an IQFT and an initial state as part of its
configuration, QPE also exposes the following parameter settings:

-  The number of time slices:

   .. code:: python

       num_time_slices = 0 | 1 | ...

   This has to be a non-negative ``int`` value.  The default value is ``1``.

-  The expansion mode:

   .. code:: python

       expansion_mode = "trotter" | "suzuki"

   Two ``str`` values are permitted: ``"trotter"`` (Lloyd's method) or
   ``"suzuki"`` (for Trotter-Suzuki expansion), with  ``"trotter"`` being the
   default one.

-  The expansion order:

   .. code:: python

       expansion_order = 1 | 2 | ...

   This parameter sets the Trotter-Suzuki expansion order.  A positive
   ``int`` value is expected.  The default value is ``1``.

-  The number of ancillae:

   .. code:: python

       num_ancillae = 1 | 2 | ...

   This parameter sets the number of ancillary qubits to be used by QPE. A
   positive ``int`` value is expected. The default value is ``1``.

- The evolution time:

  .. code:: python

     evo_time : float

  This parameter scales the eigenvalue onto the range :math:`(0,1]` (:math:`(-0.5,0.5]`
  for negative eigenvalues). If not provided, it is calculated internally by
  using an estimation of the highest eigenvalue present in the matrix. The
  default is ``None``.

- Switch for negative eigenvalues:

  .. code:: python

     negative_evals : bool

  If known beforehand that only positive eigenvalues are present, one can set
  this switch to False and achieve a higher resolution in the output. The
  default is ``True``.

.. topic:: Declarative Name

   When referring to EigsQPE declaratively inside Aqua, its code ``name``, by
   which Aqua dynamically discovers and loads it, is ``EigsQPE``.

