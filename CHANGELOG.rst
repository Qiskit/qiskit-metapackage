*********
Changelog
*********

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_.

  **Types of changes:**

  - **Added**: for new features.
  - **Changed**: for changes in existing functionality.
  - **Deprecated**: for soon-to-be removed features.
  - **Removed**: for now removed features.
  - **Fixed**: for any bug fixes.
  - **Security**: in case of vulnerabilities.

`UNRELEASED`_
=============


`0.8.1`_ - 2019-05-01
=====================

Changed
-------

- Increased the qiskit-terra version to v0.7.2 which includes a fix for the
  schema validation of backend configuration in Qiskit/qiskit-terra#2258 (#217)


`0.8.0`_ - 2019-03-05
=====================

Added
-----

- Added qiskit-ignis to the set of installed packages (#164)

Changed
-------

- Increased the qiskit-terra version to v0.7.1 which includes a fix for the
  BasicAer simulator issue documented in Qiskit/qiskit-terra#1583 and
  Qiskit/qiskit-terra#1838 (#167).


`0.7.3`_ - 2019-02-20
=====================

Fixed
-----

- Added a workaround for installing package when using pip 19.0.2 (#119)

`0.7.2`_ - 2019-01-23
=====================

Fixed
-----

- Fixed upgrading to 0.7.x  when wheel is present (#45)

`0.7.1`_ - 2019-01-17
=====================

- Fixed an issue when upgrading from an older ``qiskit`` package to a version
  `>=0.7.0` (#32)

0.7.0 - 2018-12-19
=====================

Added
-----

- First release, includes qiskit-terra and qiskit-aer

.. _UNRELEASED: https://github.com/Qiskit/qiskit-terra/compare/0.8.1...HEAD
.. _0.8.1: https://github.com/Qiskit/qiskit/compare/0.8.0...0.8.1
.. _0.8.0: https://github.com/Qiskit/qiskit/compare/0.7.3...0.8.0
.. _0.7.3: https://github.com/Qiskit/qiskit/compare/0.7.2...0.7.3
.. _0.7.2: https://github.com/Qiskit/qiskit/compare/0.7.1...0.7.2
.. _0.7.1: https://github.com/Qiskit/qiskit/compare/0.7.0...0.7.1

.. _Keep a Changelog: http://keepachangelog.com/en/1.0.0/
