# Use an official Python runtime as a parent image
FROM python:2.7-slim

RUN mkdir -p /usr/src/app 
WORKDIR /usr/src/app 
COPY requirements.txt /usr/src/app/ 
RUN pip install --no-cache-dir -r requirements.txt
COPY aldryn_newsblog /Library/Python/2.7/site-packages/
COPY . /usr/src/app