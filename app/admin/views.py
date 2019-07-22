# app/admin/views.py

# 3rd party imports
from flask import render_template

# local imports
from app.admin import admin
from app.models import Nurse, Ward

@admin.route('/create-nurse', methods=['GET', 'POST'])
def create_nurse():
  '''
  creates a new Nurse
  '''

@admin.route('/create-ward', methods=['GET', 'POST'])
def create_ward():
  '''
  creates a new Ward
  '''

@admin.route('/dashboard')
def dashboard():
  '''
  create a new Dashboard
  '''
