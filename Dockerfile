FROM python:3.8-alpine
RUN mkdir /snow_extrator
WORKDIR /snow_extrator

COPY requirements.txt requirements.txt

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN pip install -r requirements.txt
COPY ./ .
COPY ./.env .env

ENV PYTHONPATH "${PYTHONPATH}:/usr/src"

CMD ["python3", "src/main.py"]
