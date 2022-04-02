from datetime import datetime

from flask import Flask, jsonify, request, send_file, send_from_directory

from Card import make_card_entry, make_card
from Employee import *
from dbUtils import *

app = Flask(__name__)

whitelist = ["http://localhost:3000"]

@app.route("/")
def handle_index():
    return send_file("./ui/build/index.html")


@app.route("/static/<asset>/<filename>")
def handle_js(asset, filename):
    return send_file(f"./ui/build/static/{asset}/{filename}")

@app.route("/<filename>.png")
def handle_images(filename):
    return send_file(f"./ui/build/static/images/{filename}.png")

@app.route("/employees", methods=["POST", "GET"])
def handle_employees():
    if request.method == "GET":
        employees = []
        for employee in get_employees_from_db():
            employees.append(make_employee(employee))

        return jsonify({"employees": employees, "time": datetime.utcnow().isoformat(sep='-')})
    elif request.method == "POST":
        emp_info = make_employee_entry(request.json)
        insert_employee_into_db(emp_info)
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
        employees= {}
        cards_assigned_to = []
        for card in get_cards_from_db():
            cards.append(make_card(card))
            cards_assigned_to.append(card["assignedTo"])
        for employee in get_employees_by_ids(cards_assigned_to):
            employees[employee["id"]] = make_employee(employee)
        return jsonify({"cards": cards, "employees": employees, "time": datetime.utcnow().isoformat(sep='-')})


@app.after_request
def add_cors_header(response):
    if request.referrer:
        referrer = request.referrer[:-1]
        if referrer in whitelist:
            response.headers.add("Access-Control-Allow-Origin", referrer)
            response.headers.add("Access-Control-Allow-Methods", "GET,POST,OPTIONS,HEAD")
        return response
    else:
        return response


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
