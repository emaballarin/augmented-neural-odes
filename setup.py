# Copyright (c) 2018- Emilien Dupont
# Copyright (c) 2019- Yana Hasson <yana.hasson.inria@gmail.com>
# Copyright (c) 2020- AI-CPS@UniTS
# Copyright (c) 2020- Emanuele Ballarin <emanuele@ballarin.cc>
# SPDX-License-Identifier: MIT

from setuptools import find_packages, setup
import warnings


DEPENDENCY_PACKAGE_NAMES = [
    "imageio",
    "matplotlib",
    "numpy",
    "torch",
    "torchvision",
    "git+https://github.com/rtqichen/torchdiffeq.git",
]


def check_dependencies():
    missing_dependencies = []
    for package_name in DEPENDENCY_PACKAGE_NAMES:
        try:
            __import__(package_name)
        except ImportError:
            missing_dependencies.append(package_name)

    if missing_dependencies:
        warnings.warn("Missing dependencies: {}.".format(missing_dependencies))


with open("README.md", "r") as fh:
    long_description = fh.read()


check_dependencies()


setup(
    name="anode",
    version="0.0.1",
    author="Emilien Dupont",
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.7.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
)
