#!/usr/bin/env python

VERSION = '1.1.1'

import glob
from setuptools import setup

setup(
    name = "hocr-tools",
    version = VERSION,
    description = 'Advanced tools for hOCR integration',
    author = 'Thomas Breuel',
    maintainer = 'Konstantin Baierer',
    maintainer_email = 'konstantin.baierer@gmail.com',
    url = 'https://github.com/tmbdev/hocr-tools',
    download_url = 'https://github.com/tmbdev/hocr-tools/tarball/v' + VERSION,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Utilities',
    ],
    install_requires = [
        'Pillow',
        'lxml',
        'reportlab',
    ],
    scripts = [c for c in glob.glob("hocr-*")]
)
