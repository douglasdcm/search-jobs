from logging import info
from selenium.webdriver.support import wait
from src.settings import TIMEOUT
from src.exceptions.exceptions import WebDriverError
from os import environ


class BaseObjects:

    def __init__(self, driver):
        self._driver = driver
        self._wait = wait.WebDriverWait(driver, TIMEOUT)

    def _get_element(self, by_type, locator):
        if environ.get("DEBUG") == "on":
            info("Getting element '{}:{}'".format(by_type, locator))
        return self._driver.find_element(by_type, locator)

    def get_all_elements(self, by_type, locator):
        try:
            info("Getting all elements '{}:{}'".format(by_type, locator))
            elements = self._driver.find_elements(by_type, locator)
            if not elements:
                message = "No elements found. Skipping process"
                print(message)
                info(message)
            return elements
        except Exception as error:
            WebDriverError(f"Could not get elements. {str(error)}")

    def get_attribute_from_element(self, element, attribute):
        if environ.get("DEBUG") == "on":
            info("Getting attribute {} from element {}".format(attribute, element))
        return element.get_attribute(attribute)

    def wait_until_page_is_loaded(self, timeout=TIMEOUT):
        return self.wait_until(
            lambda _: self._driver.execute_script('return document.readyState') == 'complete',
            timeout=timeout)

    def wait_until(self, predicate, timeout=TIMEOUT, poll_frequency=0.001):
        return wait.WebDriverWait(self._driver, timeout, poll_frequency).until(predicate)

    def scroll_to_element(self, by_type=None, locator=None, element=None):
        if element is None:
            element = self._get_element(by_type, locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def navigate_to(self, url, timeout=TIMEOUT):
        info("Navigate to '{}'".format(url))
        self._driver.get(url)
        self.wait_until_page_is_loaded(timeout=timeout)

    def get_text(self, by_type=None, locator=None):
        try:
            return self._get_element(by_type, locator).text
        except Exception as error:
            raise WebDriverError(str(error)) from error

    def swith_to_frame(self, index=None, by_type=None, locator=None):
        """
        index (int)
        """
        if index:
            self._driver.switch_to.frame(index)
        if by_type:
            frame = self._get_element(by_type, locator)
            self._driver.switch_to.frame(frame)

    def switch_to_main_page(self):
        self._driver.switch_to.default_content()
