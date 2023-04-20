from src.helper.helper import data_pre_processing_portuguese, steam_data
from pytest import mark


@mark.functional
class TestUnitHelper:

    testdata = [
        ("mecân", "mecan"),
        ("123", ""),
        ("@#$%", ""),
        ("ãáçäx", "aacax"),
        ("", ""),
        ("administração", "administraca")
    ]

    steamdata = [
        ("maravilhoso", "maravilh"),
        ("vejam", "vej"),
        ("administrar", "administr"),
        ("testes", "test"),
        ("tests", "test"),
        ("cats", "cat"),
    ]

    @mark.parametrize("message, result", testdata)
    def test_preprocessing_return_data_for_special_char(self, message, result):
        assert data_pre_processing_portuguese(message) == result

    @mark.parametrize("message, result", steamdata)
    def test_steamming_is_striping_the_text(self, message, result):
        assert steam_data(message) == result

    def test_steamming_is_striping_the_list_of_texts(self):
        texts = ["cats", "dogs"]
        expected = ["cat", "dog"]
        actual = [steam_data(t) for t in texts]
        assert set(actual) == set(expected)

    def test_preprocessing_works_with_list_of_texts(self):
        text = "cats dogs administração testes analista"
        expected = ["cat", "dog", "administraca", "test", "anal"]
        actual = data_pre_processing_portuguese(text)
        for term in expected:
            assert term in actual


    