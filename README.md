![Image](https://raw.githubusercontent.com/Qiskit/qiskit-metapackage/master/images/qiskit_header.png)

[![License](https://img.shields.io/github/license/Qiskit/qiskit-metapackage.svg?)](https://opensource.org/licenses/Apache-2.0)
![Build Status](https://github.com/Qiskit/qiskit-metapackage/actions/workflows/main.yml/badge.svg?branch=master)
![Build Status](https://github.com/Qiskit/qiskit-metapackage/actions/workflows/docs.yml/badge.svg?branch=master)
[![](https://img.shields.io/github/release/Qiskit/qiskit-metapackage.svg)](https://github.com/Qiskit/qiskit-metapackage/releases)
[![Downloads](https://pepy.tech/badge/qiskit)](https://pypi.org/project/qiskit/)
[![DOI](https://zenodo.org/badge/161550823.svg)](https://zenodo.org/badge/latestdoi/161550823)

**Qiskit** is an open-source SDK for working with quantum computers at the level of circuits, algorithms, and application modules.

## Installation

The best way of installing `qiskit` is by using `pip`:

```bash
$ pip install qiskit
```

See [install](https://qiskit.org/documentation/getting_started.html) Qiskit for detailed instructions, how to use virtual environments, and
build from source standalone versions of the individual Qiskit elements and components.

## Qiskit Packaging

The Qiskit project used to be made up of many components. However, in the future the Qiskit metapackage will only install [**Qiskit Terra**](https://github.com/Qiskit/qiskit-terra):

| Build   | Version | Contribute |
| ---     | --- | --- |
| [**Qiskit Terra**](https://github.com/Qiskit/qiskit-terra) | [![](https://img.shields.io/github/release/Qiskit/qiskit-terra.svg?)](https://github.com/Qiskit/qiskit-terra/releases)  | [![](https://img.shields.io/github/forks/Qiskit/qiskit-terra.svg?)](https://github.com/Qiskit/qiskit-terra) |

<table>
  <tr>
    <td colspan="3" align="center">:warning: WARNING :warning:</br> <b>For the time being, two other packages are installed, but these components will be removed from the metapackage in a future release.</b></td>
  </tr>
<tr>
<th>Build</th>
<th>Version</th>
<th>Contribute</th>
</tr>
<tr>
<td><a href="https://github.com/Qiskit/qiskit-aer"><strong>Qiskit Aer</strong></a></td>
<td><a href="https://github.com/Qiskit/qiskit-aer/releases"><img src="https://camo.githubusercontent.com/7b4ebed2975693dc2d18233e49b7f9141838c1e86f22ac36f465fcd3886821b6/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f5169736b69742f7169736b69742d6165722e7376673f" alt="" data-canonical-src="https://img.shields.io/github/release/Qiskit/qiskit-aer.svg?"></a></td>
<td><a href="https://github.com/Qiskit/qiskit-aer"><img src="https://camo.githubusercontent.com/ced831707852701ae4c21b1455d6c2d2a03fa54dffe09fcf5208970112023a05/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f5169736b69742f7169736b69742d6165722e7376673f" alt="" data-canonical-src="https://img.shields.io/github/forks/Qiskit/qiskit-aer.svg?"></a></td>
</tr>
<tr>
<td><a href="https://github.com/Qiskit/qiskit-ibmq-provider"><strong>Qiskit IBM Quantum Provider</strong></a></td>
<td><a href="https://github.com/Qiskit/qiskit-ibmq-provider/releases"><img src="https://camo.githubusercontent.com/daa12aee2f03d2d310bd6ad1a5c5babe99b038fc08ad9f0309f5e1c7420c9ffe/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f5169736b69742f7169736b69742d69626d712d70726f76696465722e7376673f" alt="" data-canonical-src="https://img.shields.io/github/release/Qiskit/qiskit-ibmq-provider.svg?"></a></td>
<td><a href="https://github.com/Qiskit/qiskit-ibmq-provider"><img src="https://camo.githubusercontent.com/49f1938883f91358a594feeddecdd59b3188a353a9a20721a6fefcd64c32f6ce/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f5169736b69742f7169736b69742d69626d712d70726f76696465722e7376673f" alt="" data-canonical-src="https://img.shields.io/github/forks/Qiskit/qiskit-ibmq-provider.svg?"></a></td>
</tr>
</table>

### Using quantum services

If you are interested in using quantum services, you can check out [the Providers page](https://qiskit.org/providers/) for the list of available providers that Qiskit supports.

## Contribution Guidelines

If you'd like to contribute to Qiskit, please take a look at our
[contribution guidelines](https://qiskit.org/documentation/contributing_to_qiskit.html). This project adheres to Qiskit's [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

We use [GitHub issues](https://github.com/Qiskit/qiskit-metapackage/issues) for tracking requests and bugs. Please use our [Slack](https://qisk.it/join-slack) for discussion and simple questions. For questions that are more suited for a forum we use the Qiskit tag in the [Stack Exchange](https://quantumcomputing.stackexchange.com/questions/tagged/qiskit).

## Next Steps

Now you're set up and ready to check out our
[Qiskit Tutorials](https://github.com/Qiskit/qiskit-tutorials) repository.

## Authors and Citation

Qiskit is the work of [many people who contribute to the project](https://github.com/Qiskit/qiskit-terra/graphs/contributors) at
different levels. If you use Qiskit, please cite as per the included
[BibTeX file](https://github.com/Qiskit/qiskit-terra/blob/main/CITATION.bib).

## License

[Apache License 2.0](LICENSE.txt)
