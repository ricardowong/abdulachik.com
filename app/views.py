from app import app
from flask import (g, render_template, flash, redirect, url_for, request, session, jsonify)
from flask_login import (login_user, logout_user, login_required, current_user)
from flask_bcrypt import check_password_hash, generate_password_hash

import json
from app.helpers import *
import requests
import uuid
from app.extensions import login_manager, db
from app.blueprints.user.models import User

login_manager.init_app(app)
login_manager.login_view = 'user.login'

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_first_request
def create_database():
	db.create_all()
	user = User.query.filter_by(email='abdulachik@gmail.com').first()
	if user == None:
		admin = User(username='abdulachik', password=generate_password_hash('aa121292'), email="abdulachik@gmail.com")
		db.session.add(admin)
		db.session.commit()
@app.route('/')
def root():
	return render_template('index.html')

# @login_required
# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

@app.route('/index')
def index():
	return render_template('index-react.html')

@app.route('/demo')
def demo():
	return render_template('demo.html')

@app.before_request
def before_request():
    g.user = current_user

@app.route('/daniel-website/')
def daniel_website():
    return render_template('daniel-website.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
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


@app.route('/blog')
def blog():
    return render_template("under_construction.html")

@app.route('/portfolio')
def portfolio():
    return render_template("under_construction.html")

@app.route('/ale')
def ale():
	return render_template("ale.html")
