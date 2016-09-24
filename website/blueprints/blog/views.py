from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from website.blueprints.api.models import Post, Tag

blog = Blueprint('blog', __name__, template_folder='templates', url_prefix='/blog', static_folder='static')


@blog.route('/')
def index():
    return render_template('blog-index.html')
