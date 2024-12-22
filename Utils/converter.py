import json
from datetime import datetime
from Utils.Validation import *
from Entity.Player import *


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


def from_json(json_data, required_fields):
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

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    try:
        birth_date = string_to_date(data['birth'])
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error parsing birthdate: {e}")

    return Player(
        email=data['email'],
        speed=data['speed'],
        position=data['position'],
        birth=birth_date,
        type=data['type']
    )
