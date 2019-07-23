# config.py

# inbuilt imports
import os

class Config(object):
  '''
  global environment configurations
  '''

  DEBUG = False
  TESTING = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False
  SECRET_KEY = os.getenv('SECRET_KEY')

class DevelopmentConfig(Config):
  '''
  development environment configurations
  '''

  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
  SQLALCHEMY_ECHO = True

class TestingConfig(Config):
  '''
  testing environment configurations
  '''

  TESTING = True

class ProductionConfig(Config):
  '''
  production environment configurations
  '''

app_config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig,
  'production': ProductionConfig,
}
