import logging
from src.crawler.icrawler import ICrawler


class Toy(ICrawler):
    """This is used just to validate the system configuration"""

    def __init__(self):
        self._url = None

    def set_driver(self, driver):
        """Do nothing"""
        pass

    def set_url(self, url):
        return super().set_url(url)

    def run(self, database):
        links = self._get_link_by_browser()
        descriptions = self._get_info_from_links(links)
        for i in range(len(links)):
            msg = f"Saving {i+1} from {len(links)}..."
            print(msg)
            logging.info(msg)
            self._save(database, links[i], descriptions[i])
        return True

    def _save(self, database,  url, description):
        return super()._save(database, url, description)

    def get_url(self):
        return super().get_url()

    def _get_link_by_browser(self):
        return [
            "http://toy.com/position_1",
            "http://toy.com/position_2",
            "http://toy.com/position_3"
        ]

    def _get_info_from_links(self, links):
        toy_descriptions = [
            "Description position 1",
            "Description position 2",
            "Description position 3"
        ]
        descriptions = []
        for i in range(len(links)):
            descriptions.append(toy_descriptions[i])
        return descriptions
