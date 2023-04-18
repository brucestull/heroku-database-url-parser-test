import os

from config.settings.common import *
from utils import get_database_config_variables


DEBUG = False


ALLOWED_HOSTS = ['flynnt-knapp-parser-test.herokuapp.com']


MIDDLEWARE = MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware']


STATIC_ROOT = BASE_DIR / 'staticfiles'


database_config_variables = get_database_config_variables(
    os.environ.get('DATABASE_URL')
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': database_config_variables['DATABASE_NAME'],
        'HOST': database_config_variables['DATABASE_HOST'],
        'PORT': database_config_variables['DATABASE_PORT'],
        'USER': database_config_variables['DATABASE_USER'],
        'PASSWORD': database_config_variables['DATABASE_PASSWORD'],
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Create a specific `SECRET_KEY` for production and use it in production only.
SECRET_KEY = os.environ.get('SECRET_KEY')

# To create a new `SECRET_KEY`:
"""
    python manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""