from Data.mongodb import *
from Entity import Player


class MongoService:
    def __init__(self,monodb):
        if isinstance(monodb, MongoDB):
            self.db = monodb.db()
        else:
            raise TypeError("")








