# SqlAchemy Service
from sqlalchemy import JSON, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from Utils.const import *

from Entity.PlayerAlchemy import PlayerAlchemy
from Utils.Validation import *
from Utils.FileUtils import *
from Entity import Player
from Utils.converter import *
from Utils.log import logg
from Utils.log.logg import printer


def to_dict(selfi):
    return {
        "email": selfi.email,
        "position": selfi.position,
        "speed": selfi.speed,
        "birth": selfi.birth.isoformat() if selfi.birth else None,
        "type": selfi.type,
    }


class AlchemyService:

    def __init__(self):
        self.server = PlayerAlchemy.get_session()

    def getServer(self):
        return self.server

    def raise_Error(self, target, type, message):
        if not isinstance(target, type) or not isinstance(message, str):
            raise TypeError(message)

    def getPlayers(self, que):
        self.raise_Error(self.server, Session, "error")
        return self.server.query(que)

    def create_player(self,target):
        try:
            player = from_json(target, req_fields, type='alch')
            player_dict = to_dict(player)

            if not validate_email(player_dict['email']):
                raise TypeError("Invalid email")
            existing_player = self.server.query(PlayerAlchemy).filter_by(email=player_dict['email']).first()
            if existing_player is not None:
                raise TypeError("Player already exists")

            new_player = PlayerAlchemy(**player_dict)
            self.server.add(new_player)
            printer(f"added new player: {new_player}")

            self.server.commit()
            printer(f"commit")

            result = self.server.get(PlayerAlchemy,player_dict['email'])

            if result is None:
                printer(f"No player found with email: {player_dict['email']}","ERROR")

                raise ValueError(f"No player found with email: {player_dict['email']}")

            # Serialize using AlchemyEncoder
            return json.dumps(result, cls=AlchemyEncoder)
        except (SQLAlchemyError, TypeError) as e:
            printer(f"Error: {str(e)}","ERROR")
            raise TypeError("An error occurred while adding the player")

    def updatePlayer(self, target):
        self.raise_Error(self.server, Session, "error")
        if not target['email'] or not validate_email(target['email']) or not self.server.get(target['email']):
            printer(f"Error","ERROR")
            raise TypeError("error")
        self.server.merge(from_json(target, req_fields))
        self.server.commit()
        printer(f"commit" )


        return self.server.get(target['email'])

    def deletePlayer(self, target):
        self.raise_Error(self.server, Session, "error")
        self.raise_Error(target, str, "error")
        if not validate_email(target['email']) or not self.server.get(target['email']):
            raise TypeError("error")
        self.server.delete(target)
        printer(f"deleted: {target['email']}")
        self.server.commit()
        printer(f"commit")

    def deletePlayers(self,query):
        self.server.execute(text(str(query)))
        self.server.commit()
        printer(f"deleteds:")


