# qiskit

> Qiskit is a software development kit for writing quantum computing experiments, programs, and applications.

This is a simple meta-package to install the elements of Qiskit altogether.

## Install

The best way of installing `qiskit` is using `pip`:

```bash
$ pip install qiskit
```

## What happened to Qiskit `0.6`?

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

## Versioning

The meta-package started with version `0.7` to respect the continuity of `qiskit` versions. The
Terra element did the same to provide continuity with its own history.

Considering [`semver`](https://semver.org/), the Qiskit meta-package pins the _minor_ version
number of each Qiskit element to get new patches automatically.

Nevertheless, upon changes _minor_ or _major_ version numbers of the elements, the meta-package
version must be updated according to the following rules:

1. If a dependency increased the **major** number, increase the **major** number of the meta-package.
2. Else:
   1. If a dependency increased the **minor** number, increase the **minor** number of the meta-package.

## Contributing

If you want to contribute with one of the Qiskit elements, refer to their individual sites:

* [Terra on GitHub](https://github.com/Qiskit/qiskit-terra)
