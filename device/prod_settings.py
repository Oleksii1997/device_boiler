
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z3%*h)bh9$d1hj!ys@vcux++4sdsd=%cg(%brg12$^xm#2^yz6'

DEBUG = False

ALLOWED_HOSTS = ["45.138.24.116"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'production',
        'USER': 'maksym',
        'PASSWORD': 'CJ75mrwBM2yXgVnnW4ug',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}