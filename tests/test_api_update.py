import app
from pytest import fixture
from json import dumps
from os import environ
from tests.helper import populate_database
from tests.resources.fake_driver import FakeDriver

class Testupdate:

    hash = "dev"
    db_type = "sqlite"

    def test_update_clear_database(self, monkeypatch):
        monkeypatch.setitem(app.DB_TYPE, "p", self.db_type)  # changing th database to sqlite
        monkeypatch.setattr(app, "ChromeDriver", FakeDriver)
        payload = dumps({"hash": self.hash})
        expected = b"OK\n"
        response = app.app.test_client().post("/update", content_type="application/json", data=payload)
        assert expected in response.data
