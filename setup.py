"""
Module setup for installation
"""

import os
from setuptools import setup


def load_requirements(fname):
    """Turn requirements.txt into a list"""
    requirements = []
    if os.path.exists(fname):
        with open(fname, "r") as fp:
            requirements = [line.strip() for line in fp]
    return requirements


setup(
    name="strictdf",
    version="0.1.1",

    install_requires=load_requirements('requirements.txt'),

    tests_require=["pytest"],
    test_suite="tests",
    extras_require={'dev': load_requirements('requirements-dev.txt')},
    python_requires=">=3.9",
)
