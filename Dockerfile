FROM python:3.11.1-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app/cnab_parser

COPY . /app/cnab_parser/

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations