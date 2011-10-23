#-*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='dploi-server',
    version='0.2a',
    description='The awesome deployment server for django apps',
    author='Stefan Foulis',
    author_email='stefan.foulis@gmail.com',
    url='https://github.com/dploi/dploi-server',
    packages=find_packages(),
    install_requires=[
        'Django>=1.3.1',
        'South>=0.7.3',
        'djangorestframework>=0.2.3',
    ],
    entry_points={
        'console_scripts': [
            'dploi-server = dploi_server.main:main',
        ]
    },
)