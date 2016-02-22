from flask import (Flask, g, render_template, flash, redirect, url_for, request, session)
from flask.ext.login import (LoginManager, login_user, logout_user, login_required, current_user)
# from flask_peewee.db import Database
from flask.ext.bcrypt import check_password_hash
from playhouse.shortcuts import model_to_dict
from flask.ext.login import current_user
from flask.ext.dropbox import Dropbox, DropboxBlueprint
from werkzeug import secure_filename
from models import *
import json
import helpers
import requests
import uuid

app = Flask(__name__)

DATABASE = {
		'name' : 'abdulachik$abdul_blog',
		'engine' : 'peewee.MySQLDatabase',
		'host' : 'abdulachik.mysql.pythonanywhere-services.com',
		'port' : 3306,
		'user' : 'abdulachik',
		'passwd' : 'aa121292'
		}
DEBUG = True
TESTING = False

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# DROPBOX_KEY = '	ijsequnfjgbs2v3'
# DROPBOX_SECRET = 'athtuhs7doybhes'
# DROPBOX_ACCESS_TYPE = 'app_folder'
# dropbox = Dropbox(app)
# # dropbox.register_blueprint(url_prefix='/dropbox')
# db = Database(app)

app.config.from_object(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'root'

@login_manager.user_loader
def load_user(id):
	try:
		return User.get(User.id == id)
	except DoesNotExist:
		return None


@app.before_request
def before_request():
	g.db = db
	g.db.connect()
	g.user = current_user



@app.after_request
def after_request(response):
	g.db.close()
	return response


@app.route('/')
def root():
	return render_template('index.html')


@app.route('/cv')
def cv():
	return render_template('cv.html')

@app.route('/login', methods=["POST"])
def login():
	post = request.get_json()
	user = User.select().where(User.email == post.get('email')).get()
	if user and check_password_hash(user.password, post.get('password')):
		# session['logged_in'] = True
		status = True
		login_user(user)
		return json.dumps({"result":status})
	else:
		status = False
		return json.dumps({"result":status})

@app.route('/logout')
def logout():
    # session.pop('logged_in', None)
    logout_user()
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
	posts_dict = helpers.models_to_dict(posts)
	for post in posts_dict:
		tags = Tag.select().join(TagPost).join(Post).where(TagPost.post == post['id'])
		tags_dict = helpers.models_to_dict(tags)
		post["tags"] = tags_dict
	return json.dumps(posts_dict, default=helpers.date_handler)

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
		put = request.get_json()
		post = Post.update(
				title=put.get('title'),
				content=put.get('content'),
				published=put.get('published')
			).where(Post.id == id)
		post.execute()
		return json.dumps({ "response" : "OK!" })

@app.route('/post/new', methods=["POST"])
def new_post():
	post = request.get_json()
	new_post = Post.create(
		title=post.get('title'),
		content=post.get('content'),
		author=current_user.id,
		published=post.get('published')
		)
	new_post.save()
	return json.dumps(model_to_dict(new_post))

@app.route('/tagpost/<postid>', methods=["POST"])
def tag_in_post(postid):
	tags = request.get_json().get('tags')
	for tag in tags:
		TagPost.create(tag=tag['id'], post=postid)
	return json.dumps({ "response" : "OK!"})

@app.route('/tagpost/<postid>', methods=["PUT"])
def update_tag_in_post(postid):
	tags = request.get_json().get('tags')
	for tag in tags:
		TagPost.update(tag=tag['id'], post=postid)
	return json.dumps({ "response" : "OK!"})

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
	print request.get_json()
	post = request.get_json()
	tag = Tag.create(
		title=post.get('title')
		)
	tag.save()
	return json.dumps(model_to_dict(tag))

@app.route('/post/<id>/tags')
def tags_from_post(id):
	tags = Tag.select().join(TagPost).join(Post).where(TagPost.post == id)
	return json.dumps(helpers.models_to_dict(tags), default=helpers.date_handler)

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


if __name__ == '__main__':
	User.new(twitter="barackobama", email="demo@demo.com", password="0000", bio="Demo user for blog testing")
	User.new(twitter="abdulachik", email="abdulachik@gmail.com", password="aa121292", bio="Programer, musician, cat lover")
	app.run()
