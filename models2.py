from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin
import datetime
db = SQLAlchemy()


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)

	# User authentication information
	username = db.Column(db.String(50), nullable=False, unique=True)
	password = db.Column(db.String(255), nullable=False, server_default='')
	reset_password_token = db.Column(
		db.String(100), nullable=False, server_default='')

	# User email information
	email = db.Column(db.String(255), nullable=False, unique=True)
	confirmed_at = db.Column(db.DateTime())

	# User information
	active = db.Column(
		'is_active', db.Boolean(), nullable=False, server_default='0')
	first_name = db.Column(db.String(100), nullable=False, server_default='')
	last_name = db.Column(db.String(100), nullable=False, server_default='')
	posts = db.relationship("Post", backref="user", lazy="dynamic")


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140), nullable=False, server_default='')
	slug = db.Column(db.String(200), nullable=False, server_default='')
	content = db.Column(db.Text, nullable=False, server_default='')
	date = db.Column(db.DateTime, nullable=False, server_default=str(datetime.datetime.now().timestamp()))	
	published = db.Column(db.Boolean, nullable=False, server_default='False')  
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))   
	tags = db.relationship('Tag', secondary=tags, backref=db.backref('posts', lazy='dynamic'))
	
	def __init__(self, name):
		self.name = name
		self.slug = slugify(name)


class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tilte = db.Column(db.String(255), nullable=False, server_default='')