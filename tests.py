import unittest
from playhouse.test_utils import test_database
from peewee import MySQLDatabase

from app.models.User import User

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
			test_db.drop_table(User)
		except:
			print "doesnt exist"
		test_db.create_table(User)
		test_db.close()

	def create_test_data(self):
		for i in range(10):
			userid ='user_%s' % i
			User.new(
				twitter=userid, 
				email='user_%s@gmail.com'%userid, 
				password='passwd_%s'%userid, 
				bio='random bio for user: %s'%userid
				)

	def test_creating_ten_users(self):
		self.create_test_data()
		result = len(User.select())
		self.assertTrue(result == 10, msg='is not equal')

if __name__ == "__main__":
	unittest.main()