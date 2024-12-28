import json
from datetime import datetime

from Entity.PlayerAlchemy import PlayerAlchemy,AlchemyEncoder
from Utils.Validation import *
from Entity.Player import *


def fromTuple(myTuple: tuple):
    return Player(myTuple[0], myTuple[1], myTuple[2], myTuple[3], myTuple[4])

def string_to_date(date_string):
    """
    Converts a string representing a date to a datetime object.

    Args:
        date_string: A string representing the date.
                     Supports formats like 'YYYY-MM-DD', etc.

    Returns:
        datetime: A datetime object representing the date.

    Raises:
        ValueError: If the date_string cannot be parsed.
        TypeError: If the input is not a string.
    """
    if not isinstance(date_string, str):
        raise TypeError("date_string must be a string")

    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date string format.")


def from_json(json_data, required_fields,type=''):
    if isinstance(json_data, dict):
        # If json_data is already a dictionary, no need to load it
        data = json_data
    elif isinstance(json_data, str):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
    else:
        raise TypeError("json_data must be a dictionary or a string")

    if not isinstance(required_fields, list) or not isinstance(data['speed'],float):
        raise ValueError("err")

    for field in required_fields:
        if field not in data:
            print(field)
            raise ValueError(f"Missing field: {field}")

    try:
        birth_date = string_to_date(data['birth'])
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error parsing birthdate: {e}")


    if type is 'alch':
        return  PlayerAlchemy(
    email=data['email'],
    position=data['position'],
    speed=data['speed'],
    birth=birth_date,
    type=data['speed']
)

    else:
        return Player(
            email=data['email'],
            speed=data['speed'],
            position=data['position'],
            birth=birth_date,
            type=data['type']
        )




