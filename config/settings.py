import os
from datetime import timedelta

# Flask settings
SECRET_KEY =              os.getenv('SECRET_KEY') or 'default_secret_key'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI') or 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
CSRF_ENABLED = True
TESTING = os.getenv('TESTING') or False
DATABASE_NAME =         os.getenv('DATABASE_NAME') or 'development'
REMEMBER_COOKIE_DURATION = timedelta(days=5)
DEBUG = False if os.getenv('MODE') is "development" else True
