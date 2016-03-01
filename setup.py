#!/usr/bin/env python

import glob
from setuptools import setup
setup(
    name = "hocr_tools",
    version = "0.1",
    author = 'Thomas Breuel',
    description = 'Advanced tools for hOCR integration',
    scripts = [c for c in glob.glob("hocr-*")]
)
