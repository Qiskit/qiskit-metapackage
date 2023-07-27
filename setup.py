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

import os

from setuptools import setup

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
with open(README_PATH) as readme_file:
    README = readme_file.read()

# NOTE: The lists below require each requirement on a separate line,
# putting multiple requirements on the same line will prevent qiskit-bot
# from correctly updating the versions for the qiskit packages.
requirements = [
    "qiskit-terra==0.25.0",
]


optimization_extra = [
    "qiskit-optimization>=0.4.0",
]


finance_extra = [
    "qiskit-finance>=0.3.3",
]


machine_learning_extra = [
    "qiskit-machine-learning>=0.4.0",
]


nature_extra = [
    "qiskit-nature>=0.4.1",
]

experiments_extra = [
    "qiskit-experiments>=0.2.0",
]

visualization_extra = [
    "matplotlib>=2.1",
    "ipywidgets>=7.3.0",
    "pydot",
    "pillow>=4.2.1",
    "pylatexenc>=1.4",
    "seaborn>=0.9.0",
    "pygments>=2.4",
]


setup(
    name="qiskit",
    version="0.44.0",
    description="Software for developing quantum computing programs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://qiskit.org/",
    author="Qiskit Development Team",
    author_email="hello@qiskit.org",
    license="Apache 2.0",
    py_modules=[],
    packages=[],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    install_requires=requirements,
    project_urls={
        "Bug Tracker": "https://github.com/Qiskit/qiskit/issues",
        "Documentation": "https://qiskit.org/documentation/",
        "Source Code": "https://github.com/Qiskit/qiskit",
    },
    include_package_data=True,
    python_requires=">=3.7",
    extras_require={
        "visualization": visualization_extra,
        "all": optimization_extra
        + finance_extra
        + machine_learning_extra
        + nature_extra
        + experiments_extra
        + visualization_extra,
        "experiments": experiments_extra,
        "optimization": optimization_extra,
        "finance": finance_extra,
        "machine-learning": machine_learning_extra,
        "nature": nature_extra,
    },
)
