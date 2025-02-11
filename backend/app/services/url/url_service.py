from typing import Callable
from pydantic import TypeAdapter, HttpUrl, ValidationError

from backend.app.repository.url_repository import UrlRepository
from backend.app.services.code_generator.code_generator import CodeGeneratorService


class InvalidUrlException(Exception):
    message = "The introduced url is invalid"
    status_code = 400


class UrlService:
    def __init__(
            self,
            repository: UrlRepository,
            code_generator: CodeGeneratorService,
            get_code_length: Callable[[], int],
        ):
        self.repository = repository
        self.code_generator = code_generator
        self.get_code_length = get_code_length
        self.url_adapter = TypeAdapter(HttpUrl)

    def save(self, original_url: str):
        self._validate_url(original_url)
        url_code = self.code_generator.generate(self.get_code_length())
        return self.repository.save(original_url, url_code)

    def _validate_url(self, url):
        try:
            self.url_adapter.validate_python(url)
        except ValidationError:
            raise InvalidUrlException()