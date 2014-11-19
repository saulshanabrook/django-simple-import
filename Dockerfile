FROM python:2


COPY . /usr/src/app/
WORKDIR /usr/src/app

RUN pip install -e . -r test/requirements.txt
