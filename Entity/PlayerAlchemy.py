from sqlalchemy import create_engine, Column, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
from Utils.FileUtils import *

Base = declarative_base()


# דוגמת מחלקת PlayerAlchemy כפי שהצגת
class PlayerAlchemy(Base):
    __tablename__ = 'player'
    email = Column(String(230), primary_key=True, nullable=False)
    position = Column(String(230), nullable=False)
    speed = Column(Float, nullable=False)
    birth = Column(Date, nullable=False)
    type = Column(String(230), nullable=False)


    @classmethod
    def get_session(cls):
        engine = create_engine((readTextFile('connect.txt').split('\n')[0]))
        session_factory = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)
        return session_factory()


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields
        return json.JSONEncoder.default(self, obj)
