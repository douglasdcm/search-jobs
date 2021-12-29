import app
from json import dumps
from src.database.db_factory import DbFactory
from src.helper.commands import install, clear
from pytest import fixture, mark

@mark.api
class TestCompare:

    testdata = [
        ("rabbit ãáà", "rabbit"),
        ("test", "test"),
        ("", "Nenhum resultado encontrado."),
        ("cats", "cat"),
        ("administração", "administrar"),
    ]

    @fixture
    def setup(self):
        db_name = app.DB_NAME
        db_type = "sqlite"
        install(db_name, db_type)
        df = DbFactory(db_type)
        db = df.get_db(db_name)
        clear(db)
        fields = "url, description"
        db.salva_registro("positions", fields, "'https://test.com', 'test'")
        db.salva_registro("positions", fields, "'https://rabbit.com', 'rabbit'")
        db.salva_registro("positions", fields, "'https://cat.com', 'cats dogs cows'")
        db.salva_registro("positions", fields, "'https://administrar.com', 'administraca'")
        db.salva_registro("positions", fields, "'https://andcondition.com', 'cat dog rabbit cow cucumber'")

    def test_compare_empty_curriculum_returns_nothing(self, setup, monkeypatch):
        monkeypatch.setitem(app.DB_TYPE, "p", "sqlite")
        payload = dumps({
            "message": "",
            "condition": "or"
        })
        expected = b"Nenhum resultado encontrado."
        response = app.app.test_client().post("/receiver", content_type="application/json", data=payload)
        assert expected in response.data

    @mark.parametrize("message, response", testdata)
    def test_compare_curriculum_returns_ranking(self, monkeypatch, setup, message, response):
        monkeypatch.setitem(app.DB_TYPE, "p", "sqlite")  # changing th database to sqlite
        payload = dumps({
            "message": message,
            "condition": "or"
        })
        expected = response.encode()
        response = app.app.test_client().post("/receiver", content_type="application/json", data=payload)
        assert expected in response.data

    def test_compare_curriculum_returns_ranking(self, monkeypatch, setup):
        message = "dog cow"
        monkeypatch.setitem(app.DB_TYPE, "p", "sqlite")  # changing th database to sqlite
        payload = dumps({
            "message": message,
            "condition": "and"
        })
        expected = "andcondition".encode()
        response = app.app.test_client().post("/receiver", content_type="application/json", data=payload)
        assert expected in response.data

    def test_compare_curriculum_invalid_condition(self, monkeypatch, setup):
        message = "dog cow"
        monkeypatch.setitem(app.DB_TYPE, "p", "sqlite")  # changing th database to sqlite
        payload = dumps({
            "message": message,
            "condition": "xor"
        })
        expected = "Nenhum resultado encontrado.".encode()
        response = app.app.test_client().post("/receiver", content_type="application/json", data=payload)
        assert expected in response.data