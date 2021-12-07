from src.helper.commands import help_, install, sanity_check, clear, update
from tests.settings import DB_NAME, DB_TYPE
from src.driver.chrome import ChromeDriver
from src.database.db_factory import DbFactory
from pytest import fixture, mark
from src.crawler.generic import Generic
from os import getcwd


@mark.robustness
class TestRobustnessCommands:

    @fixture
    def get_crawlers(self):
        return [{
                "company": Generic("//a"),
                "url": "file:///" + getcwd() + "/tests/resources/p_crashed_links.html#",
                "enabled": True
            },
            {
                "company": Generic("//a"),
                "url": "file:///" + getcwd() + "/tests/resources/p_crashed_links.html#",
                "enabled": True
            },
            {
                "company": Generic("//a"),
                "url": "file:///" + getcwd() + "/tests/resources/p_crashed_links.html#",
                "enabled": True
            }]

    def test_update_get_data_from_crashed_links(self, get_crawlers):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        assert update(db, ChromeDriver(), get_crawlers) is True

