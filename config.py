import os

class Config(object):
    BASE_URI = './'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
