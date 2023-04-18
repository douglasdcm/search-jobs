from src.automation.automation import BaseObjects
from selenium.webdriver.common.by import By
from src.exceptions.exceptions import WebDriverError


class Positions:

    def __init__(self, driver) -> None:
        self._driver = driver
        self._base_objects = BaseObjects(driver)

    def get_link_of_all_positons(self, locator):
        try:
            by_type = By.XPATH
            elements = self._base_objects.get_all_elements(by_type, locator)
            links = []
            for element in elements:
                links.append(self._base_objects.get_attribute_from_element(element, 'href'))
            return links
        except Exception as error:
            raise WebDriverError(f"Could not get element(s). {str(error)}")


    def go_to_page(self, url):
        try:
            self._base_objects.navigate_to(url)
        except Exception as error:
            raise WebDriverError(f"Could not navidate to page {url}. {str(error)}")

    def get_description(self):
        try:
            by_type = By.TAG_NAME
            text = ""
            text += " " + self._base_objects.get_text(by_type, "body")
            text += " " + self._base_objects.get_text(by_type, "head")
            return text
        except Exception as error:
            raise WebDriverError(f"Could not get description from page. {str(error)}")
