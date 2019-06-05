import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('mysql://root:password@localhost/drg3') #or \
#                              'sqlite:///' + os.path.join(basedir, 'app.db')

#    SQLALCHEMY_DATABASE_URI = "sqlite:///C:\\Users\\vaio\\Downloads\\drg3.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False