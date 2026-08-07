import os
from pathlib import Path

from dotenv import load_dotenv

from syllabus.apps import SyllabusConfig
from users.apps import UsersConfig

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv("DEBUG") == "True" else False
ALLOWED_HOSTS = ["192.168.0.149", "192.168.1.2", "127.0.0.1"]

# Users config
LOGIN_URL = "syllabus:main"
AUTH_USER_MODEL = "users.User"

LOGIN_REDIRECT_URL = "users:login"
LOGOUT_REDIRECT_URL = "users:login"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    f"{UsersConfig.name}",
    f"{SyllabusConfig.name}",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Vusets_Generics.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Vusets_Generics.wsgi.application"


# Email setings
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST", default="smtp.yandex.ru")
EMAIL_PORT = os.getenv("EMAIL_PORT", default="465")
EMAIL_USE_TLS = True if os.getenv("EMAIL_USE_TLS") == "True" else False
EMAIL_USE_SSL = True if os.getenv("EMAIL_USE_SSL") == "True" else False
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", default="gorscheneow2018@yandex.ru")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", default="gorscheneow2018@yandex.ru")


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "PORT": os.getenv("DATABASE_PORT", default="5432"),
        "NAME": os.getenv("DATABASE_NAME", default="Vusets_Generics"),
        "USER": os.getenv("DATABASE_USER", default="postgres"),
        "HOST": os.getenv("DATABASE_HOST", default="localhost"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_L10N = True

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CACHES = {
    "default": {
        "BACKEND": os.getenv("BACKEND", default="django.core.cache.backends.redis.RedisCache"),
        "LOCATION": os.getenv("LOCATION", default="redis://127.0.0.1:6379/1"),
    }
}
