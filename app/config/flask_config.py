import os
from app.config.database import local_db_url


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = local_db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
