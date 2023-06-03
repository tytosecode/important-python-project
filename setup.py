# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="important-python-project",
    version="0.1.0",
    description="awesome package",
    license="MIT",
    author="tytosecode",
    packages=find_packages(),
    install_requires=[
        "chekov",
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ]
)
