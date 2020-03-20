"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
from dotenv import load_dotenv
load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'u2(#5td1-%7lkzsflw54n1he&4p+*+--2u=)*=z2mw^^n9tg%y'
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['jupiterchildart.herokuapp.com']


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'tinymce',
	'mce_filebrowser',
	'crispy_forms',
	'ckeditor',
	'ckeditor_uploader',

	'posts',
	'marketing',
	'storages',

	
	'django.contrib.sites',

	'allauth',
	'allauth.account',
	'allauth.socialaccount',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CKEDITOR_UPLOAD_PATH = "uploads/"

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.join(VENV_PATH, 'staticfiles') 
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
		os.path.join(BASE_DIR, 'static_in_env'),
]

VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

MEDIA_ROOT = os.path.join(VENV_PATH, 'media_root')   


STATIC_ROOT = os.path.join(VENV_PATH, 'staticfiles')  
# Tinymce



TINYMCE_DEFAULT_CONFIG = {
    'file_picker_callback': 'file image media',
	'cleanup_on_startup': True,
	'custom_undo_redo_levels': 20,
	'selector': 'textarea',
	'theme': 'modern',
	'plugins': '''
			textcolor save link image media preview codesample contextmenu
			table code lists fullscreen  insertdatetime  nonbreaking
			contextmenu directionality searchreplace wordcount visualblocks
			visualchars code fullscreen autolink lists  charmap print  hr
			anchor pagebreak
			''',
	'toolbar1': '''
			fullscreen preview bold italic underline | fontselect,
			fontsizeselect  | forecolor backcolor | alignleft alignright |
			aligncenter alignjustify | indent outdent | bullist numlist table |
			| link image media | codesample |
			''',
	'toolbar2': '''
			visualblocks visualchars |
			charmap hr pagebreak nonbreaking anchor |  code |
			''',
	'contextmenu': 'formats | link image',
	'menubar': True,
	'statusbar': True,
}

# django-allauth
LOGIN_REDIRECT_URL = '/blog'  # Or whatever you want to redirect to after email verification
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTHENTICATION_BACKENDS = (
	
	'django.contrib.auth.backends.ModelBackend',

	'allauth.account.auth_backends.AuthenticationBackend',

) 
SITE_ID = 1


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = 'eu-central-1'

AWS_S3_SIGNATURE_VERSION = 's3v4'
# This should already be in your settings.py
django_heroku.settings(locals())


django_heroku.settings(locals())
