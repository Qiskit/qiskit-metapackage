.. _optimizers:

==========
Optimizers
==========

Aqua  contains a variety of classical optimizers for
use by quantum variational algorithms, such as :ref:`vqe`.
Logically, these optimizers can be divided into two categories:

- :ref:`Local Optimizers`: Given an optimization problem, a *local optimizer* is a function that
  attempts to find an optimal value within the neighboring set of a candidate solution.

- :ref:`Global Optimizers`: Given an optimization problem, a *global optimizer* is a function that
  attempts to find an optimal value among all possible solutions.


.. topic:: Extending the Optimizer Library

    Consistent with its unique  design, Aqua has a modular and
    extensible architecture. Algorithms and their supporting objects, such as optimizers for quantum variational algorithms,
    are pluggable modules in Aqua.
    New optimizers for quantum variational algorithms are typically installed in the ``qiskit_aqua/utils/optimizers`` folder and derive from
    the ``Optimizer`` class.  Aqua also allows for
    :ref:`aqua-dynamically-discovered-components`: new optimizers can register themselves
    as Aqua extensions and be dynamically discovered at run time independent of their
    location in the file system.
    This is done in order to encourage researchers and
    developers interested in
    :ref:`aqua-extending` to extend the Aqua framework with their novel research contributions.

.. seealso::

    `Section :ref:`aqua-extending` provides more
    details on how to extend Aqua with new components.

.. _local-optimizers:

----------------
Local Optimizers
----------------

This section presents the classical local optimizers made available in Aqua.
These optimizers are meant to be used in conjunction with quantum variational
algorithms:

- :ref:`ADAM`
- :ref:`Analytic Quantum Gradient Descent (AQGD)`
- :ref:`Conjugate Gradient (CG) Method`
- :ref:`Constrained Optimization BY Linear Approximation (COBYLA)`
- :ref:`Limited-memory Broyden-Fletcher-Goldfarb-Shanno Bound (L-BFGS-B)`
- :ref:`Nelder-Mead`
- :ref:`Parallel Broyden-Fletcher-Goldfarb-Shann (P-BFGS)`
- :ref:`Powell`
- :ref:`Sequential Least SQuares Programming (SLSQP)`
- :ref:`Simultaneous Perturbation Stochastic Approximation (SPSA)`
- :ref:`Truncated Newton (TNC)`

Except for :ref:`ADAM`, :ref:`Analytic Quantum Gradient Descent (AQGD)` and
:ref:`Parallel Broyden-Fletcher-Goldfarb-Shann (P-BFGS)`, all these
optimizers are directly based on the ``scipy.optimize.minimize`` optimization function in the
`SciPy <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html>`__
Python library. They all have a common pattern for parameters. Specifically, the ``tol``
parameter, whose value must be a ``float`` indicating *tolerance for termination*,
is from the ``scipy.optimize.minimize``  method itself, while the remaining parameters are
from the `options
dictionary <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.show_options.html>`__,
which may be referred to for further information.

.. topic:: Transparent Parallelization of Gradient-based Local Opitmizers

   Aqua comes with a large collection of adaptive algorithms, such as the
   `Variational Quantum Eigensolver (VQE) algorithm <https://www.nature.com/articles/ncomms5213>`__,
   `Quantum Approximate Optimization
   Algorithm (QAOA) <https://arxiv.org/abs/1411.4028>`__, the `Quantum
   Support Vector Machine (SVM) Variational
   Algorithm <https://arxiv.org/abs/1804.11326>`__ for AI. All these
   algorithms interleave quantum and classical computations, making use of
   classical optimizers. Aqua includes nine local and five global
   optimizers to choose from. By profiling the execution of the adaptive
   algorithms, we have detected that a large portion of the execution time
   is taken by the optimization phase, which runs classically. Among the
   most widely used optimizers are the *gradient-based* ones; these
   optimizers attempt to compute the absolute minimum (or maximum) of a
   function :math:`f` through its gradient.

   Seven local optimizers among those integrated into Aqua are
   gradient-based: the four local optimizers *Limited-memory
   Broyden-Fletcher-Goldfarb-Shanno Bound (L-BFGS-B)*, *Sequential Least SQuares Programming
   (SLSQP)*, *Conjugate Gradient (CG)*, and *Truncated Newton (TNC)* from
   `SciPy <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html>`__,
   as well as `Simultaneous Perturbation Stochastic Approximation
   (SPSA) <https://www.jhuapl.edu/SPSA/>`__, *ADAM* and *Analytic Quantum Gradient Descent (AQGD)*.
   Aqua contains a methodology that parallelizes the classical computation of the partial
   derivatives in the gradient-based local optimizers listed above. This
   parallelization takes place *transparently*, in the sense that Aqua
   intercepts the computation of the partial derivatives and parallelizes
   it without making any change to the actual source code of the
   optimizers.

   In order to activate the parallelization mechanism for an adaptive
   algorithm included in Aqua, it is sufficient to construct it with
   parameter ``batch_mode`` set to ``True``. Our experiments have proven
   empirically that parallelizing the process of a gradient-based local
   optimizer achieves a 30% speedup in the execution time of an adaptive algorithms on
   a simulator.

