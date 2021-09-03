from src.automation.automation import BaseObjects
from selenium.webdriver.common.by import By


class Vagas:

    def __init__(self, driver) -> None:
        self._driver = driver
        self._base_objects = BaseObjects(driver)

    def get_link_of_all_positons(self, locator):
        by_type = By.XPATH
        elements = self._base_objects.get_all_elements(by_type, locator)
        links = []
        for element in elements:
            links.append(self._base_objects.get_attribute_from_element(element, 'href'))
        return links

    def go_to_page(self, url):
        self._base_objects.navigate_to(url)

    def get_description(self):
        by_type = By.CSS_SELECTOR
        locator = "body"
        return self._base_objects.get_text(by_type, locator)
