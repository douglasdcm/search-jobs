#!flask/bin/python
import asyncio
import glob
import json
from os import environ
import os
from sys import path
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.helper.commands import compare_facade
from src.media_content import load_web_content
from ast import literal_eval
from dotenv import load_dotenv
from logging import basicConfig, INFO
from src.constants import ROOT_DIR
from waitress import serve
from logging import exception, info
from caqui.easy.server import Server
from webdriver_manager.chrome import ChromeDriverManager


basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    # filename=LOG_FILE,
    level=INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

load_dotenv()  # take environment variables from .env.

app = Flask(__name__, static_folder="static", static_url_path="")
app.config["JSON_SORT_KEYS"] = False
cors = CORS(app)

path.append(ROOT_DIR)


DEFAULT_LANGUAGE = "en_US"
DEFAULT_ERROR_MESSAGE = "Unexpected error. Try again later."
if os.getenv("DEBUG", "").upper() == "ON":
    SERVER = Server()
else:
    CHROME_VERSION = "94.0.4606"  # necessary to docker
    SERVER = Server(ChromeDriverManager(driver_version=CHROME_VERSION))
MAX_CONCURRENCY = 5
SEMAPHORE = asyncio.Semaphore(MAX_CONCURRENCY)


class SessionData:
    def __init__(self):
        self.__language = None

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value


session_data = SessionData()


def __search(resume, condition, language={}):
    limit = 5000
    result = {}

    if not resume:
        result = {
            "status": "failed",
            "message": language.get("api_no_curriculum", DEFAULT_ERROR_MESSAGE),
        }
        return jsonify(result), 500

    if not condition:
        result = {
            "status": "failed",
            "message": language.get("api_no_condition", DEFAULT_ERROR_MESSAGE),
        }
        return jsonify(result), 500

    if len(resume.strip()) == 0:
        result = {
            "status": "failed",
            "message": language.get("api_invalid_curriculum", DEFAULT_ERROR_MESSAGE),
        }
        return jsonify(result), 500

    if condition.lower() not in ["and", "or"]:
        result = {
            "status": "failed",
            "message": language.get("api_invalid_condition", DEFAULT_ERROR_MESSAGE),
        }
        return jsonify(result), 500

    resume = (resume[:limit]) if len(resume) > limit else resume

    try:
        comparison = compare_facade(resume, condition)
    except Exception as error:
        exception(str(error))
        result = {"status": "failed", "message": DEFAULT_ERROR_MESSAGE}
        return jsonify(result), 500

    if not comparison:
        result = {
            "status": "failed",
            "message": language.get("api_no_result", DEFAULT_ERROR_MESSAGE),
        }
        return jsonify(result), 404

    result = {"status": "ok", "message": comparison}
    return jsonify(result), 200


def __check_informed_language(language):
    if language not in language_keys:
        language = DEFAULT_LANGUAGE
    return language


def __set_language(request):
    language = request.form.get("language")
    if language:
        session_data.language = language
    else:
        if not session_data.language:
            session_data.language = DEFAULT_LANGUAGE
    return __check_informed_language(session_data.language)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route("/", methods=["GET", "POST"])
def home():
    try:
        language = __set_language(request)
        images_data = load_web_content()
        return render_template(
            "index.html",
            images_data=images_data,
            **languages[language],
        )
    except Exception as error:
        exception(error)
        return render_template("error.html")


@app.route("/search", methods=["POST"])
def search():
    try:
        language = __set_language(request)
        resume = request.form.get("message")
        condition = request.form.get("condition")

        comparison = literal_eval(
            __search(resume, condition, languages[language])[0].response[0].decode("utf-8")
        )

        return render_template(
            "search-result.html",
            comparison=comparison,
            resume=resume,
            **languages[language],
        )
    except Exception as error:
        exception(error)
        return render_template("error.html")


@app.route("/api/images")
def api_images():
    return jsonify(load_web_content())


if __name__ == "__main__":
    # run!
    port = int(environ.get("PORT", 5001))
    languages = {}
    language_paths = glob.glob("language/*.json")
    language_keys = [
        language.replace("language/", "").replace(".json", "") for language in language_paths
    ]

    for language in language_paths:
        filename = language.split("/")
        lang_code = filename[1].split(".")[0]
        with open(language, "r", encoding="utf8") as file:
            languages[lang_code] = json.loads(file.read())

    info("Server running")
    serve(app, host="0.0.0.0", port=port)
