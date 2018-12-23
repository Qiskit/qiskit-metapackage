
# Qiskit

**Qiskit** is an open-source framework for working with noisy intermediate-scale quantum computers (NISQ) at the level of pulses, circuits, and algorithms.

This is a simple meta-package to install the elements of Qiskit altogether.

## Install

The best way of installing `qiskit` is using `pip`:

```bash
$ pip install qiskit
```

See [install](doc/install.rst) Qiskit for detailed instructions, how to use environments and 
build the individual elements.

## Qiskit Elements and Components

| Build   | Status | Version | Downloads | 
| ---             | ---    | --- | --- |
| **Qiskit**   | [![Build Status](https://travis-ci.com/Qiskit/qiskit.svg?branch=master)](https://travis-ci.com/Qiskit/qiskit) | ![](https://img.shields.io/pypi/v/qiskit.svg?style=popout-square) | ![](https://img.shields.io/pypi/dm/qiskit.svg?style=popout-square) |
| **Qiskit Terra**   |  [![Build Status](https://travis-ci.org/Qiskit/qiskit-terra.svg?branch=master)](https://travis-ci.org/Qiskit/qiskit-terra)| ![](https://img.shields.io/pypi/v/qiskit-terra.svg?style=popout-square)  |![](https://img.shields.io/pypi/dm/qiskit-terra.svg?style=popout-square) |
| **Qiskit Aer**   |  --- |  ![](https://img.shields.io/pypi/v/qiskit-aer.svg?style=popout-square)  | ![](https://img.shields.io/pypi/dm/qiskit-aer.svg?style=popout-square) |
| **Qiskit Aqua**   |  [![Build Status](https://travis-ci.com/Qiskit/qiskit-aqua.svg?branch=master)](https://travis-ci.com/Qiskit/qiskit-aqua) |  ![](https://img.shields.io/pypi/v/qiskit-aqua.svg?style=popout-square) |![](https://img.shields.io/pypi/dm/qiskit-aqua.svg?style=popout-square) |
| **Qiskit Chemistry**   |  [![Build Status](https://travis-ci.com/Qiskit/qiskit-chemistry.svg?branch=master)](https://travis-ci.com/Qiskit/qiskit-chemistry) |  ![](https://img.shields.io/pypi/v/qiskit-chemistry.svg?style=popout-square)   | ![](https://img.shields.io/pypi/dm/qiskit-chemistry.svg?style=popout-square) |
| **IBM Q Provider**   |  [![Build Status](https://travis-matrix-badges.herokuapp.com/repos/Qiskit/qiskit-terra/branches/master/8)](https://travis-ci.org/Qiskit/qiskit-terra) |  --- | --- |

## Additional Extensions

| Build   | Status | Version | Downloads |
| ---   | --- | --- | --- |
| **JKU Provider**   |  --- |  --- | --- |
| **QCGPU Provider**   |  --- |  --- | --- |
| **Project Q Provider**   |  --- |  --- | --- |
| **Sympy Provider**   |  --- |  --- | --- |


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

If you want to contribute with one of the Qiskit elements or components, refer to their individual sites:

* [Qiskit Terra on GitHub](https://github.com/Qiskit/qiskit-terra)
* [Qiskit Aer on GitHub](https://github.com/Qiskit/qiskit-aer)
* [Qiskit Aqua on Github](https://github.com/Qiskit/qiskit-aqua)
* [Qiskit Chemistry on Github](https://github.com/Qiskit/qiskit-chemistry)

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
