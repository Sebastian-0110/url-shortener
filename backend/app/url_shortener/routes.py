from flask import request, jsonify

from . import url_shortener
from backend.app.services.url import get_url_service
from backend.app.repository import get_url_repository


@url_shortener.post("/")
def create():
    url = request.json.get("url", None)

    service = get_url_service()
    shortened_url = service.save(url)

    response = jsonify(shortened_url.model_dump(mode="json"))
    response.status_code = 201
    response.headers["location"] = f"/{shortened_url.url_code}"

    return response


@url_shortener.get("/<string:url_code>/details")
def details(url_code):
    repository = get_url_repository()
    shortened_url = repository.get_by_url_code(url_code)

    return jsonify(shortened_url.model_dump(mode="json")), 200