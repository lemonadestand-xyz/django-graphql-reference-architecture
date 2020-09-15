import os

# all base settings for Django
from .base import *
# Load installed apps
from .installed import *

# Required for GraphiQL
#
# The below should never be implemented in `production.py`
if DEBUG:
    INSTALLED_APPS.append('django.contrib.staticfiles')
    INSTALLED_APPS.append('django_extensions')


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tap_db',
        'USER': 'chriscampbell',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}
