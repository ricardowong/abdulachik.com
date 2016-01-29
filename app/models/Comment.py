from helpers import BaseModel
from User import User
from Post import Post
from peewee import TextField, ForeignKeyField

class Comment(BaseModel):
	content = TextField()
	post = ForeignKeyField(Post, related_name="in_post")
	user = ForeignKeyField(User, related_name="coment_user")

	def get_comments_from_post(self):
		return Comment.select().where(Comment.post == self.post)
