import app
from json import dumps
from pytest import mark
from ast import literal_eval


@mark.functional
class TestApiOverwrite:

    def decode_reponse_in_dict(self, response):
        return literal_eval(response.data.decode('utf-8')).get("message")

    def test_does_not_overwrite_databse_if_incorrect_password(self):
        password = "incorrectpassword"
        payload = dumps({
            "password": password,
        })
        response = app.app.test_client().post(
            "/api/overwrite", content_type="application/json", data=payload)

        assert response.status_code == 404


    # @mark.skip("treggering crawler against real sites. need to mock the company pages")
    def test_overwrite_databse_if_correct_password(self):
        password = "anypassword"
        payload = dumps({
            "password": password,
        })
        response = app.app.test_client().post(
            "/api/overwrite", content_type="application/json", data=payload)

        assert response.status_code == 200
