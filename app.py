from datetime import datetime
from flask import Flask, jsonify
from pymongo import MongoClient
import os
from User import make_user

app = Flask(__name__)


def connect_to_db():
    db_conn = os.environ["ATLAS_URI"]
    client = MongoClient(db_conn)
    db = client["fin-check"]
    return db


def get_users_from_db():
    db = connect_to_db()
    users_from_db = db.users.find()
    return users_from_db


@app.route("/")
def index():
    users = []
    for user in get_users_from_db():
        users.append(make_user(user))

    return jsonify({"users": users, "time": datetime.utcnow().isoformat(sep='-')})


if __name__ == '__main__':
   app.run(threaded=True, port=5000)