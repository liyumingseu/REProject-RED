"""
Django settings for reporjectred project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&c4ygngb87+1+$g-prip$eff3ulfu&dpz-6tv7sk^(y!mus)62'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users.apps.UsersConfig',
    'apps.personal.apps.PersonalConfig',
    'apps.member.apps.MemberConfig',
    'apps.commodity.apps.CommodityConfig',
    'apps.recommendations.apps.RecommendationsConfig',
    'apps.commendation.apps.CommendationConfig',
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

ROOT_URLCONF = 'reporjectred.urls'

# 使用自定义认证模型设置的内容
AUTH_USER_MODEL = 'users.UserProfile'

AUTHENTICATION_BACKENDS = (
    'users.views.UserBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'reporjectred.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reprojectred',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 媒体文件是由用户上传的文件，路径是变化的
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 登陆url
LOGIN_URL = '/login/'

# URL white list
SAFE_URL = [r'^/$',
            '/login/',
            '/logout',
            '/index/',
            '/media/',
            '/xadmin/',
            ]

# session timeout

SESSION_COOKIE_AGE = 60 * 20
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True

# mail server
# EMAIL_HOST = "mail.sandbox.com"
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "test@sandbox.com"
# EMAIL_HOST_PASSWORD = "1234@abcd.com"
# EMAIL_USE_TLS = True
# EMAIL_FROM = "test@sandbox.com"

# 人脸配置参数
MINSIZE =20  # minimum size of face
THRESHOLD = [0.6, 0.7, 0.7]  # three steps's threshold
FACTOR =0.709  # scale factor
MODELPATH = BASE_DIR + os.sep + 'facenet' + os.sep + '20180402-114759'

MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # 图片最大为16M
MAX_DISTINCT = 1.00 #设置最大的相似距离，1.22是facenet基于lfw计算得到的

APPID = 'wx56291ba66ff53a69'
SECRET = 'f4ecc5552da2ce4241d7fe083da90592'