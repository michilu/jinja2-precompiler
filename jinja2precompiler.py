#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser
import logging
import os
import re
import sys

import jinja2

def option_parse():
  parser = OptionParser()
  parser.add_option("-a", "--all", action="store_true", dest="all_files", help="all files")
  parser.add_option("-b", "--base", dest="base", default="", help="base dir name", metavar="DIR")
  parser.add_option("-c", "--pyc", action="store_true", dest="pyc", help="byte compile")
  parser.add_option("-d", "--debug", action="store_true", dest="debug", help="debug")
  parser.add_option("-e", "--ext", dest="extensions", default="html,xhtml", help="list of extension [default: %default]", metavar="EXT[,...]")
  parser.add_option("-m", "--modulename", action="store_true", dest="modulename", help="return compiled module file name")
  parser.add_option("-q", "--quit", action="store_true", dest="quit", help="no message")
  parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="more messages")
  (options, args) = parser.parse_args()
  return parser, options, args

def get_module_filename(filename, py_compile=False):
  module_filename = jinja2.ModuleLoader.get_module_filename(filename)
  if py_compile:
    module_filename += "c"
  return module_filename

def make_filter_func(target, env, extensions=None, all_files=False):

  def filter_func(tpl):
    if extensions is not None and os.path.splitext(tpl)[1][1:] not in extensions:
      return False
    if all_files:
      return True
    _content, filename, _update = env.loader.get_source(env, tpl)
    module_filename = os.path.join(target, get_module_filename(tpl))
    if not os.path.isfile(module_filename):
      module_filename_pyc = module_filename + "c"
      if not os.path.isfile(module_filename_pyc):
        return True
      else:
        module_filename = module_filename_pyc
    if os.path.getmtime(filename) > os.path.getmtime(module_filename):
      return True
    return False

  return filter_func

def main():

  def logger(msg):
    sys.stderr.write("%s\n" % msg)

  parser, options, args = option_parse()
  if options.debug:
    logging.getLogger().setLevel(logging.DEBUG)
  elif options.verbose:
    logging.getLogger().setLevel(logging.INFO)
  elif options.quit:
    logging.getLogger().setLevel(logging.CRITICAL)
    logger = None
  logging.debug("parse_options: options %s" % options)
  logging.debug("parse_options: args %s" % args)
  for i in args:
    if not os.path.exists(i):
      logging.warning("No such directory: '%s'" % i)
      sys.exit(1)
  if options.modulename:
    basedir = re.compile(options.base)
    results = list()
    for i in args:
      results.append(os.path.join(options.base, get_module_filename(basedir.sub("", i).lstrip("/"), py_compile=options.pyc)))
    print(" ".join(results))
    sys.exit(0)
  if len(args) != 1:
    parser.print_help()
    sys.exit(1)
  logging.info("Compiling bundled templates...")
  arg = args[0]
  env = jinja2.Environment(loader=jinja2.FileSystemLoader([os.path.dirname(arg)]))
  if os.path.isdir(arg):
    if options.extensions is not None:
      extensions = options.extensions.split(",")
    else:
      extensions = None
    filter_func = make_filter_func(arg, env, extensions, options.all_files)
    target = arg
    logging.info("Now compiling templates in %s." % arg)
  else:
    basename = os.path.basename(arg)
    filter_func = lambda x: x == basename
    target = os.path.dirname(arg)
    logging.info("Now compiling a template: %s." % arg)
  env.compile_templates(target, extensions=None,
                        filter_func=filter_func, zip=None, log_function=logger,
                        ignore_errors=False, py_compile=options.pyc)
  logging.info("Finished compiling bundled templates...")

if __name__== "__main__":
  logging.getLogger().setLevel(logging.WARNING)
  main()
