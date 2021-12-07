from requests import post
from json import dumps
from tests.settings import BASE_URL
from pytest import mark


@mark.performance
class TestPerformceApp:

    def test_app_compare_curriculum_works_1000_times(self, setup_containers):

        payload = dumps({
            "message": "test_message"
        })
        limite = 1000
        for _ in range(limite):
            response = post(url=BASE_URL+"/receiver", data=payload, headers={"Content-Type": "application/json"})
            assert response.status_code == 200