from split_settings.tools import include

from djangochat.conf.environ import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', cast=bool, default=False)

include(
    'conf/api.py',
    'conf/auth.py',
    'conf/boilerplate.py',
    'conf/db.py',
    'conf/http.py',
    'conf/i18n.py',
    'conf/installed_apps.py',
    'conf/middlewares.py',
    'conf/static.py',
    'conf/templates.py',
    'conf/timezone.py',
)
