# app/__init__.py

# 3rd party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# local imports
from config import app_config

db = SQLAlchemy()
boostrap = Bootstrap()
login_manager = LoginManager()

def create_app(env_name):

  app = Flask(__name__)
  app.config.from_object(app_config[env_name])

  db.init_app(app)

  migrate = Migrate(app=app, db=db)

  boostrap.init_app(app)
  login_manager.init_app(app)

  login_manager.login_view = 'admin.login'
  login_manager.login_message = 'User verification is required to access this page'

  # import app models
  from app.models import Nurse, Patient, Ward, Record

  # flask shell
  @app.shell_context_processor
  def make_shell_context():
    return dict(app=app, db=db, nurse=Nurse, patient=Patient, ward=Ward, record=Record)

  # register blueprints
  from app.home import home as home_blueprint
  app.register_blueprint(home_blueprint)

  from app.admin import admin as admin_blueprint
  app.register_blueprint(admin_blueprint)

  return app
