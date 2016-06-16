from flask import Flask, render_template, request, jsonify
from random import choice
from collections import defaultdict
import os
app = Flask(__name__)


names = defaultdict(list)
path = os.path.abspath(__file__) + "/adjectives.txt"
with open(path, "r") as f:
    adjectives = [line.strip() for line in f]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greeting", methods=["POST"])
def greeting():
    name = request.data["name"]
    if name not in names:
        names[name] = choice(adjectives)

    greeting = "Рад тебя видеть снова, " + names[name] + name
    return jsonify({"name":name, "greeting":greeting})

if __name__ == "__main__":
    app.run

