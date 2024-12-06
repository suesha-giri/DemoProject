from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

ENVIRONMENT = os.getenv('DJANGO_ENV', 'local')

if ENVIRONMENT == 'development':
    from .development import *
else:
    from .local import *
