from tests.helper import exec_command
from pytest import mark
from pytest import raises


@mark.feature
class TestCliCommands:

    entry_point = "cli.py"
    domain = "python"

    def test_sanity_check_works(self):
        expected = "Crawler finished"
        params = ["--sanity-check"]
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual

    def test_invalid_command(self):
        params = ["--invalid"]
        expected = "Invalid command"
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual

    # def test_update_database_works(self):
    #     expected = "Update finished"
    #     params = ["--overwrite"]
    #     actual = exec_command(params, self.entry_point, self.domain)
    #     assert expected in actual
