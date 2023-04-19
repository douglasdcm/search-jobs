from src.pages.generic.positions import Positions
from tests.resources.fake_driver import FakeDriver


class TestVagas:
    def test_get_link_of_all_positons_works(self, setup_db):
        locator = "href"
        vagas = Positions(FakeDriver())
        expected = [locator, locator, locator]
        actual = vagas.get_link_of_all_positons(locator)
        assert actual == expected
