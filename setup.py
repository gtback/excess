# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import xs


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

install_requires = []

setup(
    name="excess",
    version=xs.__version__,
    author="Greg Back, MITRE Corporation",
    author_email="gback@mitre.org",
    description="Make XML Schemas feel more like Python",
    packages=find_packages(),
    install_requires=[],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
