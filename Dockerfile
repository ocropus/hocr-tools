#
# Build: docker build -t hocr-tools-app .
# Start: docker run -it --rm -v ${PWD}:/usr/src/app hocr-tools-app bash
# Test: ./test/tsht
#

FROM python:3
ENV PYTHONIOENCODING utf8

RUN apt-get update && apt-get install -y --no-install-recommends pdfgrep \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN python setup.py install

CMD ./test/tsht
