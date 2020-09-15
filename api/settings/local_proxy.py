import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'settings', '.proxy.env'))

# all base settings for Django
from .base import *
from .installed import *


DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'tap-dating-production-static-files-storage'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production',
        'USER': 'tap_production', # 'tap-dating-sql'
        'PASSWORD': '', #'qeB92rKeKCgnMbtb',
        'HOST': '127.0.0.1',
        'PORT': 6434
    }
}
