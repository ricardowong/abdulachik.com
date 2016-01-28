class Config(object):
	DATABASE = {
		'name' : 'abdul_blog',
		'engine' : 'peewee.MySQLDatabase',
		'host' : 'localhost',
		'port' : 3306,
		'user' : 'root',
		'passwd' : 'aa121292'
	}
	DEBUG = False
	TESTING = False

class ProductionConfig(Config):
	pass


class DevelopmentConfig(Config):
	DEBUG = True


class TestingConfig(Config):
	TESTING = True