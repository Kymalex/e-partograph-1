# app/admin/forms.py

# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo

# local imports
from app.models import Nurse, Ward

class CreateNurseForm(FlaskForm):
  '''
  Form to create a new nurse
  '''
  firstname = StringField('First Name: ', validators=[DataRequired()])
  lastname = StringField('Last Name: ', validators=[DataRequired()])
  email = StringField('Email: ', validators=[DataRequired(), Email()])
  phone_no = StringField('Phone No: ', validators=[DataRequired()])
  password = PasswordField('Password: ', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(), EqualTo(password)])
  create = SubmitField('Create Nurse')

class AuthenticateNurseForm(FlaskForm):
  '''
  Form to authenticate a nurse
  '''
  email = StringField('Email: ', validators=[DataRequired(), Email()])
  password = PasswordField('Password: ', validators=[DataRequired()])
  login = SubmitField('Login')

class CreateWardForm(FlaskForm):
  '''
  Form to create a new Ward
  '''
  name = StringField('Ward Name: ', validators=[DataRequired()])
  beds = StringField('Beds No.: ', validators=[DataRequired()])
  nurse_id = QuerySelectField(query_factory=lambda: Nurse.query.all(), get_label='firstname')
  create = SubmitField('Create Ward')

class CreatePatientForm(FlaskForm):
  '''
  Form to create a new patient
  '''

  firstname = StringField('First Name: ', validators=[DataRequired()])
  lastname = StringField('Last Name: ', validators=[DataRequired()])
  dob = StringField('Date Of Birth: ', validators=[DataRequired()])
  phone_no = StringField('Phone No.: ', validators=[DataRequired()])
  email = StringField('Email: ', validators=[Email()])
  id_no = StringField('ID No.: ')
  nhif_no = StringField('NHIF No.: ')
  ward_id = QuerySelectField(query_factory=lambda: Ward.query.all(), get_label='name')
  create = SubmitField('Create Patient')
