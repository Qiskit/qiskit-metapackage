.. _multiclass-extensions:

====================
Multiclass Extension
====================

Both the Quantum Support Vector Machine (QSVM) and
Variational Quantum Classifier (vqc) algorithms, as well as the
Support Vector Machine Radial Basis Function Kernel (SVM RBF Kernel) classical algorithm
integrated into Aqua for generation of reference values,
come with built-in binary classifiers. Aqua includes
the ``MulticlassExtension`` pluggable interface for QSVM and SVM RBF Kernel,
allowing for various multiclass classification
extension algorithms to be included.

.. topic:: Extending the Multiclass Extension  Library

    Consistent with its unique  design, Aqua has a modular and
    extensible architecture. Algorithms and their supporting objects, such as multiclass extensions for
    SVM algorithms,
    are pluggable modules in Aqua.
    New multiclass extensions are typically installed in the ``qiskit_aqua/components/multiclass_extensions``
    folder and derive from the ``MulticlassExtension`` class.
    Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new components can register themselves
    as Aqua extensions and be dynamically discovered at run time independent of their
    location in the file system.
    This is done in order to encourage researchers and
    developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research contributions.

Currently, Aqua supplies the following multiclass classification extension algorithms:

- :ref:`one-against-rest`
- :ref:`all-pairs`
- :ref:`error-correcting-code`

.. _one-against-rest:

----------------
One Against Rest
----------------

For an :math:`n`-class problem, the *one-against-rest*  method constructs
:math:`n` SVM  classifiers, with the :math:`i`-th classifier separating
class :math:`i` from all the remaining classes, :math:`\forall i \in \{1, 2, \ldots, n\}`.
When the :math:`n` classifiers are combined
to  make  the  final  decision,  the  classifier that generates  the
highest  value  from  its  decision  function  is  selected  as  the
winner and the corresponding class label is returned.

In order to instantiate a ``OneAgainstRest`` object, you need to provide a ``FeatureMap`` and
an ``Estimator`` object representing the binary classifier to be used.  The ``FeatureMap`` is
required only for the QSVM algorithm -- not by the SVM RBF Kernel classical algorithm.

.. topic:: Declarative Name

   When referring to the one-against-rest method declaratively inside Aqua, its code ``name``, by
   which Aqua dynamically discovers and loads it, is ``OneAgainstRest``.

.. _all-pairs:

---------
All Pairs
---------

In the *all-pairs* reduction, one trains :math:`k(k−1)/2` binary classifiers for a :math:`k`-way
multiclass problem; each receives the samples of a pair of classes from the original training set,
and must learn to distinguish these two classes. At prediction time, a *weighted voting scheme* is
used: all :math:`k(k−1)/2` classifiers are applied to an unseen sample, and each class gets
assigned the sum of all the scores obtained by the various classifiers.  The combined classifier
returns as a result the class getting the highest value.

In order to instantiate an ``AllPairs`` object, you need to provide a ``FeatureMap`` and
an ``Estimator`` object representing the binary classifier to be used.  The ``FeatureMap`` is
required only for the QSVM algorithm -- not by the SVM RBF Kernel classical algorithm.

.. topic:: Declarative Name

   When referring to the all-pair method declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it, is ``AllPairs``.

.. _error-correcting-code:

---------------------
Error Correcting Code
---------------------

Error Correcting Code (ECC) is an ensemble method designed for the
multiclass classification problem.  As for the other methods, the task
is to decide one label from :math:`k > 2` possible choices.

.. table::

    +-------+-----------------------------------------------------------------------------------+
    |       |                                     Code Word                                     |
    + Class +-------------+-------------+-------------+-------------+-------------+-------------+
    |       | :math:`f_0` | :math:`f_1` | :math:`f_2` | :math:`f_3` | :math:`f_4` | :math:`f_5` |
    +-------+-------------+-------------+-------------+-------------+-------------+-------------+
    |   1   |      0      |      1      |      0      |      1      |      0      |      1      |
    +-------+-------------+-------------+-------------+-------------+-------------+-------------+
    |   2   |      1      |      0      |      0      |      1      |      0      |      0      |
    +-------+-------------+-------------+-------------+-------------+-------------+-------------+
    |   3   |      1      |      1      |      1      |      0      |      0      |      0      |
    +-------+-------------+-------------+-------------+-------------+-------------+-------------+

The table above shows a 6-bit ECC for a 3-class problem.
Each class is assigned a unique binary string of length 6.  The string is also
called  a  *codeword*.   For  example,  class  2  has codeword ``100100``.
During training, one binary classifier is learned for each column.  For example,
for the first column, ECC builds a binary classifier to separate :math:`\{2, 3\}` from
:math:`\{1\}`.  Thus, 6 binary classifiers are trained in this way.  To classify a
new data point :math:`\mathbf{x}`, all 6 binary classifiers are evaluated to obtain a 6-bit string.
Finally, we choose the class whose bitstring is closest to
:math:`\mathbf{x}`’s output string as the predicted label.  Aqua's implementaion of ECC
uses the Euclidean distance.

In order to instantiate an ``ErrorCorrectingCode`` object, you need to provide a ``FeatureMap``,
an ``Estimator`` object representing the binary classifier to be used, and a ``code_size`` positive
integer parameter representing the length of the bitstrings.  The ``FeatureMap`` is required only
for the QSVM algorithm -- not by the SVM RBF Kernel classical algorithm.

.. topic:: Declarative Name

    When referring to the error-correcting code algorithm declaratively inside Aqua,
    its code ``name``, by which Aqua dynamically discovers and loads it,
    is ``ErrorCorrectingCode``.
