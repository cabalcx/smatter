#!/usr/bin/env python

from setuptools import setup

version_info = {}
with open('smatter/__version__.py') as f:
    exec(f.read(), version_info)

setup(
    name='smatter',
    version=version_info['__version__'],
    description='API wrapper and python client for the SMAT API.',
    author='cabalcx',
    packages=['smatter'],
    package_data={},
    url='https://github.com/cabalcx/smatter',
    python_requires='>=3.7',
    install_requires=['requests','pandas','matplotlib'],
    extras_require={
        'interactive': ['pandas', 'matplotlib'],
    },
    entry_points={},
    classifiers=[]
)