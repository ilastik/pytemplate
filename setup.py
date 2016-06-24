#!/usr/bin/env python

from distutils.core import setup

setup(
    name="PyTemplate",
    version="0.1.0",
    author="Carsten Haubold",
    author_email="carsten.haubold@iwr.uni-heidelberg.com",
    description=("Python template for projects developed in the IAL lab at the University of Heidelberg"),
    license="BSD",
    keywords="...",
    url="http://github.com/ilastik/pytemplate",
    packages=['mypackage'], # list all package folders here that should be installed, e.g. also 'mypackage.util'
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7"
    ],
)
