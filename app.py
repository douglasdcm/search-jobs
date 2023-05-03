#!flask/bin/python
from os import environ
from sys import path
from src.settings import ROOT_DIR
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.helper.commands import compare, overwrite
from src.helper.helper import load_web_content, Connection
from ast import literal_eval
from dotenv import load_dotenv
from logging import basicConfig, INFO
from src.settings import ROOT_DIR, LOG_FILE
from src.crawler.company import Company
from waitress import serve
import glob
import json


basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOG_FILE, level=INFO, datefmt='%Y-%m-%d %H:%M:%S')

load_dotenv()  # take environment variables from .env.


app = Flask(__name__, static_folder='static', static_url_path='')
app.config['JSON_SORT_KEYS'] = False
cors = CORS(app)

path.append(ROOT_DIR)


DEFAULT_LANGUAGE = "pt_BR"
DEFAULT_ERROR_MESSAGE = "Unexpected error. Try again later."


class SessionData:
    def __init__(self):
        self.__language = DEFAULT_LANGUAGE

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value


session_data = SessionData()


def __check_informed_language(language):
    if (language not in language_keys):
        language = DEFAULT_LANGUAGE
    return language


def __receiver(resume, condition, language={}):
    limit = 5000
    result = {}

    if not resume:
        result = {"status": "failed", "message": language.get(
            "api_no_curriculum", DEFAULT_ERROR_MESSAGE)}
        return jsonify(result), 500

    if not condition:
        result = {"status": "failed", "message": language.get(
            "api_no_condition", DEFAULT_ERROR_MESSAGE)}
        return jsonify(result), 500

    if len(resume.strip()) == 0:
        result = {"status": "failed", "message": language.get(
            "api_invalid_curriculum", DEFAULT_ERROR_MESSAGE)}
        return jsonify(result), 500

    if condition.lower() not in ["and", "or"]:
        result = {"status": "failed", "message": language.get(
            "api_invalid_condition", DEFAULT_ERROR_MESSAGE)}
        return jsonify(result), 500

    resume = (resume[:limit]) if len(resume) > limit else resume

    try:
        comparison = compare(Connection.get_connection_string(), resume, condition)
    except Exception as error:
        if environ.get("DEBUG") == "on":
            result = {
                "status": "failed",
                "message": f"Unexpected error. Try again later. {str(error)}"}
        else:
            result = {"status": "failed", "message": DEFAULT_ERROR_MESSAGE}
        return jsonify(result), 500

    if not comparison:
        result = {"status": "failed", "message": "Nenhum resultado encontrado"}
        return jsonify(result), 404

    result = {"status": "ok", "message": comparison}
    return jsonify(result), 200


@app.route("/", methods=["GET", "POST"])
def output():
    session_data.language = request.form.get('language', DEFAULT_LANGUAGE)
    language = __check_informed_language(session_data.language)
    images_data = load_web_content()
    return render_template(
        'index.html',
        images_data=images_data,
        **languages[language],
    )


@app.route('/receiver', methods=['POST'])
def worker():
    language = __check_informed_language(session_data.language)
    resume = request.form.get('message')
    condition = request.form.get('condition')

    comparison = literal_eval(
        __receiver(
            resume,
            condition,
            languages[language]
        )[0].response[0].decode('utf-8'))

    return render_template(
        'search-result.html',
        comparison=comparison,
        resume=resume,
        **languages[language],
    )


@app.route("/spec")
def spec():
    return render_template('spec.html')


@app.route('/api/images')
def api_images():
    return jsonify(load_web_content())


@app.route('/api/overwrite', methods=['POST'])
def api_overwrite():
    password = request.json.get('password')
    if environ.get("PASSWORD") == password:
        try:
            overwrite(Connection.get_connection_string(), Company().get_all())
            result = {"status": "ok", "message": "overwrite finished"}
            return jsonify(result), 200
        except Exception as error:
            if environ.get("DEBUG") == "on":
                result = {
                    "status": "failed",
                    "message": f"Unexpected error. Try again later. {str(error)}"}
            else:
                result = {"status": "failed", "message": DEFAULT_ERROR_MESSAGE}
            return jsonify(result), 500
    result = {"status": "failed", "message": "nothing to overwrite"}
    return jsonify(result), 404


@app.route('/api/logs', methods=["POST"])
def api_logs():
    password = request.json.get('password')
    if environ.get("PASSWORD") == password:
        try:
            with open(LOG_FILE, "r") as log:
                result = {"status": "ok", "message": log.read()}
                return jsonify(result), 200
        except Exception as error:
            if environ.get("DEBUG") == "on":
                result = {
                    "status": "failed",
                    "message": f"Unexpected error. Try again later. {str(error)}"}
            else:
                result = {"status": "failed", "message": DEFAULT_ERROR_MESSAGE}
            return jsonify(result), 500
    result = {"status": "failed", "message": "nothing to log"}
    return jsonify(result), 404


if __name__ == '__main__':
    # run!
    port = int(environ.get('PORT', 5001))
    languages = {}
    language_paths = glob.glob("language/*.json")
    language_keys = [
        language.replace("language/", "").replace(".json", "")
        for language in language_paths
    ]

    for language in language_paths:
        filename = language.split("/")
        lang_code = filename[1].split(".")[0]
        with open(language, "r", encoding="utf8") as file:
            languages[lang_code] = json.loads(file.read())

    print("Server running")
    serve(app, host="0.0.0.0", port=port)
