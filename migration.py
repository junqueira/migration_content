from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tests import *
from datetime import datetime

Base = declarative_base()
engine = create_engine('mysql://admin:admin@localhost:3306/new_schema')

class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descricao = Column(String)
    texto = Column(String)
    data = Column(String)

    # def __init__(self, transmogrifier, **kwargs):
    #     DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"
    #     engine = create_engine(DB_URI.format(
    #       user ='admin',
    #       password = 'admin',
    #       host = 'localhost',
    #       db = 'new_schema'), connect_args = {'time_zone': '+00:00'}
    #     )

    def incluir_content(self):
        Session = sessionmaker()
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)
        for content in contents:
            session = Session()
            content = Content(
                                id= content['id'],
                                titulo= content['titulo'],
                                descricao= content['descricao'],
                                texto= content['texto'],
                                data= content['data']
                            )
            session.add(content)
            session.commit()