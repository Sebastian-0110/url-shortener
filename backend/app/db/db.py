""" Module to manage db access (querying and inserting data) """

from dotenv import load_dotenv
from flask import g
import sqlite3
import os

load_dotenv()
DATABASE_PATH = os.environ["DATABASE_PATH"]

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