.. _adam_amsgrad:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ADAM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ADAM is a gradient-based optimization algorithm that is relies on adaptive estimates of lower-order
moments. The algorithm requires little memory and is invariant to diagonal rescaling of the
gradients. Furthermore, it is able to cope with non-stationary objective functions and noisy
and/or sparse gradients. AMSGRAD (a variant of ADAM) uses a 'long-term memory' of past gradients
and, thereby, improves convergence properties.

Kingma, Diederik & Ba, Jimmy. (2014).
Adam: A Method for Stochastic Optimization. International Conference on Learning Representations.

Sashank J. Reddi and Satyen Kale and Sanjiv Kumar. (2018).
On the Convergence of Adam and Beyond. International Conference on Learning Representations.

The following parameters are supported:

-  The maximum number of iterations to perform.

   .. code:: python

       maxiter = 1 | 2 | ...

   This parameters takes a positive ``int`` value.  The default is ``20``.

-  The tolerance for termination.
   .. code:: python

        tol : float

   The default value is ``1e-06``.

-  The learning rate:
   .. code:: python

        lr : float

   The default value is ``1e-03``.

-  First hyper-parameter used for the evaluation of the first moment estimate.
   .. code:: python

        beta_1 : float

   The default value is ``0.9``.

-  Second hyper-parameter used for the evaluation of the second moment estimate.
   .. code:: python

        beta_2 : float

   The default value is ``0.99``.

-  Noise factor used for reasons of numerical stability.

   .. code:: python

        noise_factor : float

   The default value is ``1e-8``.

-  Step size used for numerical approximation of the Jacobian.

   .. code:: python

        eps : float

   The default value is ``1e-10``.

-  A Boolean value indicating whether or not to use the AMSGRAD variant.

   .. code:: python

        amsgrad : bool

   The default value is ``False``.


-  A string indicating a directory for storing optimizer's parameters. If ``None`` then
   the parameters will not be stored.

   .. code:: python

        snapshot_dir: str or None

   The default value is `''`.

.. topic:: Declarative Name

   When referring to ADAM declaratively inside Aqua, its code ``name``, by which Aqua dynamically
   discovers and loads it, is ``ADAM``.


.. _aqgd:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Analytic Quantum Gradient Descent (AQGD)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Analytic Quantum Gradient Descent (AQGD) performs gradient descent optimization with a momentum
term and analytic gradients for parametrized quantum gates, i.e. Pauli Rotations.
See e.g.:

K. Mitarai, M. Negoro, M. Kitagawa, and K. Fujii. (2018).
Quantum circuit learning.Phys. Rev. A 98, 032309.

Maria Schuld, Ville Bergholm, Christian Gogolin, Josh Izaac, Nathan Killoran. (2019).
Evaluating analytic gradients on quantum hardware. Phys. Rev. A 99, 032331.

for further details on analytic gradients of parametrized quantum gates.

The following parameters are supported:

-  The maximum number of iterations to perform.

   .. code:: python

       maxiter = 1 | 2 | ...

   This parameters takes a positive ``int`` value.  The default is ``1000``.

-  The learning rate:
   .. code:: python

        eta : float

   The default value is ``3.0``.

-  The tolerance for termination.
   .. code:: python

        tol : float

   The default value is ``1e-06``.


-  A Boolean value indicating whether or not to display convergence messages.

   .. code:: python

        disp : bool

   The default value is ``False``.


-  Bias towards the previous gradient momentum. Must be within the bounds: [0,1)
   .. code:: python

        momentum : float

   The default value is ``0.25``.

