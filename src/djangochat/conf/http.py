from djangochat.conf.environ import env

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    'your.app.origin',
]

if env('DEBUG'):
    ABSOLUTE_HOST = 'http://localhost:8000'
else:
    ABSOLUTE_HOST = 'https://your.app.com'
