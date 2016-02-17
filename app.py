from flask import (Flask, g, render_template, flash, redirect, url_for, request, session)
from flask.ext.login import (LoginManager, login_user, logout_user, login_required, current_user)
from flask_peewee.db import Database
from flask.ext.bcrypt import check_password_hash
from playhouse.shortcuts import model_to_dict
from flask.ext.login import current_user
from flask.ext.dropbox import Dropbox, DropboxBlueprint
from werkzeug import secure_filename
from models import *
import json
import helpers
import requests

app = Flask(__name__)
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# app.config.from_object('config.DevelopmentConfig')
DATABASE = {
		'name' : 'abdul_blog',
		'engine' : 'peewee.MySQLDatabase',
		'host' : 'localhost',
		'port' : 3306,
		'user' : 'root',
		'passwd' : 'aa121292'
		}
DEBUG = True
TESTING = False
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
DROPBOX_KEY = '	ijsequnfjgbs2v3'
DROPBOX_SECRET = 'athtuhs7doybhes'
DROPBOX_ACCESS_TYPE = 'app_folder'

app.config.from_object(__name__)
db = Database(app)
dropbox = Dropbox(app)
dropbox.register_blueprint(url_prefix='/dropbox')

# @app.before_first_request
# def create_user():
#     for Model in (User, Role, UserRoles):
#     	try:
#         	Model.drop_table(fail_silently=True)
#         except:
#         	print "nonono"
#         Model.create_table(fail_silently=True)
#     user_datastore.create_user(email='abdulachik@gmail.com', password='aa121292', twitter='abdulachik')

@app.route('/')
def root():
	print "hello"
	return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
	print "login"
	post = request.get_json()
	user = User.select().where(User.email == post.get('email')).get()
	print user
	print user.twitter
	if user and check_password_hash(user.password, post.get('password')):
		session['logged_in'] = True
		status = True
		return json.dumps({"result":status})
	else:
		status = False
		return json.dumps({"result":status})

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return json.dumps({'result': 'success'})


@app.route('/user/all')
def all_users():
	users = User.select()
	return json.dumps(helpers.models_to_dict(users))

@app.route('/user/<id>', methods=['GET', 'DELETE', 'PUT'])
def user(id):
	if request.method == "GET":
		user = User.select().where(User.id == id).get()
		return json.dumps(model_to_dict(user), default=helpers.date_handler)

	if request.method == "DELETE":
		user = User.delete().where(User.id == id)
		user.execute()
		return json.dumps({ "response" : "OK!" })

	if request.method == "PUT":
		user = User.update(
				twitter = request.form['twitter'],
				email = request.form['email'],
				password = request.form['password'],
				bio = request.form['bio']
			).where(User.id == id)
		user.execute()
		return json.dumps({ "response" : "OK!" })

@app.route('/user/new', methods=['POST'])
def new_user():
	user = User.new(
		twitter = request.form['twitter'],
		email = request.form['email'],
		password = request.form['password'],
		bio = request.form['bio']
		)
	user.save()
	return json.dumps({ "response" : "OK!" })

@app.route('/post/all')
def all_posts():
	# posts = TagPost.select(TagPost, Tag, Post).join(Tag).switch(TagPost).join(Post).order_by(Post.date)
	posts = Post.select().order_by(Post.date)
	return json.dumps(helpers.models_to_dict(posts), default=helpers.date_handler)

@app.route('/post/<id>', methods=['GET', 'DELETE', 'PUT'])
def post(id):
	if request.method == "GET":
		post = Post.select().where(Post.id == id).get()
		return json.dumps(model_to_dict(post), default=helpers.date_handler)

	if request.method == "DELETE":
		post = Post.delete().where(Post.id == id)
		post.execute()
		return json.dumps({ "response" : "OK!" })

	if request.method == "PUT":
		post = Post.update(
				content=request.form['content'],
				date=request.form['date']
			).where(Post.id == id)
		post.execute()
		return json.dumps({ "response" : "OK!" })

@app.route('/post/new', methods=["POST"])
def new_post():
	user = current_user
	post = Post.create(
		content=request.form['content'],
		user=user
		)
	post.save()
	return json.dumps({ "response" : "OK!" })

@app.route('/imagepost/<imageid>/<postid>', methods=["POST"])
def image_in_post(imageid, postid):
	imagepost = ImagePost.create(image=imageid, post=postid)
	imagepost.save()
	return json.dumps({ "response" : "OK!" })

@app.route('/tagpost/<tagid>/<postid>', methods=["POST"])
def tag_in_post(tagid, postid):
	tagpost = TagPost.create(tag=tagid, post=postid)
	tagpost.save()
	return json.dumps({ "response" : "OK!"})

@app.route('/image/all')
def all_images():
	images = Image.select()
	return json.dumps(helpers.models_to_dict(images), default=helpers.date_handler)

@app.route('/image/<id>', methods=['GET', 'DELETE', 'PUT'])
def image(id):
	if request.method == "GET":
		image = Image.select().where(Image.id == id).get()
		return json.dumps(model_to_dict(image), default=helpers.date_handler)

	if request.method == "DELETE":
		image = Image.delete().where(Image.id == id)
		image.execute()
		return json.dumps({ "response" : "OK!" })

	if request.method == "PUT":
		image = Image.update(
				# url=request.form['url'],
				title=request.form['title'],
				post=request.form['post']
			).where(Image.id == id)
		image.execute()
		return json.dumps({ "response" : "OK!" })

@app.route('/image/new', methods=['POST'])
def new_image():
    if not dropbox.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        file_obj = request.files['file']

        if file_obj:
            client = dropbox.client
            filename = secure_filename(file.filename)

            # Actual uploading process
            result = client.put_file('/' + filename, file_obj.read())

            path = result['path'].lstrip('/')
            image = image.create(
				url=path,
				title=request.form['title']
				)
            image.save()
            return redirect(url_for('success', filename=path))

    return json.dumps({ "response" : "OK!" })

@app.route('/tag/all')
def all_tags():
	tags = Tag.select()
	return json.dumps(helpers.models_to_dict(tags), default=helpers.date_handler)

@app.route('/tag/<id>', methods=['GET', 'DELETE', 'PUT'])
def tag(id):
	if request.method == "GET":
		tag = Tag.select().where(Tag.id == id).get()
		return json.dumps(model_to_dict(tag), default=helpers.date_handler)

	if request.method == "DELETE":
		tag = Tag.delete().where(Tag.id == id)
		tag.execute()
		return json.dump({ "response" : "OK!" })

	if request.method == "PUT":
		tag = Tag.update(
				name=request.form['name']
			).where(Tag.id == id)
		tag.execute()
		return json.dumps({ "response" : "OK!" })

@app.route('/tag/new', methods=["POST"])
def new_tag():
	tag = Tag.create(
		name=request.form['name'],
		post=request.form['post']
		)
	tag.save()
	return json.dumps({ "response" : "OK!" })

@app.route('/post/<id>/tags')
def tags_from_post(id):
	tags = Tag.select().join(TagPost).join(Post).where(TagPost.post == id)
	return json.dumps(helpers.models_to_dict(tags), default=helpers.date_handler)

@app.route('/post/<id>/images')
def images_from_post(id):
	images = Image.select().join(ImagePost).join(Post).where(ImagePost.post == id)
	return json.dumps(helpers.models_to_dict(images), default=helpers.date_handler)

if __name__ == '__main__':
	User.new(twitter="abdulachik", email="abdulachik@gmail.com", password="aa121292", bio="Programer, musician, cat lover")
	app.run()
