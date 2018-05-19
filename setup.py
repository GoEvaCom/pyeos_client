#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Learn more: documentation site
"""

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyeos_client',
    version='0.1.0',
    description='Wrapper for EOS RPC API',
    long_description=readme,
    author='Merouane Benthameur',
    author_email='merouane.benth@gmail.com',
    url='https://github.com/EvaCoop/pyeos_client.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['requests']
)
