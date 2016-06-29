from app import app
from flask import (g, render_template, flash, redirect, url_for, request, session, jsonify)
from flask.ext.login import (LoginManager, login_user, logout_user, login_required, current_user)
from flask.ext.bcrypt import check_password_hash
from models import *

import json
import helpers
import requests
import uuid

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/')
def root():
	return render_template('index.html')

@login_required
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/index')
def index():
	return render_template('index-react.html')

@app.before_request
def before_request():
    g.user = current_user

@app.route('/daniel-website/')
def daniel_website():
    return render_template('daniel-website.html')

# @app.route('/contact-me', methods=['POST'])
# def contact_me():
#     message = request.get_json()
#     subject = "[blogify-notification]: " + message.get('subject')
#     sender = message.get('sender')
#     content = sender + ": " + message.get('content')
#     captcha = message.get('captcha')
#     email = Message(subject, sender=sender)
#     email.add_recipient("abdulachik@gmail.com")
#     email.body = content
#     try:
# 		# change this os we use the app.config vars instead of leaving it public
#         SITE_KEY = "6LcKAB8TAAAAAO2twN-zfqEQZ0bUz4KkRgk0p8e1"
#         SECRET_KEY = "6LcKAB8TAAAAALBGRpDf1SAYHgMtoDRmX4MnGhFl"
#         r = requests.post('https://www.google.com/recaptcha/api/siteverify',
#             data = {
#                 "secret": SECRET_KEY,
#                 "response" : captcha
#                 }
#         )
#         if r.json().get('success'):
#             mail.send(email)
#             return jsonify({ "response":"message sent" })
#         else:
#             return jsonify({ "response":"wrong captcha" })
#     except Exception:
#         return jsonify({ "response":"error" })

@app.route('/cv')
def cv():
	return render_template('cv.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if check_password_hash(user.password, password):
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))

@app.route('/blog')
def blog():
    return render_template("under_construction.html")

@app.route('/portfolio')
def portfolio():
    return render_template("under_construction.html")

@app.route('/logout')
def logout():
    logout_user()
    return json.dumps({'result': 'success'})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/post/all')
def all_posts():
	posts = Post.query.all()
	return jsonify(posts=[post.serialize for post in posts])

@app.route('/post/<id>')
def show_post(id):
    post = Post.query.get(int(id))
    if (post):
        return jsonify(post.serialize)
    else:
        return jsonify({ "response" : "not_found" })


@app.route('/post/<id>/update', methods=['PUT'])
def update_post(id):
    put = request.get_json()
    post.title= put.get('title') if put.get('title') is not None else post.title
    post.content=put.get('content') if put.get('content') is not None else post.content
    post.published=put.get('published') if put.get('published') is not None else post.published
    try:
    	db.session.commit()
    	return jsonify({ "response" : "OK!"})
    except Exception:
        return jsonify({ "response": "Error!" })

@app.route('/post/<id>/delete', methods=['GET', 'DELETE', 'PUT'])
def delete_post(id):
    post = Post.query.get(int(id))
    try:
        db.session.delete(post)
        db.session.commit()
        return jsonify({ "response" : "OK!" })
    except Exception:
        return jsonify({ "response": "Error!" })


@app.route('/post/new', methods=["POST"])
def new_post():
	post = request.get_json()
	new_post = Post(post.get('title'), post.get('content'), post.get('published'), current_user.id)
	if (len(post.get('tags')) > 0):
	    for tag in post.get('tags'):
			title = tag.get('title')
			tag = Tag.query.filter_by(title = title).first()
			print tag
			new_post.tags.append(tag)
	db.session.add(new_post)
	db.session.commit()
	return jsonify(response="OK!")

@app.route('/tag/all')
def all_tags():
	tags = Tag.query.all()
	return jsonify(tags=[tag.serialize for tag in tags])

@app.route('/tag/<id>', methods=['GET', 'DELETE', 'PUT'])
def tag(id):
	tag = Tag.query.get(int(id))
	if request.method == "GET":
		return jsonify(tag)

	if request.method == "DELETE":
		db.session.delete(tag)
		db.session.commit()
		return jsonify({ "response" : "OK!" })

	if request.method == "PUT":
		tag.name=request.form['name']
		db.session.commit()
		return json.dumps({ "response" : "OK!" })

@app.route('/tag/new', methods=["POST"])
def new_tag():
	post = request.get_json()
	tag = Tag(post.get('title'))
	db.session.add(tag)
	db.session.commit()
	return jsonify(response="OK")
