from logging import info
from src.crawler.icrawler import ICrawler
from src.pages.mms.vagas import Vagas


class Mms(ICrawler):

    def __init__(self):
        self._url = None
        self._vagas = None

    def set_driver(self, driver):
        self._vagas = Vagas(driver)

    def set_url(self, url):
        return super().set_url(url)

    def run(self, database):
        links = self._get_link_by_browser()
        self._get_info_from_links(database, links)
        return True

    def _save(self, database, url, description):
        return super()._save(database, url, description)

    def _get_link_by_browser(self):
        return self._vagas.get_link_of_all_positons()

    def _get_info_from_links(self, database, links):
        for link in links:
            print("===========================")
            print(link)
            info(link)
            self._vagas.go_to_page(link)
            descriptions = self._vagas.get_description()
            self._save(database, link, descriptions)
