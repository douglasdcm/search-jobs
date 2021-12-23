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
                "enabled": True
            },
            {
                "company": mms.Mms(),
                "url": URLS["Mms"],
                "enabled": True
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
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Sap"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Mars"],
                "enabled": True
            },
            {
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
            {
                "company": generic.Generic(
                    kenoby_locator),
                "url": URLS["3Coracoes"],
                "enabled": True
            },
            {
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
                "company": generic.Generic(trab_conosco_locator),
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
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorAdm"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorBus"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorCor"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorCul"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorDes"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorDig"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorEng"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorExe"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorFin"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorFoo"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorLeg"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorOth"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorPro"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorRes"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorRoo"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorSal"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorSec"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorTal"],
                "enabled": True
            },
            {
                "company": generic.Generic(arcor_locator),
                "url": URLS["AccorWel"],
                "enabled": True
            },
            {
                "company": generic.Generic('//section[@class="box"]//h3//a'),
                "url": URLS["AllTests"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Eurofarma"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//div[@class="job-list paragrafo-ideal"]//div[@class="job-list-content"]//h4//a'),
                "url": URLS["GrupoSaga"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//div[contains(@class,"p-panel")]//a[@data-tag="displayJobTitle"]'),
                "url": URLS["HospitalEdmVasc"],
                "enabled": True
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["Hyundai"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//div[contains(@id,"jobs-cards-wrapper")]//a'),
                "url": URLS["IBM"],
                "enabled": True
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["IcatuSeguros"],
                "enabled": True
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["LibertySeguros"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//div[contains(@class,"spf-common-search-item-header")]//a'),
                "url": URLS["Logicalis"],
                "enabled": True
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["Jumpadtail"],
                "enabled": True
            },
            {
                "company": generic.Generic('//a[contains(@class, "ui-tabs-anchor")]'),
                "url": URLS["FeComercioDf"],
                "enabled": True
            },
            {
                "company": generic.Generic('//a[contains(@class,"navbar-brand")]'),
                "url": URLS["Agiel"],
                "enabled": True
            },
            {
                "company": generic.Generic('//a[contains(@class,"navbar-brand")]'),
                "url": URLS["EmployerEstagios"],
                "enabled": True
            },
            {
                "company": generic.Generic('//div[@class="informacoes-header"]//a'),
                "url": URLS["StagEstagios"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["MercSaoluiz"],
                "enabled": True
            },
            {
                "company": generic.Generic('//div[contains(@class,"multiline-data-container")]//span//a'),
                "url": URLS["Oracle"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Riachuelo"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Santander"],
                "enabled": True
            },
            {
                "company": generic.Generic('//nav[contains(@class,"menu-footer")]//a[text()="Trabalhe Conosco"]'),
                "url": URLS["Senac"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["SlcAgricola"],
                "enabled": True
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["Suzano"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["UberlandiaRefrescos"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["Unidas"],
                "enabled": True
            },
            {
                "company": generic.Generic(gupy_locator),
                "url": URLS["UnimedFortaleza"],
                "enabled": True
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["UnimedRio"],
                "enabled": True
            },
            {
                "company": generic.Generic('//td//a[contains(@class,"joblist__link job__position")]'),
                "url": URLS["Volvo"],
                "enabled": True
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["Wiz"],
                "enabled": True
            },
            {
                "company": generic.Generic('//h2//a[contains(@class,"au-target")]'),
                "url": URLS["Microsoft"],
                "enabled": True
            },
            {
                "company": generic.Generic(hotel_hilton_locator),
                "url": URLS["HiltonHotel"],
                "enabled": True
            },
            {
                "company": generic.Generic(trab_conosco_locator),
                "url": URLS["Schmersal"],
                "enabled": True
            },
            {
                "company": generic.Generic('//div[contains(@class,"apply-button-container")]//a'),
                "url": URLS["Bistrol"],
                "enabled": True
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["ICherry"],
                "enabled": True
            },
            {
                "company": generic.Generic(kenoby_locator),
                "url": URLS["Mirum"],
                "enabled": True
            },
            {
                "company": generic.Generic('//ol[contains(@class,"m-layout")]//a'),
                "url": URLS["Dll"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Ebanx"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Invision"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Harrys"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["DonorSchoose"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Lift"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["TripAdvisor"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["WillowTree"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Datto"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Thumbtack"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["VaynerMedia"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["KeepTruckin"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Checkr"],
                "enabled": True
            },
            {
                "company": generic.Generic(green_house_locator),
                "url": URLS["Nutrabolt"],
                "enabled": True
            },
            # {
            #     "company": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            #     "enabled": True
            # },
            # {
            #     "company": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            #     "enabled": True
            # },
            # {
            #     "company": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            #     "enabled": True
            # },
            # {
            #     "company": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            #     "enabled": True
            # },
            # Add new crawlers above
        ]
        return crawlers
