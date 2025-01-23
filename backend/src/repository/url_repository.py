from abc import ABC, abstractmethod


class UrlRepository(ABC):
    @abstractmethod
    def save_shortened_url(self, url, shortened_url_code):
        pass

    @abstractmethod
    def get_shortened_url_by_uuid(self, id_: int):
        pass

    def get_shortened_url_by_url_code(self, url_code):
        pass

    def get_shortened_url_by_original_url(self, original_url):
        pass

    def get_all_shortened_urls(self):
        pass