import app
from json import dumps
from src.database.db_factory import DbFactory
from src.helper.commands import install, clear
from pytest import fixture, mark
from tests.settings import BASE_URL
from ast import literal_eval



@mark.api
class TestApiCompare:

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


    @mark.parametrize(
        "payload,error_message", [
            (
                {
                    "message": "any_essage"
                },
                "Condição não informada"
            ),
            (
                {
                    "condition": "AND"
                },
                "Conteúdo não informado"
            ),
            (
                {
                    "message": "any",
                    "condition": "invalid"
                },
                "Condição inválida"
            ),
            (
                {
                    "message": "",
                    "condition": "or"
                },
                "Conteúdo não informado"
            ),
            (
                {
                    "message": "   ",
                    "condition": "or"
                },
                "Conteúdo inválido"
            )
        ]
    )
    def test_app_compare_curriculum_missing_data_in_payload(
        self, setup, payload, error_message
    ):
        payload = dumps(payload)
        response = app.app.test_client().post(
            "/api/receiver",
            data=payload,
            content_type="application/json")
        assert response.status_code == 500
        assert error_message in literal_eval(response.data.decode('utf-8')).get("message")


    def test_api_to_compare_curriculum_works(self, setup):
        payload = dumps({
            "message": "test_message",
            "condition": "or"
        })
        response = app.app.test_client().post(
            BASE_URL + "/api/receiver",
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 200


    @mark.parametrize(
        "message, response",
        [
            ("rabbit ãáà", "rabbit"),
            ("test", "test"),
            ("cats", "cat"),
            ("administração", "administrar"),
        ]
    )
    def test_compare_curriculum_returns_ranking_with_condition_or(
        self, monkeypatch, setup, message, response
    ):
        monkeypatch.setitem(app.DB_TYPE, "p", "sqlite")  # changing th database to sqlite
        payload = dumps({
            "message": message,
            "condition": "or"
        })
        expected = response.encode()
        response = app.app.test_client().post(
            "/api/receiver", content_type="application/json", data=payload)
        assert expected in response.data

    def test_compare_curriculum_returns_ranking_condition_and(self, monkeypatch, setup):
        message = "dog cow"
        monkeypatch.setitem(app.DB_TYPE, "p", "sqlite")  # changing th database to sqlite
        payload = dumps({
            "message": message,
            "condition": "and"
        })
        expected = "andcondition".encode()
        response = app.app.test_client().post(
            "/api/receiver", content_type="application/json", data=payload)
        assert expected in response.data
