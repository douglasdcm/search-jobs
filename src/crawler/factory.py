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
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Viacredi"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//td[@data-title="Jobdescription"]/a'),
                "url": URLS["Roche"],
                "enabled": True
            },
            {  # TODO make crawler get just the job description
                "company": generic.Generic(
                    '//div[@class="positions"]//div[@class="container"]//a'),
                "url": URLS["3Coracoes"],
                "enabled": True
            },
            {  # TODO make crawler get the next pages
                "company": generic.Generic(
                    '//div[contains(@class,"search-results__jobinfo")]/a'),
                "url": URLS["3M"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Aeris"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Vivo"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Cielo"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Embraer"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Totvs"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["ViaVarejo"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Gupy"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["GupyTech"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Ambev"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Gpa"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["PicPay"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Randon"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Dasa"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Promob"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Altamogiana"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Vereda"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["PmWeb"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Sicredi"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Cocacola"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Assai"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["PetLove"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Cotesa"],
                "enabled": True
            },
            # Add new crawlers bellow
        ]
        return crawlers
