from abc import ABC, abstractmethod

from backend.src.models import ShortenedUrl


class UrlRepository(ABC):
    @abstractmethod
    def save_shortened_url(self, url, shortened_url_code) -> ShortenedUrl:
        pass

    @abstractmethod
    def get_shortened_url_by_uuid(self, uuid_: str) -> ShortenedUrl:
        pass

    @abstractmethod
    def get_shortened_url_by_url_code(self, url_code: str) -> ShortenedUrl:
        pass

    @abstractmethod
    def get_shortened_url_by_original_url(self, original_url: str) -> ShortenedUrl:
        pass

    @abstractmethod
    def get_all_shortened_urls(self) -> list[ShortenedUrl]:
        pass

