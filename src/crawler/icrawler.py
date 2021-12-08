import logging
from src.helper.helper import data_pre_processing_portuguese
from src.settings import DB_NAME, TABELA, CAMPOS
from src.database.db_factory import DbFactory


class ICrawler:

    def __init__(self) -> None:
        self.url = None

    def set_driver(self, driver):
        """This method need to be implemented by subclasses"""
        pass

    def set_url(self, url):
        """This method need to be inherited by subclasses"""
        self.url = url

    def run(self, database, company=None):
        """This method need to be implemented by subclasses"""
        pass

    def _save(self, database, url, description):
        """This method need to be inherited by subclasses
        Args:
            database: the database connection
            url (str): URL of the positon
            description (str): description of the position
        """
        msg = f"Saving '{url}'..."
        print(msg)
        logging.info(msg)
        description = data_pre_processing_portuguese(description)
        valores = (f"'{url}', '{description}'")
        db = database
        db.salva_registro(TABELA, CAMPOS, valores)

