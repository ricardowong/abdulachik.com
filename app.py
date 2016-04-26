from flask import Flask
from flask_peewee.db import Database

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config.from_object('config.DevelopmentConfig')

db = Database(app)

