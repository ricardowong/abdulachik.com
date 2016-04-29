import os
from flask import Flask, render_template_string
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

# Setup Flask app and app.config
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
# app.config.from_pyfile('application.cfg')

# Initialize Flask extensions
db = SQLAlchemy(app)                            # Initialize Flask-SQLAlchemy
mail = Mail(app)                                # Initialize Flask-Mail


from app import models, views