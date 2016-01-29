from helpers import BaseModel
from Post import Post
from peewee import CharField, TextField, ForeignKeyField
	

class Image(BaseModel):
	url = TextField()
	title = CharField()
	post = ForeignKeyField(Post, related_name='img_in_post')

	def get_images_from_post(self):
		return Image.select().where(Image.post == self.post)
