#!/usr/bin/python

import sys
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
import os
import uuid
# from models import *


# def initialize():
# 	cur = db
# 	cur.connect_db()
# 	cur.database.create_tables([User, Tag, Post, TagPost])
# 	cur.close_db([User, Tag, Post, TagPost])

# def drop():
# 	cur = db
# 	cur.connect_db()
# 	cur.database.drop_tables([User, Tag, Post, TagPost])
# 	cur.close_db([User, Tag, Post, TagPost])

# def create_tables():
# 	try:
# 		initialize()
# 	except Exception as e:
# 		print "there was a problem! which is: %s" % e.value
# 	return "executed drop tables successfully"


# def drop_tables():
# 	try:
# 		drop()
# 	except Exception as e:
# 		print "there was a problem! which is: %s" % e
# 	return "executed drop tables successfully"
# SECRET_KEY =              os.getenv('SECRET_KEY')
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
# CSRF_ENABLED = True

# # Flask-Mail settings
# MAIL_USERNAME =           os.getenv('MAIL_USERNAME')
# MAIL_PASSWORD =           os.getenv('MAIL_PASSWORD')
# MAIL_DEFAULT_SENDER =     os.getenv('MAIL_DEFAULT_SENDER')
# MAIL_SERVER =             os.getenv('MAIL_SERVER')
# MAIL_PORT =           int(os.getenv('MAIL_PORT'))

def create_all():
	from app import db
	# Create all database tables
	db.create_all()
	
def create_database_uri():
# 'mysql://abdulachik:aa121292@abdulachik.mysql.pythonanywhere-services.com/abdulachik$production'
    env_mode = raw_input("are you in production?\n")
    print env_mode
    if( env_mode == "yes"):
		username = raw_input("whats your username?\n")
		password = raw_input("whats your password?\n")
		host = 'abdulachik.mysql.pythonanywhere-services.com'
		database_name = raw_input("whats the database name?\nExample: 'username$production'\n")
		uri = 'mysql://' + username + ':' + password + '@' + host + '/' + database_name
    else:
	    uri = "sqlite:///database.db"
    return uri
	
# def config_env():
#     os.environ["SECRET_KEY"] = str(uuid.uuid4())
#     os.environ['DATABASE_URL'] = create_database_uri()
#     os.environ['MAIL_USERNAME'] = raw_input("whats your mail user?\nExample: username@gmail.com\n")
#     os.environ['MAIL_PASSWORD'] = raw_input("whats your mail password?\n")
#     os.environ['MAIL_DEFAULT_SENDER'] = raw_input('whats the displayname and email of the default sender?\nExample: "Admin" <abdulachik@gmail.com>\n')
#     os.environ['MAIL_SERVER'] = 'whats the mailserver?\nExample: smtp.gmail.com\n'
#     os.environ['MAIL_PORT'] = 'whats the port of that mailserver?\nExample: if its SSL: 465 else for TSL: 587\n'
def config_env():
# For windows only
    os.system("setx SECRET_KEY " + str(uuid.uuid4()))
    os.system("setx DATABASE_URL " + create_database_uri())
    os.system("setx MAIL_USERNAME " + raw_input("whats your mail user?\nExample: username@gmail.com\n"))
    os.system("setx MAIL_PASSWORD " + raw_input("whats your mail password?\n"))
    os.system("setx MAIL_DEFAULT_SENDER " +  raw_input('whats the displayname and email of the default sender?\nExample: "Admin" <abdulachik@gmail.com>\n'))
    os.system("setx MAIL_SERVER " +  raw_input('whats the mailserver?\nExample: smtp.gmail.com\n'))
    os.system("setx MAIL_PORT " + raw_input('whats the port of that mailserver?\nExample: if its SSL: 465 else for TSL: 587\n'))
			    
if (sys.argv[1] == "configuration"):
    config_env()
elif (sys.argv[1] == "create_all"):
    create_all()
	
	
	
	