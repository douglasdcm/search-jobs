from src.crawler import (
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
        arcor_locator = '//div[@class="content-block"]//a[@class="au-target"]'
        trab_conosco_locator = '//a[contains(@class,"job-box")]'
        hotel_hilton_locator = '//span[@role="heading"]//a[contains(@class,"au-target")]'
        green_house_locator = '//div[contains(@class,"opening")]//a'
        crawlers = [
            {
                "company": generic.Generic('//a[@class="header"]'),
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
                "enabled": False
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
                "enabled": True
            },
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["LeroyMerlin"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Sap"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Mars"],
                "enabled": False
            },
            {
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
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["3Coracoes"],
                "enabled": False
            },
            {
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
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["CopaEnergia"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["GrupoTrigo"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//section[@id="search-results-list"]//a'),
                "url": URLS["Dell"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorAdm"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorBus"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorCor"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorCul"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorDes"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorDig"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorEng"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorExe"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorFin"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorFoo"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorLeg"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorOth"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorPro"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorRes"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorRoo"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorSal"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorSec"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorTal"],
                "enabled": False
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorWel"],
                "enabled": False
            },
            {
                "company": generic.Generic('//section[@class="box"]//h3//a'),
                "url": URLS["AllTests"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Eurofarma"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//div[@class="job-list paragrafo-ideal"]//div[@class="job-list-content"]//h4//a'),
                "url": URLS["GrupoSaga"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//div[contains(@class,"p-panel")]//a[@data-tag="displayJobTitle"]'),
                "url": URLS["HospitalEdmVasc"],
                "enabled": False
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["Hyundai"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//div[contains(@id,"jobs-cards-wrapper")]//a'),
                "url": URLS["IBM"],
                "enabled": False
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["IcatuSeguros"],
                "enabled": False
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["LibertySeguros"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//div[contains(@class,"spf-common-search-item-header")]//a'),
                "url": URLS["Logicalis"],
                "enabled": False
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["Jumpadtail"],
                "enabled": False
            },
            {
                "company": generic.Generic('//a[contains(@class, "ui-tabs-anchor")]'),
                "url": URLS["FeComercioDf"],
                "enabled": False
            },
            {
                "company": generic.Generic('//a[contains(@class,"navbar-brand")]'),
                "url": URLS["Agiel"],
                "enabled": False
            },
            {
                "company": generic.Generic('//a[contains(@class,"navbar-brand")]'),
                "url": URLS["EmployerEstagios"],
                "enabled": False
            },
            {
                "company": generic.Generic('//div[@class="informacoes-header"]//a'),
                "url": URLS["StagEstagios"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["MercSaoluiz"],
                "enabled": False
            },
            {
                "company": generic.Generic('//div[contains(@class,"multiline-data-container")]//span//a'),
                "url": URLS["Oracle"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Riachuelo"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Santander"],
                "enabled": False
            },
            {
                "company": generic.Generic('//nav[contains(@class,"menu-footer")]//a[text()="Trabalhe Conosco"]'),
                "url": URLS["Senac"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["SlcAgricola"],
                "enabled": False
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["Suzano"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["UberlandiaRefrescos"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Unidas"],
                "enabled": False
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["UnimedFortaleza"],
                "enabled": False
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["UnimedRio"],
                "enabled": False
            },
            {
                "company": generic.Generic('//td//a[contains(@class,"joblist__link job__position")]'),
                "url": URLS["Volvo"],
                "enabled": False
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["Wiz"],
                "enabled": False
            },
            {
                "company": generic.Generic('//h2//a[contains(@class,"au-target")]'),
                "url": URLS["Microsoft"],
                "enabled": False
            },
            {
                "company": generic.Generic(hotel_hilton_locator),
                "url": URLS["HiltonHotel"],
                "enabled": False
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["Schmersal"],
                "enabled": False
            },
            {
                "company": generic.Generic('//div[contains(@class,"apply-button-container")]//a'),
                "url": URLS["Bistrol"],
                "enabled": False
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["ICherry"],
                "enabled": False
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["Mirum"],
                "enabled": False
            },
            {
                "company": generic.Generic('//ol[contains(@class,"m-layout")]//a'),
                "url": URLS["Dll"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Ebanx"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Invision"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Harrys"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["DonorSchoose"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Lift"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["TripAdvisor"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["WillowTree"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Datto"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Thumbtack"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["VaynerMedia"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["KeepTruckin"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Checkr"],
                "enabled": False
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Nutrabolt"],
                "enabled": False
            },
            # {
            #     "company": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            #     "enabled": False
            # },
            # {
            #     "company": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            #     "enabled": False
            # },
            # {
            #     "company": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            #     "enabled": False
            # },
            # {
            #     "company": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            #     "enabled": False
            # },
            # Add new crawlers above
        ]
        return crawlers
