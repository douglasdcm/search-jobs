import time, logging
from src.settings import DRIVER_DIR, LOGS_FOLDER, TIMEOUT, DEBUG
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class ChromeDriver:

    def __init__(self) -> None:
        try:
            logging.info("Starting driver.")
            chrome_options = Options()
            if DEBUG is False:
                chrome_options.add_argument("--headless")
                print(DRIVER_DIR)
                self._driver = webdriver.Chrome(executable_path=DRIVER_DIR, options=chrome_options)
        except Exception as e:
            print(str(e))

    def start(self, url):
        try:
            self._driver.get(url)
            self._driver.implicitly_wait(TIMEOUT)
            return self._driver
        except Exception as e:
            print(str(e))

    def quit(self):
        try:
            logging.info("Finishing driver and taking screeshot.")
            file = "screenshot_" + time.strftime("%d-%m-%H-%M-%S") + ".png"
            self._driver.save_screenshot(LOGS_FOLDER + file)
            if DEBUG is False:
                self._driver.quit()
        except Exception as e:
            print(str(e))
