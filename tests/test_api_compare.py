import app
from json import dumps
from src.database.db_factory import DbFactory
from src.helper.commands import install

class TestCompare:

    def setup(self):
        db_name = app.DB_NAME
        db_type = "sqlite"
        install(db_name, db_type)
        df = DbFactory(db_type)
        db = df.get_db(db_name)
        db.salva_registro("positions", "url, description", "'https://test_message.com', 'test_message'")
        db.salva_registro("positions", "url, description", "'https://noise1.com', 'noise1'")
        db.salva_registro("positions", "url, description", "'https://noise2.com', 'noise2'")

    def test_compare_empty_curriculum_returns_nothing(self):

        payload = dumps({
            "message": ""
        })
        expected = b"Nenhum resultado encontrado."
        response = app.app.test_client().post("/receiver", content_type="application/json", data=payload)
        assert expected in response.data

    def test_compare_curriculum_returns_ranking(self, monkeypatch):
        monkeypatch.setitem(app.DB_TYPE, "p", "sqlite")  # changing th database to sqlite
        payload = dumps({
            "message": "test_message"
        })
        expected = b"test_message"
        response = app.app.test_client().post("/receiver", content_type="application/json", data=payload)
        assert expected in response.data