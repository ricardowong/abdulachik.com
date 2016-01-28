from flask import Flask
from flask_peewee.db import Database
app = Flask(__name__, static_url_path='')
app.config.from_object('config.DevelopmentConfig')
db = Database(app)

from app.routes import index