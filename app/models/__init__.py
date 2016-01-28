from peewee import Model, MySQLDatabase

mysql_db = MySQLDatabase('abdul_blog', user='root', passwd='aa121292', port=3306, host='localhost')

class BaseModel(Model):
	class Meta:
		database = mysql_db