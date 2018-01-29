"""
Django settings for CRT project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y(v_sm_&2&f68svwg$3r=tm3u5mbqoyxkcuw!ik2@cxjak!*#%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

"""
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'brayantabares10a2014@gmail.com'
EMAIL_HOST_PASSWORD = ''
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_PORT= '25'
#EMAIL_HOST = "localhost"
#EMAIL_PORT = "1025"
EMAIL_USE_TLS = True
"""


ADMINS = (
    ('Brayan', 'brayantabares10a2014@gmail.com'),
)

MANAGERS = ADMINS

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
TEST_EMAIL_BACKEND_RECIPIENTS = ADMINS

FROM_EMAIL = ADMINS[0][1]
EMAIL_SUBJECT_PREFIX = '[main]'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = FROM_EMAIL

# Enter your gmail PW from the ADMINS email entered above.
EMAIL_HOST_PASSWORD = 'Diosesamor123'
EMAIL_PORT = 587

EMAIL_USE_TLS = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'permiso_ausentismo',
    #'main.apps.MainConfig',
    'crispy_forms',
    'datetimewidget',
    'main',
    'registration',
    'jquery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CRT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CRT.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'" , #Opcion requerida para evitar la perdida de datos.
        },
        'NAME': 'crt_db',
        'USER': 'root',
        #'PASSWORD': '1234',
        #'HOST': '192.168.1.32',
        #'HOST': '192.168.0.22',
        'HOST': 'localhost',
        'PASSWORD': 'BTabares99',
        #'HOST': '192.168.0.22',
        #'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Bogota'


USE_I18N = True

USE_L10N = True

USE_TZ = True


ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
#LOGIN_REDIRECT_URL = '/'
#CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static_pro','static'),


TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_env","static_root")
CRISPY_TEMPLATE_PACK = 'bootstrap4'
