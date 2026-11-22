from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "AppSec Pipeline Demo is Running!"

@app.route("/greet")
def greet():
    # Safe: escape() converts characters like <, >, and & into safe HTML entities
    name = escape(request.args.get("name", "Guest"))
    return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)