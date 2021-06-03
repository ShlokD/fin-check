from datetime import datetime

from flask import Flask, jsonify, request

from Card import make_card_entry, make_card
from User import make_user, make_user_entry
from dbUtils import *

app = Flask(__name__)


@app.route("/users", methods=["POST", "GET"])
def handle_users():
    if request.method == "GET":
        users = []
        for user in get_users_from_db():
            users.append(make_user(user))

        return jsonify({"users": users, "time": datetime.utcnow().isoformat(sep='-')})
    elif request.method == "POST":
        user_info = make_user_entry(request.json)
        insert_user_into_db(user_info)
        return jsonify({"msg": "OK"})


@app.route("/cards", methods=["POST", "GET"])
def handle_cards():
    if request.method == "POST":
        card_info, err = make_card_entry(request.json)
        if err:
            return jsonify(card_info), 521
        else:
            insert_card_into_db(card_info)
            return jsonify({"msg": "OK"})
    elif request.method == "GET":
        cards = []
        users = {}
        cards_assigned_to = []
        for card in get_cards_from_db():
            cards.append(make_card(card))
            cards_assigned_to.append(card["assignedTo"])
        for user in get_users_by_ids(cards_assigned_to):
            users[user["id"]] = make_user(user)
        return jsonify({"cards": cards, "users": users, "time": datetime.utcnow().isoformat(sep='-')})


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
