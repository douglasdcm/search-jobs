#!flask/bin/python
import os
import sys
from src.database.db_factory import DbFactory
from src.settings import DB_NAME, DB_TYPE, ROOT_DIR, TABELA
from flask import Flask, render_template, request
from src.helper.commands import compare, update
from src.driver.chrome import ChromeDriver
from src.crawler.factory import Factory

app = Flask(__name__)
sys.path.append(ROOT_DIR)


def service_db():
    dbf = DbFactory(DB_TYPE["p"])
    return dbf.get_db(DB_NAME)

def service_driver():
    return ChromeDriver()

@app.route('/')
def output():
    # serve index template
    return render_template('index.html')


@app.route('/receiver', methods=['POST'])
def worker():
    limit = 5000
    message = request.json['message']
    message = (message[:limit]) if len(message) > limit else message
    return compare(message, service_db())


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
    if os.getenv('HASH') == "":
        os.environ['HASH'] = "dev"
    if data["hash"] == os.getenv('HASH'):
        update(service_db(), service_driver(), Factory().get_crawlers())
        return "OK\n"
    else:
        return "NO ACTION\n"

#### ####

def _info():
    max_id = service_db().pega_maior_id(TABELA)[0][0]
    return "Number of records in database is {}\n".format(str(max_id))


if __name__ == '__main__':
    # run!
    from waitress import serve
    port = int(os.environ.get('PORT', 5001))
    serve(app, host="0.0.0.0", port=port)
    # app.run(host='0.0.0.0', threaded=True, port=port)
