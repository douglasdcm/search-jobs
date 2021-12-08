from time import strftime
from logging import info
from traceback import print_tb
from os import getenv
from src.settings import DRIVER_DIR, LOGS_FOLDER, TIMEOUT, DEBUG
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class ChromeDriver:

    def __init__(self) -> None:
        try:
            chrome_options = Options()
            if getenv('GOOGLE_CHROME_SHIM') is not None:  # used by Heroku only
                info("Starting driver.")
                if DEBUG is False:
                    chrome_options.add_argument("--headless")
                chrome_options.binary_location = getenv('GOOGLE_CHROME_SHIM')
                self._driver = webdriver.Chrome(executable_path="chromedriver",
                                                options=chrome_options)
            else:
                info("Starting driver.")
                if DEBUG is False:
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument('--no-sandbox')
                print("Runnig driver from {}".format(DRIVER_DIR))
                self._driver = webdriver.Chrome(executable_path=DRIVER_DIR,
                                                options=chrome_options)
        except Exception as e:
            print_tb(e.__traceback__)

    def start(self, url):
        try:
            self._driver.get(url)
            self._driver.implicitly_wait(TIMEOUT)
            return self._driver
        except Exception as e:
            print_tb(e.__traceback__)

    def quit(self):
        try:
            if DEBUG is False:
                info("Taking screeshot.")
                file = "screenshot_" + strftime("%d-%m-%H-%M-%S") + ".png"
                self._driver.save_screenshot(LOGS_FOLDER + file)
                info("Finishing driver.")
                self._driver.quit()
        except Exception as e:
            print_tb(e.__traceback__)
