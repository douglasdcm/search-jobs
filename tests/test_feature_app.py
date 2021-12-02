from requests import post
from json import dumps
from tests.settings import BASE_URL


class TestFeatureApp:

    def test_app_compare_curriculum_works(self, setup_containers):
        payload = dumps({
            "message": "test_message"
        })
        response = post(url=BASE_URL+"/receiver", data=payload, headers={"Content-Type": "application/json"})
        assert response.status_code == 200