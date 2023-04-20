#!flask/bin/python
from os import environ
from sys import path
from src.settings import ROOT_DIR
from flask import Flask, render_template, request, jsonify
from src.helper.commands import compare, overwrite
from src.helper.helper import load_web_content, get_connection_string
from ast import literal_eval
from dotenv import load_dotenv
from logging import basicConfig, INFO
from src.settings import ROOT_DIR, LOGS_FILE
from src.crawler.company import Company


basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOGS_FILE, level=INFO, datefmt='%Y-%m-%d %H:%M:%S')

load_dotenv()  # take environment variables from .env.


app = Flask(__name__, static_folder='static', static_url_path='')

path.append(ROOT_DIR)


@app.route('/')
def output():
    images_data = load_web_content()
    # serve index template
    return render_template('index.html', images_data=images_data)


@app.route('/api/images')
def get_images():
    return jsonify(load_web_content())


def __receiver(resume, condition):
    limit = 5000
    result = {}

    if not resume:
        result = {"status": "failed", "message": "Currículo não informado"}
        return jsonify(result), 500

    if not condition:
        result = {"status": "failed", "message": "Condição não informada"}
        return jsonify(result), 500

    if len(resume.strip()) == 0:
        result = {"status": "failed", "message": "Currículoinválido"}
        return jsonify(result), 500

    if condition.lower() not in ["and", "or"]:
        result = {"status": "failed", "message": "Condição inválida"}
        return jsonify(result), 500

    resume = (resume[:limit]) if len(resume) > limit else resume

    try:
        comparison = compare(get_connection_string(), resume, condition)
    except Exception as error:
        if environ.get("DEBUG") == "on":
            result = {
                "status": "failed",
                "message": f"Unexpected error. Try again later. {str(error)}"}
        else:
            result = {"status": "failed", "message": f"Unexpected error. Try again later."}
        return jsonify(result), 500

    if not comparison:
        result = {"status": "failed", "message": "Nenhum resultado encontrado"}
        return jsonify(result), 404

    result = {"status": "ok", "message": comparison}
    return jsonify(result), 200


@app.route('/api/overwrite', methods=['POST'])
def api_overwrite():
    password = request.json.get('password')
    if environ.get("PASSWORD") == password:
        try:
            overwrite(get_connection_string(), Company().get_all())
            result = {"status": "ok", "message": "overwrite finished"}
            return jsonify(result), 200
        except Exception as error:
            if environ.get("DEBUG") == "on":
                result = {
                    "status": "failed",
                    "message": f"Unexpected error. Try again later. {str(error)}"}
            else:
                result = {"status": "failed", "message": f"Unexpected error. Try again later."}
            return jsonify(result), 500
    result = {"status": "failed", "message": "nothing to overwrite"}
    return jsonify(result), 404


@app.route('/api/receiver', methods=['POST'])
def api_receiver():
    message = request.json.get('message')
    condition = request.json.get('condition')
    return __receiver(message, condition)


@app.route('/receiver', methods=['POST'])
def worker():
    message = request.form.get('message')
    condition = request.form.get('condition')

    comparison = literal_eval(
        __receiver(message, condition)[0].response[0].decode('utf-8'))

    return render_template('search-result.html', comparison=comparison)


if __name__ == '__main__':
    # run!
    from waitress import serve
    port = int(environ.get('PORT', 5001))
    serve(app, host="0.0.0.0", port=port)
