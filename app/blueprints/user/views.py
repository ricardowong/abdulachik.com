from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import (LoginManager, login_user, logout_user, login_required, current_user)
from flask_bcrypt import check_password_hash
from app.blueprints.user.models import User


user = Blueprint('user', __name__, template_folder='templates', url_prefix='/user')

@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('dashboard.index'))
            else:
                return redirect(url_for('user.login'))
        else:
            flash('Sorry! that email is not found.', 'error')
            return redirect(url_for('user.login'))

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('root'))

@user.route('/current_user')
def get_user(): 
    user = current_user.serialize
    return jsonify(username = user["username"], id=user["id"], email = user["email"] )
