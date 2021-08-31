
import logging
from src.pages.dqrtech.vagas import Vagas
from src.crawler.icrawler import ICrawler


class Dqrtech(ICrawler):

    def __init__(self):
        self._url = None
        self._vagas = None

    def set_url(self, url):
        return super().set_url(url)

    def set_driver(self, driver):
        self._vagas = Vagas(driver)

    def run(self):
        links = self._get_link_by_browser()
        self._get_info_from_links(links)

    def _save(self, url, description):
        return super()._save(url, description)

    def _get_link_by_browser(self):
        return self._vagas.get_link_of_all_positons()

    def _get_info_from_links(self, links):
        for link in links:
            self._vagas.go_to_page(link)
            descriptions = self._vagas.get_text_of_body()
            print("===========================")
            print(link)
            logging.info(link)
            self._save(link, descriptions)






