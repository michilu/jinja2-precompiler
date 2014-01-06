Jinja2 pre-compiler |Build Status|_
===================================

Pre-compile Jinja2 templates to Python byte code.

.. |Build Status| image:: https://travis-ci.org/MiCHiLU/jinja2-precompiler.png?branch=master
.. _`Build Status`: http://travis-ci.org/MiCHiLU/jinja2-precompiler


Usage
-----
Jinja2 pre-compiler comes with a utility script called ``jinja2precompiler``.
Please type ``jinja2precompiler --help`` at the shell prompt to
know more about this tool.

Compiling the Jinja2 template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then run ``jinja2precompiler`` command::

  $ jinja2precompiler templates
  Compiling into folder "templates"
  ...
  Compiled "templates/template.html" as tmpl_5f0fcb0ed56efa600c50d9f2870192327823c063.py
  ...
  Finished compiling templates

Will compiling to Python byte code with ``--pyc`` option::

  $ jinja2precompiler --pyc templates
  Compiling into folder "templates"
  ...
  Compiled "templates/template.html" as tmpl_5f0fcb0ed56efa600c50d9f2870192327823c063.pyc
  ...
  Finished compiling templates

Get the compiled module name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Will return a module file name with ``--modulename`` option::

  $ jinja2precompiler --modulename templates/template.html
  tmpl_41d3b4a4b71afe0c223778e57c23244caee1baec.py

  $ jinja2precompiler --modulename --pyc templates/template.html
  tmpl_41d3b4a4b71afe0c223778e57c23244caee1baec.pyc

And you can prepend directory path with ``--base`` option::

  $ jinja2precompiler --modulename --base=templates templates/template.html
  templates/tmpl_5f0fcb0ed56efa600c50d9f2870192327823c063.py

Will return module file names you specify the argument more than one::

  $ jinja2precompiler --modulename a.html b.html c.html
  tmpl_25e7e8960b03ecb19189f36b8ef611389397c95c.py tmpl_83d0d31e29a7746a19536d616218a384f62d4694.py tmpl_45ecd51cee2d33904a8cd1af7c441dd3fc320870.py

With Make
~~~~~~~~~

An example ``Makefile`` file::

  templates_compiled.zip: $(wildcard templates/*.html)
  	jinja2precompiler -c templates
  	zip -FS -j templates_compiled.zip templates/*.pyc

Will compiling only updated files and storing into the zip file.


Installation
------------
Installing from PyPI using ``pip``::

    pip install jinja2precompiler

Installing from PyPI using ``easy_install``::

    easy_install jinja2precompiler

Installing from source::

    python setup.py install


Dependencies
------------
1. Jinja2_


Changes
-------

0.2: supports walking symlink directories


Licensing
---------
Jinja2 pre-compiler is licensed under the terms of the `BSD 3-Clause`_.

Copyright 2012 ENDOH takanao.

Project `source code`_ is available at Github. Please report bugs and file
enhancement requests at the `issue tracker`_.


.. links:
.. _Jinja2: http://jinja.pocoo.org/
.. _BSD 3-Clause: http://opensource.org/licenses/BSD-3-Clause
.. _issue tracker: http://github.com/MiCHiLU/jinja2-precompiler/issues
.. _source code: http://github.com/MiCHiLU/jinja2-precompiler
