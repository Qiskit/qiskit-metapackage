#################
Qiskit Versioning
#################

The Qiskit project is made up of several elements each performing different
functionality. Each is independently useful and can be used on their own,
but for convience we provide this repository and meta-package to provide
a single entrypoint to install all the elements at once. This is to simplify
the install process and provide a unifed interface to end users. However,
because each Qiskit element has it's own releases and versions some care is
needed when dealing with versions between the different repositories. This
document outlines the guidelines for dealing with versions and releases of
both Qiskit elements and the meta-package.

For the rest of this guide the standard Sematic Versioning nomenclature will
be used of: ``Major.Minor.Patch`` to refer to the different components of a
version number. For example, if the version number was ``0.7.1``, then the major
version is ``0``, the minor version ``7``, and the patch version ``1``.


Meta-package Version
====================

The Qiskit meta-package version is an independent value that is determined by
the releases of each of the elements being tracked. Each time we push a release
to a tracked component (or add an element) the meta-package requirements, and
version will need to be updated and a new release published. The timing should
be coordinated with the release of elements to ensure that the meta-package
releases track with element releases.

Adding new elements
-------------------

When a new Qiskit element is being added to the meta-package requirements, we
need to increase the **Minor** version of the meta-package.

For example, if the meta-package is tracking 2 elements ``qiskit-aer`` and
``qiskit-terra`` and it's version is ``0.7.4``. Then we release a new element
``qiskit-ignis`` that we intend to also have included in the meta-package. When
we add the new element to the meta-package we increase the version to
``0.8.0``.


Patch Version Increases
-----------------------

When any Qiskit element that is being already tracked by the meta-package
releases a patch version to fix bugs in a release we need also bump the
requirement in the setup.py and then increase the patch version of the
meta-package.

For example, if the meta-package is tracking 3 elements ``qiskit-terra==0.8.1``,
``qiskit-aer==0.2.1``, and ``qiskit-ignis==0.1.4`` with the current version
``0.9.6``. When qiskit-terra release a new patch version to fix a bug ``0.8.2``
the meta-package will also need to increase it's patch version and release,
becoming ``0.9.7``.

Additionally, there are occasionally packaging or other bugs in the
meta-package itself that need to be fixed by pushing new releases. When those
are encountered we should increase the patch version to differentiate it from
the broken release. Do **not** delete the broken or any old releases from pypi
in any situation, instead just increase the patch version and upload a new
release.


Minor Version Increases
-----------------------

Besides adding a new element to the meta-package the minor version of the
meta-package should also be increased anytime a minor version is increased in
a tracked element.

For example, if the meta-package is tracking 2 elements ``qiskit-terra==0.7.0``
and ``qiskit-aer==0.1.1`` and the current version is ``0.7.5``. When the
``qiskit-aer`` element releases ``0.2.0`` then we need to increase the
meta-package version to be ``0.8.0`` to correspond to the new release.


Major Version Increases
-----------------------

The major version is different from the other version number components. Unlike
the other version number components, which are updated in lock step with each
tracked element, the major version is only increased when all tracked versions
are bumped (at least before ``1.0.0``). Right now all the elements still have
a major version number component of ``0`` and until each tracked element in the
meta-repository is marked as stable by bumping the major version to be ``>=1``
then the meta-package version should not increase the major version.

The behavior of the major version number component tracking after when all the
elements are at >=1.0.0 has not been decided yet.


Qiskit Element Requirement Tracking
===================================

While not strictly related to the meta-package and Qiskit versioning how we
track the element versions in the meta-package's requirements list is
important. Each element listed in the setup.py should be pinned to a single
version. This means that each version of Qiskit should only install a single
version for each tracked element. For example, the requirements list at any
given point should look something like::

  requirements = [
      "qiskit_terra==0.7.0",
      "qiskit-aer==0.1.1",
  ]

This is to aid in debugging, but also make tracking the versions across
multiple elements more transparent.

It is also worth pointing out that the order we install the elements is
critically important too. ``pip`` does not have a real dependency solver which
means the installation order matters. So if there are overlapping requirements
versions between elements or dependencies between elements we need to ensure
that the order in the requirements list installs everything as expected. If the
order needs to be change for some install time incompatibility it should be
noted clearly.
