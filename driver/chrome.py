from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config.settings import TIMEOUT


class ChromeDriver:

    def start(self, url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self._driver = webdriver.Chrome(options=chrome_options)
        self._driver.get(url)
        self._driver.implicitly_wait(TIMEOUT)
        return self._driver

    def quit(self):
        self._driver.quit()
