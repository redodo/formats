# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='formats',
    version='0.1.1',
    description='Support multiple formats with ease',
    long_description=long_description,
    url='https://github.com/redodo/formats',
    author='Hidde Bultsma',
    author_email='dodo@gododo.co',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='formats, load, dump, parse, compose, convert',
    packages=['formats'],
    install_requires=[],
)

