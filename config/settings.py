"""
Django settings for config project.
Production-ready configuration.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------------
# ENVIRONMENT
# ---------------------------------------------------

ENV = os.getenv("DJANGO_ENV", "dev")  # dev / prod

DEBUG = ENV != "prod"

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "dev-insecure-key-change-this-in-production"
)

SITE_URL = os.getenv(
    "SITE_URL",
    "http://127.0.0.1:8000" if DEBUG else "https://umayotoyedekparca.com"
)

# ---------------------------------------------------
# ALLOWED HOSTS
# ---------------------------------------------------

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = [
        "umayotoyedekparca.com",
        "www.umayotoyedekparca.com",
    ]

    CSRF_TRUSTED_ORIGINS = [
        "https://umayotoyedekparca.com",
        "https://www.umayotoyedekparca.com",
    ]

# ---------------------------------------------------
# APPLICATIONS
# ---------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "products",
]

# ---------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ---------------------------------------------------
# URL / TEMPLATES
# ---------------------------------------------------

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.business_info",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# ---------------------------------------------------
# DATABASE
# ---------------------------------------------------

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": os.getenv("POSTGRES_HOST"),
            "PORT": os.getenv("POSTGRES_PORT", "5432"),
        }
    }

# ---------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------------------------------
# LOCALIZATION
# ---------------------------------------------------

LANGUAGE_CODE = "tr-tr"
TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------
# STATIC & MEDIA
# ---------------------------------------------------

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR / "staticfiles"  # production collectstatic

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------------------------------
# SECURITY (Production)
# ---------------------------------------------------

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# ---------------------------------------------------
# DEFAULT PK
# ---------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------
# BUSINESS SETTINGS (context processor için)
# ---------------------------------------------------

BUSINESS_NAME = "Umay Oto Yedek Parça"
BUSINESS_ADDRESS = "Darıca, Kocaeli"
BUSINESS_PHONE = "+905331432357"
BUSINESS_OWNER = "Yahya Yılmaz"
BUSINESS_HOURS = "09:00 – 18:00 (Pzt – Cmt)"
BUSINESS_WHATSAPP = "905331432357"
BUSINESS_INSTAGRAM = "https://www.instagram.com/umay.oto"
BUSINESS_FACEBOOK = None
MAP_EMBED_SRC = "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d317.57589883183346!2d29.393528009666944!3d40.77723920814849!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14cadf8e01a0f4df%3A0x63d522302409b3cf!2sUmay%20Oto%20Yedek%20Par%C3%A7a!5e0!3m2!1str!2str!4v1755636859221!5m2!1str!2str"
