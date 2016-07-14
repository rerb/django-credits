#!/usr/bin/env python
from setuptools import setup
import os


# Utility function to read README file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='django-credits',
      version='0.1',
      description="A marquee for giving credit to contributors.",
      author='Bob Erb',
      author_email='bob.erb@gmail.com',
      url='https://github.com/rerb/django-credits',
      long_description=read("README.rst"),
      packages=['django_credits'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Framework :: Django',
      ],
      install_requires=["Django>=1.4"],
      zip_save=False)
