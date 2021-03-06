from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from flask_sqlalchemy import SQLAlchemy
from slugify import slugify
import datetime
from app import db
from app import app

class User(db.Model, UserMixin):
	__table_args__ = {"extend_existing": True}
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
	posts = db.relationship("Post", backref="author", lazy="dynamic")
	
	@property
	def serialize(self):
	    return {
			"username": self.username,
			"email" : self.email
		}
	

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
           'tags'  : self.serialize_many2many }
    
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
	
	
	
# Setup Flask-User
db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
user_manager = UserManager(db_adapter, app)  