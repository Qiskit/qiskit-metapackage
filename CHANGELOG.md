# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](http://keepachangelog.com/en/1.0.0/).

> **Types of changes:**
>
> -   **Added**: for new features.
> -   **Changed**: for changes in existing functionality.
> -   **Deprecated**: for soon-to-be removed features.
> -   **Removed**: for now removed features.
> -   **Fixed**: for any bug fixes.
> -   **Security**: in case of vulnerabilities.

[UNRELEASED](https://github.com/Qiskit/qiskit-terra/compare/0.10.5...HEAD)
==========================================================================

[0.10.5](https://github.com/Qiskit/qiskit/compare/0.10.4...0.10.5) - 2019-06-27
===============================================================================

Changed
-------

- Increased the qiskit-aqua version the latest release 0.5.2, which removes
  the install dependency on pyeda


[0.10.4](https://github.com/Qiskit/qiskit/compare/0.10.3...0.10.4) - 2019-06-17
===============================================================================

Changed
-------

- Increased the qiskit-terra version the latest release 0.8.2 (#332)


[0.10.3](https://github.com/Qiskit/qiskit/compare/0.10.2...0.10.3) - 2019-05-29
===============================================================================

Changed
-------

-   Increased the qiskit-terra version the latest release 0.8.1 (\#309)

[0.10.2](https://github.com/Qiskit/qiskit/compare/0.10.1...0.10.2) - 2019-05-24
===============================================================================

Changed
-------

-   Updated `qiskit-aer` dependency to 0.2.1. (\#302)
-   Increased the qiskit-aqua version the latest release 0.5.1, this
    removes torch as a mandatory requirement. (\#303)

[0.10.1](https://github.com/Qiskit/qiskit/compare/0.10.0...0.10.1) - 2019-05-07
===============================================================================

Changed
-------

-   Updated the `qiskit-ibmq-provider` dependency to 0.2.2.

[0.10.0](https://github.com/Qiskit/qiskit/compare/0.9.0...0.10.0) - 2019-05-06
==============================================================================

Changed
-------

-   Updated the `qiskit-ibmq-provider` dependency to 0.2.1 (\#244).

[0.9.0](https://github.com/Qiskit/qiskit/compare/0.8.1...0.9.0) - 2019-05-02
============================================================================

Added
-----

-   Added the qiskit-ibmq-provider package to the metapackage (\#227).
-   Added qiskit-aqua and qiskit-chemistry to the set of installed
    packages (\#185)

Changed
-------

-   The qiskit-terra version increased to the next feature release 0.8.0
    (\#227).
-   The qiskit-aer version increased to the next feature release 0.2.0
    (\#227).
-   The qiskit-ignis version increased to the next release 0.1.1
    (\#227).

[0.8.1](https://github.com/Qiskit/qiskit/compare/0.8.0...0.8.1) - 2019-05-01
============================================================================

Changed
-------

-   Increased the qiskit-terra version to v0.7.2 which includes a fix
    for the schema validation of backend configuration in
    Qiskit/qiskit-terra\#2258 (\#217)

[0.8.0](https://github.com/Qiskit/qiskit/compare/0.7.3...0.8.0) - 2019-03-05
============================================================================

Added
-----

-   Added qiskit-ignis to the set of installed packages (\#164)

Changed
-------

-   Increased the qiskit-terra version to v0.7.1 which includes a fix
    for the BasicAer simulator issue documented in
    Qiskit/qiskit-terra\#1583 and Qiskit/qiskit-terra\#1838 (\#167).

[0.7.3](https://github.com/Qiskit/qiskit/compare/0.7.2...0.7.3) - 2019-02-20
============================================================================

Fixed
-----

-   Added a workaround for installing package when using pip 19.0.2
    (\#119)

[0.7.2](https://github.com/Qiskit/qiskit/compare/0.7.1...0.7.2) - 2019-01-23
============================================================================

Fixed
-----

-   Fixed upgrading to 0.7.x when wheel is present (\#45)

[0.7.1](https://github.com/Qiskit/qiskit/compare/0.7.0...0.7.1) - 2019-01-17
============================================================================

-   Fixed an issue when upgrading from an older `qiskit` package to a
    version [\>=0.7.0]{.title-ref} (\#32)

0.7.0 - 2018-12-19
==================

Added
-----

-   First release, includes qiskit-terra and qiskit-aer
