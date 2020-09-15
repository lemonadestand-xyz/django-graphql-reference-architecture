#!/bin/bash
/usr/local/bin/gunicorn api.wsgi:application --bind "0.0.0.0:$PORT" --env DJANGO_SETTINGS_MODULE=api.settings.production
