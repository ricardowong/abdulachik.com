from app import app, db
from app.models.User import User
if __name__ == '__main__':
	#db.create_all()
	db.database.connect()
	db.database.create_table(User, safe=True)
	db.database.close()
	app.run()
