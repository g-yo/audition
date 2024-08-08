import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--l0(22d173e_70j#gkcv0r81w)f%u48)**byamgu464o0_lmub'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auditions',
    'django.contrib.sites',
    'storages',
]

AWS_ACCESS_KEY_ID = 'AKIAU6GDYCKFR7MLHJ5N'
AWS_SECRET_ACCESS_KEY = 'FxQEAskbXHcOH8YY6CvnEhQBAhIlNa26QBxqVRZ6'
AWS_STORAGE_BUCKET_NAME = 'movieaudtion'
AWS_S3_REGION_NAME = 'us-east-1'  # e.g., 'us-east-1'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_CUSTOM_DOMAIN = 'movieaudtion.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # This can be removed if you're using S3 for media

AUTH_USER_MODEL = 'auditions.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movieaudition.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'movieaudition.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movieaudtions',
        'USER': 'postgres',
        'PASSWORD': 'eZiO8301',
        'HOST': 'movieaudtions.chkka4ea4ew0.us-east-1.rds.amazonaws.com',  # e.g., 'your-db-instance.123456789012.us-east-1.rds.amazonaws.com'
        'PORT': '5432',  # PostgreSQL default port
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Optional: If you have static files locally
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
