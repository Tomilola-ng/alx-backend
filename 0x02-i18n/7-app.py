#!/usr/bin/env python3

"""
    BARE BONES FLASK APP WITH FLASK-BABEL
"""

import pytz
from typing import Union, Dict

from flask_babel import Babel
from flask import (Flask, render_template,
                   request, g)


class Config:
    """
        RECOMMENDED FLASK BABEL SETTINGS
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

# USERS
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
        RETRIEVES A USER BASED ON A USER ID
    """
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None) # RETURNS A USER
    return None


@app.before_request
def before_request() -> None:
    """
        RUNS BASIC ROUTINES BEFORE EACH REQUEST'S RESOLUTION
    """
    user = get_user() # GETS A USER
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
        GET A WEB PAGE LOCALE
    """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]: # CHECKS IF THE LOCALE IS VALID
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    # GET A WEB PAGE LOCALE FROM A HEADER
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    # GET A WEB PAGE LOCALE FROM THE BABEL DEFAULT LOCALE
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """
        GET A WEB PAGE TIMEZONE
    """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone'] # GETS A USER TIMEZONE
    try:
        return pytz.timezone(timezone).zone
    # GET A WEB PAGE TIMEZONE FROM THE BABEL DEFAULT TIMEZONE
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def get_index() -> str:
    """
        THE NO PATH/INDEX PAGE
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # RUNS THE APP
