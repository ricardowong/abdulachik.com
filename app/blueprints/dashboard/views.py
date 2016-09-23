from flask import Blueprint, render_template, jsonify, current_app, url_for
from flask_login import login_required, current_user
import urllib
dashboard = Blueprint('dashboard', __name__, static_folder='static', template_folder='templates', url_prefix='/dashboard')

@dashboard.route('/')
@login_required
def index():
    output = []
    for rule in current_app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)
        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)
    for line in sorted(output):
        print(line)
    return render_template('dashboard.html')

@dashboard.route('/create_post')
@login_required
def create_post():
    print(current_user)
    return render_template('create_post.html')
