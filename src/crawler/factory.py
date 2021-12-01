from src.crawler import (
    daitan,
    mms,
    generic
)
from src.settings import URLS


class Factory():


    def get_crawlers(self):
        """Return the list of enabled crawlers
        Returns:
            (list): list of tuples where the 1st item is the object of the crawler and se 2nd
                informs if it is enable (True). If enabled, the crawler will be executed by the
                server
        """
        gupy_locator = '//a[@class="job-list__item"]'
        kenoby_locator = '//div[@class="positions"]//div[@class="container"]//a'
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
                "company": generic.Generic('//a[contains(@class,"fade-square")]'),
                "url": URLS["Dqrtech"],
                "enabled": 1==1  # hack to return always true for test purposes
            },
            {
                "company": generic.Generic(
                    '//a[contains(@class,"wp-block-cit-block-ciandt-link")]'),
                "url": URLS["Ciandt"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Cesar"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["LeroyMerlin"],
                "enabled": False
            },
            {
                # TODO add a specific crawler to consider the pagination of the web page
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Sap"],
                "enabled": False
            },
            {
                # TODO add a specific crawler to consider the pagination of the web page
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Mars"],
                "enabled": False
            },
            {  # TODO make crawler get just the job description
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["Sabin"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="link"]'),
                "url": URLS["Novarts"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Viacredi"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//td[@data-title="Jobdescription"]/a'),
                "url": URLS["Roche"],
                "enabled": False
            },
            {  # TODO make crawler get just the job description
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["3Coracoes"],
                "enabled": False
            },
            {  # TODO make crawler get the next pages
                "company": generic.Generic(
                    '//div[contains(@class,"search-results__jobinfo")]/a'),
                "url": URLS["3M"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Aeris"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Vivo"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Cielo"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Embraer"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Totvs"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["ViaVarejo"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Gupy"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["GupyTech"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Ambev"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Gpa"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["PicPay"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Randon"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Dasa"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Promob"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Altamogiana"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Vereda"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["PmWeb"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Sicredi"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Cocacola"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Assai"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["PetLove"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Cotesa"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["TakeBlip"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Oi"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Marisa"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Atento"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Duratex"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["ShibataSupermercados"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["AguasAzuis"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["RedeBrasil"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="left-link"]'),
                "url": URLS["AstraZeneca"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["BancoBV"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["CeA"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["Danone"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["Alelo"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["CVC"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["PagueMenos"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["Kenoby"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="text-dark"]'),
                "url": URLS["AmplificaDigital"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="text-dark"]'),
                "url": URLS["ExpertiseGp"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["ClearSale"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//h3[@class="listSingleColumnItemTitle"]/a'),
                "url": URLS["Coats"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[contains(@class,"job-box")]'),
                "url": URLS["CopaEnergia"],
                "enabled": False
            },
            # Add new crawlers bellow
        ]
        return crawlers
