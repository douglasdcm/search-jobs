from src.database.db_factory import DbFactory
from tests.settings import DB_NAME, DB_TYPE
from src.helper.helper import select_with_like, data_pre_processing_portuguese
from pytest import mark
from src.helper.commands import install


@mark.integration
class TestCompareUsingDatabaseFunctions:

    def test_select_with_like(self, setup_db):
        install(DB_NAME, DB_TYPE["s"])
        p1 = """How to Shut Down the System at a Specific Time
        To schedule a shutdown, add the [time] argument and specify when you want it to take place. There are two ways to shut down the system at a specific time – using the absolute or relative time format.
        The absolute time follows the format hh:mm and allows you to schedule a shutdown at a specified time. The command follows the syntax:
        """
        p2 = """Note: Be careful when deleting records in a table! Notice the WHERE clause in the DELETE statement. The WHERE clause specifies which record(s) should be deleted. If you omit the WHERE clause, all records in the table will be deleted!
        """
        p3 = """Além da explicação em vídeo, de uma forma mais visual, trouxe também a explicação em texto, com os códigos explicando o passo a passo.
        Então para isso, todos os commits tem um ID, algo parecido com “f13bd3c…“. É esse identificador que você precisa pegar na branch do seu colega de trabalho para poder copiar ele para a sua.
        """
        cv = "shutdown time commits"
        cv = data_pre_processing_portuguese(cv).split()
        expected = 2
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        db.salva_registro("positions", "url, description", "'URL1', '{}'".format(p1))
        db.salva_registro("positions", "url, description", "'URL2', '{}'".format(p2))
        db.salva_registro("positions", "url, description", "'URL3', '{}'".format(p3))
        query = select_with_like(cv, "positions", "description")
        actual = db.pega_por_query(query)
        assert len(actual) == expected

    def test_select_with_like_using_and_condition(self, setup_db):
        install(DB_NAME, DB_TYPE["s"])
        p1 = "dog"
        p2 = "cat"
        p3 = "dog cat rabbit cow"
        cv = "dog cow"
        cv = cv.split()
        expected = 1
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        db.salva_registro("positions", "url, description", "'URL1', '{}'".format(p1))
        db.salva_registro("positions", "url, description", "'URL2', '{}'".format(p2))
        db.salva_registro("positions", "url, description", "'URL3', '{}'".format(p3))
        query = select_with_like(cv, "positions", "description", condition="AND")
        actual = db.pega_por_query(query)
        assert len(actual) == expected

    def test_select_with_like_invalid_condition(self):
        expected = "Condição inválida."
        actual = select_with_like("test", "positions", "description", "XOR")
        assert actual == expected
