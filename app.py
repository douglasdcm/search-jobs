#!flask/bin/python
import os
import sys
import logging
from time import time

from src.settings import ROOT_DIR, DATABASE, TABELA, CAMPOS

from flask import Flask, render_template, request
from src.database.db import Database
from sqlite3 import connect
from src.similarity.similarity import Similarity
from datetime import datetime, timedelta
from src.settings import ROOT_DIR, DATABASE, TABELA, CAMPOS
from src.driver.chrome import ChromeDriver
from src.database.db import Database
from src.similarity.similarity import Similarity
from sqlite3 import connect
from src.crawler.factory import Factory

app = Flask(__name__)
sys.path.append(ROOT_DIR)


@app.route('/')
def output():
    # serve index template
    return render_template('index.html')


@app.route('/receiver', methods=['POST'])
def worker():

    message = request.json['message']
    return _compare(message)


@app.route('/update', methods=['GET'])
def update():
    return _update()


def _compare(content):

    cv = content

    db = Database(connect(DATABASE))
    positions = db.pega_todos_registros(TABELA, CAMPOS)
    db.fecha_conexao_existente()
    s = Similarity()
    result = s.return_similarity_by_cossine(cv, positions)
    table = '<table class="table table-striped" style="width:100%">'
    table += '<tr><th>% Similaridade</th><th>Link da vaga</th></tr>' 
    i = 0
    for key, values in result.items():
        table += '<tr>'
        table += f'<td style="width:20%; text-align: center";> {key} </td>'
        table += f'<td style="width:80%"><a href={values[0]}> {values[0]} </a></td>'
        table += '</tr>'
    table += '</table>'
    return table


def _update():
    try:
        scheduler = os.getenv('SCHEDULER')
        print(scheduler)
        current_date_and_time = int(time())
        hours_added = 86400  # in timestamp
        if scheduler is None:
            os.environ['LAST_EXECUTION'] = str(current_date_and_time)
            os.environ['SCHEDULER'] = str(current_date_and_time + hours_added)
            _run()
            return "OK"
        else:
            last_exe = int(os.environ['LAST_EXECUTION'])
            next = last_exe + hours_added
            if current_date_and_time > next:
                os.environ['LAST_EXECUTION'] = str(current_date_and_time)
                os.environ['SCHEDULER'] = str(current_date_and_time + hours_added)
                _run()
                return "OK"
            return "NO ACTION"
    except Exception as e:
        return "FAIL: \n{}".format(str(e))


def _run(crawlers=None):
    if crawlers is None:
        crawlers = Factory().get_crawlers()
    chrome = ChromeDriver()
    for crawler in crawlers:
        try:
            if crawler["enabled"]:
                url = crawler["url"]
                driver = chrome.start(url)
                company = crawler["company"]
                company.set_driver(driver)
                company.set_url(url)
                company.run()
        except Exception as e:
            msg = "An error occurred during the execution:\n   {}".format(str(e))
            print(msg)
            logging.info(msg)
    _finish_driver(chrome)


def _finish_driver(chrome):
    chrome.quit()
    print("===========================")
    msg = "Crawler finished."
    print(msg)
    logging.info(msg)
    print("===========================")


if __name__ == '__main__':
    # run!
    from waitress import serve
    port = int(os.environ.get('PORT', 5000))
    serve(app, host="0.0.0.0", port=port)
    # app.run(host='0.0.0.0', threaded=True, port=port)
