from src.helper.helper import data_pre_processing_portuguese, notify_by_email, validate_email
from pytest import mark

@mark.unit
class TestUnitHelper:

    testdata = [
        ("mecânico", "mecanico"),
        ("123", ""),
        ("@#$%", ""),
        ("ãáçä", "aaca"),
        ("", "")
    ]

    def test_is_invallid_email(self):
        assert validate_email("email.email.com") is False

    def test_is_vallid_email(self):
        assert validate_email("email@email.com") is True

    @mark.parametrize("message, result", testdata)
    def test_preprocessing_return_data_for_special_char(self, message, result):
        assert data_pre_processing_portuguese(message) == result

    @mark.skip(reason="Working")
    def test_notify_sends_email(self):
        assert notify_by_email("douglas.dcm@gmail.com", "test message") is True