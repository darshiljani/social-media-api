from datetime import timedelta

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql",
		"NAME": os.getenv("DB_NAME"),
		"USER": os.getenv("DB_USER"),
		"PASSWORD": os.getenv("DB_PWD"),
		"HOST": "127.0.0.1",
		"PORT": "5432",
	}
}


CORS_ALLOWED_ORIGINS = [
	"http://localhost:5500",  # Live Server
	"http://localhost:3000",  # Create React App 1
	"http://localhost:3001",  # Create React App 1
	"http://localhost:5173",  # Vite
	"http://localhost:5174",  # Vite 2
]

INTERNAL_IPS = ["http://127.0.0.1"]

LOGGING = {
	"version": 1,
	"disable_existing_loggers": False,
	"formatters": {
		"verbose": {
			"format": "{levelname} - {asctime} | P : {process:d}, T : {thread:d} | {module} : {message}",
			"style": "{",
		},
		"simple": {
			"format": "{levelname} - {asctime} | {module} : {message}",
			"style": "{",
		},
	},
	"handlers": {
		"console": {
			"level": "DEBUG",
			"class": "logging.StreamHandler",
			"formatter": "simple",
		},
	},
	"loggers": {
		"django": {"handlers": ["console"], "propogate": True, "level": "INFO"}
	},
}


# Swagger documentation
SWAGGER_SETTINGS = {
	"DOC_EXPANSION": "list",
	"APIS_SORTER": "alpha",
	"USE_SESSION_AUTH": False,
	"SECURITY_DEFINITIONS": {
		"Bearer": {
			"type": "apiKey",
			"name": "Authorization",
			"in": "header",
		}
	},
}


SIMPLE_JWT = {
	"ACCESS_TOKEN_LIFETIME": timedelta(hours=10),
	"REFRESH_TOKEN_LIFETIME": timedelta(days=1),
	"AUTH_HEADER_TYPES": ("Bearer",),
	"AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
	"USER_ID_FIELD": "id",
	"USER_ID_CLAIM": "user_id",
	"USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
	"AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
	"TOKEN_TYPE_CLAIM": "token_type",
	"TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
	"JTI_CLAIM": "jti",
}
