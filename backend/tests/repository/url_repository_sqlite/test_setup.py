import unittest
import sqlite3

from backend.app.db import SchemaCreator
from backend.app.repository.url_repository_sqlite import UrlRepositorySQLite


class UrlRepositorySQLiteTestSetup(unittest.TestCase):
    def setUp(self):
        self.original_url = "https://www.google.com/"
        self.url_code = "abc123"

        self._create_db_connection()
        self._create_db_schema()
        self.repository = UrlRepositorySQLite(self.connection)

    def _create_db_schema(self):
        schema_creator = SchemaCreator(self.connection)
        schema_creator.create_schema()

    def _create_db_connection(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row

    def tearDown(self):
        self.connection.close()