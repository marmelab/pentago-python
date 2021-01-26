FROM python:3

WORKDIR /usr/pentago

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
