from peewee import (Model, MySQLDatabase, CompositeKey, BlobField, CharField, TextField, DateTimeField, ForeignKeyField,IntegrityError, DoesNotExist)
from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from app import db
import json
import datetime

class BaseModel(Model):
	class Meta:
		database = MySQLDatabase('abdul_blog', user='root', passwd='aa121292', port=3306, host='localhost')

class User(BaseModel, UserMixin):
	# name = CharField()
	# geo
	# maps
	twitter = CharField()
	email = CharField()
	password = CharField()
	bio = TextField(default="")

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
class Post(BaseModel):
	title = CharField()
	content = TextField()
	date = DateTimeField(default=datetime.datetime.now())	
	author = ForeignKeyField(User, related_name='post_author')
	# tags

	def get_posts_from_user(self):
		return Post.select().where(Post.user == self.user)

class Image(BaseModel):
	# data = BlobField()
	title = CharField()
	url = CharField()

	def get_images_from_post(self):
		return (Image.select().where(Image.post == self.post))

class ImagePost(BaseModel):
	image = ForeignKeyField(Image, related_name='image_in_post')
	post = ForeignKeyField(Post, related_name='post_has_image')

	class Meta:
		primary_key = CompositeKey('image', 'post')

class Tag(BaseModel):
	name = CharField()

	def get_tags_from_post(self):
		return (Tag.select().where(Tag.id == self.post))

class TagPost(BaseModel):
	tag = ForeignKeyField(Tag, related_name='tag_in_post')
	post = ForeignKeyField(Post, related_name='post_has_tag')

	class Meta:
		primary_key = CompositeKey('tag', 'post')