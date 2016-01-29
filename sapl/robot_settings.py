from . import settings

settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_sapl',
        'USER': 'sapl',
        'PASSWORD': 'sapl',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
