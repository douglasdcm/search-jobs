from src.crawler import generic, mms
from tests.resources.fake_driver import FakeDriver, Fake_WebDriverWait
import src.automation.automation as auto
from pytest import mark


@mark.integration
class TestCrawler:
    @mark.parametrize("crawler", [
        generic.Generic("any_locator"),
        mms.Mms()
    ])
    def test_all_crawler_types_run_succesfully(self, setup_db, monkeypatch, crawler):
        monkeypatch.setattr(auto.wait, "WebDriverWait", Fake_WebDriverWait)
        generic = crawler
        generic.set_driver(FakeDriver())
        assert generic.run(setup_db) is True
