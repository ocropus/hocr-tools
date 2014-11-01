# About

hOCR is a format for representing OCR output, including layout information, character confidences, bounding boxes, and style information.  It embeds this information invisibly in standard HTML.  By building on standard HTML, it automatically inherits well-defined support for most scripts, languages, and common layout options.  Furthermore, unlike previous OCR formats, the recognized text and OCR-related information co-exist in the same file and survives editing and manipulation.  hOCR markup is independent of the presentation.

There is a [Public Specification](http://docs.google.com/View?docid=dfxcv4vc_67g844kf) for the hOCR Format.

# Available Programs

Included command line programs:

  * hocr-check -- check the hOCR file for errors
  * hocr-combine -- combine pages in multiple hOCR files into a single document
  * hocr-eval -- compute number of segmentation and OCR errors
  * hocr-eval-geom -- compute over, under, and mis-segmentations
  * hocr-eval-lines -- compute OCR errors of hOCR output relative to text ground truth
  * hocr-split -- split an hOCR file into individual pages
  * hocr-merge-dc -- merge Dublin Core meta data into the hOCR HTML header

