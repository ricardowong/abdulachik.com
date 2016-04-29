from app import db
from flask_sqlalchemy import SQLAlchemy
import json
import datetime
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)

	# User authentication information
	username = db.Column(db.String(50), nullable=False, unique=True)
	password = db.Column(db.String(255), nullable=False, server_default='')
	reset_password_token = db.Column(db.String(100), nullable=False, server_default='')

	# User email information
	email = db.Column(db.String(255), nullable=False, unique=True)
	confirmed_at = db.Column(db.DateTime())

	# User information
	active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
	first_name = db.Column(db.String(100), nullable=False, server_default='')
	last_name = db.Column(db.String(100), nullable=False, server_default='')



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

def initialize():
	cur = db
	cur.connect_db()
	cur.database.create_tables([User, Tag, Post, TagPost])
	cur.close_db([User, Tag, Post, TagPost])

def drop():
	cur = db
	cur.connect_db()
	cur.database.drop_tables([User, Tag, Post, TagPost])
	cur.close_db([User, Tag, Post, TagPost])