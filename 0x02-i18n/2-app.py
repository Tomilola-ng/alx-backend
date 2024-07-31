#!/usr/bin/env python3

"""
    A Basic Flask app.
"""

from flask_babel import Babel
from flask import (Flask, render_template,
                   request)

class Config:
    """
        RECOMMENDED FLASK BABEL SETTINGS
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
        GET A WEB PAGE LOCALE
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
        THE NO PATH/INDEX PAGE
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
