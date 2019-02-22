.. _reciprocals:

===========
Reciprocals
===========

Aqua bundles methods to invert a fixed-point number prepared in a quantum register in the
Reciprocals library. Rather than being used as a standalone algorithm, the members of the library
are to be used in a larger algorithm such as :ref:`HHL`. The following methods are available

- :ref:`lookup`

- :ref:`longdivision`

.. topic:: Extending the Reciprocals Library

    Consistent with its unique  design, Aqua has a modular and
    extensible architecture. Algorithms and their supporting objects, such as optimizers for quantum variational algorithms,
    are pluggable modules in Aqua.
    New eigenvalue solver are typically installed in the ``qiskit_aqua/components/reciprocals`` folder and derive from
    the ``Reciprocal`` class.  Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new methods to calculate the reciprocal can register themselves
    as Aqua extensions and be dynamically discovered at run time independent of their
    location in the file system.
    This is done in order to encourage researchers and
    developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research contributions.


.. _lookup:

---------------------
Partial Table Look Up
---------------------

This method applies a variable sized binning to the values. Only a specified number of bits after
the most-significant bit is taken into account when assigning rotation angles to the numbers
prepared as states in the input register. Using precomputed angles, the reciprocal is multiplied
to the amplitude via controlled rotations. While no resolution of the result is lost for small
values, towards larger values the bin size increases. The accuracy of the result is tuned by the
parameters. The following parameters are exposed:

- The number of bits used to approximate the numbers:

  .. code:: python

      pat_length : int

  Specifies the number of bits following the most-significant bit that is used to identify a
  number. This leads to a binning of large values, while preserving the accuracy for smaller
  values. It should be chosen as :math:`min(k-1,5)` for an input register with k qubits to limit
  the error in the rotation to < 3%.

- The length of a sub string of the binary identifier:

  .. code:: python

      subpat_length : int

  This parameter is computed in the circuit creation routine and helps reducing the gate count.
  For ``pat_length<=5`` it is chosen as :math:`\left\lceil(\frac{patlength}{2})\right\rceil`.

- Switch for negative values:

  .. code:: python

      negative_evals : bool

  If known beforehand that only positive values are present, one can set this switch to False and
  achieve a higher resolution in the output. The default is ``True``.

- The scale factor of the values:

  .. code:: python

      scale : float

 This parameter is used to scale the reciprocals such that for a scale C, the rotation is performed
 by an angle :math:`\arcsin{\frac{C}{\lambda}}`. If neither the ``scale`` nor the ``evo_time`` and
 ``min_lambda`` parameters are specified, the smallest resolvable Eigenvalue is used.

- The mimimum value present:

  .. code:: python

      lambda_min : float

  If the minimum value is known beforehand, the optimal ``scale`` parameter can be calculated using
  the parameters ``lambda_min`` and ``evo_time``.

- The evolution time:

  .. code:: python

      evo_time : float

  This parameter scales the Eigenvalues in the :ref:`qpe_components` onto the range (0,1]
  ( (-0.5,0.5] for negativ EV ). If the Partial Table Look Up is used together with the QPE, the
  scale parameter can be estimated if the minimum EV and the evolution time are passed as
  parameters. The default is ``None``.

.. topic:: Declarative Name

   When referring to Look Up declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it, is ``Lookup``.


.. _longdivision:

-------------
Long Division
-------------

This method calculates inverse of eigenvalues using binary long division and performs the
corresponnding rotation. Long division is implemented as a sequance of subtraction (utilizing
ripple carry adder module) and bit shifting. The method allows for adjusting of the reciprocal
precision by changing number of iterations. The method was optimized for register conventions
used in HHL algorithm (i.e. eigenvalues rescaled to values between 0 and 1).

The rotation value is always scaled down additionally to the normal scale parameter by 0.5 to get
the angle into the linear part of the arcsin(x). The following parameters are exposed:

- The scale factor of the values:

  .. code:: python

      scale : float

This parameter is used to scale the reciprocals such that for a scale C, the rotation is performed
by an angle :math:`\arcsin{\frac{C}{\lambda}}`. If neither the ``scale`` nor the ``evo_time`` and
``min_lambda`` parameters are specified, the smallest resolvable Eigenvalue is used.

-  The number of ancillae:

   .. code:: python

       num_ancillae = 3 | 4 | ...

This parameter sets the number of ancillary qubits (the input register size).  A positive ``int``
value is expected. The default value is ``None`` and the minimum value ``3``. If negative
eigenvalues are enabled, the minimum value is ``4 ``The default is ``0``.

- Switch for negative values:

  .. code:: python

     negative_evals : bool

  If known beforehand that only positive values are present, one can set this switch to False and
  achieve a higher resolution in the output. The default is ``True``.

- The mimimum value present:

  .. code:: python

      lambda_min : float

  If the minimum value is known beforehand, the optimal ``scale`` parameter can be calculated
  using the parameters ``lambda_min`` and ``evo_time``.

- The evolution time:

  .. code:: python

     evo_time : float

  This parameter scales the Eigenvalues in the :ref:`qpe_components` onto the range (0,1]
  ( (-0.5,0.5] for negativ EV ). If the Partial Table Look Up is used together with the QPE, the
  scale parameter can be estimated if the minimum EV and the evolution time are passed as
  parameters. The default is ``None``.

- The Reciprocal precision:

  .. code:: python

     precision : int

The parameter sets minimum desired bit precision for the reciprocal. Due to shifting some of
reciprocals, however, are effectively estimated with higher than this minimum specified precision.

.. topic:: Declarative Name

   When referring to Long Division declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it, is ``LongDivision``.
