from tests.helper import exec_command
import main
from tests.resources.fake_driver import FakeDriver

class TestMain:

    entry_point = "main.py"

    def test_invalid_command_raises_error(self):
        params = ["--invalid"]
        expected = "Invalid command"
        actual = exec_command(params, self.entry_point)
        assert expected in actual

    def test_initdb_raises_erro(self):
        params = ["--initdb"]
        expected = "could not translate host name \"postgres\" to address"
        actual = exec_command(params, self.entry_point)
        assert expected in actual

    def test_install_creates_database(self, monkeypatch):
        monkeypatch.setitem(main.DB_TYPE, "p", "sqlite")  # changing th database to sqlite  
        assert main.install(main.DB_NAME, "sqlite") is True

    def test_sanity_check_output_is_correct(self, monkeypatch):
        monkeypatch.setitem(main.DB_TYPE, "p", "sqlite")  # changing th database to sqlite
        monkeypatch.setattr(main, "ChromeDriver", FakeDriver)
        main.install(main.DB_NAME, "sqlite")
        params = ["--sanity-check"]
        assert main.main(params) is True

    def test_help_output_is_correct(self):
        params = ["--help"]
        expected = ["--initdb", "--help", "--sanity-check"]
        actual = exec_command(params, self.entry_point)
        for item in expected:
            assert item in actual