import os

# Flask-User settings
USER_APP_NAME        =   "abdul-blog"             # Used by email templates
APP_NAME             =   "flask-blogify"
# Flask settings
SECRET_KEY =              os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = True
CSRF_ENABLED = True
TESTING = False

# Flask-Mail settings
MAIL_USERNAME =           os.getenv('MAIL_USERNAME')
MAIL_PASSWORD =           os.getenv('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER =     os.getenv('MAIL_DEFAULT_SENDER')
MAIL_SERVER =             os.getenv('MAIL_SERVER')
MAIL_PORT =           int(os.getenv('MAIL_PORT')) if os.getenv('MAIL_PORT') is not None else 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
#
# RECAPTCHA_ENABLED = True
# RECAPTCHA_SITE_KEY = "6LcKAB8TAAAAAO2twN-zfqEQZ0bUz4KkRgk0p8e1"
# RECAPTCHA_SECRET_KEY = "6LcKAB8TAAAAALBGRpDf1SAYHgMtoDRmX4MnGhFl"
# RECAPTCHA_THEME = "dark"
# RECAPTCHA_TYPE = "image"
# RECAPTCHA_SIZE = "compact"
# RECAPTCHA_RTABINDEX = 10
