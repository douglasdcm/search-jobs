import logging
from src.helper.helper import remove_special_characters
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
        dbf = DbFactory()
        conn = dbf.create_connnection(database=DB_NAME)
        db = dbf.make_db(conn)
        db.salva_registro(TABELA, CAMPOS, valores)
        db.fecha_conexao_existente()

    def get_url(self):
        """This method need to be inherited by subclasses"""
        return self.url
