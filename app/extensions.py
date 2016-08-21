from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

debug_toolbar = DebugToolbarExtension()
db = SQLAlchemy()
login_manager = LoginManager()
