from automation.automation import BaseObjects
from selenium.webdriver.common.by import By


class Vagas:

    def __init__(self, driver) -> None:
        self._driver = driver
        self._base_objects = BaseObjects(driver)

    def get_link_of_all_positons(self):
        by_type = By.XPATH
        locator = '//a[contains(@class,"fade-square")]'
        elements = self._base_objects.get_all_elements(by_type, locator)
        links = []
        for element in elements:
            links.append(self._base_objects.get_attribute_from_element(element, 'href'))
        return links