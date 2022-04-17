import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_URLCONF = 'djangochat.urls'

WSGI_APPLICATION = 'djangochat.wsgi.application'
