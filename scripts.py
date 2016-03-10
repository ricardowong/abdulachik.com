#!/usr/bin/python

import sys
from models import initialize, drop
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)


def create_tables():
	try:
		initialize()
	except Exception as e:
		return "there was a problem! which is: %s" % e.value
	return "OK"

def drop_tables():
	return "OK"