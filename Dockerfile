FROM python:3-alpine

WORKDIR /usr/src/app

RUN apk add postgresql-dev
RUN apk add gcc
RUN apk add musl-dev
RUN apk add g++

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "app/main.py" ]