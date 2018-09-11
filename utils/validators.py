from django.core.exceptions import ValidationError
import re


def phone_validation(phone_number):
    if not re.match(r'^\+\d{9,13}$', phone_number):
        raise ValidationError("Phone number must be entered in the format: '+999999999'. Up to 13 digits are allowed!")


def first_name_validation(first_name):
    if not re.match(r'^[a-zA-Z]+\s?[a-zA-Z]+\s?[a-zA-Z]+$', first_name):
        raise ValidationError("First name should consist of latin letters whereas a single space is allowed")


def last_name_validation(last_name):
    if not re.match(r'^[a-zA-Z]+[-]?[a-zA-Z]+$', last_name):
        raise ValidationError("Last name should consist of latin letters whereas a single dash (-) is allowed")