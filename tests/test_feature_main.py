from tests.helper import exec_command
from pytest import mark


@mark.feature
class TestFeatureMain:

    entry_point = "./tests/utils/run_main.sh"
    domain = "sh"

    def test_sanity_check_works(self, setup_containers):
        expected = "vagas cadastradas"
        params = ["--sanity-check"]
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual

    def test_help_output_is_correct(self, setup_containers):
        params = ["--help"]
        expected = ["--initdb", "--help", "--sanity-check"]
        actual = exec_command(params, self.entry_point, self.domain)
        for item in expected:
            assert item in actual

    def test_invalid_command_raises_error(self, setup_containers):
        params = ["--invalid"]
        expected = "Invalid command"
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual

    def test_update_database_works(self, setup_containers):
        expected = "vagas cadastradas"
        params = ["--update"]
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual

    def test_main_initdb_runs_completely(self, setup_containers):
        params = ["--initdb"]
        expected = "Installation finished"
        actual = exec_command(params, self.entry_point, self.domain)
        assert expected in actual
