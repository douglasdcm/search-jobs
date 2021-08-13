import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseObjects:

    def __init__(self, driver):
        self._driver = driver

    def __get_element(self, by_type, locator):
        logging.info("Getting element {}:{}".format(by_type, locator))
        return self._driver.find_element(by_type, locator)

    def get_all_elements(self, by_type, locator):
        logging.info("Getting all elements {}:{}".format(by_type, locator))
        return self._driver.find_elements(by_type, locator)

    def get_attribute_from_element(self, element, attribute):
        logging.info("Getting attribute {} from element {}".format(attribute, element))
        return element.get_attribute(attribute)

    def click(self, by_type, locator):
        logging.info("Cliking on element {}:{}".format(by_type, locator))
        self.__get_element(by_type, locator).click()

    def is_element_visible(self, by_type, locator):
        logging.info("Checking if element {}:{} is visible".format(by_type, locator))
        """Returns (bool)"""
        return EC.visibility_of_element_located((by_type, locator))(self._driver) is not False

    def is_element_present(self, by_type, locator):
        logging.info("Checking if element {}:{} is present".format(by_type, locator))
        """Returns (bool)"""
        return len(self.get_all_elements(by_type, locator)) > 0

    def wait_element_is_visible(self,by_type, locator):
        logging.info("Waiting element {}:{} be visible".format(by_type, locator))
        WebDriverWait(self._driver, timeout=3).until(EC.visibility_of_element_located((by_type, locator))(self._driver))
  
    def scroll_to_element(self, by_type=None, locator=None, element=None):
        if element is None:
            element = self.__get_element(by_type, locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
