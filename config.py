import os
from datetime import timedelta

# Flask settings
SECRET_KEY =              os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = True
CSRF_ENABLED = True
TESTING = False
