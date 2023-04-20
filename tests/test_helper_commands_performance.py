from src.helper.commands import compare
from tests.settings import DRIVER_TYPE
from pytest import fixture, mark
from src.crawler.generic import Generic
from os import getcwd


@mark.nonfunctional
class TestPerformanceCommands:

    @fixture
    def get_companies(self):
        return [
            {
                "company": Generic("//a"),
                "url": "file:///" + getcwd() + "/tests/resources/p_15000_links.html#",
                "enabled": True
            }
        ]

    def test_update_get_data_from_1500_links(self, get_companies):
        # TODO generate the htlm iteractively
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        assert update(db, DRIVER_TYPE, get_companies) is True


    def test_compare_runs_1000_times(self):
        crawlers = [
            {
                "company": Generic("//a"),
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
                "enabled": True
            }]
        content = "not_found"
        expected = "not_found"
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        update(db, DRIVER_TYPE, crawlers)
        for _ in range(1000):
            assert expected in compare(content, db, condition="OR").lower()
