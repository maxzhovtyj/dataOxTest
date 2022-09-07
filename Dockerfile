FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install

COPY . .

CMD [ "python3", "./main.py"]