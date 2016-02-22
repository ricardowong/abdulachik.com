class Config(object):
	DATABASE = {
		'name' : 'abdulachik$abdul_blog',
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
	Config.DATABASE['name'] = 'abdulachik$development'


class TestingConfig(Config):
	TESTING = True
	Config.DATABASE['name'] = 'abdulachik$testing'