import automation
from src.crawler.toy import Toy
from src.crawler.generic import Generic
from tests.resources.fake_driver import FakeDriver, Fake_WebDriverWait
import src.automation.automation as auto

class TestCrawler:

    def test_generic_crawler_runs_succesfully(self, setup_db, monkeypatch):
        monkeypatch.setattr(auto.wait, "WebDriverWait", Fake_WebDriverWait)
        generic = Generic('test_locator')
        generic.set_driver(FakeDriver())
        assert generic.run(setup_db) is True

    def test_crawler_toy_runs_succefully(self, setup_db):
        toy = Toy()
        assert toy.run(setup_db) is True