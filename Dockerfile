FROM python:latest
MAINTAINER CloudBase

#ENV pythonunbuffered 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install mysqlclient

RUN  mkdir /code
WORKDIR /code
COPY . /code


#RUN adduser -D user
#USER user