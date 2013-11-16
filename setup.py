#!/usr/bin/env python

import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))


install_requires = [
    'Jinja2'
    ]

setup(name='Heractor',
      version='1.0',
      description='Static site Creator',
      author='Dmitry Vysochin',
      author_email='dmitry.vysochin@gmail.com',
      url='',
      install_requires=install_requires,
      packages=['heractor',],
     )