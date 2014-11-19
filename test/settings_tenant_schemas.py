import dj_database_url

from .settings import *


DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['ENGINE'] = 'tenant_schemas.postgresql_backend'

SHARED_APPS = (
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.sessions',

)

TENANT_APPS = (
    'tenant_schemas',
    'simple_import',
    'test',  # you must list the app where your tenant model resides in

    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.contenttypes',
    'django.contrib.auth',
)

TENANT_MODEL= 'tenant_schemas.Tenant'

INSTALLED_APPS = TENANT_APPS[1:] + SHARED_APPS + ('tenant_schemas',)


MIDDLEWARE_CLASSES = ('tenant_schemas.middleware.TenantMiddleware',) + MIDDLEWARE_CLASSES
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.request',)
