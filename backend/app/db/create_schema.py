import sqlite3

from .schema import SchemaCreator


def create_schema(database_path: str):
    connection = sqlite3.connect(database_path)
    schema_creator = SchemaCreator(connection)

    try:
        schema_creator.create_schema()
    finally:
        connection.close()