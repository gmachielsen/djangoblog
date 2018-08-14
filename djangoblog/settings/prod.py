from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['artist-blog.herokuapp.com']

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

