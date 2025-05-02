from src.driver.driver import Driver
from src.helper.commands import (
    help_facade_,
    overwrite_facade,
    get_positions_data,
    compare_facade,
    sanity_check_facade,
)
from pytest import fixture
from os import getcwd
from pytest import mark


@mark.functional
class TestHelperCommands:
    @fixture
    def get_crashed_crawlers(self):
        return [
            {
                "locator": "//a",
                "url": "file:///" + getcwd() + "/tests/resources/p_crashed_links.html#",
                "active": "Y",
            },
            {
                "locator": "//a",
                "url": "file:///" + getcwd() + "/tests/resources/p_crashed_links.html#",
                "active": "Y",
            },
            {
                "locator": "//a",
                "url": "file:///" + getcwd() + "/tests/resources/p_crashed_links.html#",
                "active": "Y",
            },
        ]

    @fixture
    def populate_db(self, setup_db):
        db = setup_db
        db.salva_registro(
            "positions", "url, description", "'https://test_message_1.com', 'test_message_1'"
        )
        db.salva_registro(
            "positions", "url, description", "'https://test_message_2.com', 'test_message_2'"
        )
        db.salva_registro(
            "positions", "url, description", "'https://test_message_3.com', 'test_message_3'"
        )
        return db

    @fixture
    def get_company(self):
        return {
            "active": "Y",
            "locator": "//a",
            "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
        }

    @fixture
    def setup_driver(self):
        driver = Driver()
        yield driver
        driver.quit()

    @mark.asyncio
    async def test_update_get_data_from_many_links(self, setup_driver):
        companiy = {
            "active": "Y",
            "locator": "//a",
            "url": f"file:///{getcwd()}/tests/resources/p_many_links.html#",
        }
        assert await overwrite_facade(setup_driver, companiy) is True

    @mark.asyncio
    async def test_compare_runs_many_times(self, setup_driver):
        company = {
            "active": "Y",
            "locator": "//a",
            "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
        }
        resume = "senior python pytest"
        expected = "basic_page"
        await overwrite_facade(setup_driver, company)
        for _ in range(10):
            assert expected in str(compare_facade(resume, condition="OR"))

    @mark.asyncio
    async def test_compare_runs_list_of_links_ranked_by_similarity_using_or_condition(self, setup_driver):
        company = {
            "active": "Y",
            "locator": "//a",
            "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
        }

        resume = "senior python pytest"
        expected = "basic_page"
        await overwrite_facade(setup_driver, company)
        assert expected in str(compare_facade(resume, condition="OR"))

    @mark.asyncio
    async def test_run_by_db_string(self, get_company, setup_driver):
        assert await get_positions_data(setup_driver, company=get_company) is True

    @mark.asyncio
    async def test_overwrite_database_returns_true(self, get_company, setup_driver):
        assert await overwrite_facade(setup_driver, get_company) is True

    @mark.asyncio
    async def test_sanity_check_works(self, setup_db, get_company, setup_driver):
        assert await sanity_check_facade(setup_driver, get_company) is True

    def test_help_is_opened(self):
        actual = help_facade_()
        assert "--help" in actual
        assert "--sanity-check"
