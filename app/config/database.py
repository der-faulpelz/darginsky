from sqlalchemy import create_engine, select, Table, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://b2dc52e90f0871:db613689@eu-cdbr-west-02.cleardb.net/heroku_01913328053f6da", convert_unicode=True)
connection = engine.connect()
metadata = MetaData()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
