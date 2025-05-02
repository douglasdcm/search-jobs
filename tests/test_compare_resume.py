from tests.settings import DATABASE_STRING
from src.helper.helper import search_positions_based_on_resume, data_pre_processing_portuguese
from pytest import mark, raises
from src.exceptions.exceptions import DatabaseError


@mark.functional
class TestSearchPostionsBasedOnResume:
    def test_search_positions_based_on_resume_with_large_search(self, setup_db):
        resume = "tester manager python"
        expected = 3

        actual = search_positions_based_on_resume(condition="or", resume=resume)

        assert len(actual) == expected

    def test_search_positions_based_on_resume_with_restricted_search(self, setup_db):
        resume = "jira tester"
        expected = 1

        actual = search_positions_based_on_resume(condition="and", resume=resume)

        assert len(actual) == expected

    def test_select_with_like_invalid_condition(self, setup_db):
        resume = "jira tester"

        with raises(DatabaseError):
            search_positions_based_on_resume(condition="invalid", resume=resume)
