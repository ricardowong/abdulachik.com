#!/usr/bin/python

import sys
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

from app import db
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


def create_all():
	# Create all database tables
	db.create_all()
	
if (sys.argv[1] == "create_tables"):
	create_tables()
elif(sys.argv[1] == "drop_tables"):
	drop_tables()
elif (sys.argv[1] == "create_all"):
    create_all()
	
	
	
	