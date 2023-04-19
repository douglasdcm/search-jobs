#!flask/bin/python
from os import environ, getenv
from sys import path
from src.database.db_factory import DbFactory
from src.settings import DB_NAME, DB_TYPE, ROOT_DIR, TABLE_NAME, DRIVER_TYPE
from flask import Flask, render_template, request, jsonify
from src.helper.commands import update, compare_by_db_string
from src.crawler.company import Company
from src.helper.helper import load_web_content
from ast import literal_eval
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.


app = Flask(__name__, static_folder='static', static_url_path='')

path.append(ROOT_DIR)


def service_db():
    dbf = DbFactory(DB_TYPE["p"])
    return dbf.get_db(DB_NAME)


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

    comparison = compare_by_db_string(environ.get("DATABASE_STRING"), resume, condition)

    if not comparison:
        result = {"status": "failed", "message": "Nenhum resultado encontrado"}
        return jsonify(result), 404

    result = {"status": "ok", "message": comparison}
    return jsonify(result), 200


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



@app.route('/info', methods=['POST'])
def info():
    """
    Get information of the database, for example, number of rows.
    Request example:
        curl -XPOST -H "Content-type: application/json" -d '{"hash": "dev"}' 'localhost:5000/info'
    """
    return _info()


#### TODO to be removed ####
@app.route('/update', methods=['POST'])
def update_():
    """
    Run the crawlers and update the database with the positons information.
    Request example:
        curl -XPOST -H "Content-type: application/json" -d '{"hash": "dev"}' 'localhost:5000/update'
    """
    data = request.json
    if getenv('HASH') == "":
        environ['HASH'] = "dev"
    if data["hash"] == getenv('HASH'):
        update(service_db(), DRIVER_TYPE, Company().get_all())
        return "OK\n"
    else:
        return "NO ACTION\n"

#### ####


def _info():
    max_id = service_db().pega_maior_id(TABLE_NAME)[0][0]
    return "Number of records in database is {}\n".format(str(max_id))


if __name__ == '__main__':
    # run!
    from waitress import serve
    port = int(environ.get('PORT', 5001))
    serve(app, host="0.0.0.0", port=port)
