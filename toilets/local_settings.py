DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'toilets',
        'USER': 'aleksejtihonov',
        'PASSWORD': 'Dmesggrepeth1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
