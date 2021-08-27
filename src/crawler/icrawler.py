from src.settings import DATABASE
from src.settings import DATABASE, TABELA, CAMPOS
from src.database.db import Database
from sqlite3 import connect

class ICrawler:

    def __init__(self) -> None:
        self.url = None

    def run(self):
        """This method need to be implemented by subclasses"""
        pass

    def _save(self, url, description):
        valores = (f"'{url}', '{description}'")
        db = Database(connect(DATABASE))
        db.salva_registro(TABELA, CAMPOS, valores)
        db.fecha_conexao_existente()

    def get_url(self):
        return self.url