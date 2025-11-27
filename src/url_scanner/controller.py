from src.constants import COMPANY_OUTPUT
from src.driver.driver import Driver
from src.url_scanner.fetcher import Fetcher
from logging import warning


class Controller:
    def __init__(self, driver: Driver):
        self._driver = driver

    async def run_fetcher(self):
        fetcher = Fetcher(self._driver)
        urls = await fetcher.extracts_all_links()
        return fetcher.return_candidate_links(urls)

    def save_output(self, best_links, save):
        if not save:
            return
        with open(COMPANY_OUTPUT, "a") as f:
            for link in best_links:
                f.write(f"{link}\n")

    async def execute(self, save=True):
        best_links = await self.run_fetcher()
        if not best_links:
            warning(f"{self._driver.current_url} No link found")
        self.save_output(best_links, save)
        return best_links
