import os
from flask import Flask, render_template_string
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from app.blueprints.dashboard import dashboard
from app.blueprints.user import user
from app.blueprints.api import api
from app.blueprints.blog import blog
from flask_webpack import Webpack


# webpack = Webpack()

# Setup Flask app and app.config
app = Flask(__name__)
app.config.from_object('config')
# app.config.update( WEBPACK_MANIFEST_PATH = os.path.dirname(os.path.abspath(__file__)) + '/build/manifest.json')
# app.config['WEBPACK_MANIFEST_PATH']= "\\".join(os.path.dirname(os.path.abspath(__file__)).split('\\')[:-1]) + '/build/manifest.json'

# webpack.init_app(app)
app.register_blueprint(dashboard)
app.register_blueprint(user)
app.register_blueprint(api)
app.register_blueprint(blog)

from extensions import *
db.init_app(app)
from app import views
