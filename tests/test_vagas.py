from pytest import mark
from src.pages.generic.positions import Positions
from tests.resources.fake_driver import FakeDriver


class TestVagas:
    @mark.asyncio
    async def test_get_link_of_all_positons_works(self, setup_db):
        locator = "href"
        vagas = Positions(FakeDriver())
        expected = [locator, locator, locator]
        actual = await vagas.get_link_of_all_positons(locator)
        assert actual == expected
