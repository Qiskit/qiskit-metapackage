:orphan:

.. _Transpilation Passes:

====================
Transpilation Passes
====================

- Passes run with the implementation of the abstract method ``run``, which
  takes and returns a DAG (directed acyclic graph) representation of the
  circuit.
- Passes are instances of either ``AnalysisPass`` or ``TransformationPass``.
- Passes are described not just by their class, but also by their parameters
- Analysis passes analyze the DAG and write conclusions to a common context, a
  ``PropertySet`` object. They cannot modify the DAG.
- Transformation passes can alter the DAG, but have read-only access to the
  property set.

All of Qiskit's transpiler passes are accessible from
``qiskit.transpiler.passes``.

.. code:: python

  from qiskit.transpiler import passes
  [pass_ for pass_ in dir(passes) if pass_[0].isupper()]

.. parsed-literal::

  ['BarrierBeforeFinalMeasurements',
   'BasicSwap',
   'CXCancellation',
   'CXDirection',
   'CheckCXDirection',
   'CheckMap',
   'Collect2qBlocks',
   'CommutationAnalysis',
   'CommutativeCancellation',
   'ConsolidateBlocks',
   'CountOps',
   'DAGFixedPoint',
   'Decompose',
   'DenseLayout',
   'Depth',
   'EnlargeWithAncilla',
   'FixedPoint',
   'FullAncillaAllocation',
   'LegacySwap',
   'LookaheadSwap',
   'MergeAdjacentBarriers',
   'NoiseAdaptiveLayout',
   'NumTensorFactors',
   'Optimize1qGates',
   'OptimizeSwapBeforeMeasure',
   'RemoveDiagonalGatesBeforeMeasure',
   'RemoveResetInZeroState',
   'ResourceEstimation',
   'SetLayout',
   'Size',
   'StochasticSwap',
   'TrivialLayout',
   'Unroll3qOrMore',
   'Unroller',
   'Width']
