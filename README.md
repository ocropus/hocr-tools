# hocr-tools

## About

hOCR is a format for representing OCR output, including layout information, character confidences, bounding boxes, and style information.  It embeds this information invisibly in standard HTML.  By building on standard HTML, it automatically inherits well-defined support for most scripts, languages, and common layout options.  Furthermore, unlike previous OCR formats, the recognized text and OCR-related information co-exist in the same file and survives editing and manipulation.  hOCR markup is independent of the presentation.

There is a [Public Specification](http://docs.google.com/View?docid=dfxcv4vc_67g844kf) for the hOCR Format.

## about the code

Each command line program is self contained; if you have the right
Python packages installed, it should just work.  (Unfortunately, that
means some code duplication; we may revisit this issue in later
revisions.)

## pointers

The format itself is defined here:

    http://docs.google.com/View?docID=dfxcv4vc_67g844kf&revision=_latest


## Available Programs

Included command line programs:

  * [hocr-check -- check the hOCR file for errors](#hocr-check)
  * [hocr-combine -- combine pages in multiple hOCR files into a single document](#hocr-combine)
  * [hocr-eval -- compute number of segmentation and OCR errors](#hocr-eval)
  * [hocr-eval-geom -- compute over, under, and mis-segmentations](#hocr-eval-geom)
  * [hocr-eval-lines -- compute OCR errors of hOCR output relative to text ground truth](#hocr-eval-lines)
  * [hocr-extract-images -- extract the images and texts within all the ocr_line elements](#hocr-extract-images)
  * [hocr-lines -- extract the text within all the ocr_line elements](#hocr-lines)
  * [hocr-pdf -- create a searchable PDF from a pile of hOCR and JPEG](#hocr-pdf)
  * [hocr-split -- split an hOCR file into individual pages](#hocr-split)
  * [hocr-merge-dc -- merge Dublin Core meta data into the hOCR HTML header](#hocr-merge-dc)

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

### hocr-split

```
hocr-split file.html pattern
```

Split a multipage hOCR file into hOCR files containing one page each.
The pattern should something like "base-%03d.html"

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

### hocr-extract-images

TODO

### hocr-lines

TODO

### hocr-pdf

TODO

### hocr-merge-dc

```
### hocr-merge-dc dc.xml hocr.html > hocr-new.html
```

Merges the Dublin Core metadata into the hOCR file by encoding the data in its header.


