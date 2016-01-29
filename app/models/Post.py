from helpers import BaseModel
from User import User
from peewee import CharField, TextField, ForeignKeyField

class Post(BaseModel):
	content = TextField()
	user = ForeignKeyField(User, 'user_posted')

	def get_posts_from_user(self):
		return Post.select().where(Post.user == self.user)

	# def get_all_images(self):
	# 	images = Image.select().where(Image.post == self.id)
	# 	return images

	# def get_all_comments(self):
	# 	comments = Comment.select().where(Comment.post == self.id)
	# 	return comments
