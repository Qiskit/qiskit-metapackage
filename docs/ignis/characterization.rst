
Characterization
================

Ignis provides a set of tools to characterize specific aspects
of the quantum device and the gates, generically, circuits
and analysis tools to extract single characterization parameters.

Circuits
---------

There are modules to generate circuits for coherence, hamiltonian and
gate characterization. Each follows a general template of specifying
a list of values to vary, and the qubits to characterize. Qubits in the list
are characterized in parallel.

Coherence
~~~~~~~~~

The coherence circuit scripts are in

.. code:: python

    qiskit.ignis.characterization.coherence.circuits

To generate coherence circuits, call the functions ``t1_circuits``,
``t2_circuits``, and  ``t2star_circuits``. These circuits contain blocks of
identity gates (``id``) between particular gates depending on the experiment.
The user specifies a list with the number of identity gates for each
experiment; the list must be in ascending order. The length of the ``id``
gate is backend dependent and the user must provide that time (``gate_time``)
to these functions. For each experiment the user also specifies a list of
qubits; identical experiments will occur in parallel on these qubits. Only
these qubits are measured and the results are mapped to a classical register
of size ``len(qubits)`` (the first qubit specified is mapped to the first
bit of the classical register, etc.). Each circuit function returns
a list of circuits (objects of type ``QuantumCircuit``),
and a list of delay times indicating the total time of identity gates in that
sequence.

The |T1| circuits consist of an `X` gate to excite the qubit and then
varying length of identity gates before a measurement. Here is a usage
example for ``t1_circuit``:

.. code:: python

    circs, xdata = t1_circuits(
        num_of_gates=[10, 20, 30],
        gate_time=0.1,
        qubits=[0, 2])

|TS| circuits consist of one Hadamard gate, one block of identity gates,
a phase gate, and an additional Hadamard gate. You can control the
phase gate by setting the number of oscillations. Example:

.. code:: python

    circs, xdata, osc_frec = t2star_circuits(
        num_of_gates=[5, 10],
        gate_time=0.4,
        qubits=[1],
        nosc=3)

Note an additional return parameter, the expected oscillation frequency which
can be used as an initial value for the fit.

``t2_circuits`` follow the CPMG protocol. Specify the number of echoes,
and whether to alternate the echo between X and Y. The ``num_of_gates``
specifies the wait between the :math:`\pi/2` pulse and the first echo.
The ``xdata`` is the total time of the sequence.

.. code:: python

    circs, xdata, osc_frec = t2star_circuits(
        num_of_gates=[100, 500, 1000],
        gate_time=0.3,
        qubits=[2, 1],
        n_echos=4,
        phase_alt_echo=True)

Hamiltonian  Parameters
~~~~~~~~~~~~~~~~~~~~~~~

Circuits for studying Hamiltonian parameters are in

.. code:: python

    qiskit.ignis.characterization.hamiltonian.circuits

The circuits to study the ZZ interaction between qubits perform a |TS|
experiment on a qubit with a specator qubit in the :math:`|0\rangle` state and
another |TS| experiment with the qubit in the :math:`|1\rangle` state.
The difference frequency between these experiments is the ZZ rate.
Here is a usage example for ``zz_circuits``:

.. code:: python

    circs, xdata = zz_circuits(
        num_of_gates=[10, 20, 30],
        gate_time=0.1,
        qubits=[0, 2],
        spectators=[1, 3],
        nosc=5)

``qubits`` is the list of qubits to be measured using the |TS| sequence and
``spectators`` is the list of qubits to be flipped. These lists must be
the same length and be unique. The sequences therefore measure ZZ between
the elements of ``qubits`` and ``spectators`` at the same index.


Gate Characterization
~~~~~~~~~~~~~~~~~~~~~

Circuits for studying gate errors are in

.. code:: python

    qiskit.ignis.characterization.gates.circuits

These circuits repeat gates in a particular sequence to amplify either
rotation (amplitude) or angle error. There are circuits to look at the
single qubit ``U2`` gates and circuits to look at the two-qubit ``CX`` gate.

For the single qubit gates an example of the amplitude calibration is

.. code:: python

    circs, xdata = ampcal_1Q_circuits(
        max_reps=10,
        qubits=[0, 1])


The amplitude calibration does a ``U2`` gate followed by the same ``U2`` gate in
pairs. The ``max_reps`` is the number of pair repetitions. ``xdata`` gives the
total number of applied ``U2`` gates. An example usage of the angle calibration
is

