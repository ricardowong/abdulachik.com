from flask import Flask
from flask_peewee.db import Database

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config.from_object('config.DevelopmentConfig')

db = Database(app)

from routes import *


@app.before_request
def before_request():
	g.db = db
	g.db.connect_db()
	g.user = current_user



@app.after_request
def after_request(response):
	g.db.close_db(True)
	return response

if __name__ == '__main__':
	# twitter = CharField()
	# email = CharField(unique=True)
	# password = CharField()
	# bio = TextField()
	try:
		drop()
	except:
		initialize()

	try:
		User.new(twitter="abdulachik", email="abdulachik@gmail.com", password="aa121292", bio="python developer")
		User.new(twitter="barackobama", email="barackobama@whitehouse.com", password="rapisthebest", bio="python developer")
	except:
		print "already exists"
	app.run()
