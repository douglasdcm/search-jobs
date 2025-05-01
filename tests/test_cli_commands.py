from tests.helper import exec_command
from pytest import mark


@mark.functional
class TestCliCommands:

    entry_point = "cli.py"
    domain = "python"

    def test_sanity_check_works_cli(self):
        expected = "Crawler finished"
        params = ["--sanity-check"]
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual

    def test_invalid_command(self):
        params = ["--invalid"]
        expected = "Invalid command"
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual
