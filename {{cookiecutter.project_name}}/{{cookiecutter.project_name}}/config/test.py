from .base import *

# Use sqlite3 as test database backend

DATABASES = {
    "default": {
       "ENGINE": "django.db.backends.sqlite3",
       "NAME": "memory", 
    }
}

# Just in case I need to test emails
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
