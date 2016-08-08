from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask import current_app
from slugify import slugify
import datetime
from app.extensions import db
from app.blueprints.user.models import User

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)

class Post(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False, default='')
    slug = db.Column(db.String(200), nullable=False, default='')
    content = db.Column(db.Text, nullable=False, default='')
    date = db.Column(db.DateTime, nullable=False, default=str(datetime.datetime.now()))
    published = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('posts', lazy='dynamic'))

    @property
    def serialize(self):
        return {
           'id'         : self.id,
           'slug'	: self.slug,
           'title' : self.title,
           'author' : User.query.get(self.user_id).serialize,
           'content' : self.content,
           'published' : self.published,
           'date' : self.date,
           # This is an example how to deal with Many2Many relations
           'tags'  : self.serialize_many2many,
           'preview' : self.preview()
           }

    @property
    def serialize_many2many(self):
        return [ tag.serialize for tag in self.tags]

    def __init__(self, title, content, published, user_id):
        self.title = title
        self.slug = slugify(title)
        self.content = content
        self.published = published
        self.user_id = user_id
        self.date = datetime.datetime.now()

    def preview(self):
        return self.content[0:140]


class Tag(db.Model):
	__table_args__ = {"extend_existing": True}
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False, server_default='')

	def __init__(self, title):
	    self.title = title

	@property
	def serialize(self):
		return {
			'id' : self.id,
			'title' : self.title
		}
