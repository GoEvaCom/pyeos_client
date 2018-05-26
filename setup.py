#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Learn more: documentation site
"""

from setuptools import setup, find_packages


with open('README.md', "r") as f:
    readme = f.read()

setup(
    name='pyeos_client',
    version='0.1.9',
    description='Wrapper for EOS RPC API',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Merouane Benthameur',
    author_email='merouane.benth@gmail.com',
    url='https://github.com/EvaCoop/pyeos_client.git',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['requests'],
    python_requires='>=3',
    classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools'
        ),
)
