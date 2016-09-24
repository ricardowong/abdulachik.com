# import os
# from flask import Flask, render_template_string
# from flask_sqlalchemy import SQLAlchemy
# from app.blueprints.dashboard import dashboard
# from app.blueprints.user import user
# from app.blueprints.api import api
# from app.blueprints.blog import blog
# from app.extensions import *
# # Setup Flask app and app.config
# app = Flask(__name__)
# app.config.from_object('app.settings')
# app.register_blueprint(dashboard)
# app.register_blueprint(user)
# app.register_blueprint(api)
# app.register_blueprint(blog)
#
# # from app.extensions import *
# db.init_app(app)
# from app import views
#
# # def create_app(config_filename):
# #     # Setup Flask app and app.config
# #     app = Flask(__name__)
# #     app.config.from_object('config')
# #     app.config['debug'] = True
# #     app.register_blueprint(dashboard)
# #     app.register_blueprint(user)
# #     app.register_blueprint(api)
# #     app.register_blueprint(blog)
# #
# #     # from app.extensions import *
# #     db.init_app(app)
# #     # from app import views
# #
# #     return app