.. topic:: Declarative Name

   When referring to AQGD declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and
   loads it, is ``AQGD``.

----


.. _cg:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Conjugate Gradient (CG) Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
CG is an algorithm for the numerical solution of systems of linear equations whose matrices are
symmetric and positive-definite. It is an *iterative algorithm* in that it uses an initial guess
to generate a sequence of improving approximate solutions for a problem,
in which each approximation is derived from the previous ones.  It is often used to solve
unconstrained optimization problems, such as energy minimization.

The following parameters are supported:

-  The maximum number of iterations to perform:

   .. code:: python

       maxiter = 1 | 2 | ...

   This parameters takes a positive ``int`` value.  The default is ``20``.

-  A Boolean value indicating whether or not to print convergence messages:

   .. code:: python

        disp : bool

   The default value is ``False``.

-  A tolerance value that must be greater than the gradient norm before successful
   termination.

   .. code:: python

        gtol : float

   The default value is ``1e-05``.


-  The tolerance for termination:

   .. code::

        tol : float

   This parameter is optional.  If specified, the value of this parameter must be a ``float`` value,
   otherwise, it is set to ``None``.  The default is ``None``.

-  Step size used for numerical approximation of the Jacobian.

   .. code:: python

        eps : float

   The default value is ``1.4901161193847656e-08``.

.. topic:: Declarative Name

   When referring to CG declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``CG``.

.. _cobyla:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Constrained Optimization BY Linear Approximation (COBYLA)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

COBYLA is a numerical optimization method for constrained problems
where the derivative of the objective function is not known.
COBYLA supports the following parameters:

-  The maximum number of iterations to perform:

   .. code:: python

       maxiter = 1 | 2 | ...

   A positive ``int`` value is expected.  The default is ``1000``.

-  A Boolean value indicating whether or not to print convergence messages:

   .. code:: python

       disp : bool

   The default value is ``False``.

-  Reasonable initial changes to the variable:

   .. code:: python

       rhobeg : float

   The default value is ``1.0``.

-  The tolerance for termination:

   .. code::

        tol : float

   This parameter is optional.  If specified, the value of this parameter must be of type ``float``, otherwise, it is set to ``None``.
   The default is ``None``.

.. topic:: Declarative Name

   When referring to COBYLA declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``COBYLA``.

.. _l-bfgs-b:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Limited-memory Broyden-Fletcher-Goldfarb-Shanno Bound (L-BFGS-B)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The target goal of L-BFGS-B is to minimize the value of a differentiable scalar function :math:`f`.
This optimizer is a *quasi-Newton method*, meaning that, in contrast to *Newtons's method*, it
does not require :math:`f`'s *Hessian* (the matrix of :math:`f`'s second derivatives)
when attempting to compute :math:`f`'s minimum value.
Like BFGS, L-BFGS is an iterative method for solving unconstrained, non-linear optimization
problems, but approximates BFGS using a limited amount of computer memory.
L-BFGS starts with an initial estimate of the optimal value, and proceeds iteratively
to refine that estimate with a sequence of better estimates.
The derivatives of :math:`f` are used to identify the direction of steepest descent,
and also to form an estimate of the Hessian matrix (second derivative) of :math:`f`.
L-BFGS-B extends L-BFGS to handle simple, per-variable bound constraints.

The following parameters are supported:

-  The maximum number of function evaluations:

   .. code:: python

        maxfun = 1 | 2 | ...

   A positive ``int`` value is expected.  The default is ``1000``.

-  The maximum number of iterations:

   .. code:: python

        factr = 1 | 2 | ...

   A positive ``int`` value is expected.  The default is ``10``.

-  An ``int`` value controlling the frequency of the printed output showing the  optimizer's
   operations:

   .. code:: python

       iprint : int

   The default is ``-1``.

-  Step size used if numerically calculating the gradient.

   .. code:: python

        epsilon : float

   The default value is ``1e-08``.

.. seealso::
    Further detailed information on ``factr`` and ``iprint`` may be found at
    `scipy.optimize.fmin_l_bfgs_b <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin_l_bfgs_b.html>`__.

.. topic:: Declarative Name

   When referring to L-BFGS-B declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``L_BFGS_B``.

.. _nelder-mead:

^^^^^^^^^^^
Nelder-Mead
^^^^^^^^^^^

