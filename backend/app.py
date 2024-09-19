from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS

import string
import random
import re

import db


app = Flask(
	__name__, 
	template_folder="../frontend/dist/", # Temporal setting to allow the use of the frontend
	static_folder="../frontend/dist/" # Temporal setting to allow the use of the frontend
)

CORS(app)


URL_VALIDATION_REGEX = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

URL_CODE_LENGTH = 5 # Can hold up to 311.8M urls


@app.get("/")
def index():
	""" Index page. Since it's a SPA, this is all we need """

	return render_template("index.html")


@app.post("/url/")
def shorten_url():
	""" Shorthen the url submited """

	url = request.form.get("url", None)
	
	# Validation
	if url is None:
		return jsonify({"error": "You must provide an url to shorten."}), 400
	
	elif re.match(URL_VALIDATION_REGEX, url) is None: # If url is not valid
		return jsonify({"error": "The provided url is not valid."}), 400

	# Checking for duplicates
	result = db.query_db("SELECT * FROM urls WHERE original_url = ?", (url,), one=True)

	if result is None:
		# Since we are generating a random code, there is a -tiny- chance of code duplication.
		# We handle this by recomputing the code in case of duplication.
		# In practice, this will never happen.

		while True:
			shortened_url_code = "".join([random.choice(string.ascii_letters) for _ in range(URL_CODE_LENGTH)])	
			duplicate_check = db.query_db("SELECT * FROM urls WHERE shortened_url_code = ?", (shortened_url_code,), one=True)

			if duplicate_check is None:
				break
		
		db.query_db("INSERT INTO urls (original_url, shortened_url_code) VALUES (?, ?)", (url, shortened_url_code))

	else: # The url has been alredy shortened. No need to shorten it again
		shortened_url_code = result["shortened_url_code"]

	shortened_url = request.url_root + "go/" + shortened_url_code
	return jsonify({"shortened_url": shortened_url}), 200



@app.get("/go/<string:url_code>")
def go(url_code: str):
	""" Go to an url """

	result = db.query_db("SELECT * FROM urls WHERE shortened_url_code = ?", (url_code,), one=True)

	if result is None:
		return jsonify({"error": "The url doesn't exist"}), 400
	 
	return redirect(result["original_url"], code=302)


@app.teardown_appcontext
def ensure_db_close(exception):
	""" Ensure the db closes correctly """

	db.close_db()