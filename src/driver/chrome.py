import time
import logging
import traceback
import os
from src.settings import DRIVER_DIR, LOGS_FOLDER, TIMEOUT, DEBUG
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class ChromeDriver:

    def __init__(self) -> None:
        try:
            chrome_options = Options()
            if os.getenv('GOOGLE_CHROME_SHIM') is not None:  # used by Heroku only
                # GOOGLE_CHROME_SHIM = "/app/.apt/usr/bin/google-chrome-stable"
                logging.info("Starting driver.")
                if DEBUG is False:
                    chrome_options.add_argument("--headless")
                chrome_options.binary_location = os.getenv('GOOGLE_CHROME_SHIM')
                # print("Runnig driver from {}".format(os.getenv('GOOGLE_CHROME_SHIM')))
                self._driver = webdriver.Chrome(executable_path="chromedriver",
                                                options=chrome_options)
            else:
                logging.info("Starting driver.")
                if DEBUG is False:
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument('--no-sandbox')
                print("Runnig driver from {}".format(DRIVER_DIR))
                self._driver = webdriver.Chrome(executable_path=DRIVER_DIR,
                                                options=chrome_options)
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            raise

    def start(self, url):
        try:
            self._driver.get(url)
            self._driver.implicitly_wait(TIMEOUT)
            return self._driver
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            raise

    def quit(self):
        try:
            if DEBUG is False:
                logging.info("Taking screeshot.")
                file = "screenshot_" + time.strftime("%d-%m-%H-%M-%S") + ".png"
                self._driver.save_screenshot(LOGS_FOLDER + file)
                logging.info("Finishing driver.")
                self._driver.quit()
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            raise

    def close(self):
        try:
            if DEBUG is False:
                logging.info("Taking screeshot.")
                file = "screenshot_" + time.strftime("%d-%m-%H-%M-%S") + ".png"
                self._driver.save_screenshot(LOGS_FOLDER + file)
                logging.info("Finishing driver.")
                self._driver.close()
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            raise

    def start_session(self):
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "96.0.4664.45"
        }
        self._driver.start_session(capabilities)

