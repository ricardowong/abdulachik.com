from flask import Blueprint, render_template
from flask_login import login_required
dashboard = Blueprint('dashboard', __name__, template_folder='templates', url_prefix='/dashboard')

@dashboard.route('/')
@login_required
def index():
    return render_template('dashboard.html')
