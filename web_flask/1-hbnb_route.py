#!/usr/bin/python3
"""
Script starting Flask web app with two routes
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Print hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Print hbnb"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
