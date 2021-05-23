import random
import string

def make_user(entry):
    return {
        "name": entry["name"]
    }


def make_user_entry(entry):
    id = make_autogenerate_id(6)
    db_data = {
    "id": id,
    "name": entry["name"].title(),
    "department":entry["department"].title(),
    "location": entry["location"].title()
    }
    return db_data

def make_autogenerate_id(length):
    id =''
    for value in range(length):
        if value == 0:
            id += random.choice(string.ascii_uppercase)
        else:
            id += random.choice(string.digits)
    print(id)
    return id