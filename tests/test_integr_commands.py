from src.settings import DB_NAME
from src.helper.commands import help_, install, sanity_check, clear
from tests.settings import DATABASE, DB_TYPE
from pytest import fixture
from src.database.db_factory import DbFactory
from tests.resources.fake_driver import FakeDriver

class TestCommands:

    @fixture
    def setup_db(self):
        df = DbFactory("sqlite")
        db = df.get_db()
        db.cria_tabela("positions", "url, description")
        yield db
        df = DbFactory("sqlite")
        db = df.get_db()
        db.deleta_tabela("positions")

    def test_clear_remove_data_from_database(self, setup_db, monkeypatch):
        expected = []
        db = setup_db
        db.salva_registro("positions", "url, description", "'https://test_message_1.com', 'test_message_1'")
        db.salva_registro("positions", "url, description", "'https://test_message_2.com', 'test_message_2'")
        db.salva_registro("positions", "url, description", "'https://test_message_3.com', 'test_message_3'")
        clear(DB_NAME, DB_TYPE["s"])
        actual = db.pega_maior_id("positions")
        assert actual == expected

    def test_sanity_check_works(self, setup_db):
        assert sanity_check(setup_db, FakeDriver())

    def test_install_creates_database(self):
        assert install(DATABASE, DB_TYPE["s"])

    def test_help_is_opened(self):
        actual = help_()
        assert "--initdb" in actual
        assert "--help" in actual
        assert "--sanity-check"
