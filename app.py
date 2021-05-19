from datetime import datetime
from flask import Flask, jsonify

from User import make_user
from dbUtils import get_users_from_db

app = Flask(__name__)

@app.route("/")
def index():
    users = []
    for user in get_users_from_db():
        users.append(make_user(user))

    return jsonify({"users": users, "time": datetime.utcnow().isoformat(sep='-')})


if __name__ == '__main__':
   app.run(threaded=True, port=5000)