# Contributing

The documentation and benchmarking of Qiskit is contained in this repository. To contribute
to them please read the
[contributing guide](https://qiskit.org/documentation/contributing_to_qiskit.html).

## Contributor License Agreement

Before you can submit any code we need all contributors to sign a
contributor license agreement. By signing a contributor license
agreement (CLA) you're basically just attesting to the fact
that you are the author of the contribution and that you're freely
contributing it under the terms of the Apache-2.0 license.

When you contribute to the Qiskit project with a new pull request,
a bot will evaluate whether you have signed the CLA. If required, the
bot will comment on the pull request, including a link to accept the
agreement. The [individual CLA](https://qiskit.org/license/qiskit-cla.pdf)
document is available for review as a PDF.

**Note**:
> If your contribution is part of your employment or your contribution
> is the property of your employer, then you will likely need to sign a
> [corporate CLA](https://qiskit.org/license/qiskit-corporate-cla.pdf) too and
> email it to us at <qiskit@us.ibm.com>.


## Documentation

The documentation of Qiskit is in the ``docs`` directory. The
documentation is generated using [Sphinx](http://www.sphinx-doc.org). In the main directory are the installing and general files. Once a pull request is accepted the documentation will be auto-generated and rendered at [https://qiskit.org/documentation](https://qiskit.org/documentation).

To edit the documentation, edit the rst files directly and then a html version can be made using:

```bash
    $> make doc
```

The local html version of the documentation can be found at `docs/_build/html/index.html`.  

