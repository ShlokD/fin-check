from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"msg": "Namaste Samsara", "time": datetime.utcnow().isoformat(sep='-')})

if __name__ == '__main__':
   app.run(threaded=True, port=5000)