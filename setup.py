"""
Module setup for installation
"""

from setuptools import find_packages, setup
from subprocess import call


requirements = None
if not call(['pipenv', 'lock', '--requirements', '>', 'requirements.txt']):
    with open("requirements.txt", "r") as fp:
        requirements = [line.strip() for line in fp]
else:
    print('Error generating requirements.txt file')
    exit(1)


setup(
    name="strict_df",

    author="Cristian Contrera",
    author_email="cristiancontrera95@gmail.com",

    packages=find_packages(exclude=['tests']),
    version="0.1.0",
    license="MIT",
    description="pandas DataFrame wrapper",

    install_requires=requirements,

    tests_require=["pytest"],
    test_suite="tests",
    extras_require=["requests"],
    python_requires='>=3.9',

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
