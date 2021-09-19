FROM python:3.9.6-alpine

WORKDIR /usr/src/aminoreader_project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install -r requirements.txt
RUN pip install djangorestframework
RUN pip install requests

COPY . .
