import os
from datetime import timedelta

# Flask settings
SECRET_KEY =              os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = True
CSRF_ENABLED = True
TESTING = os.getenv('TESTING') or False

# SEED_ADMIN_EMAIL = 'dev@local.host'
# SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)
WEBPACK_MANIFEST_PATH = os.path.dirname(os.path.abspath(__file__)) + '/build/manifest.json'
