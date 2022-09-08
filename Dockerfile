FROM python:3-alpine

# install psycopg2 dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . .

CMD ["python3", "./main.py"]
