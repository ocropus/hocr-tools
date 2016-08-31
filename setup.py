#!/usr/bin/env python

import glob
from setuptools import setup
setup(
    name = "hocr_tools",
    version = "1.2.2",
    description = 'Advanced tools for hOCR integration',
    author = 'Thomas Breuel',
    author_email = 'tmbdev@gmail.com',
    url = 'https://github.com/tmbdev/hocr-tools',
    download_url = 'https://github.com/tmbdev/hocr-tools/tarball/1.2.2',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Utilities',
    ],
    scripts = [c for c in glob.glob("hocr-*")]
)
