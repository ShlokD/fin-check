import random
import string


def make_user(entry):
    return {
        "name": entry["name"]
    }


def make_autogenerate_id(length):
    id = ''
    for value in range(length):
        if value == 0:
            id += random.choice(string.ascii_uppercase)
        else:
            id += random.choice(string.digits)
    return id


def make_user_entry(entry):
    return {
        "id": make_autogenerate_id(6),
        "name": entry["name"].title(),
        "department":entry["department"].title(),
        "location": entry["location"].title()
    }
