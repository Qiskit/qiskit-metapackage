:orphan:

.. _Transpilation Passes:

====================
Transpilation Passes
====================

Circuit optimization is a difficult task (in general QMA-complete). Each
**transpiler pass** (circuit transformation) is responsible for doing one small,
well-defined task to make the overall task of circuit optimization tractable.

Circuits are internally represented by **directed acyclic graphs** (**DAGs**) in
Qiskit. Transpiler passes are transformations of a circuit's DAG representation.

There are two general classes of transpiler passes:

- ``AnalysisPass`` analyze a DAG and write
  conclusions to a common context, a ``PropertySet`` object. They cannot modify
  a DAG.
- ``TransformationPass`` can alter a DAG, but have read-only access to the
  property set.

Concrete transpiler passes derived from either of the classes above implement
the abstract method ``run()``, which takes and returns a DAG.

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
