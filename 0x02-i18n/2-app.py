#!/usr/bin/env python3
"""
0-app module
"""

from flask import Flask, render_template, request
from typing import Any
from flask_babel import Babel


app = Flask(__name__)


@app.route("/")
def hello() -> Any:
    """
    renders the index template
    """
    return render_template('0-index.html')


class Config:
    """
    Our translation configuration
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

def get_locale() -> Any:
    """
    get_locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app)
