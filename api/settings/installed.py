# Application definition
# Environment specific overrides are to be placed in respective environment .py files.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "graphene_django",
    "graphql_jwt.refresh_token.apps.RefreshTokenConfig",
    "graphql_auth",
    "django_filters",
    "corsheaders",
    "profiles",
]