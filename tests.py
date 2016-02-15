import unittest
from playhouse.test_utils import test_database
from peewee import MySQLDatabase

from models import *

import random

test_db = MySQLDatabase(
	'abdul_blog',
	user='root',
	passwd='aa121292',
	port=3306,
	host='localhost'
	)

class TestUsers(unittest.TestCase):
	def setUp(self):
		test_db.connect()
		try:
			test_db.drop_tables((User, Post, Image), safe=True)
		except:
			print "doesnt exist"
		test_db.create_tables((User, Post, Image), safe=True)
		self.create_test_data()
		test_db.close()

	def create_test_data(self):
		for u in range(10):
			userid ='user_%s' % u
			User.new(
				twitter=userid, 
				email='user_%s@gmail.com'%userid, 
				password='passwd_%s'%userid, 
				bio='random bio for user: %s'%userid
			)
			for p in range(5):
				content = 'post_content_%s' % p
				Post.create(content=content, user=u+1)
				url = 'http://test.com/%s_example_%s'
				Image.create(url=url% (p, u + random.randint(0,10)), title='image_%s'%(u+1), post=p+1)
				Image.create(url=url% (p, u + random.randint(0,10)), title='image_%s'%(u+1), post=p+1)


	def test_creating_ten_users(self):
		result = len(User.select())
		self.assertTrue(result == 10, msg='is not equal')
	
	def test_user_has_posts(self):
		posts = len(Post.select().where(Post.id == 1))
		self.assertTrue(posts != 0)

if __name__ == "__main__":
	unittest.main()