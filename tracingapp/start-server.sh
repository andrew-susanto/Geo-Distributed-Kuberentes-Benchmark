#!/bin/sh
# bash script as start point of docker app
(python manage.py collectstatic) & (python manage.py seeddb) & (gunicorn tracing.wsgi:application --bind 0.0.0.0:12111 --workers 3) & nginx -g "daemon off;"