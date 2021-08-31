from src.crawler import (
    daitan,
    dqrtech,
    mms,
    ciandt,
    cesar
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
                "enabled": False
            },
            {
                "company": mms.Mms(),
                "url": URLS["Mms"],
                "enabled": False
            },
            {
                "company": dqrtech.Dqrtech(),
                "url": URLS["Dqrtech"],
                "enabled": False
            },
            {
                "company": ciandt.Ciandt(),
                "url": URLS["Ciandt"],
                "enabled": False
            },
            {
                "company": cesar.Cesar(),
                "url": URLS["Cesar"],
                "enabled": True
            },
            # Add new crawlers bellow
        ]
        return crawlers
