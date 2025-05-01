from time import strftime
from logging import info
from src.constants import SERVER_URL
from src.settings import DRIVER_DIR, LOGS_FOLDER, TIMEOUT
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from src.exceptions.exceptions import WebDriverError
from os import environ
from caqui.easy.page import AsyncPage
from caqui.easy.capabilities import ChromeCapabilitiesBuilder
from caqui.easy.options import ChromeOptionsBuilder
class Driver:

    def __init__(self) -> None:
        try:
            # chrome_options = Options()
            # info("Starting driver.")
            # chrome_options.add_argument("--headless")
            # chrome_options.add_argument('--no-sandbox')
            # print("Runnig driver from {}".format(DRIVER_DIR))
            # self._driver = webdriver.Chrome(executable_path=DRIVER_DIR,
            #                                 options=chrome_options)
            options = ChromeOptionsBuilder().args(["headless"]).to_dict()
            capabilities = (
                ChromeCapabilitiesBuilder()
                .accept_insecure_certs(True)
                .page_load_strategy("normal")
                .add_options(options)
            ).to_dict()
            self._driver = AsyncPage(SERVER_URL, capabilities)

        except Exception as error:
            info(str(error))
            raise WebDriverError(
                f"Unexpected error while initializing the webdriver. {str(error)}"
            ) from error

    async def start(self, url):
        try:
            await self._driver.get(url)
            await self._driver.implicitly_wait(TIMEOUT)
            return self._driver
        except Exception as error:
            info(str(error))
            raise WebDriverError(
                f"Unexpected error while starting the webdriver. {str(error)}"
            )

    async def quit(self):
        try:
            if environ.get("DEBUG") == "on":
                info("Taking screeshot.")
                file = "screenshot_" + strftime("%d-%m-%H-%M-%S") + ".png"
                await self._driver.save_screenshot(LOGS_FOLDER + file)
            info("Finishing driver.")
            self._driver.quit()
        except Exception as error:
            info(str(error))
            raise WebDriverError(
                f"Unexpected error while finishing the webdriver. {str(error)}"
            )
