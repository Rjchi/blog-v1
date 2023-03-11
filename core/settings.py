"""
configuraciones de mi sitio

"""

from pathlib import Path
import os # os nos permite acceder a los archivos del servidor
import environ # nos permite configurar las variables de ambiente

env = environ.Env() # Con env podremos definir las variables de ambiente
environ.Env.read_env() # Con esto activamos environ para que lea settings

BASE_DIR = Path(__file__).resolve().parent.parent # Esto apunta a la carpeta base del proyecto (blog_personal)


# Con esto protegemos la clave secreta
# pidiendola al archivo .env
SECRET_KEY = os.environ.get('SECRET_KEY')

# Tambien protegemos esta:
DEBUG = os.environ.get('DEBUG')

# Aqui van los dominios tambien protegidos y como es una lista utilizamos env.list
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')


# Estan son las apps de django que bienen preinstaladas con django

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Aqui para mas orden vamos a tener las app de nuestro proyecto

PROJECT_APPS = [
    # Llamamos las apps que tenemos

    'apps.blog',
    'apps.category',
]

# Este va a contener nuestros paquetes de requirements.txt

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader'
]

# Aqui vamos a convinar las tres anteriores en una sola

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# Con esto activamos ckeditor, tambien lo podemos configurar (custom, basic, full etc) ver:
# https://django-ckeditor.readthedocs.io/en/latest/

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'autoParagraph': False,
    },
}

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             ['Bold', 'Italic', 'Underline'],
#             ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
#             ['Link', 'Unlink'],
#             ['RemoveFormat', 'Source']
#         ],
#         'autoParagraph': False,
#     }
# }

CKEDITOR_UPLOAD_PATH = "uploads/" # Esto indica donde queremos subir nuestros archivos

# Los middleware son una pieza de código la cual se ejecutará antes y/o
# después de cada petición realizada al servidor y a traves de ellos podemos
# hacer operaciones antes de renderizar el template al usuario

MIDDLEWARE = [
    # corsheaders debe estar encima de security
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# Aqui va la configuracion de las plantillas que vamos a utilizar

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')], # Con esto le indicamos donde estan nuestros templates
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

WSGI_APPLICATION = 'core.wsgi.application'


# Mientras estamos en la construccion del software se recomienda utilizar sqlite3
# posteriormente migramos a otro motor de BD

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Cambiamos el lenguaje a español (es) la zona horaria (GMT-5 o America/Bogota)

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True # Para el lenguaje
USE_TZ = True # Para usar el time_zone

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'


# Con esto le indicamos donde van a estar los archivos estaticos (css, js, img, audios ...)

STATIC_ROOT = os.path.join(BASE_DIR, 'static') # Le indicamos el nombre del directorio y de la carpeta(agencia..., static)
# Ruta de los archivos estaticos (css, js, img...)
STATIC_URL = '/static/'


# Indicamos donde vamos a guardar las imagenes

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Ruta del media url
MEDIA_URL = '/media/'


STATICFILES_DIRS = [
    # Indicamos que esta dentro de la carpeta build
    os.path.join(BASE_DIR, 'build/static')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Con esto le indicamos quien puede acceder a la informacion

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # Con esto permitimos el acceso de solo lectura a los usuarios no autenticados y
        # permiso completo a los usuarios autenticados
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}

# Configuracion de los llamados y indicamos quien puede usar nuestro sitio

# Con esto decimos que react puede acceder a esta informacion
CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEV')
# Aqui determinamos que dominios pueden hacer respons - request
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEV')

# Email (este es para cuando estamos en la etapa de construccion)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Con esto indicamos que cuando estemos en modo despliegue use esos dominios en caso contrario todos los dominios
# Y tambien cambiamos de motor de base de datos, los dominios...
if not DEBUG:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEPLOY')
    # indicamos tambien que cambie el quien puede usar nuestro sitio
    CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEPLOY')
    # cambiamos el dominio que puede hacer request - response
    CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEPLOY')

    DATABASES = {
        "default": env.db("DATABASE_URL"), # Llamamos el url de una base de datos
    }
    DATABASES['default']["ATOMIC_REQUESTS"] = True # Con esto hacemos que con los request y respons eviten los duplicados