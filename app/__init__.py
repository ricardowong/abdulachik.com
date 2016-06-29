import os
from flask import Flask, render_template_string
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask.ext.security import Security
from flask.ext.jwt import JWT

# Setup Flask app and app.config
app = Flask(__name__)
app.config.from_object('config')
# app.config.from_pyfile('application.cfg')
# Initialize Flask extensions
db = SQLAlchemy(app)                            # Initialize Flask-SQLAlchemy
mail = Mail(app)                                # Initialize Flask-Mail

# JWT Token authentication  ===================================================
def authenticate(username, password):
    user = user_datastore.find_user(email=username)
    if user and username == user.email and check_password_hash(user.password, password):
        return user
    else:
        return None


def load_user(payload):
    if validate_token(payload):
        identity = payload['identity']
        user = User.query.get(identity)
        return user
    else:
        abort(401)


jwt = JWT(app, authenticate, load_user)


from app import models, views

from models import user_datastore
security = Security(app, user_datastore)
