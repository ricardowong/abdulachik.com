import sys
from os.path import expanduser
import os
import uuid
import sqlalchemy

home = expanduser("~/")

def create_all():
	from app.extensions import db
	# Create all database tables
	db.create_all()

def create_database_uri(database_name):
	print("Creating database uri")
	username = input("whats your username?\n")
	password = input("whats your password?\n")
	host = 'localhost'
	port = '3306'
	uri = 'mysql://' + username + ':' + password + '@' + host + ':' + port + '/' + database_name
	print(uri)
	return uri

def config_env():
	try:
		with open(home + "/.bashrc", "w+") as outfile:
			print(outfile)
			if input("Are you in production?\n") in ['yes', 'y']:
				database_name = "production"
				outfile.write("export MODE=" + database_name +";")
			else:
				database_name = "development"
				outfile.write("export MODE=" + database_name +";")
			outfile.write("export DATABASE_NAME=" + database_name +";")
			outfile.write("export SECRET_KEY=" + str(uuid.uuid4()) + ";")
			outfile.write("export DATABASE_URI=" + create_database_uri(database_name) + ";")
			if input("do you want to configure a mail?\n") in ['yes', 'y']:
				outfile.write("export USERNAME ="+ input("whats your mail user?\nExample: username@gmail.com\n") + ";")
				outfile.write("export PASSWORD ="+ input("whats your mail password?\n") + ";")
			os.system("source ~/.bashrc")
	except IOError as e:
		print("cant open the file!" + e)

def create_db():
	engine = sqlalchemy.create_engine(os.getenv('DATABASE_URI')) # connect to server
	engine.execute("CREATE DATABASE " + os.getenv('DATABASE_NAME')) #create db
	engine.execute("USE " + os.getenv('DATABASE_ENV')) # select new db

command = input("You are using the shell, add --help for help\nType esc to exit, type menu to see available options and tool.\n>>> ")
while(command):
	if (command == "install"):
		config_env()
	elif (command == "create tables"):
	    create_all()
	elif (command == "create database"):
		create_db()
	elif (command == "habibti"):
		print("alejandra estefania aguilera")
	elif (command == "system specs"):
	    print(sys.platform)
	elif (command in ["help", "h"]):
		print("help will go here")
	elif(command in ['esc', 'exit', 'e']):
		break
	else:
		print("Error!")
	command = input(">>> ")
