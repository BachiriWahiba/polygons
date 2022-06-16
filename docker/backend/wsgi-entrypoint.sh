#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

until python manage.py makemigrations 
do
    echo "Waiting for db to be ready..."
    sleep 2
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

until python manage.py test
do
    echo "Waiting for db test to be ready..."
    sleep 2
done


# Dumpdata
# python manage.py loaddata dumpdata/serviceArea.json
# python manage.py loaddata dumpdata/provider.json
python manage.py collectstatic --noinput

gunicorn polygons.wsgi --bind 0.0.0.0:8004 --workers 1 --threads 1


