#!/usr/bin/env python
from setuptools import setup

from longshot import __title__ as title
from longshot import __version__ as version

required = [
    'click',
    'webdriverplus',
]

extras = {
    'develop': [
        'nose',
        'pinocchio',
        'mock',
    ]
}

setup(
    name=title,
    version=version,
    description="Site Tester python package.",
    author="Aaron Fay",
    author_email="afay@strathcom.com",
    packages=['longshot'],
    scripts=['bin/longshot'],
    install_requires=required,
    extras_require=extras,
)
