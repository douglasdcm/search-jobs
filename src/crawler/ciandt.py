import logging
from src.crawler.icrawler import ICrawler
from src.pages.ciandt.vagas import Vagas


class Ciandt(ICrawler):

    def __init__(self):
        self._url = None
        self._vagas = None

    def set_driver(self, driver):
        self._vagas = Vagas(driver)

    def set_url(self, url):
        return super().set_url(url)

    def run(self):
        links = self._get_link_by_browser()
        self._get_info_from_links(links)

    def _save(self, url, description):
        return super()._save(url, description)

    def get_url(self):
        return super().get_url()

    def _get_link_by_browser(self):
        return self._vagas.get_link_of_all_positons()

    def _get_info_from_links(self, links):
        for link in links:
            print("===========================")
            print(link)
            logging.info(link)
            self._vagas.go_to_page(link)
            descriptions = self._vagas.get_description()
            self._save(link, descriptions)
