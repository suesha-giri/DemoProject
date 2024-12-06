import os
from .base import *
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL backend
#         'USERNAME': 'demodb_xqww_user',  # Replace with your database name
#         'DATABASE': 'demodb_xqww',  # Replace with your PostgreSQL username
#         'PASSWORD': 'B3RQK4wkCzs2sV0ND2J6wz7QU3xEgRX4',  # Replace with your PostgreSQL password
#         'EXTERNAL URL': 'postgresql://demodb_xqww_user:B3RQK4wkCzs2sV0ND2J6wz7QU3xEgRX4@dpg-ct8v39aj1k6c73bspuc0-a.oregon-postgres.render.com/demodb_xqww'
#     }
# }