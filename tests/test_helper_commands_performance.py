from src.helper.commands import compare, overwrite
from tests.settings import DATABASE_STRING
from pytest import fixture, mark
from src.crawler.generic import Generic
from os import getcwd


@mark.nonfunctional
class TestPerformanceCommands:

    def test_update_get_data_from_1500_links(self):
        companies = [
            {
                "crawler": Generic("//a"),
                "url": "file:///" + getcwd() + "/tests/resources/p_15000_links.html#",
            }
        ]
        assert overwrite(DATABASE_STRING, companies) is True


    def test_compare_runs_1000_times(self):
        crawlers = [
            {
                "crawler": Generic("//a"),
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
            }]
        resume = "senior python pytest"
        expected = "basic_page"
        overwrite(DATABASE_STRING, crawlers)
        for _ in range(1000):
            assert expected in str(compare(DATABASE_STRING, resume, condition="OR"))
