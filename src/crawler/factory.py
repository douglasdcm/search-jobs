from re import T
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
                "company": generic.Generic('//a[@class="header"]'),
                "url": URLS["Daitan"],
                "enabled": True
            },
            {
                "company": mms.Mms(),
                "url": URLS["Mms"],
                "enabled": 1 == 0
            },
            {
                "company": generic.Generic('//a[contains(@class,"fade-square")]'),
                "url": URLS["Dqrtech"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[contains(@class,"wp-block-cit-block-ciandt-link")]'),
                "url": URLS["Ciandt"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Cesar"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
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
                    kenoby_locator),
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
                    gupy_locator),
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
                    kenoby_locator),
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
                    gupy_locator),
                "url": URLS["Aeris"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Vivo"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Cielo"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Embraer"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Totvs"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["ViaVarejo"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Gupy"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["GupyTech"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Ambev"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Gpa"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["PicPay"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Randon"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Dasa"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Promob"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Altamogiana"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Vereda"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["PmWeb"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Sicredi"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Cocacola"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Assai"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["PetLove"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Cotesa"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["TakeBlip"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Oi"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Marisa"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Atento"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["Duratex"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["ShibataSupermercados"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["AguasAzuis"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    gupy_locator),
                "url": URLS["RedeBrasil"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="left-link"]'),
                "url": URLS["AstraZeneca"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["BancoBV"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["CeA"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["Danone"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["Alelo"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["CVC"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["PagueMenos"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["Kenoby"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="text-dark"]'),
                "url": URLS["AmplificaDigital"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="text-dark"]'),
                "url": URLS["ExpertiseGp"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["ClearSale"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//h3[@class="listSingleColumnItemTitle"]/a'),
                "url": URLS["Coats"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[contains(@class,"job-box")]'),
                "url": URLS["CopaEnergia"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["GrupoTrigo"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//section[@id="search-results-list"]//a'),
                "url": URLS["Dell"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//div[@class="content-block"]//a[@class="au-target"]'),
                "url": URLS["ArcorAdm"],
                "enabled": True
            },
            # Add new crawlers bellow
        ]
        return crawlers
