import os
from datetime import timedelta

# Flask settings
SECRET_KEY =              os.getenv('SECRET_KEY') or 'default_secret_key'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
CSRF_ENABLED = True
TESTING = os.getenv('TESTING') or False

REMEMBER_COOKIE_DURATION = timedelta(days=90)
