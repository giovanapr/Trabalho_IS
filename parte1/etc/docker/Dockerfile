FROM python:3.7-alpine

WORKDIR /app
COPY Parte1.py /app
COPY RequisicaoRobo_pb2.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt
RUN pip install --upgrade protobuf

