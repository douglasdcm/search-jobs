from time import strftime
from logging import info
from src.settings import DRIVER_DIR, LOGS_FOLDER, TIMEOUT
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from src.exceptions.exceptions import WebDriverError
from os import environ


class ChromeDriver:

    def __init__(self) -> None:
        try:
            chrome_options = Options()
            info("Starting driver.")
            # chrome_options.add_argument("--headless")
            chrome_options.add_argument('--no-sandbox')
            print("Runnig driver from {}".format(DRIVER_DIR))
            self._driver = webdriver.Chrome(executable_path=DRIVER_DIR,
                                            options=chrome_options)
        except Exception as error:
            info(str(error))
            raise WebDriverError(
                f"Unexpected error while initializing the webdriver. {str(error)}"
            )

    def start(self, url):
        try:
            self._driver.get(url)
            self._driver.implicitly_wait(TIMEOUT)
            return self._driver
        except Exception as error:
            info(str(error))
            raise WebDriverError(
                f"Unexpected error while starting the webdriver. {str(error)}"
            )

    def quit(self):
        try:
            if environ.get("DEBUG") == "on":
                info("Taking screeshot.")
                file = "screenshot_" + strftime("%d-%m-%H-%M-%S") + ".png"
                self._driver.save_screenshot(LOGS_FOLDER + file)
            info("Finishing driver.")
            self._driver.quit()
        except Exception as error:
            info(str(error))
            raise WebDriverError(
                f"Unexpected error while finishing the webdriver. {str(error)}"
            )
