#!flask/bin/python
import os, sys
from src.settings import ROOT_DIR, DATABASE, TABELA, CAMPOS
sys.path.append(ROOT_DIR)

from flask import Flask, render_template, request
from src.database.db import Database
from sqlite3 import connect
from src.similarity.similarity import Similarity

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html')

@app.route('/receiver', methods = ['POST'])
def worker():

	message = request.json['message']
	return _compare(message)

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

if __name__ == '__main__':
	# run!
	port = int(os.environ.get('PORT', 5000))
	app.run(host='localhost', threaded=True, port=port)