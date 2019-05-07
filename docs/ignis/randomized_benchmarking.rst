
Randomized Benchmarking
==========================

Randomized benchmarking (RB) is a well-known technique to measure average gate
performance by running sequences of random Clifford gates that should return the
qubits to the initial state. Ignis has tools to generate one- and two-qubit
Clifford gate sequences simultaneously.

To use the Qiskit Ignis randomized benchmarking (RB) module, import it with

.. code:: python

    import qiskit.ignis.verification.randomized_benchmarking as rb

Generating RB Sequences
-----------------------

In order to generate the RB sequences ``rb_circs``, which is a  list of lists of
quantum circuits, run

.. code:: python

    rb_circs, xdata = randomized_benchmarking_seq(
        nseeds,
        length_vector,
        rb_pattern,
        length_multiplier,
        seed_offset,
        align_cliffs)

The parameters given to this function are:

* ``nseeds``: the number of seeds. For each seed there you will get a separate
  list of output circuits in ``rb_circs``
* ``length_vector``: the length vector of Clifford lengths. Must be in
  ascending order. RB sequences of increasing length grow on top of the
  previous sequences
* ``rb_pattern``: a list of the form ``[[i,j],[k],...]`` which will make
  simultaneous RB sequences where :math:`Q_i,\,Q_j` are a 2-qubit RB sequence
  and :math:`Q_k` is a 1-qubit sequence, etc. The number of qubits is the sum
  of the entries. For 'regular' RB the ``qubit_pattern`` is just
  ``[[0]],[[0,1]]``
* ``length_multiplier``: if this is an array it scales each ``rb_sequence`` by
  the multiplier
* ``seed_offset``: Use this to create new seeds (trials) if we later determine
  that more are needed
* ``align_cliffs``: Use this to align the Cliffords across simultaneous
  sequences, i.e., this will add barriers after each Clifford x ``length_multiplier``
  that applies to all qubits in ``rb_pattern``

For example,

.. code:: python

    # Number of qubits
    nQ = 4
    # i.e., [Q0,Q1,Q2,Q3]

    # Number of seeds, which is the number of lists of RB sequences
    nseeds = 5

    # Number of Cliffords in each sequence (start, stop, steps)
    length_vector = np.arange(1,200,20)

    # Simultaneous 2-qubit RB on qubits Q0,Q2 and 1-qubit RB on qubits Q1 and Q3
    rb_pattern = [[0,2],[3],[1]]

    # Do three times as many 1Q Cliffords
    length_multiplier = [1,3,3]

This function returns:

* ``rb_circs``: a list of lists of circuits for the RB sequences (separate list
  for each seed)
* ``xdata``: the Clifford lengths (with multiplier if applicable)
* ``rb_opts_dict``: option dictionary back out with default options appended


Analyzing Results
-----------------
Now, you can execute the randomized benchmarking either using Qiskit Aer
Simulator (with some noise model) or using IBMQ provider, and obtain a list of
results ``result_list`` for the RB sequences.

.. code:: python

    result_list = [] # Output results
    for rb_seed,rb_circ_seed in enumerate(rb_circs):
        print('Executing seed %d'%rb_seed)
        # Executing each RB sequence
        job = qiskit.execute(
            rb_circ_seed,
            backend=backend,
            basis_gates=basis_gates,
            shots=shots,
            noise_model=noise_model)
        result_list.append(job.result())

To get the statistics about the survival probabilities add the results to a RB
fitter.

.. code:: python

    rbfit = rb.RBFitter(result_list, xdata, rb_pattern)

where ``results_list``, ``xdata`` and ``rb_patterns`` are as above. The results
can be added as a list or as one result. Results can be added to an existing
fitter as

.. code:: python

    rbfit.add_data(more_results)

The number of seeds in the fitter is based on the number of added results. To
compute the data, calculate the mean over seeds and fit the results to an
exponential curve (fit each of the RB patterns ``pattern_index``):

.. code:: python

    rbfit.calc_data()
    rbfit.calc_statistics()
    rbfit.fit_data()

These steps are performed automatically when data is added (unless ``rerun_fit``
is set to ``False`` in ``add_data()``). The fit parameters are:

.. code:: python

    # The three parameters (a, alpha, b)
    # of the function a * alpha ** x + b.
    # The middle one is the exponent alpha.
    rbfit.fit[pattern_index]['params']
    # The error limits of the parameters.
    rbfit.fit[pattern_index]['err']
    # The error per Clifford
    rbfit.fit[pattern_index]['epc']
    # The error limit per Clifford
    rbfit.fit[pattern_index]['epc_err']

To plot the data plus fit, use

.. code:: python

    rbfit.plot_rb_data(
        pattern_index,
        ax=ax,
        add_label=True,
        show_plt=False)

where:

* ``pattern_index``: which RB pattern to plot
* ``ax`` (``Axes`` or ``None``): plot axis (if passed in)
* ``add_label`` (``bool``): add an error per Clifford label
* ``show_plt`` (``bool``): display the plot


Predicted Results
-----------------

From the known depolarizing errors on the simulation you can predict the
fidelity. First you need to count the number of gates per Clifford.

.. code:: python

    gates_per_cliff = rb.rb_utils.gates_per_clifford(
        qobj_list,
        xdata[0],
        basis_gates,
        rb_opts['rb_pattern'][0])

Then you need to prepare lists of the number of qubits and the errors and
calculate the predicted error per Clifford (epc):

.. code:: python

    pred_epc = rb.rb_utils.twoQ_clifford_error(ngates,gate_qubits,gate_errs)

where:

* ``ngates``: a list of the number of gates per 2Q Clifford
* ``gate_qubit``: a list of the qubit corresponding to the gate (0, 1 or -1).
  -1 corresponds to the 2Q gate
* ``gate_err``: list of the gate errors
