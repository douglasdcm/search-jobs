from src.pages.generic.vagas import Vagas
from tests.resources.fake_driver import FakeDriver

class TestVagas:

    def test_get_link_of_all_positons_works(self, setup_db):
        locator = "href"
        vagas = Vagas(FakeDriver())
        expected = [locator, locator, locator]
        actual = vagas.get_link_of_all_positons(locator)
        assert actual == expected
