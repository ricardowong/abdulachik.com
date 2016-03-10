from peewee import (Model, CompositeKey, BlobField, CharField, BooleanField, TextField, DateTimeField, ForeignKeyField,IntegrityError, DoesNotExist)
from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from app import db
import json
import datetime
import re
from unicodedata import normalize


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
	twitter = CharField(unique=True)
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
	title = CharField(unique=True)

	def get_tags_from_post(self, post):
		return (TagPost.select().where(Tag.id == post.id))

class Post(BaseModel):
	title = CharField(unique=True)
	slug = CharField(unique=True)
	content = TextField()
	date = DateTimeField(default=datetime.datetime.now())	
	author = ForeignKeyField(User, related_name='post_author')
	published = BooleanField(default=False)

	@classmethod
	def new(cls, title, content, author, published):
		try:
			delim=u'-'
			u = unicode(title, "utf-8") if not isinstance(title, unicode) else title
			_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
			result = []
			for word in _punct_re.split(u.lower()):
				word = normalize('NFKD', word).encode('ascii', 'ignore')
				if word:
					result.append(word)
			post = cls.create(
				title=title,
				slug=unicode(delim.join(result)),
				content=content,
				author=author,
				published=published
				)
			post.save()
			return post
		except IntegrityError:
			raise ValueError("Post already exists")

	def get_posts_from_user(self):
		return Post.select().where(Post.author == self.author)

class TagPost(BaseModel):
	tag = ForeignKeyField(Tag, related_name='tag_in_post', on_delete='CASCADE')
	post = ForeignKeyField(Post, related_name='post_has_tag', on_delete='CASCADE')

	def __repr__(self):
		return self.post.title + self.tag.title
	class Meta:
		primary_key = CompositeKey('tag', 'post')
