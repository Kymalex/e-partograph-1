# app/home/views.py

# 3rd party imports
from flask import render_template

# local imports
from app.home import home

@home.route('/')
def index():
  return render_template('index.html', title='E-partograph')

@home.route('/about')
def about():
  return render_template('about.html', title='About')
