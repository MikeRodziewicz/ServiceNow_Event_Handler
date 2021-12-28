FROM python:3.8-alpine
RUN mkdir /code
WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY ./ .
COPY ./.env .env
CMD ["python3", "main.py"]
