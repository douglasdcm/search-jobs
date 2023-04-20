from src.helper.commands import (
    help_,
    overwrite_by_db_string,
    run_by_db_string,
    compare_by_db_string,
    sanity_check_by_db_string
)
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
                "locator": Generic("//a"),
                "url": "file:///" + getcwd() + "/tests/resources/p_crashed_links.html#",
                "enabled": True
            },
            {
                "locator": Generic("//a"),
                "url": "file:///" + getcwd() + "/tests/resources/p_crashed_links.html#",
                "enabled": True
            },
            {
                "locator": Generic("//a"),
                "url": "file:///" + getcwd() + "/tests/resources/p_crashed_links.html#",
                "enabled": True
            }]

    @fixture
    def populate_db(self, setup_db):
        db = setup_db
        db.salva_registro("positions", "url, description", "'https://test_message_1.com', 'test_message_1'")
        db.salva_registro("positions", "url, description", "'https://test_message_2.com', 'test_message_2'")
        db.salva_registro("positions", "url, description", "'https://test_message_3.com', 'test_message_3'")
        return db

    @fixture
    def get_companies(self):
        return [{
            "locator": Generic("//a"),
            "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
        }]

    def test_compare_runs_list_of_links_ranked_by_similarity_using_or_condition(self):
        companies = [
            {
                "locator": Generic("//a"),
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
            }
        ]
        resume = "senior python pytest"
        expected = "basic_page"
        overwrite_by_db_string(DATABASE_STRING, companies)
        assert expected in str(compare_by_db_string(DATABASE_STRING, resume, condition="OR"))

    def test_run_by_db_string(self, get_companies):
        assert run_by_db_string(
            database_string=DATABASE_STRING, companies=get_companies
        ) is True

    def test_overwrite_database_returns_true(self, get_companies):
        assert overwrite_by_db_string(DATABASE_STRING, get_companies) is True

    def test_sanity_check_works(self, setup_db, get_companies):
        assert sanity_check_by_db_string(DATABASE_STRING, get_companies) is True

    def test_help_is_opened(self):
        actual = help_()
        assert "--help" in actual
        assert "--sanity-check"
