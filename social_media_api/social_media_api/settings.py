"""
Django settings for social_media_api project.

Generated by 'django-admin startproject' using Django 5.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qw%==2pzfaq5p%%@99o#188fgu#m+1_zo69k!8k@3^o)8fe@c)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'posts',
    'accounts',
    'notifications',
]
AUTH_USER_MODEL = 'accounts.Customuser'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_media_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'social_media_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        #'PORT': config('DB_PORT', default='5432')
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py

# Enable browser's XSS filtering and prevent rendering pages if XSS is detected.
SECURE_BROWSER_XSS_FILTER = True

# Prevent the site from being loaded in an iframe, protecting against clickjacking attacks.
X_FRAME_OPTIONS = 'DENY'  # Options: 'DENY', 'SAMEORIGIN', 'ALLOW-FROM'

# Prevent the browser from interpreting files as something else than declared by the content type.
SECURE_CONTENT_TYPE_NOSNIFF = True

# Redirect all HTTP traffic to HTTPS to ensure secure communication.
SECURE_SSL_REDIRECT = True

# Enforce HTTPS for cookies.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS settings (HTTP Strict Transport Security)
# Instructs the browser to only communicate with your site over HTTPS.
SECURE_HSTS_SECONDS = 31536000  # 1 year; adjust the time as necessary
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Applies HSTS policy to all subdomains.
SECURE_HSTS_PRELOAD = True  # Enables the preload flag for HSTS

# Secure cookie settings
CSRF_COOKIE_HTTPONLY = True  # Prevents JavaScript from accessing CSRF cookie
SESSION_COOKIE_HTTPONLY = True  # Prevents JavaScript from accessing the session cookie

# Content Security Policy (CSP) settings - Optional but recommended
# Example header value: adjust as needed based on your app's resources
CSP_DEFAULT_SRC = ("'self'",)  # Only allow content from the site's own origin

# Other security-related settings (optional)
SECURE_REFERRER_POLICY = 'no-referrer-when-downgrade'  # Controls the referrer information sent with requests.
