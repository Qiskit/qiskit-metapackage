![Image](https://raw.githubusercontent.com/Qiskit/qiskit/master/images/qiskit_header.png)

[![License](https://img.shields.io/github/license/Qiskit/qiskit.svg?)](https://opensource.org/licenses/Apache-2.0)
![Build Status](https://github.com/Qiskit/qiskit/actions/workflows/main.yml/badge.svg?branch=master)
![Build Status](https://github.com/Qiskit/qiskit/actions/workflows/docs.yml/badge.svg?branch=master)
[![](https://img.shields.io/github/release/Qiskit/qiskit.svg)](https://github.com/Qiskit/qiskit/releases)
[![Downloads](https://pepy.tech/badge/qiskit)](https://pypi.org/project/qiskit/)
[![DOI](https://zenodo.org/badge/161550823.svg)](https://zenodo.org/badge/latestdoi/161550823)

**Qiskit** is an open-source SDK for working with quantum computers at the level of circuits, algorithms, and application modules.

Qiskit is made up of elements that work together to enable quantum computing. This is a simple meta-package to install the elements of Qiskit altogether.

## Installation

The best way of installing `qiskit` is by using `pip`:

```bash
$ pip install qiskit
```

See [install](https://qiskit.org/documentation/getting_started.html) Qiskit for detailed instructions, how to use virtual environments, and
build from source standalone versions of the individual Qiskit elements and components.

## Qiskit Packaging

The Qiskit project is made up of many components that all serve a particular purpose. 
This repository contains a meta-package that will install the following components:


| Build   | Version | Contribute |
| ---     | --- | --- |
| [**Qiskit Terra**](https://github.com/Qiskit/qiskit-terra) | [![](https://img.shields.io/github/release/Qiskit/qiskit-terra.svg?)](https://github.com/Qiskit/qiskit-terra/releases)  | [![](https://img.shields.io/github/forks/Qiskit/qiskit-terra.svg?)](https://github.com/Qiskit/qiskit-terra) |
| [**Qiskit Aer**](https://github.com/Qiskit/qiskit-aer) | [![](https://img.shields.io/github/release/Qiskit/qiskit-aer.svg?)](https://github.com/Qiskit/qiskit-aer/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-aer.svg?)](https://github.com/Qiskit/qiskit-aer) |

### Deprecated

These components are installed as part of the metapackage for the time being,
but are deprecated (or will be deprecated in the near future) and will be
removed in a future release.

| Build   | Version | Contribute |
| ---     | ---     | --- |
| [**Qiskit Ignis**](https://github.com/Qiskit/qiskit-ignis) | [![](https://img.shields.io/github/release/Qiskit/qiskit-ignis.svg?)](https://github.com/Qiskit/qiskit-ignis/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-ignis.svg?)](https://github.com/Qiskit/qiskit-ignis) |
| [**Qiskit IBM Quantum Provider**](https://github.com/Qiskit/qiskit-ibmq-provider)  |  [![](https://img.shields.io/github/release/Qiskit/qiskit-ibmq-provider.svg?)](https://github.com/Qiskit/qiskit-ibmq-provider/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-ibmq-provider.svg?)](https://github.com/Qiskit/qiskit-ibmq-provider) |

### Optional components

These components are part of the Qiskit ecosystem but are built on top of
`qiskit` and are not installed by default with the meta-package. You can either
install them manually, as an optional extra
(ie `pip install "qiskit[finance,experiments]"`), or all together with
`pip install "qiskit[all]"`.

| Build | Version | Contribute |
| ---   | --- | --- |
| [**Qiskit Optimization**](https://github.com/Qiskit/qiskit-optimization) | [![](https://img.shields.io/github/release/Qiskit/qiskit-optimization.svg?)](https://github.com/Qiskit/qiskit-optimization/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-optimization.svg?)](https://github.com/Qiskit/qiskit-optimization) |
| [**Qiskit Finance**](https://github.com/Qiskit/qiskit-finance) |  [![](https://img.shields.io/github/release/Qiskit/qiskit-finance.svg?)](https://github.com/Qiskit/qiskit-finance/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-finance.svg?)](https://github.com/Qiskit/qiskit-finance) |
| [**Qiskit Machine Learning**](https://github.com/Qiskit/qiskit-machine-learning) | [![](https://img.shields.io/github/release/Qiskit/qiskit-machine-learning.svg?)](https://github.com/Qiskit/qiskit-machine-learning/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-machine-learning.svg?)](https://github.com/Qiskit/qiskit-machine-learning) |
| [**Qiskit Nature**](https://github.com/Qiskit/qiskit-nature) |  [![](https://img.shields.io/github/release/Qiskit/qiskit-nature.svg?)](https://github.com/Qiskit/qiskit-nature/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-nature.svg?)](https://github.com/Qiskit/qiskit-nature) |
| [**Qiskit Experiments**](https://github.com/Qiskit/qiskit-experiments) |  [![](https://img.shields.io/github/release/Qiskit/qiskit-experiments.svg?)](https://github.com/Qiskit/qiskit-experiments/releases) | [![](https://img.shields.io/github/forks/Qiskit/qiskit-experiments.svg?)](https://github.com/Qiskit/qiskit-experiments) |

### Using quantum services

If you are interested in using quantum services (i.e. using a real quantum
computer, not a simulator) you can look at the Qiskit Partners program for
partner organizations that have provider packages available for their offerings:

https://qiskit.org/documentation/partners/

## Contribution Guidelines

If you'd like to contribute to Qiskit, please take a look at our
[contribution guidelines](https://qiskit.org/documentation/contributing_to_qiskit.html). This project adheres to Qiskit's [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

We use [GitHub issues](https://github.com/Qiskit/qiskit/issues) for tracking requests and bugs. Please use our [Slack](http://ibm.co/joinqiskitslack) for discussion and simple questions. For questions that are more suited for a forum we use the Qiskit tag in the [Stack Exchange](https://quantumcomputing.stackexchange.com/questions/tagged/qiskit).

## Next Steps

Now you're set up and ready to check out our
[Qiskit Tutorials](https://github.com/Qiskit/qiskit-tutorials) repository.

## Authors and Citation

Qiskit is the work of [many people](AUTHORS) who contribute to the project at
different levels. If you use Qiskit, please cite as per the included
[BibTeX file](Qiskit.bib).

## License

[Apache License 2.0](LICENSE.txt)
