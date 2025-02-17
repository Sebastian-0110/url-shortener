from flask import request, jsonify, redirect

from . import url_shortener
from backend.app.services.url.url_service import InvalidUrlException
from backend.app.services.url import get_url_service

from backend.app.repository import get_url_repository, ShortenedUrlNotFound


@url_shortener.post("/")
def create():
    url = request.json.get("url", None)

    try:
        service = get_url_service()
        shortened_url = service.save(url)

        response = jsonify(shortened_url.model_dump(mode="json"))
        response.status_code = 201
        response.headers["location"] = f"/{shortened_url.url_code}"

        return response

    except InvalidUrlException as e:
        return jsonify({"error": e.message}), e.status_code


@url_shortener.get("/<string:url_code>/details")
def details(url_code):
    try:
        repository = get_url_repository()
        shortened_url = repository.get_by_url_code(url_code)
        return jsonify(shortened_url.model_dump(mode="json")), 200

    except ShortenedUrlNotFound as e:
        return jsonify({"error": "Not found"}), 404
