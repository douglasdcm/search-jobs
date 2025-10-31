from src.crawler.generic import Generic
from src.crawler.company import Company
from tests.resources.fake_driver import FakeDriver
from pytest import mark


@mark.functional
class TestCrawler:
    def test_get_all_companies_from_csv(self):

        companies = Company().get_all()[0]

        assert '//a' in companies.locator
        assert 'http' in companies.url
        assert companies.active is not None

    @mark.asyncio
    async def test_all_crawler_types_run_succesfully(self, setup_db, monkeypatch):
        crawler = Generic("any_locator")
        crawler.set_driver(FakeDriver())
        assert await crawler.run() is True
