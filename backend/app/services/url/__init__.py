from .url_service import UrlService

from backend.app.repository import get_url_repository
from backend.app.services.code_generator import code_generator


def get_url_service() -> UrlService:
    get_code_length = lambda: 5 # TODO: Replace with actual implementation
    url_repository = get_url_repository()
    return UrlService(url_repository, code_generator, get_code_length)