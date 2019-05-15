:orphan:

.. _Transpilation Passes:

====================
Transpilation Passes
====================

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
