#!/usr/bin/env python3
"""
4-app module
"""

from flask_babel import Babel, gettext as _
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


@babel.localeselector
def get_locale() -> Any:
    """
    get_locale
    """
    loc = request.args.get('locale')
    if loc in LANGUAGES:
        return loc
    return request.accept_languages.best_match(LANGUAGES)


@app.route('/')
def index() -> Any:
    """
    renders the index template
    """
    return render_template('4-index.html')
