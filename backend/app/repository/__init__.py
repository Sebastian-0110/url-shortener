from .url_repository import UrlRepository
from .url_repository_sqlite import UrlRepositorySQLite, ShortenedUrlNotFound
from backend.app.db import get_db


def get_url_repository() -> UrlRepository:
    conn = get_db()
    return UrlRepositorySQLite(conn)