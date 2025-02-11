from flask import Blueprint

url_shortener = Blueprint("url_shortener", __name__)

from . import routes