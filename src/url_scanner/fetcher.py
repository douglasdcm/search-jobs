from src.driver.driver import Driver


class Fetcher:
    def __init__(self, driver: Driver):
        self._driver = driver

    async def extracts_all_links(self):
        return await self._driver.get_all_links()

    def normalizes_items(self, urls):
        pass

    def return_candidate_links(self, urls):
        return []
