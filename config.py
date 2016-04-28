# import os

# Use a Class-based config to avoid needing a 2nd file
# os.getenv() enables configuration through OS environment variables
# class ConfigClass(object):
    # # Flask settings
    # SECRET_KEY =              os.getenv('SECRET_KEY',       'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT')
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',     'sqlite:///development.db')
    # CSRF_ENABLED = True

    # # Flask-Mail settings
    # MAIL_USERNAME =           os.getenv('MAIL_USERNAME',        'abdulachik@gmail.com')
    # MAIL_PASSWORD =           os.getenv('MAIL_PASSWORD',        'aa121292')
    # MAIL_DEFAULT_SENDER =     os.getenv('MAIL_DEFAULT_SENDER',  '"MyApp" <abdulachik@gmail.com>')
    # MAIL_SERVER =             os.getenv('MAIL_SERVER',          'smtp.gmail.com')
    # MAIL_PORT =           int(os.getenv('MAIL_PORT',            '465'))
    # MAIL_USE_SSL =        int(os.getenv('MAIL_USE_SSL',         True))
    
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
CSRF_ENABLED = True

# Flask-Mail settings
MAIL_USERNAME =  'abdulachik@gmail.com'
MAIL_PASSWORD = 'aa121292'
MAIL_DEFAULT_SENDER = '"Admin" <abdulachik@gmail.com>'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = '465'
MAIL_USE_SSL = True
MAIL_USE_TSL = False

# Flask-User settings
USER_APP_NAME        = "abdul-blog"                # Used by email templates

