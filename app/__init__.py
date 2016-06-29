import os
from flask import Flask, render_template_string
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from app.blueprints.dashboard import dashboard
from app.blueprints.user import user
# Setup Flask app and app.config
app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(dashboard)
app.register_blueprint(user)
# app.config.from_pyfile('application.cfg')
# Initialize Flask extensions
db = SQLAlchemy(app)                            # Initialize Flask-SQLAlchemy
mail = Mail(app)                                # Initialize Flask-Mail


def load_user(payload):
    if validate_token(payload):
        identity = payload['identity']
        user = User.query.get(identity)
        return user
    else:
        abort(401)




from app import models, views
