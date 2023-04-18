from tests.helper import exec_command
from pytest import mark
from pytest import raises


@mark.feature
class TestFeatureMain:

    entry_point = "cli.py"
    domain = "python"

    def test_sanity_check_works(self):
        expected = "vagas cadastradas"
        params = ["--sanity-check"]
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual

    def test_help_output_is_correct(self):
        params = ["--help"]
        expected = ["--initdb", "--help", "--sanity-check"]
        actual = exec_command(params, self.entry_point, self.domain)
        for item in expected:
            assert item in actual

    def test_invalid_command_raises_error(self):
        params = ["--invalid"]
        expected = "Invalid command"
        with raises(Exception):
            actual = exec_command(params, self.entry_point, self.domain)
            assert expected in actual

    def test_update_database_works(self):
        expected = "vagas cadastradas"
        params = ["--update"]
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual

    def test_main_initdb_runs_completely(self):
        params = ["--initdb"]
        expected = "Installation finished"
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual
