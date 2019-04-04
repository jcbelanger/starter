"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY'] #avoid using getenv to fail loudly


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', default='0') == '1'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sites',
	'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'app.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        #'APP_DIRS': True,
        'OPTIONS': {
			'loaders': [
				('django.template.loaders.cached.Loader', [
					'django.template.loaders.filesystem.Loader',
					'django.template.loaders.app_directories.Loader',
				]),
			],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', default='postgres'),
        'USER': os.getenv('POSTGRES_USER', default='postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgres'),
        'HOST': os.getenv('POSTGRES_HOST', default=os.getenv('POSTGRES_USER', default='postgres')),
        'PORT': os.getenv('POSTGRES_PORT', default=5432),
		'CONN_MAX_AGE': None,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

MIGRATION_MODULES = {
    'sites': 'app.fixtures.sites_migrations',
}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', default='en-us')

TIME_ZONE = os.getenv('TIME_ZONE', default='US/Eastern')

USE_I18N = False

USE_L10N = False

USE_TZ = True

SITE_ID = 1

DOMAIN = os.getenv('DOMAIN')

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'django']
if DOMAIN is not None:
    ALLOWED_HOSTS.append(DOMAIN)
    ALLOWED_HOSTS.append(f'www.{DOMAIN}')

CSRF_TRUSTED_ORIGINS = ['.localhost', '.127.0.0.1', '.[::1]']
if DOMAIN is not None:
    CSRF_TRUSTED_ORIGINS.append(f'.{DOMAIN}')

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CONN_MAX_AGE = None
USE_ETAGS = True

USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = '/static'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"
    }
}


REDIS_HOST = os.getenv('REDIS_HOST', default='redis')
REDIS_PORT = os.getenv('REDIS_PORT', default='6379')
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': f'{REDIS_HOST}:{REDIS_PORT}',
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
if ADMIN_EMAIL is not None:
	ADMINS = [('Admin', ADMIN_EMAIL)]


if DEBUG:
	INSTALLED_APPS += (
		'debug_toolbar',
		'mail_panel',
		'template_profiler_panel',
	)
	MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

	DEBUG_TOOLBAR_PANELS = [
		'debug_toolbar.panels.versions.VersionsPanel',
		'debug_toolbar.panels.timer.TimerPanel',
		'debug_toolbar.panels.settings.SettingsPanel',
		'debug_toolbar.panels.headers.HeadersPanel',
		'debug_toolbar.panels.request.RequestPanel',
		'debug_toolbar.panels.sql.SQLPanel',
		'debug_toolbar.panels.staticfiles.StaticFilesPanel',
		'debug_toolbar.panels.templates.TemplatesPanel',
		'debug_toolbar.panels.cache.CachePanel',
		'debug_toolbar.panels.signals.SignalsPanel',
		'debug_toolbar.panels.logging.LoggingPanel',
		'debug_toolbar.panels.redirects.RedirectsPanel',
		'mail_panel.panels.MailToolbarPanel',
		'template_profiler_panel.panels.template.TemplateProfilerPanel',
	]
	DEBUG_TOOLBAR_CONFIG = {
		'SHOW_TOOLBAR_CALLBACK' : lambda request: DEBUG,
	}


	EMAIL_BACKEND = 'mail_panel.backend.MailToolbarBackend'