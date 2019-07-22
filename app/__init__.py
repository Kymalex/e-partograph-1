# app/__init__.py

# 3rd party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

db = SQLAlchemy()

def create_app(env_name):

  app = Flask(__name__)
  app.config.from_object(app_config[env_name])

  db.init_app(app)

  migrate = Migrate(app=app, db=db)

  from app.home import home as home_blueprint
  app.register_blueprint(home_blueprint)

  from app.admin import admin as admin_blueprint
  app.register_blueprint(admin_blueprint)

  return app
