# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

from setuptools import setup

requirements = [
    "qiskit-terra>=0.7,<0.8",
    "qiskit-aer>=0.1,<0.2",
]

setup(
    name="qiskit",
    version="0.7.0",
    description="Software for developing quantum computing programs",
    long_description="""Qiskit is a software development kit for writing
        quantum computing experiments, programs, and applications. Works with
        Python 3.5 and 3.6""",
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
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.5"
)
