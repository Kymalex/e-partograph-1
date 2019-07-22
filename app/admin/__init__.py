# app/admin/__init__.py

# 3rd party imports
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views
