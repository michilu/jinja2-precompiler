#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, Command

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py', 'tests'])
        raise SystemExit(errno)

class PyTestWithCov(PyTest):
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py', 'tests', '--cov-report=html', '--cov=.', '--pdb'])
        raise SystemExit(errno)

setup(name="jinja2-precompiler",
      version="0.2",
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        ],
      py_modules=['jinja2precompiler'],
      install_requires=['jinja2'],
      entry_points={
        'console_scripts': [
          'jinja2precompiler = jinja2precompiler:main',
          ]
      },
      zip_safe=False,
      cmdclass = {
        'test': PyTest,
        'cov': PyTestWithCov,
      },
)
