from peewee import (Model, CompositeKey, BlobField, CharField, BooleanField, TextField, DateTimeField, ForeignKeyField,IntegrityError, DoesNotExist)
from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from app import db
import json
import datetime

class BaseModel(Model):
	
	def __repr__(self):
		return self.title

	class Meta:
		database = db.database

class User(BaseModel, UserMixin):
	# first_name = CharField()
	# last_name = CharField()
	# geo
	# maps
	twitter = CharField()
	email = CharField(unique=True)
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

	def get_tags_from_post(self, post):
		return (TagPost.select().where(Tag.id == post.id))

class Post(BaseModel):
	title = CharField()
	content = TextField()
	date = DateTimeField(default=datetime.datetime.now())	
	author = ForeignKeyField(User, related_name='post_author')
	published = BooleanField()
	# tags

	def get_posts_from_user(self):
		return Post.select().where(Post.author == self.author)

class TagPost(BaseModel):
	tag = ForeignKeyField(Tag, related_name='tag_in_post', on_delete='CASCADE')
	post = ForeignKeyField(Post, related_name='post_has_tag', on_delete='CASCADE')

	def __repr__(self):
		return self.post.title + self.tag.title
	class Meta:
		primary_key = CompositeKey('tag', 'post')

def initialize():
	cur = db
	cur.connect_db()
	cur.database.create_tables([User, Tag, Post, TagPost], safe=True)
	cur.close_db([User, Tag, Post, TagPost])

def drop():
	cur = db
	cur.connect_db()
	cur.database.drop_tables([User, Tag, Post, TagPost], safe=True, cascade=True)
	cur.close_db([User, Tag, Post, TagPost])
