from abc import ABC, abstractmethod


class UrlRepository(ABC):
    @abstractmethod
    def save_shortened_url(self, url, shortened_url_code):
        pass

    @abstractmethod
    def get_shortened_url_by_uuid(self, id_: int):
        pass