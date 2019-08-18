# Contributing

The documentation and benchmarking of Qiskit is contained in this repository. To contribute
to them please read the
[contributing guide](https://qiskit.org/documentation/contributing_to_qiskit.html).

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

