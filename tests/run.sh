#!/bin/sh

../hocr-check sample.html
../hocr-extract-images -p "words-from-test-%03d.png" -e "ocrx_word" tess.hocr
rm words-from-test*
