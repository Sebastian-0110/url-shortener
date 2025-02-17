from flask import Flask, jsonify

from .exceptions.domain_exception import DomainException
from .url_shortener import url_shortener
from .db import close_db

def create_app():
    app = Flask(__name__)

    app.register_blueprint(url_shortener, url_prefix="/urls")

    @app.errorhandler(DomainException)
    def handle_exception(e):
        return jsonify({ "error": e.message }), e.status_code

    @app.teardown_appcontext
    def ensure_db_closing(exception):
        close_db()

    return app