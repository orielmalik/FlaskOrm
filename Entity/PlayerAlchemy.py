from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from Utils.FileUtils import *
from Utils.converter import string_to_date
Base = declarative_base()


class PlayerAlchemy(Base):
    __tablename__ = 'player'  # Table name in the database
    email = Column(String(230), primary_key=True, nullable=False)
    position = Column(String(230), nullable=False)
    speed = Column(Float, nullable=False)
    birth = Column(Date, nullable=False)
    type = Column(String(230), nullable=False)

    @classmethod
    def get_session(cls):
        # Assuming the connection string is stored in a variable called 'connection_string'
        engine = create_engine(readTextFile('connect.txt','Queries'))
        session_factory = sessionmaker(bind=engine)
        return session_factory()
