FROM python:3.8

WORKDIR /app

COPY Parte2.py /app
COPY RequisicaoRobo_pb2.py /app
COPY requirements.txt /app

RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade protobuf
