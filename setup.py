#!/usr/bin/env python
try:
    from sixpack_client import __version__
except ImportError:
    __version__ = 'derp'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='Sixpack-client',
    version=__version__,
    author='SeatGeek',
    author_email='hi@seatgeek.com',
    packages=['sixpack_client', 'sixpack_client.test'],
    url='http://github.com/seatgeek/sixpack-py',
    license=open('LICENSE.txt').read(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    description='Python client for Sixpack, an A/B testing framework under active development at SeatGeek',
    long_description=open('README.rst').read(),
    tests_require=['nose'],
    test_suite='nose.collector',
    install_requires=open('requirements.txt').readlines(),
    include_package_data=True,
)
