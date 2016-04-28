from app import app
from flask_user import login_required
from flask import render_template_string
from flask import (g, render_template, flash, redirect, url_for, request, session, jsonify)
from flask.ext.login import (LoginManager, login_user, logout_user, login_required, current_user)
from flask.ext.bcrypt import check_password_hash
from playhouse.shortcuts import model_to_dict
from app import app
from models2 import *
import json
import helpers
import requests
import uuid

# The Home page is accessible to anyone
@app.route('/admin')
def home_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
            <h2>Home page</h2>
            <p>This page can be accessed by anyone.</p><br/>
            <p><a href={{ url_for('home_page') }}>Home page</a> (anyone)</p>
            <p><a href={{ url_for('members_page') }}>Members page</a> (login required)</p>
        {% endblock %}
        """)

# The Members page is only accessible to authenticated users
@app.route('/admin/members')
@login_required                                 # Use of @login_required decorator
def members_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
            <h2>Members page</h2>
            <p>This page can only be accessed by authenticated users.</p><br/>
            <p><a href={{ url_for('home_page') }}>Home page</a> (anyone)</p>
            <p><a href={{ url_for('members_page') }}>Members page</a> (login required)</p>
        {% endblock %}
        """)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'root'

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))
	
@app.route('/')
def root():
	return render_template('index.html')

@app.before_request
def before_request():
    g.user = current_user

@app.route('/daniel-website/')
def daniel_website():
    return render_template('daniel-website.html')

@app.route('/cv')
def cv():
	return render_template('cv.html')

@app.route('/login', methods=["POST"])
def login():
	post = request.get_json()
	user = User.query.filter_by(email=post.get('email')).first()
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


# @app.route('/user/all')
# def all_users():
# 	users = User.query.all()
# 	return jsonify(users)

# @app.route('/user/<id>', methods=['GET', 'DELETE', 'PUT'])
# def user(id):
# 	if request.method == "GET":
# 		user = User.get(int(id))
# 		return jsonify(user)

# 	if request.method == "DELETE":
# 		user = User.get(int(id))
# 		db.session.delete(user)
# 		db.session.commit()
# 		return json.dumps({ "response" : "OK!" })

# 	if request.method == "PUT":
# 		user = User.update(
# 				twitter = request.form['twitter'],
# 				email = request.form['email'],
# 				password = request.form['password'],
# 				bio = request.form['bio']
# 			).where(User.id == id)
# 		user.execute()
# 		return json.dumps({ "response" : "OK!" })

# @app.route('/user/new', methods='POST')
# def new_user():
# 	user = User.new(
# 		twitter = request.form['twitter'],
# 		email = request.form['email'],
# 		password = request.form['password'],
# 		bio = request.form['bio']
# 		)
# 	user.save()
# 	return json.dumps({ "response" : "OK!" })

@app.route('/post/all')
def all_posts():
	posts = Post.query.all()
	print dir(posts)
	return jsonify(posts=[post.serialize for post in posts])

@app.route('/post/<slug>', methods=['GET', 'DELETE', 'PUT'])
def post(slug):
	if request.method == "GET":
		post = Post.select().where(Post.slug == slug).get()
		return json.dumps(model_to_dict(post), default=helpers.date_handler)

	if request.method == "DELETE":
		post = Post.delete().where(Post.slug == slug)
		post.execute()
		return json.dumps({ "response" : "OK!" })

	if request.method == "PUT":
		put = request.get_json()
		post = Post.update(
				title=put.get('title'),
				content=put.get('content'),
				published=put.get('published')
			).where(Post.slug == slug)
		post.execute()
		post = Post.select().where(Post.slug == slug).first()
		return json.dumps({ "response" : "OK!", "id": post.id })

@app.route('/post/new', methods=["POST"])
def new_post():
	post = request.get_json()
	new_post = Post(post.get('title'), post.get('content'), post.get('published'), current_user.id)
	db.session.add(new_post)
	db.session.commit()
	return jsonify(response="created")

@app.route('/tag/all')
def all_tags():
	tags = Tag.query.all()
	return jsonify(tags)

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

