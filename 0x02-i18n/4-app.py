#!/usr/bin/env python3

"""A basic flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configs for Flask-Babel"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determines the best language to use in the application"""
    # use the detected locale, otherwise, choose the best match
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def home():
    """Displays the homepage"""
    return render_template('4-index.html', locale=get_locale())


if __name__ == '__main__':
    app.run()
