FROM python:3.5.1-alpine

MAINTAINER Miguel Ángel Durán <hi@mangel.me>

ENV APP_HOME /opt/app/

WORKDIR $APP_HOME

RUN apk --update add postgresql-client

RUN apk --update add --virtual build-dependencies \
    build-base \
    python3-dev \
    postgresql-dev && \
    apk del build-dependencies && \
    rm -f /var/cache/apk/*
    
COPY ./requirements.txt $APP_HOME

RUN pip3 install -r requirements.txt

COPY . $APP_HOME

ENTRYPOINT ["python", "manage.py"]