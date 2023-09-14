"""
Django settings for locallibrary project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-1x$a7@uwz+0#r^vi#&=-ho*db&)^g3%#0h&p*=jlicl8u5y8%2"
# test deploy secret key: ^CdKEcV&~=uN'(Jd9!{~WW49.KiaA&g'N^4oy2o+Jo$c#w}t.<C-_E}
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "^CdKEcV&~=uN'(Jd9!{~WW49.KiaA&g'N^4oy2o+Jo$c#w}t.<C-_E}",
)

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get("DJANGO_DEBUG", "") != False

# Set hosts to allow any app on Railway and the local testing URL
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "catalog.apps.CatalogConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "locallibrary.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "locallibrary.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = "/"

# Add to test email:
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Update database configuration from $DATABASE_URL environment variable (if defined)
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / "staticfiles/"  # . os.path.join(BASE_DIR, 'staticfiles')
# The URL to use when referring to static files (where they will be served from)
STATIC_URL = "static/"


# Static file serving.
# http://whitenoise.evans.io/en/stable/django.html#django-middleware
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# SECURE_HSTS_SECONDS = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_PRELOAD = True

# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
# SECURE_SSL_REDIRECT = False
# SECURE_HSTS_PRELOAD = False
# SECURE_HSTS_SECONDS = False
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False
