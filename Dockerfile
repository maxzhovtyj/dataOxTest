FROM python:3.8-slim-buster

WORKDIR /dataOxTest

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./app ./app

CMD ["python3", "./app/main.py"]