.. code:: python

    circs, xdata = anglecal_1Q_circuits(
        max_reps=10,
        qubits=[0, 1],
        angleerr=0.0)

``angleerr`` is an artifial angle error that can be added using ``U1`` gates
to test the sequence.

The functions are similar for ``CX``,

.. code:: python

    circs, xdata = ampcal_cx_circuits(
        max_reps=10,
        qubits=[0, 1],
        control_qubits=[2, 3])

    circs, xdata = anglecal_cx_circuits(max_reps=10,
        qubits=[0, 1],
        control_qubits=[2, 3],
        angleerr=0.0)

where ``control_qubits`` specifies the control of the ``cx`` gate and
``qubits`` are the targets.


Fitters
-------

All characterization experiments are analyzed by fitters derived by the
``BaseFitter`` class. Using the |T1| fitter as an example

.. code:: python

    fit = T1Fitter(
        backend_result,
        xdata,
        qubits=[0, 2],
        fit_p0=[initial_a, initial_t1, initial_c],
        fit_bounds=([0, 0, -1], [2, 80, 1]))

we pass in the result, the ``xdata``, and the ``qubits`` plus guess values
for the fit parameters and fit bounds. The results can be passed in as
a single result, as a list of results (e.g., if the experiment has
to be run across several jobs) or as an empty result. Data can be added
later using

.. code:: python

    fit.add_data(new_results, re_calc=True, re_fit=True)

``add_data`` can be used to add results from new circuits or to add more
shots to circuits that have already been added. If ``re_calc`` is True then
the data is processed. If ``re_fit`` is True then the data is fit.
The data can also be fit by an explicit call to

.. code:: python

    fit.fit_data(qid=-1, p0=None, bounds=None, series=None)

``qid`` can be used to fit only a single qubit's data (this refers to
the qubit index in the list passed to init). As specified (``qid=-1``),
this fits all the data. New initial values and bounds for the fit can also
be passed in. ``series`` specifies the data series to fit. Most circuits
only have a single series by default, but certain experiments (e.g. ZZ)
have multiple series. The data can be plotted with a call to ``fit.plot``.
The properties ``params`` and ``params_err`` return the fit parameters
and errors.

Coherence
~~~~~~~~~

Analysis is done by classes ``T1Fitter``, ``T2Fitter``, and ``T2StarFitter``.

The |T1| data is fit to

.. math::

    f(t) = a \, e^{-t/T_1} + c,

for unknown parameters :math:`a`, :math:`c`, and |T1|. If there are no SPAM
errors, :math:`a=1` and :math:`c=0`. After initializing the fitter object,
the function ``time()`` of ``T1Fitter`` gives the estimated |T1|. Similarly,
for |T2| and |TS|, the ground state population is expected to behave like

.. math::

    a \, e^{-t/T_1} + c

and

.. math::
    a \, e^{-t/{T_2}^*} \, \cos(2\pi ft + \phi) + c,

respectively; both with :math:`a=c=0.5` in the lack of SPAM errors.

Hamiltonian
~~~~~~~~~~~

Analysis is done by the class ``ZZFitter``. There are two data series ``0`` and
``1``. The data is fit to the same function |TS| and the ZZ rate (obtained
using function ``ZZ_rate``) is the  difference between the values of ``f``
from the two fits.

Gates
~~~~~

Analysis is done by classes ``AmpCalFitter``, ``AngleCalFitter``,
``AmpCalCXFitter``, ``AngleCalCXFitter``.

``AmpCalFitter`` and ``AngleCalFitter`` is fit to the function

.. math::

    c - \frac{1}{2} \, \cos \left( \left(\theta+\frac{\pi}{2}\right) (x + 1)
    \right),

where :math:`x` is the number of gate repetitions and :math:`\theta` is the
error for the pulse (amplitude/error).

``AmpCalCXFitter`` and ``AngleCalCXFitter`` is fit to the function

.. math::

    c + \frac{1}{2} \, \sin\left((\theta+\pi) \, x \right),

where :math:`x` is the number of gate repetitions and :math:`\theta` is the
amplitude error for the pulse.



.. |T1| replace:: :math:`T_1`
.. |T2| replace:: :math:`T_2`
.. |TS| replace:: :math:`T_2^*`
