from src.settings import LOGS_FOLDER, TIMEOUT, DEBUG, DRIVER_DIR
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class ChromeDriver:

    def start(self, url):
        chrome_options = Options()
        if DEBUG is False:
            chrome_options.add_argument("--headless")
        self._driver = webdriver.Chrome(options=chrome_options)
        self._driver.get(url)
        self._driver.implicitly_wait(TIMEOUT)
        return self._driver

    def quit(self):
        self._driver.save_screenshot(LOGS_FOLDER + "screenshot.png")
        if DEBUG is False:
            self._driver.quit()
