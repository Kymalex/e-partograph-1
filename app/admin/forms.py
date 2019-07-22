# app/admin/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

# local imports
from app.models import Nurse

class CreateNurseForm(FlaskForm):
  '''
  Form to create a new nurse
  '''

class CreateWardForm(FlaskForm):
  '''
  Form to create a new Ward
  '''
