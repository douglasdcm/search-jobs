import time, logging
from src.settings import DRIVER_DIR, LOGS_FOLDER, TIMEOUT, DEBUG
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from chromedriver_py import binary_path


class ChromeDriver:

    def __init__(self) -> None:
        logging.info("Starting driver.")
        chrome_options = Options()
        if DEBUG is False:
            chrome_options.add_argument("--headless")
        try:
            self._driver = webdriver.Chrome(executable_path=binary_path, options=chrome_options)
        except Exception as e:
            print(str(e))

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
