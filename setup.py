#!/usr/bin/env python
from setuptools import setup

from longshot import __title__ as title
from longshot import __version__ as version

required = [
]

extras = {
    'develop': [
        'nose',
        'pinocchio',
    ]
}

setup(
    name=title,
    version=version,
    description="Site Tester python package.",
    scripts=[],
    author="Aaron Fay",
    author_email="afay@strathcom.com",
    packages = ['longshot'],
    install_requires=required,
    extras_require=extras,
)