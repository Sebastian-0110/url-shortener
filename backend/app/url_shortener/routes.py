from flask import request, jsonify, redirect
import uuid

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


@url_shortener.get("/<string:url_code>/details")
def details(url_code):
    try:
        repository = get_url_repository()
        shortened_url = repository.get_by_url_code(url_code)
        return jsonify(shortened_url.model_dump(mode="json")), 200

    except ShortenedUrlNotFound as e:
        return jsonify({"error": "Not found"}), 404
