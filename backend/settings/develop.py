"""
    Настройки среды для разработки
"""
from . import *  # NOQA

import os

ALLOWED_HOSTS = ['*']

SITE_ID = 1

DEBUG = True

COMPRESS_ENABLED = not DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),  # NOQA
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),  # NOQA
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),  # NOQA
        'HOST': os.environ.get('BACKEND_CONTAINER_NAME', 'db_backend'),  # NOQA
        'PORT': os.environ.get('POSTGRES_PORT', 5432)
    },
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ('rest_framework.renderers.BrowsableAPIRenderer', )

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
