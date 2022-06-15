# docker/backend/Dockerfile

FROM python:3.9.7-alpine

WORKDIR /app
ADD ./polygons/requirements.txt /app/backend/


RUN pip install --upgrade pip
RUN pip install gunicorn
RUN apk add musl-dev mariadb-dev gcc zlib-dev jpeg-dev alpine-sdk python3-dev libffi-dev openssl-dev cargo jpeg-dev zlib-dev ffmpeg
# RUN pip install -r backend/requirements.txt
RUN pip install django djangorestframework django-rest-swagger psycopg2-binary 
RUN pip install drf-yasg 
ADD ./docker /app/docker
ADD ./polygons /app/backend
RUN ["chmod", "+x", "/app/docker/wsgi-entrypoint.sh"]
