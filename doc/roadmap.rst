# The QISKit Roadmap 2018

With a very successful r0.4 release behind us, now is a good time to look towards the future. We are going to look out 6-12 months to establish a set of goals we want to work towards. When planning, we typically look at potential work from three perspectives:

* **Streamlining the building of quantum programs:** As the quantum programs get more advanced we need new features to make the work flow simpler. Features include load/save, better inquires about backend information (estimated program size/status/time laps), tools for making quantum circuits, and libraries to load different quantum programs (tomography/randomized benchmarking/vqe algorithms).
 
* **Improved compiling and running of quantum programs:** At the heart of QISKit is the ability to launch a job on different backends these include simulators and real devices. Features to be added are improved simulators, additional simulators (c++, Clifford, t-gate simulators), smarter compilers (the current one unrolls and then swaps to the configuration and then compresses single qubit gates), and methods such as a quantum initiator (you give a quantum state and it returns the circuit to make it).  

* **Methods for combining data from quantum programs and visualizations:** As the quantum programs become more advanced we don't just want to look at the counts for each circuit. These will be combined together for all elements of the program to evaluate some function (cost function, observable, state reconstruction) and we need tools to do this. These include verification methods such as tomography and randomized benchmarking, optimization of classical cost functions, optimization of quantum cost functions, and more. An important component of analyzing the results of a quantum program is visualization. Some useful simple additions are plotting to the Bloch sphere, q-sphere, Pauli-vectors, spin Wigner functions, Pauli Transfer Matrix etc. 

QISKit will continue to update regularly, and we'll make progress against each of the following themes during each iteration. 

# Streamlining the building of quantum programs

* Load/Save a quantum program: The ability to save a quantum program and the results from a quantum program for analyzation at a later time.

* functions to make building quantum circuits faster 

      - QFT
      - adding a control qubit to a gate
      - approximating a unitary transformation

* tools for making experiments for randomized benchmarking, quantum volume, etc. 

# Improved compiling and running of quantum programs.

* Experiment working with the qobj and fixing the return error for qubit labels.

* Returning the calibrations for the user to better correct for measurement crosstalk error

* Introducing a cleaner job running class

* making the complier more modular with configuration options to allow better control of the compile stage

      - Randomized compiling for reducing error
      - CNOT + SU(2) template-based optimization
      - CNOT + SU(2) peephole optimization
      - Do we want to consider circuit synthesis over discrete gate sets?

# Methods for combining data from quantum programs and visualizations

* Data processing tools: Tools for better fitting returned data.

* Visualization tools: interactive plotting quantum results, quantum states, and quantum maps. 
 
# Backend documentation and integration

* Tools for interacting with the hardware backends easier (including estimating circuit lengths and run time)

# Improved and more simulator backends

* Adding noise simulators 

* Clifford simulators

# Summary

These are examples of just some of the work we will be focusing on in the next 6 to 12 months. We will continuously adapt the plan based on feedback. Please follow along and let us know what you think!