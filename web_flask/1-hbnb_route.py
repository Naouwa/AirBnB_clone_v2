#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """It displays the message 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """It displays the message 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)