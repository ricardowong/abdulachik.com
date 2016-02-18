from peewee import MySQLDatabase
from models import *
import random

db = MySQLDatabase(
	'abdul_blog',
	user='root',
	passwd='aa121292',
	port=3306,
	host='localhost'
	)

def initialize():
	db.connect()
	db.create_tables([User, Post, Tag, TagPost, Image, ImagePost], safe=True)
	db.close()

def drop():
	db.connect()
	db.drop_tables([User, Post, Tag, TagPost, Image, ImagePost], safe=False, cascade=True)
	db.close()

def create_test_data():
	userid ='user_%s' % 1
	User.new(
		twitter=userid, 
		email='user_%s@gmail.com'%userid, 
		password='passwd_%s'%userid, 
		bio='random bio for user: %s'%userid
	)
	print "User: #%s"%1
	for p in range(random.randint(0,10)):
		content = 'post_content_%s' % p
		Post.create(title="post_%s"%p, content=content, author=1)
		print "Post: #%s"%p
		for t in range(random.randint(0,10)):
			print "Tag: #%s for post %s"%(t + 1, p + 1)
			Tag.create(name="tag_%s"%t, post=p+1)
			TagPost.create(tag=t+1, post=p+1)
		for i in range(random.randint(0,10)):
			print "Image: #%s for post %s"%(i + 1, p + 1)
			Image.create(url=(i + random.randint(0,10)), title='image_%s'%(i+1), post=p+1)
			ImagePost.create(image=i+1, post=p+1)

if __name__ == "__main__":
	drop()
	initialize()
	create_test_data()