#!/usr/bin/env python

from distutils.core import setup

setup(name='todo_deploy',
      version='1.0',
      description='Deployment framework for todo',
      author='Kenny Tsung',
      author_email='ktsung@todo.com',
      url='http:/todo.com',
      packages=['toto_deploy'],
      install_requires=[
          'ansible',
      ]
)