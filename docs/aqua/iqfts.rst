.. _iqfts:

==========================
Quantum Fourier Transforms
==========================

In quantum computing, a Quantum Fourier Transform (QFT) is a linear transformation
on quantum bits, and is the quantum analogue of the discrete Fourier transform.
QFT is a part of many quantum algorithms, such as Shor's algorithm for factoring
and computing the discrete logarithm, and the :ref:`QPE` algorithm for
estimating the eigenvalues of a unitary operator.
A QFT can be performed efficiently on a quantum computer, with a particular
decomposition into a product of simpler unitary matrices.
`It has been shown <http://csis.pace.edu/ctappert/cs837-18spring/QC-textbook.pdf>`__ how,
using a simple decomposition,
the discrete Fourier transform on :math:`2^n` amplitudes can be implemented as a
quantum circuit consisting of only :math:`O(n^2)` Hadamard gates and controlled phase
shift gates, where :math:`n` is the number of qubits, in contrast
with the classical discrete Fourier transform, which takes :math:`O(n2^n)`
gates, where in the classical case :math:`n` is the number of bits.
`The best quantum Fourier transform algorithms currently known \
<https://pdfs.semanticscholar.org/deff/d6774d409478734db5f92011ff66bebd4a05.pdf>`__
require only :math:`O(n\log n)` gates to achieve an efficient approximation.

Most of the properties of the QFT follow from the fact that it is a unitary
transformation. This implies that, if :math:`F` is the matrix representing the QFT,
then :math:`FF^\dagger = F^{\dagger}F=I`, where :math:`F^\dagger` is the Hermitian
adjoint of :math:`F` and :math:`I` is the identity matrix.
It follows that :math:`F^{-1} = F^\dagger`.
Since there is an efficient quantum circuit implementing the QFT, the circuit can be
run in reverse to perform the Inverse Quantum Fourier Transform (IQFT).
Thus, both transforms can be efficiently performed on a quantum computer.

As mentioned above, the :ref:`QPE` algorithm uses the QFT for estimating the eigenvalues
of a unitary operator.  More precisely, QPE uses the Inverse Quantum Fourier Transform
(IQFT).  IQFTs in Aqua are pluggable objects.  Among the IQFTs provided by Aqua, the user
can choose which IQFT to use when instantiating QPE or any other algorithm that requires
the use of an IQFT.  Furthermore, researchers interested in contributing new algorithms to
Aqua can plug their own IQFT implementation.

Although discussions below focus on IQFT, the similar also apply for QFT.


.. topic:: Extending the IQFT Library

    Consistent with its unique  design, Aqua has a modular and
    extensible architecture. Algorithms and their supporting objects, such as IQFTs,
    are pluggable modules in Aqua. This is done in order to encourage researchers and
    developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research contributions.
    New IQFTs are typically installed in the ``qiskit/aqua/components/iqfts``
    folder and derive from the ``IQFT`` class.  Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new IQFTs can register themselves
    as Aqua extensions and be dynamically discovered at run time independent of their
    location in the file system.

Aqua comes with two IQFTs:

1.  `Standard IQFT <#standard-iqft>`__
2.  `Approximate IQFT <#approximate-iqft>`__

The ``iqft`` section in the :ref:`aqua-input-file` becomes relevant
only for algorithms that require an IQFT.  This is reflected also in the
:ref:`aqua-gui`, which enables the ``iqft`` section for the IQFT configuration
only when an algorithm requiring an IQFT is selected.  When the ``iqft`` section is
indeed enabled, then the user can choose which IQFT to apply by assigning a ``str`` value
to the ``name`` field of the ``iqft`` section.

-------------
Standard IQFT
-------------

The standard version of the IQFT is simply the inverse of a plain QFT.
It generates the inverse of a QFT circuit with no approximation.
The standard IQFT takes no parameters and is not configurable.

.. topic:: Declarative Name

    When referring to the standard IQFT declaratively inside Aqua, its code ``name``,
    by which Aqua dynamically discovers and loads it, is ``STANDARD``.

----------------
Approximate IQFT
----------------

This form of IQFT generates the inverse of an Approximate
Quantum Fourier Transform (AQFT) as described in
`arXiv:1803.04933 <https://arxiv.org/abs/1803.04933>`__.
The degree of approximation can be configured using the following parameter:

.. code:: python

    degree = 0 | 1 | ...

This parameter controls the level of approximation of the IQFT,
expressed as a non-negative ``int`` value.
The value provided will reduce the depth of neighbor terms allowed in the
IQFT circuit. The default value is ``0``, which results in no approximation --- in which
case the resulting IQFT is exactly the same as the `standard IQFT <#standard-iqft>`__.
Each value above ``0``, however ,
reduces by the corresponding amount the range of the neighbor terms allowed,
which in turn reduces the circuit complexity.

.. topic:: Declarative Name

    When referring to the approximate IQFT declaratively inside Aqua, its code ``name``,
    by which Aqua dynamically discovers and loads it, is ``APPROXIMATE``.
