Qiskit Aer Release Notes
========================

`Issues <https://github.com/Qiskit/qiskit-aer/issues>`_

Qiskit Aer 0.1.0
----------------

QASM Simulator: the main Qiskit Aer backend. 
  This backend emulates execution of a quantum circuits on a real device and returns measurement counts. 
  It includes highly configurable noise models and can even be loaded with automatically generated approximate 
  noise models based on the calibration parameters of actual hardware devices.

Statevector Simulator: an auxiliary backend for Qiskit Aer. 
  It simulates the ideal execution of a quantum circuit and returns the final quantum state vector of the device 
  at the end of simulation. This is useful for education, as well as the theoretical study and debugging of algorithms.

Unitary Simulator: another auxiliary backend for Qiskit Aer. 
  It allows simulation of the final unitary matrix implemented by an ideal quantum circuit. 
  This is also useful for education and algorithm studies.
