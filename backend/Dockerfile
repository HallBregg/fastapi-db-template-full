FROM python:3.8
RUN apt-get update && apt-get -y upgrade

WORKDIR /tmp
COPY ./linkorage/app/requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /linkorage
COPY ./linkorage /linkorage
ENV PYTHONPATH=/

EXPOSE 5000
