# import asyncio
# from time import strftime
# from logging import info
# from src.constants import SERVER_URL
# from src.constants import DRIVER_DIR, LOGS_FOLDER, TIMEOUT
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from src.exceptions.exceptions import WebDriverError
# from os import environ
# from caqui.easy.page import AsyncPage
# from caqui.easy.capabilities import ChromeCapabilitiesBuilder
# from caqui.easy.options import ChromeOptionsBuilder
# import pytest


# @pytest.mark.asyncio
# async def test_smoke():
#     options = (
#         ChromeOptionsBuilder()
#         # .args(["headless"])
#         .to_dict()
#     )
#     capabilities = (
#         ChromeCapabilitiesBuilder()
#         .accept_insecure_certs(True)
#         .page_load_strategy("normal")
#         .add_options(options)
#     ).to_dict()
#     page = AsyncPage(SERVER_URL, capabilities)
#     await page.get("https://www.mobilityware.com/all-jobs")
