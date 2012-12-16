# -*- coding: utf-8 -*-

import jinja2
import pytest

import jinja2precompiler

def test_IndexError():
  env = jinja2.Environment(loader=jinja2.FileSystemLoader(["."]))
  filter_func = jinja2precompiler.make_filter_func("", env, extensions=["html"], all_files=True)
  assert filter_func("test.html") == True
  assert filter_func("test.xml") == False
  assert filter_func("html") == False
