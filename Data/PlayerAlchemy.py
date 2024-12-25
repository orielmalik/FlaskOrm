from sqlalchemy import create_engine, Column, Integer, String,Date,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def PlayerAlchemy(base):
    __tablename__ = 'player'
    email = Column("email", String(230), primary_key=True, nullable=False)
    position = Column("position", String(230), nullable=False)
    speed = Column("speed", Float, nullable=False)
    birth = Column("birth", Date, nullable=False)
    type = Column("type", String(230), nullable=False)


