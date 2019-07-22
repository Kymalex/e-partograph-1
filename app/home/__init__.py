# app/home/__init__.py

# 3rd party imports
from flask import Blueprint

home = Blueprint('home', __name__)

# local imports
from . import views
