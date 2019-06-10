import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# server side
if os.environ.get("SERVER"):
    db_url = "eu-cdbr-west-02.cleardb.net"
    db_name = "heroku_53199c23d12784e"
    db_user = "b459a0d52487c1"
    db_password = "5ff65131"

else:  # local dev
    db_url = 'localhost:3306'
    db_name = 'drg3'
    db_user = 'root'
    db_password = 'password'

local_db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_url}/{db_name}"

engine = create_engine(local_db_url, pool_pre_ping=True)
connection = engine.connect()
# metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
