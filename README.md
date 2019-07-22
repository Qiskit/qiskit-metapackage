
# Qiskit

[![License](https://img.shields.io/github/license/Qiskit/qiskit.svg?)](https://opensource.org/licenses/Apache-2.0) [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit/master.svg?)](https://travis-ci.com/Qiskit/qiskit) [![](https://img.shields.io/github/release/Qiskit/qiskit.svg)](https://github.com/Qiskit/qiskit/releases) [![Downloads](https://pepy.tech/badge/qiskit)](https://pypi.org/project/qiskit/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2562110.svg)](https://doi.org/10.5281/zenodo.2562110)

**Qiskit** is an open-source framework for working with noisy quantum computers at the level of pulses, circuits, and algorithms.

Qiskit is made up elements that each work together to enable quantum computing. This is a simple meta-package to install the elements of Qiskit altogether.

## Installation

The best way of installing `qiskit` is using `pip`:

```bash
$ pip install qiskit
```

See [install](docs/install.rst) Qiskit for detailed instructions, how to use virtual environments, and
build from source standalone versions of the individual Qiskit elements and components.

### Note for upgrading from Qiskit < 0.7.0

If you have an older Qiskit version, < 0.7.0, upgrading to the latest version
with `pip install -U` is not supported. To upgrade from these older versions
you'll first have to uninstall qiskit and then install the newer version. To
do this run:

```bash
$ pip uninstall qiskit
$ pip install -U qiskit
```

## Qiskit Details

Qiskit consists of elements and components and it is our goal to have all the elements and components install
using this mega package. However, currently some still are not included
in the default pip and need to be installed following instructions in their individual packages (this will be fixed
in the next update)

### Qiskit Elements

The four elements of Qiskit are the essential parts that give Qiskit its power.

| Build   | Status | Version | Contribute |
| ---             | ---    | --- | --- |
| [**Qiskit Terra**](https://qiskit.org/terra)   |  [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-terra/master.svg?)](https://travis-ci.com/Qiskit/qiskit-terra)| [![](https://img.shields.io/github/release/Qiskit/qiskit-terra.svg?)](https://github.com/Qiskit/qiskit-terra/releases)  | [![](https://img.shields.io/github/forks/Qiskit/qiskit-terra.svg?)](https://github.com/Qiskit/qiskit-terra) |
| [**Qiskit Aer**](https://qiskit.org/aer)   |  [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-aer/master.svg?)](https://travis-ci.com/Qiskit/qiskit-aer) | [![](https://img.shields.io/github/release/Qiskit/qiskit-aer.svg?)](https://github.com/Qiskit/qiskit-aer/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-aer.svg?)](https://github.com/Qiskit/qiskit-aer) |
| [**Qiskit Aqua**](https://qiskit.org/aqua) |  [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-aqua/master.svg?)](https://travis-ci.com/Qiskit/qiskit-aqua) |  [![](https://img.shields.io/github/release/Qiskit/qiskit-aqua.svg?)](https://github.com/Qiskit/qiskit-aqua/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-aqua.svg?)](https://github.com/Qiskit/qiskit-aqua) |
| [**Qiskit Ignis**](https://qiskit.org/ignis)  |  [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-ignis/master.svg?)](https://travis-ci.com/Qiskit/qiskit-ignis) |  [![](https://img.shields.io/github/release/Qiskit/qiskit-ignis.svg?)](https://github.com/Qiskit/qiskit-ignis/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-ignis.svg?)](https://github.com/Qiskit/qiskit-ignis) |

### Qiskit Components

Qiskit components are smaller self-contained parts of Qiskit that are needed for full functionality.

| Build   | Status | Version | Contribute |
| ---             | ---    | --- | --- |
| **Qiskit Tutorial**  | --- |  [![](https://img.shields.io/github/release/Qiskit/qiskit-tutorial.svg?)](https://github.com/Qiskit/qiskit-tutorial/releases)   | [![](https://img.shields.io/github/forks/Qiskit/qiskit-tutorial.svg?)](https://github.com/Qiskit/qiskit-tutorial) |
| **Qiskit Chemistry** |  [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-chemistry/master.svg?)](https://travis-ci.com/Qiskit/qiskit-chemistry) |  [![](https://img.shields.io/github/release/Qiskit/qiskit-chemistry.svg?)](https://github.com/Qiskit/qiskit-chemistry/releases)   | [![](https://img.shields.io/github/forks/Qiskit/qiskit-chemistry.svg?)](https://github.com/Qiskit/qiskit-chemistry) |
| **IBM Q Provider** |  [![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-ibmq-provider/master.svg?)](https://travis-ci.com/Qiskit/qiskit-ibmq-provider) |  [![](https://img.shields.io/github/release/Qiskit/qiskit-ibmq-provider.svg?)](https://github.com/Qiskit/qiskit-ibmq-provider/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-ibmq-provider.svg?)](https://github.com/Qiskit/qiskit-ibmq-provider) |


## Contribution Guidelines

If you'd like to contribute to Qiskit, please take a look at our
[contribution guidelines](CONTRIBUTING.md). This project adheres to Qiskit's [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expect to uphold to this code.

We use [GitHub issues](https://github.com/Qiskit/qiskit/issues) for tracking requests and bugs. Please use our [slack](https://qiskit.slack.com) for discussion and simple questions. To join our Slack community use the [link](https://qiskit.slack.com/join/shared_invite/enQtNjQ5OTc5ODM1ODYyLTBlMWY1ZGJiYmZkNjliZTY4MTViNTQ3NzI2ZmU2MzQxZjlhZDZlYTAzZTNlMDU0ZjVmNzEyMzY3OGE1Y2UyNjk). For questions that are more suited for a forum we use the Qiskit tag in the [Stack Exchange](https://quantumcomputing.stackexchange.com/questions/tagged/qiskit).

## Next Steps

Now you're set up and ready to check out our
[Qiskit Tutorials](https://github.com/Qiskit/qiskit-tutorials) repository.

## Authors and Citation

Qiskit is the work of [many people](AUTHORS) who contribute to the project at
different levels. If you use Qiskit, please cite as per the included
[BibTeX file](Qiskit.bib).

## License

[Apache License 2.0](LICENSE.txt)
