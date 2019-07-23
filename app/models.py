# models.py

# inbuilt imports
from datetime import datetime
from uuid import uuid4
from random import randint

# 3rd party imports
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from random import seed
import forgery_py

# local imports
from app import db

class Nurse(db.Model):
  '''
  create nurses table
  '''

  __tablename__ = 'nurses'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  emp_id = db.Column(db.String(64), nullable=False, default=uuid4().hex)
  firstname = db.Column(db.String(32), nullable=False)
  lastname = db.Column(db.String(32), nullable=False)
  email = db.Column(db.String(64), nullable=False)
  phone_no = db.Column(db.String(64))
  password_hash = db.Column(db.String(255), nullable=False)
  is_admin = db.Column(db.Boolean, default=False)
  created_at = db.Column(db.DateTime, default = datetime.utcnow())

  def __init__(self, firstname, lastname, email, phone_no, password):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.phone_no = phone_no
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    '''
    verify nurses password
    '''

    return check_password_hash(self.password_hash, password)

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def generate_fake(count=5):
    seed()
    for i in range(count):
      nurse = Nurse(
        firstname=forgery_py.internet.user_name(),
        lastname=forgery_py.internet.user_name(),
        email=forgery_py.internet.email_address(),
        phone_no = forgery_py.address.phone(),
        password=forgery_py.lorem_ipsum.word(),
      )
      db.session.add(nurse)
      try:
        db.session.commit()
      except IntegrityError as e:
        db.session.rollback()

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

  @staticmethod
  def generate_fake():
    seed()
    wards = Ward.query.count()
    ward = Ward.query.offset(randint(0, wards - 1)).first()
    patient = Patient(
      firstname = forgery_py.name.first_name(),
      lastname = forgery_py.name.last_name(),
      dob = forgery_py.date.date(),
      phone_no = forgery_py.address.phone(),
      email = forgery_py.internet.email_address(),
      id_no = forgery_py.date.day(),
      nhif_no = forgery_py.address.street_number(),
      ward_id = ward.id
    )
    db.session.add(patient)
    try:
      db.session.commit()
    except IntegrityError as e:
      db.session.rollback()

  def __repr__(self):
    return '<Patient: {}>'.format(self.id)

class Ward(db.Model):
  '''
  create wards table
  '''

  __tablename__ = 'wards'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(64), nullable=False)
  beds = db.Column(db.Integer)
  nurse_id = db.Column(db.Integer, db.ForeignKey('nurses.id'))
  created_at = db.Column(db.DateTime, default=datetime.utcnow())

  def __init__(self, name, beds, nurse_id):
    self.name = name
    self.beds = beds
    self.nurse_id = nurse_id

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def generate_fake(count=5):

    seed()
    nurses = Nurse.query.count()
    nurse = Nurse.query.offset(randint(0, nurses - 1)).first()
    ward = Ward(
      name = forgery_py.name.industry(),
      beds = forgery_py.date.day(),
      nurse_id = nurse.id
    )
    db.session.add(ward)
    try:
      db.session.commit()
    except IntegrityError as e:
      db.session.rollback()

  def __repr__(self):
    return '<Ward: {}>'.format(self.id)

class Record(db.Model):
  '''
  create records table
  '''

  __tablename__ = 'records'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  full_blood_count = db.Column(db.String(64))
  patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
  created_at = db.Column(db.DateTime, default=datetime.utcnow())

  def __init__(self, patient_id):
    self.patient_id = patient_id

  def save(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return '<Record: {}>'.format(self.id)
