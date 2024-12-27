#SqlAchemy Service
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from Utils.const import *

from Entity.PlayerAlchemy import PlayerAlchemy
from Utils.Validation import *
from Utils.FileUtils import *
from Entity import Player
from Utils.converter import *


class AlchemyService:

    def __init__(self):
        self.server = PlayerAlchemy.get_session()

    def getServer(self):
        return self.server

    def raise_Error(self, target,type,message):
        if not isinstance(target, type) or not isinstance(message, str):
            raise TypeError(message)

    def getPlayers(self, que):
        self.raise_Error(self.server, Session,"error")
        return self.server.query(que)

    def createPlayer(self, target):
       # if not isinstance(target, tuple) or not isinstance(self.server, Session):
            #raise TypeError("error")
        self.raise_Error(self.server, Session,"error")
        if not target['email'] or not validate_email(target['email']):
            raise TypeError("error")
        try:
            self.server.add(from_json(target),req_fields)
            self.server.commit()
            return self.server.get(target['email'])
        except SQLAlchemyError as e:
             raise TypeError(str(e))

    def updatePlayer(self, target):
        self.raise_Error(self.server, Session, "error")
        if not target['email'] or not validate_email(target['email']) or not self.server.get(target['email']):
            raise TypeError("error")
        self.server.merge(from_json(target,req_fields))
        self.server.commit()
        return self.server.get(target['email'])

    def deletePlayer(self, target):
        self.raise_Error(self.server, Session, "error")
        self.raise_Error(target, str, "error")
        if not validate_email(target['email']) or not self.server.get(target['email']):
            raise TypeError("error")
        self.server.delete(target)
        self.server.commit()












