#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


README = open('README.md', 'r').read()


requirements = [
    'click==6.7',
    'boto3>=1.9.0,<2.0.0',
    'sh>=1.10.0,<2.0.0',
]


setup(
    name='aws-secrets-sync',
    version='0.0.1',
    description='Keep a local repo and AWS Secrets Manager in sync',
    long_description=README,
    author='Spacetime Labs',
    author_email='dev@spacetimelabs.ai',
    packages=find_packages(),
    package_dir={'awssecretssync': 'awssecretssync'},
    install_requires=requirements,
    license='BSD',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'secretssync=awssecretssync.__main__:run',
            'secretssynceditor=awssecretssync.passeditor:editor'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ]
)
