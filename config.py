import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'add your DB con URI'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
