import logging
from pages.daitan.vagas import Vagas
import requests
from bs4 import BeautifulSoup as bs
from crawler.icrawler import ICrawler


class Factory(ICrawler):

    def __init__(self, crawler):
        self.crawler = crawler
        self.url = crawler.get_url()

    def run(self):
        msg = "Running crawler: '{}'".format(self.url)
        print(msg)
        logging.info(msg)
        self.crawler.run()
        msg = "Data saved."
        print(msg)
        logging.info(msg)

    def _save(self, url, description):
        self.crawler.save()
