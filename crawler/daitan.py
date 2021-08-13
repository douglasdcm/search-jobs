import logging
from pages.daitan.vagas import Vagas
import requests
from bs4 import BeautifulSoup as bs
from crawler.icrawler import ICrawler


class Daitan(ICrawler):

    def __init__(self, url, drive):
        self._url = url
        self._vagas = Vagas(drive)

    def run(self):
        msg = "Running Daitan crawler..."
        print(msg)
        logging.info(msg)
        links = self._get_link_by_browser()
        descriptions = self._get_info_from_links(links)
        for i in range(len(links)):
            msg = f"Saving {i} from {len(links)}..."
            print(msg)
            logging.info(msg)
            self._save(links[i], descriptions[i])
        msg = "Data from Daitan saved."
        print(msg)
        logging.info(msg)

    def _save(self, url, description):
        return super()._save(url, description)

    def _get_link_by_browser(self):        
        links = []
        next_ = True
        while next_:
            elements = self._vagas.get_link_of_all_positons()
            for element in elements:
                links.append(element)
            next_ = self._vagas.check_next_page_available()
            if next_:
                self._vagas.scroll_to_last_position()
                self._vagas.go_to_next_page()
        return links

    def _get_info_from_links(self, links):
        descriptions = []
        for link in links:
            page = requests.get(link)
            soup = bs(page.content, 'html.parser')
            result = soup.find_all('li')
            print("===========================")
            print(link)
            logging.info(link)
            txt = ""
            for item in result:
                txt += item.get_text() + "\n"
            descriptions.append(txt)
        return descriptions



