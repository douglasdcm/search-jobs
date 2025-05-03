from logging import exception, info
from src.pages.generic.positions import Positions
from src.exceptions.exceptions import WebDriverError, CrawlerError
from os import environ
from src.helper.helper import save_description_to_database


class Generic:
    def __init__(self, locator):
        """
        This is what the name says: a generic crawler. It is intended to be used if the company's
            page that has all the links of positions available in a single page without pagination.
            Take the page bellow:
            (...)
                <div class="menu-container">
                    <a class = "menu" herf="www.fake.com">
                </div>
                <div class="positions-container>
                    <a class = "positions" href="www.fake.com/jobs/position_1">
                    <a class = "positions" href="www.fake.com/jobs/position_2">
                    <a class = "positions" href="www.fake.com/jobs/position_3">
                </div>
            (...)
            The locators a.positions (css locator) are the ones we are looking for.
        Arsg:
            locator (str): the locator of the links of positions, e.g. a.positions
        """
        self._url = None
        self._positions = None
        self.locator = locator

    def set_driver(self, driver):
        self._positions = Positions(driver)

    def set_url(self, url):
        self.url = url

    async def run(self):
        links = await self._get_link_by_browser()
        return await self._get_info_from_links(links)

    async def _get_link_by_browser(self):
        return await self._positions.get_link_of_all_positons(self.locator)

    async def _get_info_from_links(self, links):
        for link in links:
            try:
                # It is necessary because the function `Element.get_attribute`
                # does not return a Coroutine
                if not isinstance(link, str):
                    link = await link
                info(f"Collecting data from postion '{link}'")
                await self._positions.go_to_page(link)
                save_description_to_database(
                    link,
                    await self._positions.get_description(),
                )
            except WebDriverError as error:
                message = f"Skipping process. Failed to get data from {link}"
                exception(message)
                if environ.get("DEBUG") == "on":
                    raise CrawlerError(str(error)) from error
            except Exception as error:
                raise CrawlerError(str(error)) from error
        return True
