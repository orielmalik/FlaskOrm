import json
from datetime import date
from Utils.Validation import *


class Player:
    def __init__(self, email, position, speed, birth, type):
        self.__email = email
        self.__position = position
        self.__speed = speed
        self.__birth = birth
        self.__type = type

    def to_json(self):
        try:
            birth_date = string_to_date(self.__birth)
            birth_str = birth_date.strftime("%Y-%m-%d")  # Format date for JSON
        except (TypeError, ValueError) as e:
            raise ValueError(f"Error converting birth date: {e}")

        return json.dumps({
            "email": self.__email,
            "position": self.__position,
            "speed": self.__speed,
            "birth": birth_str,
            "type": self.__type
        })

    def to_tuple(self):  # email, position, speed, birth, type)
        return self.__email, self.__position, self.__speed, self.__birth, self.__type

    def fromTuple(myTuple: tuple):
        return Player(myTuple[0], myTuple[1], myTuple[2], myTuple[3], myTuple[4])

    def setByOption(self, opt, value):
        if not isinstance(value, str):
            raise ValueError(f"err")
        if opt == 'birth':
            try:
                self.__birth = string_to_date(value)
            except ValueError as e:
                raise ValueError(f"err")
        elif opt == 'position':
            self.__position = value
        elif opt == 'type':
            self.__type = value
        elif opt == 'speed':
            self.__speed = value
        else:
            raise ValueError(f"err")
