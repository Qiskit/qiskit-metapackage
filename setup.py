# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

from setuptools import setup

qiskit_terra = "qiskit_terra==0.8.2"

requirements = [
    qiskit_terra,
    "qiskit-aer==0.2.3",
    "qiskit-ibmq-provider==0.3.0",
    "qiskit-ignis==0.1.1",
    "qiskit-aqua==0.5.2",
    "qiskit-chemistry==0.5.0"
]


setup(
    name="qiskit",
    version="0.11.0",
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
)
