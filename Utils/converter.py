import json
from datetime import datetime

from Entity.PlayerAlchemy import PlayerAlchemy, AlchemyEncoder
from Utils.Validation import *
from Entity.Player import *


def fromTuple(myTuple: tuple):
    return Player(myTuple[0], myTuple[1], myTuple[2], myTuple[3], myTuple[4])


from datetime import datetime
import json

def string_to_date(date_string):
    """
    Converts a string representing a date to a datetime object.
    Returns a date in 'YYYY-MM-DD' format or an error message.

    Args:
        date_string: A string representing the date.
                     Supports formats like 'YYYY-MM-DD', etc.

    Returns:
        str: A formatted string representing the date 'YYYY-MM-DD',
             or an error message if the date format is invalid.
    """
    if not isinstance(date_string, str):
        raise TypeError("date_string must be a string")

    try:
        # Try to parse the date in the format YYYY-MM-DD
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.strftime("%Y-%m-%d")  # Return in desired format
    except ValueError:
        # If there's an error in parsing, return the original string or a default error message
        return "Invalid date format"


def from_json(json_data, required_fields, type=''):
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

    if not isinstance(required_fields, list) or not isinstance(data.get('speed'), float):
        raise ValueError("err")

    for field in required_fields:
        if field not in data:
            print(field)
            raise ValueError(f"Missing field: {field}")

    # Use the string_to_date function to format the birth date
    birth_date = string_to_date(data['birth'])
    if birth_date == "Invalid date format":
        raise ValueError(f"Error parsing birthdate: Invalid date format")

    if type == 'alch':
        return PlayerAlchemy(
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

def from_tuple(tup,player_type=''):
        email = tup[0]
        birth_string = tup[1]  # Birthdate is expected in string format (e.g., "YYYY-MM-DD")
        position = tup[2]
        speed = tup[3]

        # Convert birthdate using string_to_date function
        birth_date = string_to_date(birth_string)
        if birth_date == "Invalid date format":
            raise ValueError(f"Invalid birthdate format for email {email}: {birth_string}")

        # Assuming the type determines which object to return
        if player_type == 'alch':
            return PlayerAlchemy(
                email=email,
                position=position,
                speed=speed,
                birth=birth_date,
                type=player_type
            )
        else:
            return Player(
                email=email,
                position=position,
                speed=speed,
                birth=birth_date,
                type=player_type
            )
