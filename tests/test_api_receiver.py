import app
from json import dumps
from pytest import mark
from tests.settings import BASE_URL
from ast import literal_eval


@mark.functional
class TestApiCompare:

    def decode_reponse_in_dict(self, response):
        return literal_eval(response.data.decode('utf-8')).get("message")

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
                "Currículo não informado"
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
                "Currículo não informado"
            ),
            (
                {
                    "message": "   ",
                    "condition": "or"
                },
                "Currículoinválido"
            )
        ]
    )
    def test_app_compare_curriculum_missing_data_in_payload(
        self, payload, error_message
    ):
        payload = dumps(payload)
        response = app.app.test_client().post(
            "/api/receiver",
            data=payload,
            content_type="application/json")
        assert response.status_code == 500
        assert error_message in self.decode_reponse_in_dict(response)


    def test_api_to_compare_curriculum_works(self, setup_db):
        payload = dumps({
            "message": "jira python manager",
            "condition": "or"
        })
        response = app.app.test_client().post(
            BASE_URL + "/api/receiver",
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 200

    def test_compare_curriculum_returns_ranking_with_condition_or(self, setup_db):
        resume = "jira manager"
        payload = dumps({
            "message": resume,
            "condition": "or"
        })
        expected_1 = "position1"
        expected_2 = "position2"
        expected_3 = "position3"

        response = app.app.test_client().post(
            "/api/receiver", content_type="application/json", data=payload)

        assert expected_1 in str(self.decode_reponse_in_dict(response))
        assert expected_2 in str(self.decode_reponse_in_dict(response))
        assert expected_3 in str(self.decode_reponse_in_dict(response))

    def test_compare_curriculum_returns_ranking_condition_and(self, setup_db):
        message = "jira manager"
        payload = dumps({
            "message": message,
            "condition": "and"
        })
        expected_1 = "position1"
        expected_2 = "position2"
        expected_3 = "position3"
        response = app.app.test_client().post(
            "/api/receiver", content_type="application/json", data=payload)
        assert expected_1 in str(self.decode_reponse_in_dict(response))
        assert expected_2 not in str(self.decode_reponse_in_dict(response))
        assert expected_3 not in str(self.decode_reponse_in_dict(response))
