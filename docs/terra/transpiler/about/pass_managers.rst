.. _Pass Managers:

=============
Pass Managers
=============

- A ``PassManager`` instance determines the schedule for running registered
  passes.
- The pass manager is in charge of deciding the next pass to run, not the pass
  itself.
- Registering passes in the pass manager pipeline is done by the ``append``
  method.
- While registering, you can specify basic control primitives over each pass
  (conditionals and loops).
- Options to control the scheduler:

	- Passes can have arguments at init time that can affect their scheduling. If
    you want to set properties related to how the pass is run, you can do so by
    accessing these properties (e.g. ``pass_.max_iteration = 10``).
	- Options set from the pass manager take more precedence over those set at
    the time of adding a pass set, and those take more precedence over the
    options of each individual pass. (see [tests](https://github.com/Qiskit/
    qiskit-terra/master/test/transpiler/test_pass_scheduler.py))

All of Qiskit's transpiler pass managers are accessible from
``qiskit.transpiler``. The PassManager class is documented :py:mod:`here
<qiskit.transpiler.passmanager>`.
