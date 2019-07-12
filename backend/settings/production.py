# -*- coding: utf-8 -*-
"""
    Настройки для боевого сервера
"""
from . import *  # NOQA
import raven  # NOQA

DEBUG = False

COMPRESS_ENABLED = not DEBUG
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),  # NOQA
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),  # NOQA
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),  # NOQA
        'HOST': os.environ.get('BACKEND_CONTAINER_NAME', 'db_backend'),  # NOQA
        'PORT': os.environ.get('POSTGRES_PORT', 5432)
    },
}


REDIS_LOCATION = 'redis://redis.hamster:6379/%s'

ALLOWED_HOSTS = ['*']

# ==============================================================================
# ssl
# ==============================================================================

SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

CSRF_COOKIE_SECURE = True

# ==============================================================================
# Celery
# ==============================================================================

BROKER_URL = REDIS_LOCATION % 1

CELERY_RESULT_BACKEND = REDIS_LOCATION % 1


# ==============================================================================
# django-redis
# ==============================================================================

# CACHES['default']['LOCATION'] = REDIS_LOCATION % 2  # NOQA


# ==============================================================================
# Sentry
# ==============================================================================

INSTALLED_APPS += ('raven.contrib.django.raven_compat',)  # NOQA

# SENTRY_CELERY_LOGLEVEL = logging.INFO

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
