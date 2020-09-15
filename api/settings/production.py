import os

# all base settings for Django
from .base import *

from .installed import *

ALLOWED_HOSTS = [ # TODO: will need to replace with specific domains and with Google Run id!!!
    'tap-dating-uc.a.run.app',
    'tapdatinginc.com'
]

# We're in production so turn off debugging
DEBUG = os.environ.get('DEBUG', False)

# Add transactional email abilities.
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_PROJECT_ID = 'tap-dating-app'
GS_BUCKET_NAME = 'tap-dating-static-files-storage'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
INSTANCE_CONNECTION_NAME = os.environ.get("INSTANCE_CONNECTION_NAME")
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production',
        # keeping this hardcoded so that someone doesn't change eviron value and think things will work.
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': f'/cloudsql/{INSTANCE_CONNECTION_NAME}',
    }
}
