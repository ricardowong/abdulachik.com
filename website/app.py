import os
from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
from website.blueprints.dashboard import dashboard
from website.blueprints.user import user
from website.blueprints.api import api
from website.blueprints.blog import blog
from website.blueprints.page import page
from website.extensions import *
# from website.app import views

def create_app():
    # Setup Flask app and app.config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    app.register_blueprint(page)
    app.register_blueprint(dashboard)
    app.register_blueprint(user)
    app.register_blueprint(api)
    app.register_blueprint(blog)

    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    db.init_app(app)
    return app
