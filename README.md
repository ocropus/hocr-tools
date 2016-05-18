# hocr-tools

[![Build Status](https://travis-ci.org/tmbdev/hocr-tools.svg?branch=master)](https://travis-ci.org/tmbdev/hocr-tools)


* [About](#about)
  * [About the code](#about-the-code)
  * [Pointers](#pointers)
* [Installation](#installation)
  * [System-wide](#system-wide)
  * [Virtualenv](#virtualenv)
* [Available Programs](#available-programs)
  * [hocr-check](#hocr-check) -- check the hOCR file for errors
  * [hocr-combine](#hocr-combine) -- combine pages in multiple hOCR files into a single document
  * [hocr-eval](#hocr-eval) -- compute number of segmentation and OCR errors
  * [hocr-eval-geom](#hocr-eval-geom) -- compute over, under, and mis-segmentations
  * [hocr-eval-lines](#hocr-eval-lines) -- compute OCR errors of hOCR output relative to text ground truth
  * [hocr-extract-g1000](#hocr-extract-g1000) -- extract lines from Google 1000 book sample
  * [hocr-extract-images](#hocr-extract-images) -- extract the images and texts within all the ocr_line elements
  * [hocr-lines](#hocr-lines) -- extract the text within all the ocr_line elements
  * [hocr-merge-dc](#hocr-merge-dc) -- merge Dublin Core meta data into the hOCR HTML header
  * [hocr-pdf](#hocr-pdf) -- create a searchable PDF from a pile of hOCR and JPEG
  * [hocr-split](#hocr-split) -- split an hOCR file into individual pages
* [Unit tests](#unit-tests)
  * [Running the full test suite:](#running-the-full-test-suite)
  * [Running a single test](#running-a-single-test)
  * [Writing a test](#writing-a-test)

## About

hOCR is a format for representing OCR output, including layout information,
character confidences, bounding boxes, and style information.
It embeds this information invisibly in standard HTML.
By building on standard HTML, it automatically inherits well-defined support
for most scripts, languages, and common layout options.
Furthermore, unlike previous OCR formats, the recognized text and OCR-related
information co-exist in the same file and survives editing and manipulation.
hOCR markup is independent of the presentation.

There is a [Public Specification](http://docs.google.com/View?docid=dfxcv4vc_67g844kf) for the hOCR Format.

### About the code

Each command line program is self contained; if you have the right
Python packages installed, it should just work.  (Unfortunately, that
means some code duplication; we may revisit this issue in later
revisions.)

### Pointers

The format itself is defined here:

http://docs.google.com/View?docID=dfxcv4vc_67g844kf&revision=_latest

## Installation

### System-wide

On a Debian/Ubuntu system, install the dependencies from packages:

```
sudo apt-get install python-lxml python-reportlab python-pil \
  python-beautifulsoup python-numpy python-scipy python-matplotlib
```

Or, to fetch dependencies from the [cheese shop](https://pypi.python.org/pypi):

```
sudo pip install -r requirements.txt  # basic
```

Then install the dist:

```
sudo python setup.py install
```

### Virtualenv

Once

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Subsequently

```
source venv/bin/activate
./hocr-...
```

## Available Programs

Included command line programs:

### hocr-check

```
hocr-check file.html
```

Perform consistency checks on the hOCR file.

### hocr-combine

```
hocr-combine file1.html file2.html...
```

Combine the OCR pages contained in each HTML file into a single document.
The document metadata is taken from the first file.

### hocr-eval-lines

```
hocr-eval-lines [-v] true-lines.txt hocr-actual.html
```

Evaluate hOCR output against ASCII ground truth.  This evaluation method
requires that the line breaks in true-lines.txt and the ocr_line elements
in hocr-actual.html agree (most ASCII output from OCR systems satisfies this
requirement).

### hocr-eval-geom

```
hocr-eval-geom [-e element-name] [-o overlap-threshold] hocr-truth hocr-actual
```

Compare the segmentations at the level of the element name (default: ocr_line).
Computes undersegmentation, oversegmentation, and missegmentation.

### hocr-eval

```
hocr-eval hocr-true.html hocr-actual.html
```

Evaluate the actual OCR with respect to the ground truth.  This outputs
the number of OCR errors due to incorrect segmentation and the number
of OCR errors due to character recognition errors.

It works by aligning segmentation components geometrically, and for each
segmentation component that can be aligned, computing the string edit distance
of the text the segmentation component contains.

### hocr-extract-g1000

Extract lines from [Google 1000 book sample](http://commondatastorage.googleapis.com/books/icdar2007/README.txt)

### hocr-extract-images

TODO

### hocr-lines

TODO

### hocr-merge-dc

```
hocr-merge-dc dc.xml hocr.html > hocr-new.html
```

Merges the Dublin Core metadata into the hOCR file by encoding the data in its header.

### hocr-pdf

```
Usage: hocr-pdf <imgdir>
```

Create a searchable PDF from a pile of hOCR and JPEG

### hocr-split

```
hocr-split file.html pattern
```

Split a multipage hOCR file into hOCR files containing one page each.
The pattern should something like "base-%03d.html"

## Unit tests

The unit tests are written using the [tsht](https://github.com/kba/tsht) framework.

### Running the full test suite:

```sh
./test/tsht
```

### Running a single test

```sh
./test/tsht <path-to/unit-test.tsht>
```

e.g.

```sh
./test/tsht hocr-pdf/test-hocr-pdf.tsht
```

### Writing a test

Please see the documentation in the [tsht](https://github.com/kba/tsht) repository and
take a look at the existing [unit tests](./test/).

1) Create a new directory under `./test`
2) Copy any test assets (images, hocr files...) to this directory
3) Create a file `<name-of-your-test>.tsht` starting from this template:

```sh
#!/usr/bin/env tsht

# adjust to the number of your tests
plan 1

# write your tests here
exec_ok "hocr-foo" "-x" "foo" 

# remove any temporary files
# rm some-generated-file
```
