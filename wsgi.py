from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


with app.test_request_context():
    print(url_for("hello_world"))
