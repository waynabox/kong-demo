FROM python:3

WORKDIR /deploy
COPY start.sh /deploy
COPY requirements.txt /deploy
RUN chmod +x /deploy/start.sh

RUN pip install -r /deploy/requirements.txt
RUN pip install requests
RUN pip install pytesseract
RUN pip install git+https://github.com/jflesch/pyocr.git
RUN pip install wand
RUN pip install grequests


ENTRYPOINT /deploy/start.sh
