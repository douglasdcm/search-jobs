from config.settings import DATABASE
from database.db import Database
from sqlite3 import connect
from config.settings import DATABASE, TABELA, CAMPOS

class ICrawler:

    def run(self):
        """This method need to be implemented by subclasses"""
        pass

    def _save(self, url, description):
        valores = (f"'{url}', '{description}', 'today'")
        db = Database(connect(DATABASE))
        db.salva_registro(TABELA, CAMPOS, valores)