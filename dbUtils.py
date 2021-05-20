from pymongo import MongoClient
import os

def connect_to_db():
    db_conn = os.environ["ATLAS_URI"]
    client = MongoClient(db_conn)
    db = client["fin-check"]
    return db, client


def get_users_from_db():
    db, client = connect_to_db()
    users_from_db = db.users.find()
    client.close()
    return users_from_db


def insert_card_into_db(card):
    db, client = connect_to_db()
    db.cards.insert_one(card)
    client.close()
