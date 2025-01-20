""" Module to manage db access (querying and inserting data) """

import sqlite3
from flask import g



DATABASE_PATH = "database.sqlite"


def get_db() -> sqlite3.Connection:
	""" Return an instance of a db """

	db = getattr(g, "_database", None)

	if db is None:
		db = sqlite3.connect(DATABASE_PATH)
		db.row_factory = sqlite3.Row

		g._database = db

	return db


def close_db() -> None:
	""" Ensure the db closes correctly """

	db = getattr(g, "_database", None)

	if db is not None:
		db.close()


def query_db(query, args, one=False) -> list[sqlite3.Row] | sqlite3.Row | None:
	""" Query the db and return the result """

	db = get_db()
	cursor = db.cursor()

	result = cursor.execute(query, args).fetchall()

	if len(result) == 0: # No results
		return None

	return result[0] if one else result


def close_db():
	""" Ensure closing the db """

	db = getattr(g, "_database", None)

	if db is not None:
		db.commit()
		db.close()