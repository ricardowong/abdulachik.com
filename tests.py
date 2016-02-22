import unittest
from playhouse.test_utils import test_database
from models import *
import random
import requests

test_db = db

class TestUsers(unittest.TestCase):
	@classmethod
	def setUp(cls):
		test_db.connect_db()
		try:
			test_db.database.drop_tables((User, Post, Image, Tag), safe=True)
		except:
			print "doesnt exist"
		test_db.database.create_tables((User, Post, Image, Tag), safe=True)
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
		test_db.close_db((User, Post, Image, Tag))


	def test_creating_users(self):
		result = len(User.select())
		self.assertTrue(result != 0, msg='is not equal')
	
	def test_user_has_posts(self):
		posts = len(Post.select().where(Post.id == 1))
		self.assertTrue(posts != 0)

if __name__ == "__main__":
	unittest.main()