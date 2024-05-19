#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
Dispalys  Heloo hbnb
    """
    return 'Hello HBNB!'

=======

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


>>>>>>> 3992b821a4d1ce080a4c75b334d8e0f6f45e4963
if __name__ == "__main__":
    app.run(host="0.0.0.0")
