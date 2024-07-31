#!/usr/bin/env python3

"""
    BARE BONES FLASK APP WITH FLASK-BABEL
"""

import pytz
from typing import Union, Dict

from flask_babel import Babel, format_datetime
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
    login_id = request.args.get('login_as', '') # GETS A USER ID
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
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else f'{x}=').split('='),
        queries,
    )) # GETS A WEB PAGE LOCALE FROM QUERY STRING
    locale = query_table.get('locale', '') # GETS A WEB PAGE LOCALE FROM QUERY STRING
    if locale in app.config["LANGUAGES"]: # CHECKS IF THE LOCALE IS VALID
        return locale
    user_details = getattr(g, 'user', None) # GETS A USER
    if user_details and user_details['locale'] in app.config["LANGUAGES"]:
        return user_details['locale']
    # GET A WEB PAGE LOCALE FROM A HEADER
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]: # CHECKS IF THE LOCALE IS VALID
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
        return pytz.timezone(timezone).zone # RETURNS A WEB PAGE TIMEZONE
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def get_index() -> str:
    """
        THE NO PATH/INDEX PAGE
    """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # RUNS THE APP
