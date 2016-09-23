from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.blueprints.api.models import *
from app.blueprints.user.models import User

api = Blueprint('api', __name__, template_folder='templates', url_prefix='/api')

@api.route('/post/all')
def all_posts():
	posts = Post.query.all()
	if posts:
		return jsonify(posts=[post.serialize for post in posts])
	else:
		return jsonify(response = "There are no posts")

@api.route('/post/<id>')
def show_post(id):
	post = Post.query.get(int(id))
	if not post:
		return jsonify(response="Post not found")
	if request.method == "GET":
		return jsonify(post.serialize)
	if request.method == "PUT":
		try:
			title = request.form['title']
			content = request.form['content']
			published = request.form['published'] == "true"
			post.title = title if title is not None else post.title
			post.content= content if content is not None else post.content
			post.published = published if published is not None else post.published
			db.session.commit()
			return jsonify(response = "Post updated")
		except Exception:
			return jsonify(response = "Error updating post")

	if request.method == "DELETE":
		try:
			db.session.delete(post)
			db.session.commit()
			return jsonify(response = "Post deleted")
		except Exception:
			return jsonify(response = "Error deleting post")


@api.route('/post/new', methods=["POST"])
@login_required
def new_post():
	title = request.form['title']
	content = request.form['content']
	published = request.form['published'] == "true"
	tags = request.form['tags']
	new_post = Post(title, content, published, current_user.id)
	db.session.add(new_post)
	if tags is not None and len(tags) > 0:
		for tag in tags:
			title = tag.get('text')
			tag = Tag.query.filter_by(title = title).first()
			if tag:
				new_post.tags.append(tag)
				db.session.commit()
				return jsonify(response="Tag appended to the post")
			else:
				tag = Tag(title=title)
				db.session.add(tag)
				db.session.commit()
				return jsonify(response="New tag created and appended to the post")
	else:
		db.session.commit()

		if published:
			return jsonify(response = "Post published without tags")
		else:
			return jsonify(response="Post created as a draft without tags!")

@api.route('/tag/all')
def all_tags():
	tags = Tag.query.all()
	return jsonify(tags=[tag.serialize for tag in tags])


@api.route('/tag/<id>')
@login_required
def tag(id):
	tag = Tag.query.get(int(id))
	if not tag:
		return jsonify(response = "Tag not found")
	if request.method == "GET":
		return jsonify(tag=tag)
	if request.method == "DELETE":
		db.session.delete(tag)
		db.session.commit()
		return jsonify(response = "Tag deleted")
	elif request.method == "PUT":
		title = request.form['title']
		tag.name = title
		db.session.commit()
		return json.dumps(response = "Updated tag")

@api.route('/tag/new', methods=["POST"])
@login_required
def new_tag():
	title = request.form['title']
	tag = Tag(title)
	db.session.add(tag)
	db.session.commit()
	return jsonify(response="OK")
