# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from setuptools import setup, find_packages

import xs

install_requires = []

setup(
    name="excess",
    version=xs.__version__,
    author="Greg Back, MITRE Corporation",
    author_email="gback@mitre.org",
    description="Make XML Schemas feel more like Python",
    packages=find_packages(),
    install_requires=install_requires,
    test_requires=['pytest'],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
