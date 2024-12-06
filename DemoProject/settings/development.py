import os
import dj_database_url
from .base import *
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

MIDDLEWARE += [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',
   ]

DATABASES = {
       'default': dj_database_url.parse(os.getenv('DATABASE_URL', ''))
   }