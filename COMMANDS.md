# Project Reference Commands
These are some of the commands that will be used for managing the django api.

## Django Settings


### Standard Migration

`python manage.py migrate`

### Using Different Settings via Module

Migrate:
`python manage.py migrate --settings api.settings.production`

Run Server:
`python manage.py runserver --settings api.settings.production`

### Using Environment Variables
`DJANGO_SETTINGS_MODULE=api.settings.production python manage.py migrate`


## WSGI Server
### Gunicorn (perferred)

`gunicorn api.wsgi:application`

Production:
`gunicorn api.wsgi:application --env DJANGO_SETTINGS_MODULE=api.settings.production`