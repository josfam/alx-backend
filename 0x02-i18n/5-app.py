#!/usr/bin/env python3

"""A basic flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Configs for Flask-Babel"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@app.before_request
def before_request():
    """Fetch the correct user before each request"""
    g.user = get_user()

def get_user():
    """Fetch the user that is trying to log in from the mock dictionary"""
    user_id = request.args.get('login_as')
    if (user_id):
        return users.get(int(user_id))
    return None

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
    return render_template('5-index.html', locale=get_locale())


if __name__ == '__main__':
    app.run()
