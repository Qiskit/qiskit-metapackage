
Contributing
============

If you want to contribute with one of the Qiskit elements or components, 
refer to their individual Contributing guidelines:

* `Qiskit Terra <https://github.com/Qiskit/qiskit-terra/blob/master/.github/CONTRIBUTING.rst>`_
* `Qiskit Aer <https://github.com/Qiskit/qiskit-aer/blob/master/.github/CONTRIBUTING.rst>`_
* `Qiskit Aqua <https://github.com/Qiskit/qiskit-aqua/blob/master/.github/CONTRIBUTING.rst>`_
* `Qiskit Chemistry <https://github.com/Qiskit/qiskit-chemistry/blob/master/.github/CONTRIBUTING.rst>`_

What happened to Qiskit `0.6`?
------------------------------

Prior to version `0.7`, both Terra and Aer elements lived together under the `qiskit` package. In
`0.7` we split `qiskit` into `qiskit-terra` and `qiskit-aer`.

The Terra element is the foundation of Qiskit and allows you to write quantum circuits with our
Python API and run them using the built-in simulators provided with the package. Aer element is a
collection of native simulators designed to be fast and full-featured.

If you don't need/want these simulators, you can always install `qiskit-terra` in isolation by
doing:

```bash
$ pip install qiskit-terra
```
