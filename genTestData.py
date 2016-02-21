from peewee import MySQLDatabase
from models import *
import random
import requests

db = MySQLDatabase(
	'abdul_blog',
	user='root',
	passwd='aa121292',
	port=3306,
	host='localhost'
	)

def initialize():
	db.connect()
	db.create_tables([User, Tag, Post, TagPost], safe=True)
	db.close()

def drop():
	db.connect()
	db.drop_tables([User, Tag, Post, TagPost], safe=True, cascade=True)
	db.close()

def create_test_data():
	userid ='user_%s' % 1
	publish = [True, False]
	User.new(
		twitter=userid, 
		email='user_%s@gmail.com'%userid, 
		password='passwd_%s'%userid, 
		bio='random bio for user: %s'%userid
	)
	for t in range(random.randint(5,10)):
		print "Tag: #%s \n"%(t + 1)
		Tag.create(title="tag_%s"%t)
	print "User: #%s \n"%1
	for p in range(random.randint(5,15)):
		result = requests.get('http://hipsterjesus.com/api/', params={"paras": random.randint(1, 10)})
		content = result.json()['text']
		# short_content = content.split('\n')[:1]
		# short_content = "".join(reversed(short_content))
		ls_tags = (Tag.select())
		post = Post.create(
			title="post_%s \n"%p, 
			content=content, author=1, 
			# short_content=short_content, 
			published=publish[random.randint(0,1)]
			)
		print "Post: #%s \n"%p
		for t in range(random.randint(0, len(ls_tags) - 1)):
			try:
				tag = TagPost.create(tag=ls_tags[random.randint(1, len(ls_tags) - 1)], post=post) if random.randint(0,1) == 1 else None
				if tag:
					print "Post %s tagged with %s tag \n" % (post, tag)
			except:
				continue

if __name__ == "__main__":
	drop()
	initialize()
	create_test_data()