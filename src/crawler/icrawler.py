import logging
from src.helper.helper import remove_special_characters
from src.settings import DATABASE
from src.settings import DATABASE, TABELA, CAMPOS
from src.database.db import Database
from sqlite3 import connect


class ICrawler:

    def __init__(self) -> None:
        self.url = None

    def set_driver(self, driver):
        """This method need to be implemented by subclasses"""
        pass

    def set_url(self, url):
        """This method need to be inherited by subclasses"""
        self.url = url

    def run(self, company=None):
        """This method need to be implemented by subclasses"""
        pass

    def _save(self, url, description):
        """This method need to be inherited by subclasses"""
        msg = f"Saving '{url}'..."
        print(msg)
        logging.info(msg)
        description = remove_special_characters(description)
        valores = (f"'{url}', '{description}'")
        db = Database(connect(DATABASE))
        db.salva_registro(TABELA, CAMPOS, valores)
        db.fecha_conexao_existente()

    def get_url(self):
        """This method need to be inherited by subclasses"""
        return self.url
