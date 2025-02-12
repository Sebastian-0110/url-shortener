from flask import Flask

from .url_shortener import url_shortener
from .db import close_db

def create_app():
    app = Flask(__name__)

    app.register_blueprint(url_shortener, url_prefix="/urls")

    @app.teardown_appcontext
    def ensure_db_closing(exception):
        close_db()

    return app