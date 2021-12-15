from src.helper.helper import data_pre_processing_portuguese
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

    @mark.parametrize("message, result", testdata)
    def test_preprocessing_return_data_for_special_char(self, message, result):
        assert data_pre_processing_portuguese(message) == result