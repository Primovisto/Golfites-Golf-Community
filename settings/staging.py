from settings.base import *

DEBUG = False

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_vl0D4IPFphDE1u3Ckqnx3A9e')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_PDReg0EVRNz11YIG1pZo5iWV')

# PayPal Settings
SITE_URL = 'https://golfites-golf-community.herokuapp.com'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'edward@primovisto.com'

ALLOWED_HOSTS.append('golfites-golf-community.herokuapp.com', 'localhost')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}