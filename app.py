from datetime import datetime
from flask import Flask, jsonify, request

from User import make_user
from Card import make_card_entry
from dbUtils import get_users_from_db, insert_card_into_db

app = Flask(__name__)


@app.route("/users")
def get_users():
    users = []
    for user in get_users_from_db():
        users.append(make_user(user))

    return jsonify({"users": users, "time": datetime.utcnow().isoformat(sep='-')})


@app.route("/cards", methods=["POST", "GET"])
def handle_cards():
    if request.method == "POST":
        card_info, err = make_card_entry(request.json)
        if err:
            return jsonify(card_info), 521
        else:
            insert_card_into_db(card_info)
            return jsonify({ "msg": "OK"})


if __name__ == '__main__':
    app.run(threaded=True, port=5000)