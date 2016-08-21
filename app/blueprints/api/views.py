from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.blueprints.api.models import *
from app.blueprints.user.models import User

api = Blueprint('api', __name__, template_folder='templates', url_prefix='/api')

@api.route('/post/all')
def all_posts():
	posts = Post.query.all()
	return jsonify(posts=[post.serialize for post in posts])

@api.route('/post/<id>')
def show_post(id):
	post = Post.query.get(int(id))
	if (post):
		return jsonify(post.serialize)
	else:
		return jsonify({ "response" : "not_found" })


@api.route('/post/<id>/update', methods=['PUT', 'DELETE'])
@login_required
def update_post(id):
	if request.method == "PUT":
		put = request.get_json()
		post.title= put.get('title') if put.get('title') is not None else post.title
		post.content=put.get('content') if put.get('content') is not None else post.content
		post.published=put.get('published') if put.get('published') is not None else post.published
		try:
			db.session.commit()
			return jsonify({ "response" : "OK!"})
		except Exception:
			return jsonify({ "response": "Error!" })

			if request.method == "DELETE":
				post = Post.query.get(int(id))
				try:
					db.session.delete(post)
					db.session.commit()
					return jsonify({ "response" : "OK!" })
				except Exception:
					return jsonify({ "response": "Error!" })

@api.route('/post/new', methods=["POST"])
@login_required
def new_post():
	post = request.get_json()
	print(post)
	print(dir(post))
	new_post = Post(post.get('title'), post.get('content'), post.get('published'), current_user.id)
	tags = post.get('tags')
	if tags:
		if (len(tags) > 0):
			for tag in tags:
				title = tag.get('text')
				tag = Tag.query.filter_by(title = title).first()
				if (not tag):
					tag = Tag(title=title)
					db.session.add(tag)
					new_post.tags.append(tag)
					db.session.add(new_post)
					db.session.commit()
					return jsonify(response="OK!")

@api.route('/tag/all')
def all_tags():
	tags = Tag.query.all()
	return jsonify(tags=[tag.serialize for tag in tags])

@api.route('/tag/<id>')
def get_tag(id):
	tag = Tag.query.get(int(id))
	return jsonify(tag)

@api.route('/tag/<id>', methods=['DELETE', 'PUT'])
@login_required
def tag(id):
	tag = Tag.query.get(int(id))
	if request.method == "DELETE":
		db.session.delete(tag)
		db.session.commit()
		return jsonify({ "response" : "OK!" })

		if request.method == "PUT":
			tag.name = request.get_json().get('name')
			db.session.commit()
			return json.dumps({ "response" : "OK!" })

@api.route('/tag/new', methods=["POST"])
@login_required
def new_tag():
	post = request.get_json()
	tag = Tag(post.get('title'))
	db.session.add(tag)
	db.session.commit()
	return jsonify(response="OK")
