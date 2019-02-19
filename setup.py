# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import sys
import subprocess

from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop

qiskit_terra = "qiskit-terra>=0.7,<0.8"

requirements = [
    qiskit_terra,
    "qiskit-aer>=0.1,<0.2",
]


def _reinstall_terra():
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--no-deps", "-I", qiskit_terra])


class _install(install):
    """Custom install command to force reinstalling qiskit-terra after removing
    qiskit."""

    def run(self):
        super().run()
        _reinstall_terra()


class _develop(develop):
    """Custom develop command to force reinstalling qiskit-terra after removing
    qiskit."""

    def run(self):
        super().run()
        _reinstall_terra()


_COMMANDS = { 'develop': _develop, 'install': _install }


try:
    from wheel.bdist_wheel import bdist_wheel

    class _bdist_wheel(bdist_wheel):
        """Custom bdist_wheel command to force cancelling qiskit-terra wheel
        creation."""

        def run(self):
            """Intentionally terminating the process with an error code."""
            sys.exit(-1)


    _COMMANDS['bdist_wheel'] = _bdist_wheel

except:
    pass


setup(
    name="qiskit",
    version="0.7.3",
    description="Software for developing quantum computing programs",
    long_description="Qiskit is a software development kit for writing "
                     "quantum computing experiments, programs, and "
                     "applications. Works with Python 3.5, 3.6, and 3.7",
    url="https://github.com/Qiskit/qiskit",
    author="Qiskit Development Team",
    author_email="qiskit@us.ibm.com",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.5",
    # qiskit 0.7 metapackage has a bug for which qiskit 0.6.1 cannot correctly
    # upgrade to 0.7: some Terra files are deleted when removing qiskit 0.6.1
    # before installing qiskit 0.7 but after installing its dependencies. More
    # detailed info is provided at:
    # https://github.com/Qiskit/qiskit/issues/27#issue-396844438
    # https://github.com/Qiskit/qiskit/issues/27#issuecomment-455598103
    #
    # The fix overrides 'install' and 'develop' setuptools commands to force
    # reinstalling 'qiskit-terra' after installation to restore the missing files.
    #
    # For this fix to work, we cannot distribute a wheel version of the metapackage
    # (which does not provide any advantage right now). We can remove the fix once
    # we don't support updating from 0.6.
    cmdclass=_COMMANDS
)
