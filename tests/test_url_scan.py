from time import sleep
from pytest import mark, fixture
from src.driver.driver import Driver
from src.url_scanner.controller import Controller
from os import getcwd
from caqui.easy.server import Server
from src.url_scanner.fetcher import Fetcher


COMPANY_PAGE = f"file:///{getcwd()}/tests/resources/basic_company_page.html#"
COMPANY_PAGE_NO_JOBS = (
    f"file:///{getcwd()}/tests/resources/basic_company_page_no_jobs.html#"
)


@mark.functional
class TestUrlScan:
    @fixture
    def driver_fixture(self):
        driver = Driver()
        yield driver
        driver.quit()

    @mark.asyncio
    async def test_return_candidate_links_related_to_careers(self):
        links = [
            "file:///foo/careers",
            "file:///foo/jobs",
            "file:///foo/noise",
            "file:///foo/opportunities",
        ]
        expected = sorted(
            [
                "file:///foo/careers",
                "file:///foo/jobs",
                "file:///foo/opportunities",
            ]
        )
        assert sorted(Fetcher(None).return_candidate_links(links)) == expected

    @mark.asyncio
    async def test_extract_all_links_return_empty_when_no_links(
        self, driver_fixture: Driver
    ):
        expected = []
        await driver_fixture.start(COMPANY_PAGE_NO_JOBS)
        assert await Fetcher(driver_fixture).extracts_all_links() == expected

    @mark.asyncio
    async def test_extract_all_links_from_company_page(self, driver_fixture: Driver):
        expected = ["file:///foo/careers", "file:///foo/jobs", "file:///foo/noise"]
        await driver_fixture.start(COMPANY_PAGE)
        assert await Fetcher(driver_fixture).extracts_all_links() == expected

    # acceptance criteria
    @mark.asyncio
    async def test_urls_are_scanned_correctly(self):
        urls = [COMPANY_PAGE, COMPANY_PAGE]
        expected = sorted(["file:///foo/careers", "file:///foo/jobs"])
        driver = Driver()
        for url in urls:
            await driver.start(url)
            controller = Controller(driver)
            assert sorted(await controller.execute(save=False)) == expected
