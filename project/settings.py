from pathlib import Path
import os
import cloudinary_storage

BASE_DIR = Path(__file__).resolve().parent.parent
WSGI_APPLICATION = 'project.wsgi.application'


SECRET_KEY = 'django-insecure-30k0(2-nq(*ip0woww(m+1ll%_m@6-#-#w!xhm#g@-!vllz4)3'


ROOT_URLCONF = 'project.urls'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# django-allauth setup
LOGIN_REDIRECT_URL = 'mass_mail:mail_handler'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION= True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL= 'mass_mail:mail_handler'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True


# Gmail setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'   
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mohammadfayaj36@gmail.com'
EMAIL_HOST_PASSWORD = 'sonofgun362536329252'


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# media settings
MEDIA_URL = os.path.join(BASE_DIR, '/media/')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
SITE_ID = 1


CLOUDINARY_STORAGE = {

    'CLOUD_NAME': 'dc1nfucu5',
    'API_KEY': '815863632269532',
    'API_SECRET': 'e3UR7bsNBL2MXodN9FpYXA19m_s'
}

# CLOUDINARY_URL=cloudinary://your_api_key:your_api_secret@your_cloud_name

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third party app
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'cloudinary_storage',
    # 'cloudinary',



    'mass_mail.apps.MassMailConfig',
]

AUTHENTICATION_BACKENDS = [
    # `allauth` specific authentication methods, such as login by e-mail
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

]


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


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



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


