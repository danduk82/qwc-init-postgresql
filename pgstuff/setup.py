# Setup.py
# install pgstuff module

import os
import setuptools

setuptools.setup(
    name="pgstuff",
    version="0.0.1",
    author="Andrea Borghi",
    author_email="",  # TODO
    description="PostgreSQL stuff",
    long_description="PostgreSQL stuff",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    url="",  # TODO
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
