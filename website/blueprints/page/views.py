from flask import (Blueprint, g, render_template, flash, redirect, url_for, request, session, jsonify)
from flask_login import (login_user, logout_user, login_required, current_user)
from flask_bcrypt import check_password_hash, generate_password_hash

import json
from website.helpers import *
import requests
import uuid
from website.extensions import login_manager, db
from website.blueprints.user.models import User


page = Blueprint('page', __name__, template_folder='templates')

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

#
# hoja de papel, todo aquello por lo que me sienta culpable
# doblar y quemar
# me libero del pasado, para tomar el futuro con amor
#
# al dormir cuando sienta que no pueda dormir
# dificultades por respirar
#


@page.route('/')
def root():
	return render_template('index.html')

@page.route('/demo')
def demo():
	return render_template('demo.html')



@page.route('/daniel-website/')
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

@page.route('/cv')
def cv():
	return render_template('cv.html')

#
# @page.route('/blog')
# def blog():
#     return render_template("under_construction.html")

@page.route('/portfolio')
def portfolio():
    return render_template("under_construction.html")

@page.route('/ale')
def ale():
	return render_template("ale.html")