The Nelder-Mead algorithm performs unnconstrained optimization; it ignores bounds
or constraints.  It is used to find the minimum or maximum of an objective function
in a multidimensional space.  It is based on the Simplex algorithm. Nelder-Mead
is robust in many applications, especially when the first and second derivatives of the
objective function are not known. However, if the numerical
computation of the derivatives can be trusted to be accurate, other algorithms using the
first and/or second derivatives information might be preferred to Nelder-Mead for their
better performance in the general case, especially in consideration of the fact that
the Nelder–Mead technique is a heuristic search method that can converge to non-stationary points.

The following parameters are supported:

-  The maximum number of iterations:

   .. code:: python

       maxiter = 1 | 2 | ...

   This parameter is optional.  If specified, the value of this parameter must be a positive
   ``int``, otherwise, it is  ``None``. The default is ``None``.

-  The maximum number of functional evaluations to perform:

   .. code:: python

       maxfev = 1 | 2 | ...

   A positive ``int`` value is expected.  The default is ``1000``.

-  A ``bool`` value indicating whether or not to print convergence messages:

   .. code:: python

       disp : bool

   The default is ``False``.

-  A tolerance parameter indicating the absolute error in ``xopt`` between iterations that will
   be considered acceptable for convergence.

   .. code:: python

       xatol : float

   The default value is ``0.0001``.

-  The tolerance for termination:

   .. code::

       tol : float

   This parameter is optional.  If specified, the value of this parameter must be of type ``float``, otherwise, it is  ``None``.
   The default is ``None``.

   .. code:: python

       adaptive : bool

   The default is ``False``.

-  If true will adapt algorithm to dimensionality of problem.

.. topic:: Declarative Name

   When referring to Nelder-Mead declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``NELDER_MEAD``.

