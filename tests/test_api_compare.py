import app
from json import dumps
from src.database.db_factory import DbFactory
from src.helper.commands import clear, install
from pytest import fixture, mark

@mark.api
class TestCompare:

    @fixture
    def setup(self):
        db_name = app.DB_NAME
        db_type = "sqlite"
        df = DbFactory(db_type)
        db = df.get_db(db_name)
        clear(db)
        install(db_name, db_type)
        db.salva_registro("positions", "url, description", "'https://test_message.com', 'test_message'")

    def test_compare_empty_curriculum_returns_nothing(self, setup, monkeypatch):
        monkeypatch.setitem(app.DB_TYPE, "p", "sqlite")
        payload = dumps({
            "message": ""
        })
        expected = b"Nenhum resultado encontrado."
        response = app.app.test_client().post("/receiver", content_type="application/json", data=payload)
        assert expected in response.data

    def test_compare_curriculum_returns_ranking(self, monkeypatch, setup):
        monkeypatch.setitem(app.DB_TYPE, "p", "sqlite")  # changing th database to sqlite
        payload = dumps({
            "message": "test_message"
        })
        expected = b"test_message"
        response = app.app.test_client().post("/receiver", content_type="application/json", data=payload)
        assert expected in response.data