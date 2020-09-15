#!/bin/bash
gunicorn api.wsgi:application --bind "127.0.0.1:8000" --env DJANGO_SETTINGS_MODULE=api.settings.local_proxy
#python manage.py runserver --settings api.settings.local_proxy