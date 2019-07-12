FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV LANG ru_RU.UTF-8

ARG ENV

RUN apt-get update --fix-missing


RUN yes | apt-get install binutils libproj-dev gdal-bin

RUN yes | apt-get install locales \
    && echo "ru_RU.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

RUN mkdir -p /webapp

ADD ./requirements /webapp/requirements

WORKDIR /webapp

RUN pip install --upgrade pip \
    && pip install -r requirements/$ENV.txt
