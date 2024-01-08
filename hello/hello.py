from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h2>This is the homepage of my flask app.</h2>"

@app.route("/<name>")
def print_name(name):
    return f"your name is: {escape(name)}"
# this type of url is used to bind a fucntion with the url dynamically

