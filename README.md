
# Qiskit

[![License](https://img.shields.io/github/license/Qiskit/qiskit.svg?style=popout-square)](https://opensource.org/licenses/Apache-2.0)[![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit/master.svg?style=popout-square)](https://travis-ci.com/Qiskit/qiskit)![](https://img.shields.io/pypi/v/qiskit.svg?style=popout-square)![](https://img.shields.io/pypi/dm/qiskit.svg?style=popout-square)

**Qiskit** is an open-source framework for working with noisy intermediate-scale quantum computers (NISQ) at the level of pulses, circuits, and algorithms.

Qiskit is made up elements that each work together to enable quantum computing. This is a simple meta-package to install the elements of Qiskit altogether.

## Installation 

The best way of installing `qiskit` is using `pip`:

```bash
$ pip install qiskit
```

See [install](doc/install.rst) Qiskit for detailed instructions, how to use virtual environments, and 
build from source standalone versions of the individual Qiskit elements and components.

## Qiskit Details

Qiskit consists of elements and components and it is our goal to have all the elements and components install 
using this mega package. However, currently some still are not included
in the default pip and need to be installed following instructions in their individual packages (this will be fixed
in the next update)

### Qiskit Elements

The four elements of Qiskit are the essential parts that give Qiskit its power. 

| Build   | Status | Version | Downloads | 
| ---             | ---    | --- | --- |
| [**Qiskit Terra**](https://github.com/Qiskit/qiskit-terra)   |  [![Build Status](https://img.shields.io/travis/Qiskit/qiskit-terra/master.svg?style=popout-square)](https://travis-ci.org/Qiskit/qiskit-terra)| ![](https://img.shields.io/pypi/v/qiskit-terra.svg?style=popout-square)  |![](https://img.shields.io/pypi/dm/qiskit-terra.svg?style=popout-square) |
| [**Qiskit Aer**](https://github.com/Qiskit/qiskit-aer)   |  [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-aer/master.svg?style=popout-square)](https://travis-ci.com/Qiskit/qiskit-aer) |  ![](https://img.shields.io/pypi/v/qiskit-aer.svg?style=popout-square)  | ![](https://img.shields.io/pypi/dm/qiskit-aer.svg?style=popout-square) |
| [**Qiskit Aqua**](https://github.com/Qiskit/qiskit-aqua)<sup>1</sup>  |  [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-aqua/master.svg?style=popout-square)](https://travis-ci.com/Qiskit/qiskit-aqua) |  ![](https://img.shields.io/pypi/v/qiskit-aqua.svg?style=popout-square) |![](https://img.shields.io/pypi/dm/qiskit-aqua.svg?style=popout-square) |
| **Qiskit Ignus**<sup>3</sup>   |  --- |  ---| --- |

### Qiskit Components

Qiskit compoents are smaller self-contained parts of Qiskit that are needed for full functionality.

| Build   | Status | Version | Downloads | 
| ---             | ---    | --- | --- |
| [**Qiskit Chemistry**](https://github.com/Qiskit/qiskit-chemistry)<sup>1</sup>  |  [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-chemistry/master.svg?style=popout-square)](https://travis-ci.com/Qiskit/qiskit-chemistry) |  ![](https://img.shields.io/pypi/v/qiskit-chemistry.svg?style=popout-square)   | ![](https://img.shields.io/pypi/dm/qiskit-chemistry.svg?style=popout-square) |
| **IBM Q Provider**<sup>2</sup>   |  [![Build Status](https://travis-matrix-badges.herokuapp.com/repos/Qiskit/qiskit-terra/branches/master/8)](https://travis-ci.org/Qiskit/qiskit-terra) |  --- | --- |

1: Currently these need to be installed separately see repository for details. 

2: Currently included as part of Qiskit Terra. There is no separate repository (estimation early 2019 for separate repository)

3: Not currently released (estimation early 2019).

### Additional Extensions

To extend Qiskit and its functionality the following extensions are avaialable.

| Build   | Status | Version | Downloads |
| ---   | --- | --- | --- |
| [**JKU Provider**](https://github.com/Qiskit/qiskit-jku-provider)   |  --- |  --- | --- |
| [**QCGPU Provider**](https://github.com/Qiskit/qiskit-qcgpu-provider)  |  --- |  --- | --- |
| [**Project Q Provider**](https://github.com/Qiskit/qiskit-projectq-provider)   |  --- |  --- | --- |
| [**Sympy Provider**](https://github.com/Qiskit/qiskit-sympy-provider)   |  --- |  --- | --- |

Note These are WIP in progress and when Qiskit 0.7 compatible will be added here. 

## Contribution guidelines

If you'd like to contribute to Qiskit, please take a look at our
[contribution guidelines](.github/CONTRIBUTING.rst). This project adheres to Qiskit's [code of conduct](.github/CODE_OF_CONDUCT.rst). By participating, you are expect to uphold to this code.

We use [GitHub issues](https://github.com/Qiskit/qiskit/issues) for tracking requests and bugs. Please use our [slack](https://qiskit.slack.com) for discussion and simple questions. To join our Slack community use the [link](https://join.slack.com/t/qiskit/shared_invite/enQtNDc2NjUzMjE4Mzc0LTMwZmE0YTM4ZThiNGJmODkzN2Y2NTNlMDIwYWNjYzA2ZmM1YTRlZGQ3OGM0NjcwMjZkZGE0MTA4MGQ1ZTVmYzk). For questions that are more suited for a forum we use the Qiskit tag in the [Stack Overflow](https://stackoverflow.com/questions/tagged/qiskit).

### Next Steps

Now you're set up and ready to check out some of the other examples from our
[Qiskit Tutorial](https://github.com/Qiskit/qiskit-tutorial) repository.

## Authors

Qiskit is the work of [many people](https://github.com/Qiskit/qiskit/graphs/contributors) who contribute to the project at different levels.

## License

[Apache License 2.0](LICENSE.txt)
