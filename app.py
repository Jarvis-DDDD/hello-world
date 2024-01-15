import json
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def auth():
    name = request.args.get("name",'')
    return jsonify({'result': name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)