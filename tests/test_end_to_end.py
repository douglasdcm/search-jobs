from settings import DB_TYPE, DRIVER_TYPE
from src.helper.commands import install, update, compare
from tests.settings import DB_NAME, DB_TYPE
from src.database.db_factory import DbFactory
from pytest import mark
from src.crawler.factory import Factory


@mark.end_to_end
class TestEndToEnd:

    def test_install_update_compare(self, setup_containers):
        install(DB_NAME, DB_TYPE["s"])
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        update(db, DRIVER_TYPE, Factory().get_crawlers())
        expected = "Nenhum resultado encontrado."
        assert expected in compare("blablabla", db, "or")