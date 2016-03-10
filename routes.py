from flask import (g, render_template, flash, redirect, url_for, request, session)
from flask.ext.login import (LoginManager, login_user, logout_user, login_required, current_user)
from flask.ext.bcrypt import check_password_hash
from playhouse.shortcuts import model_to_dict
from flask.ext.login import current_user
from app import app
from models import *
import json
import helpers
import requests
import uuid


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'root'

@login_manager.user_loader
def load_user(id):
	try:
		return User.get(User.id == id)
	except DoesNotExist:
		return None



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

@app.route('/user/new', methods='POST')
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
	try:
		posts_dict = helpers.models_to_dict(posts)
		for post in posts_dict:
			tags = Tag.select().join(TagPost).join(Post).where(TagPost.post == post['id'])
			tags_dict = helpers.models_to_dict(tags)
			post["tags"] = tags_dict
	except Exception as e:
		return json.dumps({ "response" : e })

	if len(posts_dict) is not 0:
		return json.dumps(posts_dict, default=helpers.date_handler)
	else:
		return json.dumps({ "response": "EMPTY" })

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
		return json.dumps({ "response" : "OK!", "id": id })

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
	return json.dumps(model_to_dict(new_post), default=helpers.date_handler)

@app.route('/tag/all')
def all_tags():
	tags = Tag.select()
	if len(tags) is not 0:
		return json.dumps(helpers.models_to_dict(tags), default=helpers.date_handler)
	else:
		return json.dumps({ "response": "EMPTY" })

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
	post = request.get_json()
	tag = Tag.create(
		title=post.get('title')
		)
	tag.save()
	return json.dumps(model_to_dict(tag))

# tagpost management, post and put
# TODO: i have to make every model to follow the same pattern in code structure
# tagpost/postid -> this makes posible to tag a post
@app.route('/tagpost/<postid>', methods=["POST", "PUT"])
def tagpost(postid):
	if request.method == "POST":
		tags = request.get_json().get('tags')
		for tag in tags:
			TagPost.create(tag=tag['id'], post=postid)
		return json.dumps({ "response" : "OK!"})
	elif request.method == "PUT":
		tags = request.get_json().get('tags')
		for tag in tags:
			TagPost.update(tag=tag['id'], post=postid)
		return json.dumps({ "response" : "OK!"})

@app.route('/tagpost/<id>/tags')
def tags_from_post(id):
	tags = Tag.select().join(TagPost).join(Post).where(TagPost.post == id)
	return json.dumps(helpers.models_to_dict(tags), default=helpers.date_handler)

@app.route('/tagpost/<postid>/tag/<tagid>/untag', methods=["DELETE"])
def untag_post(postid, tagid):
	untag = TagPost.delete().where((post == postid), (tag == postid))
	untag.save()
	return json.dumps({ "response": "OK!" })

