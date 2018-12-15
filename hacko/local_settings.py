import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'onlineportal',
        'USER': 'guest',
        'PASSWORD': 'guest',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# BROKER_URL = 'amqp://hello:guest@localhost/myvhost'
DEBUG = True