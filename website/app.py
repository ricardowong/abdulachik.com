from flask import Flask, render_template
from website.blueprints.dashboard import dashboard
from website.blueprints.user import user
from website.blueprints.api import api
from website.blueprints.blog import blog
from website.blueprints.page import page
from website.blueprints.models import User
from website.extensions import *
# from website.app import views

def create_app():
    # Setup Flask app and app.config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    app.register_blueprint(page)
    app.register_blueprint(dashboard)
    app.register_blueprint(user)
    app.register_blueprint(api)
    app.register_blueprint(blog)

    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    db.init_app(app)

    @app.before_first_request
    def create_database():
    	db.create_all()
    	user = User.query.filter_by(email='abdulachik@gmail.com').first()
    	if user == None:
    		admin = User(username='abdulachik', password=generate_password_hash('aa121292'), email="abdulachik@gmail.com")
    		db.session.add(admin)
    		db.session.commit()

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('500.html'), 500

    @app.before_request
    def before_request():
        g.user = current_user
    return app
