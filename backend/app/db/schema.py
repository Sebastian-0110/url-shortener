import sqlite3


class SchemaCreator:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def create_schema(self):
        self._create_shortened_urls_table()
        self._commit_changes()

    def _create_shortened_urls_table(self):
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS "urls" (
                "uuid"	TEXT NOT NULL UNIQUE,
                "original_url"	TEXT NOT NULL UNIQUE,
                "url_code"	TEXT NOT NULL UNIQUE,
                PRIMARY KEY("uuid")
            )
        """)

    def _commit_changes(self):
        self.connection.commit()