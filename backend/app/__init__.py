from flask import Flask

from .url_shortener import url_shortener


def create_app():
    app = Flask(__name__)

    app.register_blueprint(url_shortener, url_prefix="/urls")

    return app