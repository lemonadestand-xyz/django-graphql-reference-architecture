"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from .settings import *

urlpatterns = [
    path('admin/', admin.site.urls),
]

## Development only URLs to add
# again this needs to be off in Production
##
if DEBUG:
    urlpatterns.append(path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))))
    urlpatterns += staticfiles_urlpatterns() # used if running `gunicorn` in development, but why?! ;)
else:
    urlpatterns.append(path('graphql/', jwt_cookie(GraphQLView.as_view(graphiql=False))))