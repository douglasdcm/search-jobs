import asyncio
from src.automation.automation import BaseObjects
from src.exceptions.exceptions import WebDriverError
from caqui.by import By

class Positions:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._base_objects = BaseObjects(driver)
        self._links = None

    async def get_link_of_all_positons(self, locator):
        try:
            by_type = By.XPATH
            elements = await self._base_objects.get_all_elements(by_type, locator)
            tasks = []
            for element in elements:
                tasks.append(await self._base_objects.get_attribute_from_element(element, "href"))
            return await asyncio.gather(*tasks)
        except Exception as error:
            raise WebDriverError(f"Could not get element(s). {str(error)}") from error

    async def go_to_page(self, url):
        try:
            await self._base_objects.navigate_to(url)
        except Exception as error:
            raise WebDriverError(f"Could not navidate to page {url}. {str(error)}")

    async def get_description(self):
        try:
            by_type = By.TAG_NAME
            text = ""
            text += " " + await self._base_objects.get_text(by_type, "body")
            text += " " + await self._base_objects.get_text(by_type, "head")
            return text
        except Exception as error:
            raise WebDriverError(f"Could not get description from page. {str(error)}")
