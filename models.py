from peewee import (Model, MySQLDatabase, CompositeKey, BlobField, CharField, BooleanField, TextField, DateTimeField, ForeignKeyField,IntegrityError, DoesNotExist)
from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from app import db
import json
import datetime

class BaseModel(Model):
	
	def __repr__(self):
		return self.title

	class Meta:
		database = MySQLDatabase('abdul_blog', user='root', passwd='aa121292', port=3306, host='localhost')

class User(BaseModel, UserMixin):
	# first_name = CharField()
	# last_name = CharField()
	# geo
	# maps
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

	def __repr__(self):
		return self.email


class Image(BaseModel):
	# data = BlobField()
	title = CharField()
	url = CharField()

	def get_images_from_post(self):
		return (Image.select().where(Image.post == self.post))


class Tag(BaseModel):
	title = CharField()

	def get_tags_from_post(self):
		return (Tag.select().where(Tag.id == self.post))

class Post(BaseModel):
	title = CharField()
	content = TextField()
	date = DateTimeField(default=datetime.datetime.now())	
	author = ForeignKeyField(User, related_name='post_author')
	short_content = TextField()
	published = BooleanField()
	# tags

	def get_posts_from_user(self):
		return Post.select().where(Post.user == self.user)

class TagPost(BaseModel):
	tag = ForeignKeyField(Tag, related_name='tag_in_post', on_delete='CASCADE')
	post = ForeignKeyField(Post, related_name='post_has_tag', on_delete='CASCADE')

	class Meta:
		primary_key = CompositeKey('tag', 'post')