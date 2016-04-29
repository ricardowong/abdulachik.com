import sys
import os
import uuid

def create_all():
	from app import db
	# Create all database tables
	db.create_all()
	
def create_database_uri():
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
	
def config_env():
# For windows only
    if (sys.platform == 'win32'):
		os.system("setx SECRET_KEY " + str(uuid.uuid4()))
		os.system("setx DATABASE_URL " + create_database_uri())
		os.system("setx MAIL_USERNAME " + raw_input("whats your mail user?\nExample: username@gmail.com\n"))
		os.system("setx MAIL_PASSWORD " + raw_input("whats your mail password?\n"))
		os.system("setx MAIL_DEFAULT_SENDER " +  raw_input('whats the displayname and email of the default sender?\nExample: "Admin" <abdulachik@gmail.com>\n'))
		os.system("setx MAIL_SERVER " +  raw_input('whats the mailserver?\nExample: smtp.gmail.com\n'))
		os.system("setx MAIL_PORT " + raw_input('whats the port of that mailserver?\nExample: if its SSL: 465 else for TSL: 587\n'))
    else: 
		with open(".bashrc", "a") as outfile:  # 'a' stands for "append"
			outfile.write("export SECRET_KEY " + str(uuid.uuid4()) + ";")
			outfile.write("export DATABASE_URL " + create_database_uri() + ";")
			outfile.write("export MAIL_USERNAME " + raw_input("whats your mail user?\nExample: username@gmail.com\n") + ";")
			outfile.write("export MAIL_PASSWORD " + raw_input("whats your mail password?\n") + ";")
			outfile.write("export MAIL_DEFAULT_SENDER " +  raw_input('whats the displayname and email of the default sender?\nExample: "Admin" <abdulachik@gmail.com>\n') + ";")
			outfile.write("export MAIL_SERVER " +  raw_input('whats the mailserver?\nExample: smtp.gmail.com\n') + ";")
			outfile.write("export MAIL_PORT " + raw_input('whats the port of that mailserver?\nExample: if its SSL: 465 else for TSL: 587\n') + ";")
		os.system("source .bashrc")
	    
			    
if (sys.argv[1] == "configuration"):
    config_env()
elif (sys.argv[1] == "create_all"):
    create_all()
elif (sys.argv[1] == "Sys specs"):
    print sys.platform
	
	
	
	