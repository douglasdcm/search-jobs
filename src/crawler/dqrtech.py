
import requests
import logging
from src.helper.helper import cleanhtml
from src.pages.dqrtech.vagas import Vagas
from src.crawler.icrawler import ICrawler
from bs4 import BeautifulSoup as bs


class Dqrtech(ICrawler):

    def __init__(self, url, drive):
        self._url = url
        self._vagas = Vagas(drive)
        self._company = "DqrTech"

    def run(self):
        msg = "Running {} crawler...".format(self._company)
        print(msg)
        logging.info(msg)
        links = self._get_link_by_browser()
        descriptions = self._get_info_from_links(links)
        for i in range(len(links)):
            msg = f"Saving {i} from {len(links)}..."
            print(msg)
            logging.info(msg)
            self._save(links[i], descriptions[i])
        msg = "Data from {} saved.".format(self._company)
        print(msg)
        logging.info(msg)

    def _save(self, url, description):
        return super()._save(url, description)

    def _get_link_by_browser(self):        
        return self._vagas.get_link_of_all_positons()

    def _get_info_from_links(self, links):
        descriptions = []
        for link in links:
            self._vagas.go_to_page(link)
            page = self._vagas.get_text_of_body()
            txt = cleanhtml(page)
            print("===========================")
            print(link)
            logging.info(link)
            descriptions.append(txt)
        return descriptions






