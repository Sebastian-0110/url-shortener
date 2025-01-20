from typing import Callable
import sqlite3
import uuid

from .url_repository import UrlRepository


class UrlRepositorySQLite(UrlRepository):
    def __init__(self, database_path: str):
        self.database_path: str = database_path
        self.connection: sqlite3.Connection

    def save_shortened_url(self, url, shortened_url_code):
        def sql_executing_function():
            self.connection.execute(
                "INSERT INTO urls (uuid, original_url, shortened_url_code) VALUES (?, ?, ?)",
                (uuid.uuid4(), url, shortened_url_code)
            )
        self._execute(sql_executing_function)

    def get_shortened_url_by_id(self, id_: int):
        def sql_executing_function():
            return self.connection.execute(
                "SELECT * FROM urls WHERE id = ?",
                (id_, )
            ).fetchone()
        self._execute(sql_executing_function)

    def _execute(self, sql_executing_function: Callable):
        try:
            self._connect_to_database()
            result = sql_executing_function()
            self._commit_changes()
            return result
        finally:
            self._close_connection()

    def _connect_to_database(self):
        self.connection = sqlite3.connect(self.database_path)
        self.connection.row_factory = sqlite3.Row

    def _commit_changes(self):
        self.connection.commit()

    def _close_connection(self):
        self.connection.close()