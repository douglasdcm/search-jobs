from tests.helper import exec_command
from requests import post
from json import dumps
from tests.settings import BASE_URL
from os import environ
from pytest import mark


@mark.skip(reason="Need to fix the call to .sh files")
class TestEndToEndApp:

    def test_update_get_data_from_url(self):
        payload = dumps({
            "hash": ""
        })
        # exec_command("", "sh ./utils/make_dev.sh", "")
        response = post(url=BASE_URL+"/update", data=payload, headers={"Content-Type": "application/json"})
        assert response.content == 200

    def test_compare_curriculum_works(self):
        payload = dumps({
            "message": "test_message"
        })
        # exec_command("", "./utils/build_container.sh", "")
        response = post(url=BASE_URL+"/receiver", data=payload, headers={"Content-Type": "application/json"})
        assert response.status_code == 200