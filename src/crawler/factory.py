from src.crawler import (
    daitan,
    dqrtech,
    mms,
    ciandt,
    cesar,
    generic
)
from src.settings import URLS



class Factory():


    def get_crawlers(self):
        """Retunr the list of enabled crawlers
        Returns:
            (list): list of tuples where the 1st item is the object of the crawler and se 2nd
                informs if it is enable (True). If enabled, the crawler will be executed by the
                server
        """
        crawlers = [
            {
                "company": daitan.Daitan(),
                "url": URLS["Daitan"],
                "enabled": True
            },
            {
                "company": mms.Mms(),
                "url": URLS["Mms"],
                "enabled": True
            },
            {
                "company": dqrtech.Dqrtech(),
                "url": URLS["Dqrtech"],
                "enabled": True
            },
            {
                "company": ciandt.Ciandt(),
                "url": URLS["Ciandt"],
                "enabled": True
            },
            {
                "company": cesar.Cesar(),
                "url": URLS["Cesar"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//div[@class="positions"]//div[@class="container"]//a'),
                "url": URLS["LeroyMerlin"],
                "enabled": True
            },
            {
                # TODO add a specific crawler to consider the pagination of the web page
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Sap"],
                "enabled": True
            },
            {
                # TODO add a specific crawler to consider the pagination of the web page
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Mars"],
                "enabled": True
            },
            {  # TODO make crawler get just the job description
                "company": generic.Generic(
                    '//div[@class="positions"]//div[@class="container"]//a'),
                "url": URLS["Sabin"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="link"]'),
                "url": URLS["Novarts"],
                "enabled": True
            },
            # Add new crawlers bellow
        ]
        return crawlers
