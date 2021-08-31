import time, logging
from src.settings import LOGS_FOLDER, TIMEOUT, DEBUG
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class ChromeDriver:

    def __init__(self) -> None:
        logging.info("Starting driver.")
        chrome_options = Options()
        if DEBUG is False:
            chrome_options.add_argument("--headless")
        self._driver = webdriver.Chrome(options=chrome_options)

    def start(self, url):
        self._driver.get(url)
        self._driver.implicitly_wait(TIMEOUT)
        return self._driver

    def quit(self):
        logging.info("Finishing driver and taking screeshot.")
        file = "screenshot_" + time.strftime("%d-%m-%H-%M-%S") + ".png"
        self._driver.save_screenshot(LOGS_FOLDER + file)
        if DEBUG is False:
            self._driver.quit()
