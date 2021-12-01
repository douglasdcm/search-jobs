from requests import post
from json import dumps
from tests.settings import BASE_URL
from tests.helper import exec_command
from pytest import fixture


class TestEndToEnd:

    entry_point = "./tests/utils/run_main.sh"

    def test_help_output_is_correct(self, setup_containers):
        params = ["--help"]
        expected = ["--initdb", "--help", "--sanity-check"]
        actual = exec_command(params, self.entry_point, "sh")
        for item in expected:
            assert item in actual

    def test_invalid_command_raises_error(self, setup_containers):
        params = ["--invalid"]
        expected = "Invalid command"
        actual = exec_command(params, self.entry_point, "sh")
        assert expected in actual

    def test_update_database_works(self, setup_containers):
        expected = "vagas cadastradas"
        params = ["--update"]
        actual = exec_command(params, self.entry_point, "sh")
        assert expected in actual

    def test_main_initdb_runs_completely(self, setup_containers):
        params = ["--initdb"]
        expected = "Installation finished"
        actual = exec_command(params, self.entry_point, "sh")
        assert expected in actual

    def test_app_compare_curriculum_works(self, setup_containers):
        payload = dumps({
            "message": "test_message"
        })
        response = post(url=BASE_URL+"/receiver", data=payload, headers={"Content-Type": "application/json"})
        assert response.status_code == 200