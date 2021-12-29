from requests import post
from json import dumps
from tests.settings import BASE_URL
from pytest import mark


@mark.feature
class TestFeatureApp:

    def test_app_compare_curriculum_works(self, setup_containers):
        payload = dumps({
            "message": "test_message",
            "condition": "or"
        })
        response = post(url=BASE_URL+"/receiver", data=payload, headers={"Content-Type": "application/json"})
        assert response.status_code == 200
