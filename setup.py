#!/usr/bin/env python

__version__ = '1.3.0'

import glob
from setuptools import setup

setup(
    name="hocr-tools",
    version=__version__,
    description='Advanced tools for hOCR integration',
    author='Thomas Breuel',
    maintainer='Konstantin Baierer',
    maintainer_email='konstantin.baierer@gmail.com',
    url='https://github.com/tmbdev/hocr-tools',
    download_url='https://github.com/tmbdev/hocr-tools/tarball/v'
                 + __version__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Utilities',
    ],
    install_requires=[
        'Pillow',
        'lxml',
        'python-bidi',
        'reportlab',
    ],
    scripts=[c for c in glob.glob("hocr-*")]
)
