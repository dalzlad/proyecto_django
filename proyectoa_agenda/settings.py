#https://www.youtube.com/watch?v=bE8UllxfFC8
#pip freeze > requirements.txt
from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tk%c(=%d)ygd25@%11tj_2ujw+7ry!(t$=jae97v6jht%e9@-f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['proyectoa-agenda.onrender.com']

# Application definition
INSTALLED_APPS = [
    #'django_bootstrap5',
    #'widget_tweaks',    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

	'app_contactos',
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

ROOT_URLCONF = 'proyectoa_agenda.urls'

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

WSGI_APPLICATION = 'proyectoa_agenda.wsgi.application'
#postgres://root:Bc774Rr9KIhz4dhmk5dP5z8oDVnz7cDD@dpg-cjrbq2ojbais738hsvug-a/testsena
# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'blog',
#         'USER': 'root',
#         'PASSWORD': 'Bc774Rr9KIhz4dhmk5dP5z8oDVnz7cDD',
#         'HOST': 'dpg-cjrbq2ojbais738hsvug-a',
#         'PORT': '5432'#,
#         #'OPTIONS': {
#          #   'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         # }   
#     }
# }	

# DATABASES = {
#     "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
# }


DATABASES = {
    'default': dj_database_url.parse(
        'postgres://sena_user:sQsCbmMBGt9a2jzv0buS78t4nJXxOpV8@dpg-cjsf2o63m8ac73cid8g0-a.oregon-postgres.render.com/sena',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Ruta para las imágenes de cada registro
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'app_contactos/static/fotos')
 
# Activar 'CookieStorage' para enviar los mensajes de respuesta al Crear, Eliminar y Actualizar un registro
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
