#!/bin/sh

../hocr-check sample.html
../hocr-extract-images -p "test-%02d.png" sample.html
#../hocr-extract-images -e "ocrx_word" tess.htm
