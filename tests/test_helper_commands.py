from src.helper.commands import help_, overwrite, get_positions_data, compare, sanity_check
from tests.settings import DATABASE_STRING
from pytest import fixture
from src.crawler.generic import Generic
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
    def get_companies(self):
        return [
            {
                "active": "Y",
                "locator": "//a",
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
            }
        ]

    @mark.asyncio
    async def test_update_get_data_from_many_links(self):
        companies = [
            {
                "active": "Y",
                "locator": "//a",
                "url": f"file:///{getcwd()}/tests/resources/p_many_links.html#",
            }
        ]
        assert await overwrite(DATABASE_STRING, companies) is True

    @mark.asyncio
    def test_compare_runs_many_times(self):
        crawlers = [
            {
                "active": "Y",
                "locator": "//a",
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
            }
        ]
        resume = "senior python pytest"
        expected = "basic_page"
        overwrite(DATABASE_STRING, crawlers)
        for _ in range(10):
            assert expected in str(compare(DATABASE_STRING, resume, condition="OR"))

    def test_compare_runs_list_of_links_ranked_by_similarity_using_or_condition(self):
        companies = [
            {
                "active": "Y",
                "locator": "//a",
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
            }
        ]
        resume = "senior python pytest"
        expected = "basic_page"
        overwrite(DATABASE_STRING, companies)
        assert expected in str(compare(DATABASE_STRING, resume, condition="OR"))

    @mark.asyncio
    async def test_run_by_db_string(self, get_companies):
        assert (
            await get_positions_data(database_string=DATABASE_STRING, companies=get_companies)
            is True
        )

    @mark.asyncio
    async def test_overwrite_database_returns_true(self, get_companies):
        assert await overwrite(DATABASE_STRING, get_companies) is True

    @mark.asyncio
    async def test_sanity_check_works(self, setup_db, get_companies):
        assert await sanity_check(DATABASE_STRING, get_companies) is True

    def test_help_is_opened(self):
        actual = help_()
        assert "--help" in actual
        assert "--sanity-check"
