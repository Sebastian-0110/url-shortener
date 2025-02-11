import sqlite3
import uuid

from backend.app.repository.url_repository import UrlRepository
from backend.app.models import ShortenedUrl


class ShortenedUrlNotFound(Exception):
    pass

class UrlRepositorySQLite(UrlRepository):
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def save(self, original_url: str, url_code: str) -> ShortenedUrl:
        try:
            return self.get_by_original_url(original_url)
        except ShortenedUrlNotFound:
            return self._save_new_url(original_url, url_code)

    def _save_new_url(self, original_url: str, url_code: str):
        uuid_ = str(uuid.uuid4())

        self.connection.execute(
            "INSERT INTO urls (uuid, original_url, url_code) VALUES (?, ?, ?)",
            (uuid_, original_url, url_code)
        )

        return ShortenedUrl(uuid=uuid_, original_url=original_url, url_code=url_code)

    def get_by_uuid(self, uuid_: str) -> ShortenedUrl:
        return self._get_or_raise_not_found(
            "SELECT * FROM urls WHERE uuid = ?",
            (uuid_, )
        )


    def get_by_original_url(self, original_url: str) -> ShortenedUrl:
        return self._get_or_raise_not_found(
            "SELECT * FROM urls WHERE original_url = ?",
            (original_url, )
        )

    def get_by_url_code(self, url_code: str) -> ShortenedUrl:
        return self._get_or_raise_not_found(
            "SELECT * FROM urls WHERE url_code = ?",
            (url_code, ),
        )

    def _get_or_raise_not_found(self, query: str, params: tuple):
        result = self.connection.execute(query, params).fetchone()

        try:
            return ShortenedUrl(**result)
        except TypeError:
            raise ShortenedUrlNotFound()

    def get_all(self) -> list[ShortenedUrl]:
        urls = self.connection.execute("""
            SELECT * FROM urls
        """).fetchall()

        return list(map(lambda url: ShortenedUrl(**url), urls))


