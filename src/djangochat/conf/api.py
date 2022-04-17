from djangochat.conf.environ import env

# Django REST Framework
# https://www.django-rest-framework.org/api-guide/settings/

DISABLE_THROTTLING = env('DISABLE_THROTTLING', cast=bool, default=False)
MAX_PAGE_SIZE = env('MAX_PAGE_SIZE', cast=int, default=1000)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'djangochat.api.renderers.AppJSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_PAGINATION_CLASS': 'djangochat.api.pagination.AppPagination',
    'PAGE_SIZE': env('PAGE_SIZE', cast=int, default=20),
    'DEFAULT_THROTTLE_RATES': {
        'anon-auth': '10/min',
    },
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
}

# Adding session auth and browsable API at the developer machine
if env('DEBUG', cast=bool, default=False):
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer')
