from src.helper.commands import help_, install, sanity_check, clear, update
from tests.settings import DB_NAME, DB_TYPE
from tests.resources.fake_driver import FakeDriver
from pytest import fixture

class TestCommands:

    @fixture
    def populate_db(self, setup_db):
        db = setup_db
        db.salva_registro("positions", "url, description", "'https://test_message_1.com', 'test_message_1'")
        db.salva_registro("positions", "url, description", "'https://test_message_2.com', 'test_message_2'")
        db.salva_registro("positions", "url, description", "'https://test_message_3.com', 'test_message_3'")
        return db

    def test_update_database_clear_database(self, populate_db):
        expected = []
        db = populate_db
        update(DB_NAME, DB_TYPE["s"], FakeDriver())
        actual = db.pega_maior_id("positions")
        assert actual == expected

    def test_update_database_returns_true(self):
        assert update(DB_NAME, DB_TYPE["s"], FakeDriver()) is True

    def test_clear_remove_data_from_database(self, populate_db):
        expected = []
        db = populate_db
        clear(DB_NAME, DB_TYPE["s"])
        actual = db.pega_maior_id("positions")
        assert actual == expected

    def test_sanity_check_works(self, setup_db):
        assert sanity_check(setup_db, FakeDriver())

    def test_install_creates_database(self):
        assert install(DB_NAME, DB_TYPE["s"])

    def test_help_is_opened(self):
        actual = help_()
        assert "--initdb" in actual
        assert "--help" in actual
        assert "--sanity-check"
