Tomography
==========

Ignis has tools to perform state and process tomography on a given Qiskit
circuit (the outcome of the circuit for state tomography, the circuit itself for
process). Tomography attempts to reconstruct the state (density matrix) or the
process map (superoperator) given the constraints of quantum measurements.

To use the tomography module, import it with

.. code:: python

    import qiskit.ignis.verification.tomography

Generating Tomography Circuits
------------------------------

The goal of the generation stage is to obtain a family of circuits that can be
passed to the backend in order to obtain enough measurement for full tomography.

For state tomography this amounts to adding measurement gates, and in process
tomography this amounts to adding both measurement and initialization gates.

.. code:: python

    state_tomography_circuits(
        circuit,
        measured_qubits,
        meas_labels='Pauli',
        meas_basis='Pauli')

* Creates state tomography circuits from ``circuit`` for the given
  ``measured_qubits``.
* The optional ``meas_basis`` is a string or an ``TomographyBasis`` object,
  which by default is ``PauliBasis``
* The optional ``meas_labels`` are used in naming the generated circuits.

.. code:: python

    process_tomography_circuits(
        circuit,
        measured_qubits,
        prepared_qubits=None,
        meas_labels='Pauli',
        meas_basis='Pauli',
        prep_labels='Pauli',
        prep_basis='Pauli')

* Creates process tomography circuits from ``circuit`` for the given ``measured_qubits``.
* The optional ``prepared_qubits`` is used to specify a set of qubits to prepare
  in case they are different than ``measured_qubits``.
* The optional ``meas_basis`` is a string or an ``TomographyBasis`` object,
  which by default is ``PauliBasis``
* The optional ``prep_basis`` is a string or an ``TomographyBasis`` object,
  which by default is ``PauliBasis``
* The optional ``meas_labels`` are used in naming the generated circuits.
* The optional ``prep_labels`` are used in naming the generated circuits.

Fitting Tomography Results
--------------------------

The fitting stage extracts the experimental results obtained from the backend
into a matrix representation of the state (density matrix) or process (Choi
matrix) described by the input circuit.

To perform fitting, an object of the class ``TomographyFitter`` needs to be
created. This is done by creating an ``StateTomographyFitter`` object for state
tomography and ``ProcessTomographyFitter`` for process tomography.

Fitting is performed by solving an optimization problem using a dedicated
library the current implementations rely on *scipy* and *cvxpy*. The
implementations differ in how they ensure the result is a proper density
matrix/Choi matrix: in cvxpy the constraints are encoded directly into the
optimization problem whereas in the scipy based algorithm the solution is
rescaled to ensure it is a proper solution.

.. code:: python

    StateTomographyFitter(result, circuits, meas_basis='Pauli')

Creates a state tomography fitter object.

.. code:: python

    ProcessTomographyFitter(
        result,
        circuits,
        meas_basis='Pauli',
        prep_basis='Pauli')

Creates a process tomography fitter object.

Here ``result`` is the result obtained via the backend run on ``circuits`` and
``meas_basis`` and ``prep_basis`` should be the same as used in the circuit
generation.

Both fitter classes include the ``fit`` method:

.. code:: python

    fit(
        self,
        method='auto',
        standard_weights=True,
        beta=0.5,
        ``kwargs)

This method performs the actual fitting. The parameters are:

* ``method``: can be ``'auto'``, ``'cvx'`` or ``'lstsq'``. The ``'auto'`` options attempts
  to use cvx and resorts to lstsq if cvx is not available.
* ``standard_weights``: a boolean deciding whether to apply weights to
  tomography data based on count probability
* ``beta``: a float hedging parameter for converting counts
* ``kwargs``: holds additional parameters passed directly to the solver
  engine (e.g. ``cvxopt``)
