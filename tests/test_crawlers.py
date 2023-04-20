from src.crawler.generic import Generic
from tests.resources.fake_driver import FakeDriver, Fake_WebDriverWait
import src.automation.automation as auto
from pytest import mark


@mark.functional
class TestCrawler:
    def test_all_crawler_types_run_succesfully(self, setup_db, monkeypatch):
        monkeypatch.setattr(auto.wait, "WebDriverWait", Fake_WebDriverWait)
        expected = ('href', ' text_1 text_1')
        crawler = Generic("any_locator")
        crawler.set_driver(FakeDriver())
        assert crawler.run() == expected
