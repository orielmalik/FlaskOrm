import validators
import phonenumbers
from datetime import datetime


def validate_email(email):
    return validators.email(email)


def validate_gender(gender):
    return gender.lower() in ["male", "female"]


def date_to_string(date_obj):
    return date_obj.strftime("%Y-%m-%d %H:%M:%S")


def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date string format.")


def getTime():
    return datetime.now()


def validate_phone_number(phone_number, country_code):
    try:
        parsed_number = phonenumbers.parse(phone_number, country_code)
        if phonenumbers.is_valid_number(parsed_number):
            return True
        else:
            return False
    except phonenumbers.NumberParseException:
        return False

