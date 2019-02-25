# Contributing

The documentation and bechmarking of Qiskit is contained in this repository. Below you will find the information for contributing to them. If you want to contribute with one of the Qiskit elements or components, refer to their individual Contributing guidelines:

* [Qiskit Terra](https://github.com/Qiskit/qiskit-terra/blob/master/.github/CONTRIBUTING.rst)
* [Qiskit Aer](https://github.com/Qiskit/qiskit-aer/blob/master/.github/CONTRIBUTING.md)
* [Qiskit Aqua](https://github.com/Qiskit/qiskit-aqua/blob/master/.github/CONTRIBUTING.rst)
* [Qiskit Chemistry](https://github.com/Qiskit/qiskit-chemistry/blob/master/.github/CONTRIBUTING.rst)

## Contributor License Agreement

We'd love to accept your code! Before we can, we have to get a few legal
requirements sorted out. By having you sign a Contributor License Agreement (CLA), we
ensure that the community is free to use your contributions.

When you contribute to the Qiskit project with a new pull request, a bot will
evaluate whether you have signed the CLA. If required, the bot will comment on
the pull request,  including a link to accept the agreement. The
[individual CLA](https://qiskit.org/license/qiskit-cla.pdf) document is
available for review as a PDF.

If you work for a company that wants to allow you to contribute your work,
then you'll need to sign a [corporate CLA](https://qiskit.org/license/qiskit-corporate-cla.pdf)
and email it to us at qiskit@qiskit.org.

## Documentation

The documentation of Qiskit is in the ``docs`` directory. The
documentation is generated using [Sphinx](http://www.sphinx-doc.org). In the main directory are the installing and general files and then in each subdirectory contains documentation for each element of Qiskit. Once a pull request is accepted the documentation will be auto-generated and rendered at [https://qiskit.org/documentation](https://qiskit.org/documentation).

To edit the documentation, edit the rst files directly and then a html version can be made using:

```bash
    $> make doc
```

The local html version of the documentation can be found at `docs/_build/html/index.html`.  


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


## What Happened to Qiskit `0.6`?

Prior to version `0.7`, both Terra and Aer elements lived together under the `qiskit` package. In
`0.7` we split `qiskit` into `qiskit-terra` and `qiskit-aer`.

The Terra element is the foundation of Qiskit and allows you to write quantum circuits with our
Python API and run them using the built-in simulators provided with the package. The Aer element is a
collection of native simulators designed to be fast and full-featured.

If you don't need/want these simulators, you can always install `qiskit-terra` in isolation by
issuing the following command:

```
$ pip install qiskit-terra
```
