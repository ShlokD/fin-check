from datetime import datetime
from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)


def connect_to_db():
    db_conn = os.environ["ATLAS_URI"]
    client = MongoClient(db_conn)
    db = client["fin-check"]
    return db

@app.route("/")
def index():
    db = connect_to_db()
    users_from_db = db.users.find()
    users = []
    for user in users_from_db:
        users.append({"name": user["name"]})

    return jsonify({"users": users, "time": datetime.utcnow().isoformat(sep='-')})


if __name__ == '__main__':
   app.run(threaded=True, port=5000)