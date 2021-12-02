import main
from tests.resources.fake_driver import FakeDriver
from pytest import mark

@mark.skip(reason="To de removed")
class TestMain:

    entry_point = "main.py"

    def test_install_creates_database(self, monkeypatch):
        monkeypatch.setitem(main.DB_TYPE, "p", "sqlite")  # changing th database to sqlite  
        assert main.install(main.DB_NAME, "sqlite") is True

    def test_install_creates_database(self, monkeypatch):
        monkeypatch.setitem(main.DB_TYPE, "p", "sqlite")  # changing th database to sqlite  
        assert main.install(main.DB_NAME, "sqlite") is True

    def test_sanity_check_output_is_correct(self, monkeypatch):
        monkeypatch.setitem(main.DB_TYPE, "p", "sqlite")  # changing th database to sqlite
        monkeypatch.setattr(main, "ChromeDriver", FakeDriver)
        main.install(main.DB_NAME, "sqlite")
        params = ["--sanity-check"]
        assert main.main(params) is True
