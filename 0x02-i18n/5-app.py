#!/usr/bin/env python3
"""
5-app module - Flask application
"""

from flask_babel import Babel, gettext as _
from flask import Flask, render_template, request, g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Any:
    """
    returns a user dictionary or None if the ID cannot
    be found or if login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> Any:
    """
    use get_user to find a user if any, and set it as a global
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> Any:
    """
    get_locale - returns the best match with our supported languages
    """
    loc = request.args.get('locale')
    if loc in Config.LANGUAGES:
        return loc
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index() -> Any:
    """
    index - renders the index template
    """
    return render_template('5-index.html')
