import os
import dj_database_url
from .base import *
from dotenv import load_dotenv

load_dotenv()

MIDDLEWARE += [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',
   ]

DATABASES = {
       'default': dj_database_url.parse(os.getenv('DATABASE_URL', ''))
   }