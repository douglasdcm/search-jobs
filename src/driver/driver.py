from os import environ
from time import strftime
from logging import info
from src.constants import DRIVER_SERVER_URL
from src.constants import TIMEOUT
from src.exceptions.exceptions import WebDriverError
from caqui.easy.page import AsyncPage
from caqui.easy.capabilities import ChromeCapabilitiesBuilder
from caqui.easy.options import ChromeOptionsBuilder
from caqui.by import By


class Driver:
    def __init__(self) -> None:
        try:
            options = ChromeOptionsBuilder().args(["headless"]).to_dict()
            capabilities = (
                ChromeCapabilitiesBuilder()
                .accept_insecure_certs(True)
                .page_load_strategy("eager")
                .add_options(options)
            ).to_dict()
            self._driver = AsyncPage(DRIVER_SERVER_URL, capabilities)

        except Exception as e:
            raise WebDriverError(
                f"Unexpected error while initializing the webdriver. {str(e)}"
            ) from e

    async def start(self, url):
        try:
            await self._driver.get(url)
            await self._driver.refresh()
            await self._driver.implicitly_wait(TIMEOUT)
            return self._driver
        except Exception as e:
            raise WebDriverError(
                f"Unexpected error while starting the webdriver. {str(e)}"
            )

    async def save_screenshot(self):
        try:
            if environ.get("DEBUG") == "on":
                info("Taking screeshot.")
                file = f"./captures/screenshot_{strftime('%d-%m-%H-%M-%S')}.png"
                await self._driver.save_screenshot(file)
        except Exception as e:
            raise WebDriverError(
                f"Unexpected error while taking screeshot. {str(e)}"
            ) from e

    async def get_all_links(self):
        try:
            result = []
            links = await self._driver.find_elements(By.XPATH, "//a")
            for link in links:
                result.append(await link.get_property("href"))
            return result
        except Exception as e:
            raise WebDriverError(
                f"Unexpected error while getting URLs. {str(e)}"
            ) from e

    def quit(self):
        try:
            info("Finishing driver.")
            self._driver.quit()
        except Exception as e:
            raise WebDriverError(
                f"Unexpected error while finishing the webdriver. {str(e)}"
            ) from e
