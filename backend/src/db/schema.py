import sqlite3


class SchemaCreator:
    def __init__(self, database_path):
        self.database_path = database_path
        self.connection: sqlite3.Connection | None = None

    def create_schema(self):
        try:
            self._connect_to_database()
            self._create_shortened_urls_table()
            self._commit_changes()
        finally:
            self._close_connection()

    def _connect_to_database(self):
        self.connection = sqlite3.connect(self.database_path)

    def _create_shortened_urls_table(self):
        self.connection.execute("""
            CREATE TABLE "urls" (
                "uuid"	TEXT NOT NULL UNIQUE,
                "original_url"	TEXT NOT NULL UNIQUE,
                "url_code"	TEXT NOT NULL UNIQUE,
                PRIMARY KEY("uuid")
            )
        """)

    def _commit_changes(self):
        self.connection.commit()

    def _close_connection(self):
        self.connection.close()

