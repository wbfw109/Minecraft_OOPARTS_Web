"""
Django settings for Minecraft_OOPARTS_Web project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7d7c5fdd-42cd-4ac8-86cc-fb1ed034280a'

# SECURITY WARNING: don't run with debug turned on in production!
# With debug turned off Django won't handle static files for you any more - your production web server (Apache or something) should take care of that.
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'mc.ooparts.xyz']
# nginx : upstream django
# nignx : X-Forwarded-For
# Application definition

INSTALLED_APPS = [
    'app',
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE= [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Minecraft_OOPARTS_Web.urls'

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

WSGI_APPLICATION = 'Minecraft_OOPARTS_Web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))



"""
    # MIDDLEWARE_CLASSES is deprecated
    # deprecated 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

    DEBUG = True
        DEBUG = False 가 되면 접속가능한 호스트를 ALLOWED_HOSTS 에 추가해줘야 한다.
        'localhost', '127.0.0.1' 는 다름!
        - WhiteNoise 환경을 추가해주거나  --insecure 로 실행해야 정적 파일을 제공할 수 있다.
        - 또는 NginX 같은 웹 서버 환경에서 직접 제공받아야 한다.

    ★ 내부 서버 테스트에시는 꼭 True 로 한다.

    Test
        SECURE_SSL_REDIRECT = True 
            - Web 서버 세팅에 사용하고 있기 때문에 Redirection 횟수가 많다고 에러가 난다.
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
"""