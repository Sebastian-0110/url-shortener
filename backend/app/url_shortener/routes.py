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
        return jsonify(shortened_url.model_dump(mode="json")), 200

    except InvalidUrlException as e:
        return jsonify({"error": e.message}), 400


@url_shortener.get("/<string:url_code>/")
def go(url_code):
    try:
        repository = get_url_repository()
        shortened_url = repository.get_by_url_code(url_code)
        return redirect(str(shortened_url.original_url),301)

    except ShortenedUrlNotFound as e:
        return jsonify({"error": "Not found"}), 404


@url_shortener.get("/<uuid:uuid>/details")
def details(uuid):
    try:
        repository = get_url_repository()
        shortened_url = repository.get_by_uuid(str(uuid))
        return jsonify(shortened_url.model_dump(mode="json")), 200

    except ShortenedUrlNotFound as e:
        return jsonify({"error": "Not found"}), 404
