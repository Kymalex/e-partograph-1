# models.py

# inbuilt imports
from datetime import datetime

# 3rd party imports
from werkzeug.security import generate_password_hash, check_password_hash

# local imports
from app import db

class Nurse(db.Model):
  '''
  create nurses table
  '''

  __tablename__ = 'nurses'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  emp_id = db.Column(db.String(32), nullable=False)
  firstname = db.Column(db.String(32), nullable=False)
  lastname = db.Column(db.String(32), nullable=False)
  password_hash = db.Column(db.String(255), nullable=False)
  is_admin = db.Column(db.Boolean, default=False)
  created_at = db.Column(db.DateTime, default = datetime.utcnow())

  def __init__(self, emp_id, firstname, lastname, password):
    self.emp_id = emp_id
    self.firstname = firstname
    self.lastname = lastname
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    '''
    verify nurses password
    '''

    return check_password_hash(self.password_hash, password)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return '<Nurse: {}>'.format(self.emp_id)

class Patient(db.Model):
  '''
  create patients table
  '''

  __tablename__ = 'patients'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  firstname = db.Column(db.String(32), nullable=False)
  lastname = db.Column(db.String(32), nullable=False)
  dob = db.Column(db.DateTime)
  phone_no = db.Column(db.String(32))
  email = db.Column(db.String(64), unique=True)
  id_no = db.Column(db.Integer)
  nhif_no = db.Column(db.String(64))
  ward_id = db.Column(db.Integer, db.ForeignKey('wards.id'))
  created_at = db.Column(db.DateTime, default=datetime.utcnow())

  def __init__(self, firstname, lastname, dob, phone_no, email, id_no, nhif_no, ward_id):
    self.firstname = firstname
    self.lastname = lastname
    self.dob = dob
    self.phone_no= phone_no
    self.email = email
    self.id_no = id_no
    self.nhif_no = nhif_no
    self.ward_id = ward_id

  def save(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return '<Patient: {}>'.format(self.id)

class Ward(db.Model):
  '''
  create wards table
  '''

  __tablename__ = 'wards'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(64), nullable=False)
  beds = db.Column(db.Integers)
  nurse_id = db.Column(db.Integer, db.ForeignKey('nurses.id'))
  created_at = db.Column(db.DateTime, default=datetime.utcnow())

  def __init__(self, name, beds, nurse_id):
    self.name = name
    self.beds = beds
    self.nurse_id = nurse_id

  def save(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return '<Ward: {}>'.format(self.id)

class Record(db.Model):
  '''
  create records table
  '''

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
  created_at = db.Column(db.DateTime, default=datetime.utcnow())

  def __init__(self, patient_id):
    self.patient_id = patient_id

  def save(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return '<Record: {}>'.format(self.id)
