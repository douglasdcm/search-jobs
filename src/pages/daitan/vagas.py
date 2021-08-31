from src.automation.automation import BaseObjects
from selenium.webdriver.common.by import By


class Vagas:

    def __init__(self, driver) -> None:
        self._driver = driver
        self._base_objects = BaseObjects(driver) 

    def scroll_to_next_button(self):
        by_type = By.XPATH
        locator = '//i[contains(@class,"angle right")]'
        self._base_objects.scroll_to_element(by_type, locator)

    def scroll_to_last_position(self):
        by_type = By.CSS_SELECTOR
        locator = 'a.header'
        elements = self._base_objects.get_all_elements(by_type, locator)
        last = elements[len(elements) - 1]
        self._base_objects.scroll_to_element(element=last)

    def go_to_next_page(self):
        by_type = By.XPATH
        locator = '//i[contains(@class,"angle right")]'
        self._base_objects.click(by_type, locator)

    def check_next_page_available(self):
        by_type = By.XPATH
        locator = '//i[contains(@class,"angle right")]'
        return self._base_objects.is_element_present(by_type, locator)

    def get_link_of_all_positons(self):
        by_type = By.CSS_SELECTOR
        locator = 'a.header'
        elements = self._base_objects.get_all_elements(by_type, locator)
        links = []
        for element in elements:
            links.append(self._base_objects.get_attribute_from_element(element, 'href'))
        return links
