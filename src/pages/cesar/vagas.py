import logging
from src.helper.helper import cleanhtml
from src.automation.automation import BaseObjects
from selenium.webdriver.common.by import By


class Vagas:

    def __init__(self, driver) -> None:
        self._driver = driver
        self._base_objects = BaseObjects(driver)

    def get_link_of_all_positons(self):
        locator = '//a[@title="Apply"]'
        elements = self._base_objects.get_all_elements(By.XPATH, locator)
        links = []
        for element in elements:
            links.append(self._base_objects.get_attribute_from_element(element, 'href'))
        return links

    def go_to_page(self, url):
        self._base_objects.navigate_to(url)

    def get_description(self):
        locator = '//body/*'
        elements = self._base_objects.get_all_elements(By.XPATH, locator)
        descriptions = ""
        for element in elements:
            descriptions += self._base_objects.get_text(element=element)
        return descriptions
