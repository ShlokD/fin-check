import os

from pymongo import MongoClient


def connect_to_db():
    db_conn = os.environ["ATLAS_URI"]
    client = MongoClient(db_conn, ssl=True, ssl_cert_reqs="CERT_NONE")
    db = client["fin-check"]
    return db, client


def get_employees_from_db(condition={}):
    db, client = connect_to_db()
    employees_from_db = db.users.find(condition)
    client.close()
    return employees_from_db


def get_employees_by_ids(emp_ids):
    condition = {"id": {"$in": emp_ids}}
    return get_employees_from_db(condition)


def get_cards_from_db():
    db, client = connect_to_db()
    cards_from_db = db.cards.find()
    client.close()
    return cards_from_db


def insert_card_into_db(card):
    db, client = connect_to_db()
    db.cards.insert_one(card)
    client.close()


def insert_employee_into_db(employee):
    db, client = connect_to_db()
    db.users.insert_one(employee)
    client.close()
