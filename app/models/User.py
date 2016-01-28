from app.models import BaseModel
from peewee import CharField, TextField, IntegrityError
from flask.ext.bcrypt import generate_password_hash
from flask.ext.security import UserMixin

class User(BaseModel, UserMixin):
	twitter = CharField()
	email = CharField()
	password = CharField()
	bio = TextField()

	@classmethod
	def new(cls, twitter, email, password, bio):
		try:
			cls.create(
				twitter=twitter,
				email=email,
				password=generate_password_hash(password),
				bio=bio
				)
		except IntegrityError:
			raise ValueError("User already exists")
