from sqlalchemy import create_engine, select, Table, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://b2dc52e90f0871:db613689@eu-cdbr-west-02.cleardb.net/heroku_01913328053f6da"), convert_unicode=True)
connection = engine.connect()
metadata = MetaData()

#db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
#Base.query = db_session.query_property()

#class Query(table_name):
#    q_tab = Table(table_name, metadata, autoload=True, autoload_with=engine)
#    sel_tab = select([q_tab])
#    my_query = sel_tab.where(q_tab.columns.translation_rus="абаз")
#    connection.execute(my_query).fetchall()
