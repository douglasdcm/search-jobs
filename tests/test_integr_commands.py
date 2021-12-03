from src.helper.commands import help_, install, sanity_check, clear, update
from tests.settings import DB_NAME, DB_TYPE
from src.driver.chrome import ChromeDriver
from tests.resources.fake_driver import FakeDriver
from pytest import fixture
from src.crawler.generic import Generic
from os import getcwd

class TestCommands:

    @fixture
    def populate_db(self, setup_db):
        db = setup_db
        db.salva_registro("positions", "url, description", "'https://test_message_1.com', 'test_message_1'")
        db.salva_registro("positions", "url, description", "'https://test_message_2.com', 'test_message_2'")
        db.salva_registro("positions", "url, description", "'https://test_message_3.com', 'test_message_3'")
        return db

    @fixture
    def get_crawlers(self):
        return [{
                "company": Generic("//a"),
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
                "enabled": True
            }]

    def test_update_database_clear_database(self, populate_db, get_crawlers):
        expected = []
        db = populate_db
        update(DB_NAME, DB_TYPE["s"], FakeDriver(), get_crawlers())
        actual = db.pega_maior_id("positions")
        assert actual == expected

    def test_update_database_returns_true(self, get_crawlers):
        assert update(DB_NAME, DB_TYPE["s"], FakeDriver(), get_crawlers) is True

    def test_clear_remove_data_from_database(self, populate_db):
        expected = []
        db = populate_db
        clear(DB_NAME, DB_TYPE["s"])
        actual = db.pega_maior_id("positions")
        assert actual == expected

    def test_sanity_check_works(self, setup_db, get_crawlers):
        assert sanity_check(setup_db, FakeDriver(), get_crawlers) is True

    def test_install_creates_database(self):
        assert install(DB_NAME, DB_TYPE["s"])

    def test_help_is_opened(self):
        actual = help_()
        assert "--initdb" in actual
        assert "--help" in actual
        assert "--sanity-check"