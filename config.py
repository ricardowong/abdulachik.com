class Config(object):
	DATABASE = {
		'name' : 'abdulachik$production',
		'engine': 'peewee.MySQLDatabase',
		'host' : 'abdulachik.mysql.pythonanywhere-services.com',
		'port' : 3306,
		'user' : 'abdulachik',
		'passwd' : 'aa121292'
	}
	DEBUG = False
	TESTING = False

class ProductionConfig(Config):
	Config.DATABASE['name'] = 'abdulachik$production'


class DevelopmentConfig(Config):
	DEBUG = True
	Config.DATABASE = {
		'name' : 'development.db',
		'engine': 'peewee.SqliteDatabase',
	}


class TestingConfig(Config):
	TESTING = True
	Config.DATABASE = {
		'name' : 'test.db',
		'engine': 'peewee.SqliteDatabase',
	}