.. _p-bfgs:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Parallel Broyden-Fletcher-Goldfarb-Shann (P-BFGS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

P-BFGS is a parallellized version of
`L-BFGS-B <#limited-memory-broyden-fletcher-goldfarb-shanno-bound-l-bfgs-b>`__,
with which it shares the same parameters.
P-BFGS can be useful when the target hardware is a quantum simulator running on a classical
machine. This allows the multiple processes to use simulation to
potentially reach a minimum faster. The parallelization may help the optimizer avoid getting stuck
at local optima.  In addition to the parameters of
L-BFGS-B, P-BFGS supports an following parameter --- the maximum number of processes spawned by
P-BFGS:

.. code:: python

    max_processes = 1 | 2 | ...

By default, P-BFGS runs one optimization in the current process
and spawns additional processes up to the number of processor cores.
An ``int`` value may be specified to limit the total number of processes
(or cores) used.  This parameter is optional.  If specified, the value of this parameter must be
a positive ``int``, otherwise, it is ``None``.  The default is ``None``.

.. warning::

   The parallel processes do not currently work for this optimizer
   on the Microsoft Windows platform. There, P-BFGS will just run the one
   optimization in the main process, without spawning new processes.
   Therefore, the resulting behavior
   will be the same as the L-BFGS-B optimizer.

.. topic:: Declarative Name

   When referring to P-BFGS declaratively inside Aqua,
   its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``P_BFGS``.

.. _powell:

^^^^^^
Powell
^^^^^^

The Powell algorithm performs unconstrained optimization; it ignores bounds or
constraints. Powell is
a *conjugate direction method*: it performs sequential one-dimensional
minimization along each directional vector, which is updated at
each iteration of the main minimization loop. The function being minimized need not be
differentiable, and no derivatives are taken.

The following parameters are supported:

-  The maximum number of iterations:

   .. code:: python

       maxiter = 1 | 2 | ...

   This parameter is optional. If specified, the value of this parameter must be a positive
   ``int``, otherwise, it is  ``None``.
   The default is ``None``.

-  The maximum number of functional evaluations to perform:

   .. code:: python

       maxfev = 1 | 2 | ...

   A positive ``int`` value is expected.  The default value is ``1000``.

-  A ``bool`` value indicating whether or not to print convergence messages:

   .. code:: python

      disp : bool

   The default is ``False``.

-  A tolerance parameter indicating the absolute error in ``xopt`` between iterations that will be
   considered acceptable for convergence.

   .. code:: python

       xtol : float

   The default value is ``0.0001``.

-  The tolerance for termination:

   .. code::

       tol : float

   This parameter is optional.  If specified, the value of this parameter must be of type ``float``, otherwise, it is  ``None``.
   The default is ``None``.

.. topic:: Declarative Name

   When referring to Powell declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``POWELL``.

.. _slsqp:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sequential Least SQuares Programming (SLSQP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SLSQP minimizes a
function of several variables with any combination of bounds, equality
and inequality constraints. The method wraps the SLSQP Optimization
subroutine originally implemented by Dieter Kraft.
SLSQP is ideal for  mathematical problems for which the objective function and the constraints are
twice continuously differentiable. Note that the wrapper handles infinite values in bounds by
converting them into large floating values.

The following parameters are supported:

-  The maximum number of iterations:

   .. code:: python

       maxiter = 1 | 2 | ...

   A positive ``int`` value is expected.  The default is ``100``.

-  A ``bool`` value indicating whether or not to print convergence messages:

   .. code:: python

       disp : bool

   The default is ``False``.

-  A tolerance value indicating precision goal for the value of the objective function in the
   stopping criterion.

   .. code:: python

       gtol : float

   A ``float`` value is expected.  The default value is ``1e-06``.

-  The tolerance for termination:

   .. code::

       tol : float

   This parameter is optional.  If specified, the value of this parameter must be a ``float``, otherwise, it is  ``None``.
   The default is ``None``.

-  Step size used for numerical approximation of the Jacobian.

   .. code:: python

        eps : float

   The default value is ``1e-08``.

.. topic:: Declarative Name

   When referring to SLSQP declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``SLSQP``.

.. _spsa:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Simultaneous Perturbation Stochastic Approximation (SPSA)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SPSA is an algorithmic method for optimizing systems with multiple unknown parameters.
As an optimization method, it is appropriately suited to large-scale population models,
adaptive modeling, and simulation optimization.

.. seealso::
    Many examples are presented at the `SPSA Web site <http://www.jhuapl.edu/SPSA>`__.

SPSA is a descent method capable of finding global minima,
sharing this property with other methods as simulated annealing.
Its main feature is the gradient approximation, which requires only two
measurements of the objective function, regardless of the dimension of the optimization problem.

.. note::

    SPSA can be used in the presence of noise, and it is therefore indicated in situations
    involving measurement uncertainty on a quantum computation when finding a minimum. If you are
    executing a variational algorithm using a Quantum ASseMbly Language (QASM) simulator or a real device,
    SPSA would be the most recommended choice among the optimizers provided here.

The optimization process includes a calibration phase, which requires additional
functional evaluations.  Overall, the following parameters are supported:

-  Maximum number of trial steps to be taken for the optimization.
   There are two function evaluations per trial:

   .. code:: python

        max_trials = 1 | 2 | ...

   A positive ``int`` value is expected.  The default value is ``1000``.

-  An ``int`` value determining how often optimization outcomes should be stored during execution:

   .. code:: python

        save_steps = 1 | 2 | ...

   A positive ``int`` value is expected.
   SPSA will store optimization outcomes every ``save_steps`` trial steps.  The default value is ``1``.

-  The number of last updates of the variables to average on for the
   final objective function:

   .. code:: python

       last_avg = 1 | 2 | ...

   A positive ``int`` value is expected.  The default value is ``1``.

-  Control parameters for SPSA:

   .. code:: python

       c0 : float; default value is 0.62831853071796 (which is 0.2*PI)
       c1 : float; default value is 0.1
       c2 : float; default value is 0.602
       c3 : float; default value is 0.101
       c4 : float; default value is 0

   These are the SPSA control parameters, consisting of 5 ``float`` values, and are used as
   described below.

   SPSA updates the parameters (``theta``)
   for the objective function (``J``) through the following equation at
   iteration ``k``:

   .. code:: python

        theta_{k+1} = theta_{k} + step_size * gradient
        step_size = c0 * (k + 1 + c4)^(-c2)
        gradient = (J(theta_{k}+) - J(theta_{k}-)) * delta / (2 * c1 * (k + 1)^(-c3))
        theta_{k}+ = theta_{k} + c1 * ( k + 1)^(-c3) * delta
        theta_{k}- = theta_{k} - c1 * ( k + 1)^(-c3) * delta

   ``J(theta)`` is the  objective value of ``theta``. ``c0``, ``c1``, ``c2``, ``c3`` and ``c4``
   are the five control parameters.
   By default, ``c0`` is calibrated through a few evaluations on the
   objective function with the initial ``theta``. ``c1``, ``c2``, ``c3`` and ``c4`` are set as
   ``0.1``,
   ``0.602``, ``0.101``, ``0.0``, respectively.

- Calibration step for SPSA.

   .. code:: python

       skip_calibration: bool

   The default value is ``False``. When calibration is done, i.e. when ``skip_calibration`` is
   ``False`` (by default) the
   control parameter ``c0`` as supplied is adjusted by the calibration step before optimization.
   If ``skip_calibration``
   is ``True`` then the calibration step, which occurs ahead of optimization, is skipped and
   ``c0`` will be used unaltered.

.. topic:: Declarative Name

   When referring to SPSA declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``SPSA``.

.. _tnc:

^^^^^^^^^^^^^^^^^^^^^^
Truncated Newton (TNC)
^^^^^^^^^^^^^^^^^^^^^^
TNC uses a truncated Newton algorithm to minimize a function with
variables subject to bounds. This algorithm uses gradient information;
it is also called Newton Conjugate-Gradient. It differs from the
:ref:`Conjugate Gradient (CG) Method` method as it wraps a C implementation and
allows each variable to be given upper and lower bounds.

The following parameters are supported:

-  The maximum number of iterations:
   .. code:: python

        maxiter = 1 | 2 | ...

   A positive ``int`` value is expected.  The default is ``100``.

-  A Boolean value indicating whether or not to print convergence messages:
   .. code:: python

        disp : bool

   The default value is ``False``.

-  Relative precision for finite difference calculations:
   .. code:: python

        accuracy : float

   The default value is ``0.0``.

-  A tolerance value indicating the precision goal for the value of the objective function
   ``f`` in the stopping criterion.
   .. code:: python

        ftol : float

   The default value is ``-1``.

-  A tolerance value indicating precision goal for the value of ``x`` in the stopping criterion,
   after applying ``x`` scaling factors.
   .. code:: python

        xtol : float

   The default value is ``-1``.

-  A tolerance value indicating precision goal for the value of the projected gradient ``g`` in
   the stopping criterion,
   after applying ``x`` scaling factors.
   .. code:: python

        gtol : float

   The default value is ``-1``.

-  The tolerance for termination:
   .. code::

        tol : float

   This parameter is optional.  If specified, the value of this parameter must be a ``float``, otherwise, it is  ``None``.
   The default is ``None``

-  Step size used for numerical approximation of the Jacobian.
   .. code:: python

        eps : float

   The default value is ``1.4901161193847656e-08``.

.. topic:: Declarative Name

   When referring to TNC declaratively inside Aqua, its code ``name``, by which Aqua dynamically discovers and loads it,
   is ``TNC``.

.. _global-optimizers:

-----------------
Global Optimizers
-----------------
Aqua supports a number of classical global optimizers,
all based on the open-source `NonLinear optimization (NLopt) library <https://nlopt.readthedocs.io>`__.
Each of these optimizers uses the corresponding named optimizer from NLopt.
This package has native code implementations and must be
installed locally for these global optimizers to be accessible by Aqua.
Wrapper code allowing Aqua to interface these optimizers is installed
in the ``nlopt`` subfolder of the ``optimizers`` folder.

.. topic:: Installation of NLopt

    The `NLopt download and installation instructions <https://nlopt.readthedocs.io/en/latest/#download-and-installation>`__
    describe how to install NLopt.

    If you running Aqua on Windows, then you might want to refer to the specific `instructions for
    NLopt on Windows <https://nlopt.readthedocs.io/en/latest/NLopt_on_Windows/>`__.

    If you are running Aqua on a Unix-like system, first ensure that your environment is set
    to the Python executable for which the qiskit_aqua package is installed and running.
    Now, having downloaded and unpacked the NLopt archive file
    (for example, ``nlopt-2.4.2.tar.gz`` for version 2.4.2), enter the following commands:

    .. code:: sh

        ./configure --enable-shared --with-python
        make
        sudo make install

    The above makes and installs the shared libraries and Python interface in `/usr/local`. To have these be used
    by Aqua, the following commands can be entered to augment the dynamic library load path and python path respectively,
    assuming that you choose to leave these entities where they were built and installed as per above commands and that you
    are running Python 3.6:

    .. code:: sh

        export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib64
        export PYTHONPATH=/usr/local/lib/python3.6/site-packages:${PYTHONPATH}

    The two ``export`` commands above can be pasted into the ``.bash_profile`` file in the user's home directory for
    automatic execution.  Now you can run Aqua and these optimizers should be available for you to use.

.. topic:: The ``max_evals`` Parameter

    All the NLopt optimizers are supported by a common interface,
    allowing the optimizers to share the same common parameters.
    For quantum variational algorithms, it is necessary to assign a value
    to the following parameter:

    .. code:: python

        max_evals = 1 | 2 | ...

    This parameter takes a positive ``int`` as its value, indicating the maximum
    object function evaluation.  The default value is ``1000``.

Currently, Aqua supplies the following global optimizers from NLOpt:

- :ref:`Controller Random Search (CRS) with Local Mutation`
- :ref:`DIviding RECTangles algorithm - Locally based (DIRECT-L)`
- :ref:`DIviding RECTangles algorithm - Locally based - RANDomized (DIRECT-L-RAND)`
- :ref:`Evolutionary Strategy algorithm with CaucHy distribution (ESCH)`
- :ref:`Improved Stochastic Ranking Evolution Strategy (ISRES)`

.. _crs:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Controller Random Search (CRS) with Local Mutation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`CRS with local mutation <http://nlopt.readthedocs.io/en/latest/NLopt_Algorithms/#controlled-random-search-crs-with-local-mutation>`__
is part of the family of the CRS optimizers.
The CRS optimizers start with a random population of points, and randomly evolve these points by
heuristic rules. In the case of CRS with local mutation, the evolution is a randomized version of
the :ref:`Nelder-Mead` local optimizer.

.. topic:: Declarative Name

   When referring to CRS with local mutation declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it, is ``CRS``.

.. _direct-l:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
DIviding RECTangles algorithm - Locally based (DIRECT-L)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DIviding RECTangles (DIRECT) is a deterministic-search algorithms based on systematic division of
the search domain into increasingly smaller hyperrectangles.
The `DIRECT-L <http://nlopt.readthedocs.io/en/latest/NLopt_Algorithms/#direct-and-direct-l>`__ version
is a variant of DIRECT that makes the algorithm more biased towards local search,
so that it is more efficient for functions with few local minima.

.. topic:: Declarative Name

   When referring to DIRECT-L declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it, is ``DIRECT_L``.

.. _direct-l-rand:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
DIviding RECTangles algorithm - Locally based - RANDomized (DIRECT-L-RAND)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`DIRECT-L-RAND <http://nlopt.readthedocs.io/en/latest/NLopt_Algorithms/#direct-and-direct-l>`__ is a variant of
:ref:`DIviding RECTangles algorithm - Locally based (DIRECT-L)`
that uses some randomization to help decide which dimension to halve next in the case of near-ties.

.. topic:: Declarative Name

   When referring to DIRECT-L-RAND declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it, is ``DIRECT_L_RAND``.

.. _esch:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Evolutionary Strategy algorithm with CaucHy distribution (ESCH)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`ESCH <http://nlopt.readthedocs.io/en/latest/NLopt_Algorithms/#esch-evolutionary-algorithm>`__
is an evolutionary algorithm for global optimization that supports bound constraints only.
Specifically, it does not support nonlinear constraints.

.. topic:: Declarative Name

   When referring to ESCH declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it, is ``ESCH``.

.. _isres:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Improved Stochastic Ranking Evolution Strategy (ISRES)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`ISRES <http://nlopt.readthedocs.io/en/latest/NLopt_Algorithms/#isres-improved-stochastic-ranking-evolution-strategy>`__
is an algorithm for nonlinearly-constrained global optimization.
It has heuristics to escape local optima, even though convergence to a global optima is not
guaranteed. The evolution strategy is based on a combination of a mutation rule and differential
variation. The fitness ranking is simply via the objective function for problems without nonlinear
constraints. When nonlinear constraints are included, the
`stochastic ranking proposed by Runarsson and Yao <https://notendur.hi.is/^tpr/software/sres/Tec311r.pdf>`__
is employed. This method supports arbitrary nonlinear inequality and equality constraints, in
addition to the bound constraints.

.. topic:: Declarative Name

   When referring to ISRES declaratively inside Aqua, its code ``name``,
   by which Aqua dynamically discovers and loads it, is ``ISRES``.
