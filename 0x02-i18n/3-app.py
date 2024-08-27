#!/usr/bin/env python3
"""
0-app module
"""

from flask_babel import Babel
from flask import Flask, render_template, request
from typing import Any


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Our translation configuration
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index() -> Any:
    """
    renders the index template
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> Any:
    """
    get_locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
