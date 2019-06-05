import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('mysql://b2dc52e90f0871:db613689@eu-cdbr-west-02.cleardb.net/heroku_01913328053f6da')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
