from src.driver.driver import Driver


class Fetcher:
    def __init__(self, driver: Driver):
        self._driver = driver

    async def extracts_all_links(self):
        return await self._driver.get_all_links()

    def return_candidate_links(self, urls):
        result = []
        for url in urls:
            original_url = url
            url = url.lower()
            for term in ["career", "carreir", "job", "opportun", "talent"]:
                if term in url:
                    result.append(original_url)
        return list(set(result))
