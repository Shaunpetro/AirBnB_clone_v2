#!/usr/bin/python3
"""starts a flusk web app"""
from flask import Flusk

app = Flusk(__name__)


@app.route('/', strict_slashes=False)
def home():
    """

    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
