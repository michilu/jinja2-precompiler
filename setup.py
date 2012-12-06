#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name="jinja2-precompiler",
      version="0.1",
      description="Pre-compile Jinja2 templates to Python byte code",
      long_description=open('README.rst').read(),
      author="ENDOH takanao",
      license="BSD",
      url="http://github.com/MiCHiLU/jinja2-precompiler",
      keywords=' '.join([
        'jinja2',
        'python',
        'template',
        ]
      ),
      classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Utilities',
        ],
      py_modules=['jinja2precompiler'],
      install_requires=['jinja2'],
      entry_points={
        'console_scripts': [
          'jinja2precompiler = jinja2precompiler:main',
          ]
      },
      zip_safe=False,
)
