
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!(zhi+zeq$e+&7oa0iw@#9nhdn^9!29l-&e6*lyu$cz@!*%enz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'webdev',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'portfolio',
    'login',
    'crypto_stock',
    'currencies',
    'search_bar',
    'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    'channels',
    'side_panel',
    'register',
    'channels_redis',
    'userArea',
    'adminArea',
]

CHANNEL_LAYERS = {
    'DEFAULT': {
        'BACKEND': 'CHANNELS_REDIS.CORE.REDISCHANNELLAYER',
        'CONFIG': {
            'HOSTS': [('127.0.0.1', 6379),],
        },
    },
}

STATICFILES_FINDERS = {
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_plotly_dash.finders.DashAssetFinder',
    'django_plotly_dash.finders.DashComponentFinder'
}

PLOTLY_COMPONENTS = {
    'dash_core_components',
    'dash_html_components',
    'dash_renderer',
    'dpd_components',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stock.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR, 'template'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'currencies.context_processors.extras',
            ],
        },
    },
]

WSGI_APPLICATION = 'stock.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': '31177086_stock_web_app',
#        'USER': '31177086_stock_web_app',
#        'PASSWORD': 'mKMlNg__ag',
#        'HOST': 'serwer1990534.home.pl',
#        'PORT': '5432',
#    }
#}

DATABASES = {
    'default': {},
    'remote': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stockmastersdatabase',
        'USER': 'azureuser@stockmastersserver',
        'PASSWORD': 'TW*$Y%sdjfh',
        'HOST': 'stockmastersserver.mysql.database.azure.com',
        'PORT': 3306,
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    },
    'local': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    },
}

DATABASE_ROUTERS = [
    'stock.routers.LocalDatabaseRouter',
    'stock.routers.RemoteDatabaseRouter',
]

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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ASGI_APPLICATION = 'stock.routing.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'home/static'),
    os.path.join(BASE_DIR, 'portfolio/static'),
    os.path.join(BASE_DIR, 'userArea/static'),
    os.path.join(BASE_DIR, 'adminArea/static'),
    os.path.join(BASE_DIR, 'search_bar/static'),
    os.path.join(BASE_DIR, 'login/static'),
]
