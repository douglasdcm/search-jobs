import logging
from src.helper.helper import cleanhtml
from src.automation.automation import BaseObjects
from selenium.webdriver.common.by import By


class Vagas:

    def __init__(self, driver) -> None:
        self._driver = driver
        self._base_objects = BaseObjects(driver) 

    def get_link_of_all_positons(self):
        self._base_objects.swith_to_frame(1)
        locator = '//a[text()="Department"]'
        self._base_objects.scroll_to_element(By.XPATH, locator)
        locator = '//div[@class="gnewtonCareerGroupJobTitleClass"]//a'
        elements = self._base_objects.get_all_elements(By.XPATH, locator)
        links = []
        for element in elements:
            links.append(self._base_objects.get_attribute_from_element(element, 'href'))
        self._base_objects.switch_to_main_page()
        return links

    def go_to_page(self, url):
        self._base_objects.navigate_to(url)        

    def get_text_of_body(self):
        by_type = By.CSS_SELECTOR
        locator = "body"
        return self._base_objects.get_text(by_type, locator)

    def get_description(self):
        self._base_objects.swith_to_frame(by_type=By.CSS_SELECTOR, locator='iframe#gnewtonIframe')
        locator = '//body/*'
        elements = self._base_objects.get_all_elements(By.XPATH, locator)
        descriptions = ""
        for element in elements:
            descriptions += self._base_objects.get_text(element=element)
        self._base_objects.switch_to_main_page()
        return descriptions
