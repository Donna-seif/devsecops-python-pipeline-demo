from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return "AppSec Pipeline Demo is Running!"

@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    # Safe: Jinja2 auto-escapes {{ name }} and satisfies Semgrep's template rules
    return render_template_string("<h1>Hello, {{ name }}!</h1>", name=name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)