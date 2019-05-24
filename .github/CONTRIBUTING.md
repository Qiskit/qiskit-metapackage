# Contributing

The documentation and bechmarking of Qiskit is contained in this repository. Below you will find the information for contributing to them. If you want to contribute with one of the Qiskit elements or components, refer to their individual Contributing guidelines:

* [Qiskit Terra](https://github.com/Qiskit/qiskit-terra/blob/master/.github/CONTRIBUTING.rst)
* [Qiskit Aer](https://github.com/Qiskit/qiskit-aer/blob/master/.github/CONTRIBUTING.md)
* [Qiskit Ignis](https://github.com/Qiskit/qiskit-ignis/blob/master/.github/CONTRIBUTING.md)
* [Qiskit Aqua](https://github.com/Qiskit/qiskit-aqua/blob/master/.github/CONTRIBUTING.rst)
* [Qiskit Chemistry](https://github.com/Qiskit/qiskit-chemistry/blob/master/.github/CONTRIBUTING.rst)
* [Qiskit IBM Q Provider](https://github.com/Qiskit/qiskit-ibmq-provider/blob/master/.github/CONTRIBUTING.rst)

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

Details on the versioning procedure are documented here:
<https://qiskit.org/documentation/versioning.html>

