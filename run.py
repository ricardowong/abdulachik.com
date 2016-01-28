from app import app, db
from app.models.User import User
from app.models.Role import Role
from app.models.UserRoles import UserRoles
from flask.ext.security import Security, PeeweeUserDatastore

user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    for Model in (User, Role, UserRoles):
        Model.drop_table(fail_silently=True)
        Model.create_table(fail_silently=True)
    user_datastore.create_user(email='abdulachik@gmail.com', password='aa121292', twitter='abdulachik')


if __name__ == '__main__':
	app.run()
