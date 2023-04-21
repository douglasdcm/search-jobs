from src.crawler import generic
from src.settings import URLS


class Company():
    def get_all(self):
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
        companies = [
            {
                "crawler": generic.Generic('//a[contains(@title,"Veja detalhes")]'),
                "url": "https://www.dqrtech.com.br/vagas/"
            },
            {
                "crawler": generic.Generic(
                    '//a[contains(@class,"wp-block-cit-block-ciandt-link")]'),
                "url": "https://ciandt.com/us/en-us/careers/open-positions"
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": "https://vagascesar.gupy.io"
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": "https://jobs.kenoby.com/leroymerlin"
            },
            {
                "crawler": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Sap"]
            },
            {
                "crawler": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Mars"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["Sabin"]
            },
            {
                "crawler": generic.Generic(
                    '//a[@class="link"]'),
                "url": URLS["Novarts"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Viacredi"]
            },
            {
                "crawler": generic.Generic(
                    '//td[@data-title="Jobdescription"]/a'),
                "url": URLS["Roche"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["3Coracoes"]
            },
            {
                "crawler": generic.Generic(
                    '//div[contains(@class,"search-results__jobinfo")]/a'),
                "url": URLS["3M"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Aeris"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Vivo"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Cielo"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Embraer"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Totvs"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["ViaVarejo"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Gupy"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["GupyTech"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Ambev"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Gpa"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["PicPay"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Randon"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Dasa"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Promob"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Altamogiana"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Vereda"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["PmWeb"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Sicredi"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Cocacola"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Assai"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["PetLove"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Cotesa"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["TakeBlip"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Oi"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Marisa"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Atento"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["Duratex"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["ShibataSupermercados"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["AguasAzuis"]
            },
            {
                "crawler": generic.Generic(
                    gupy_locator),
                "url": URLS["RedeBrasil"]
            },
            {
                "crawler": generic.Generic(
                    '//a[@class="left-link"]'),
                "url": URLS["AstraZeneca"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["BancoBV"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["CeA"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["Danone"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["Alelo"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["CVC"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["PagueMenos"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["Kenoby"]
            },
            {
                "crawler": generic.Generic(
                    '//a[@class="text-dark"]'),
                "url": URLS["AmplificaDigital"]
            },
            {
                "crawler": generic.Generic(
                    '//a[@class="text-dark"]'),
                "url": URLS["ExpertiseGp"]
            },
            {
                "crawler": generic.Generic(
                    kenoby_locator),
                "url": URLS["ClearSale"]
            },
            {
                "crawler": generic.Generic(
                    '//h3[@class="listSingleColumnItemTitle"]/a'),
                "url": URLS["Coats"]
            },
            {
                "crawler": generic.Generic(trab_conosco_locator),
                "url": URLS["CopaEnergia"]
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": URLS["GrupoTrigo"]
            },
            {
                "crawler": generic.Generic(
                    '//section[@id="search-results-list"]//a'),
                "url": URLS["Dell"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorAdm"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorBus"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorCor"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorCul"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorDes"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorDig"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorEng"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorExe"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorFin"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorFoo"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorLeg"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorOth"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorPro"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorRes"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorRoo"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorSal"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorSec"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorTal"]
            },
            {
                "crawler": generic.Generic(arcor_locator),
                "url": URLS["AccorWel"]
            },
            {
                "crawler": generic.Generic('//section[@class="box"]//h3//a'),
                "url": URLS["AllTests"]
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": URLS["Eurofarma"]
            },
            {
                "crawler": generic.Generic(
                    '//div[@class="job-list paragrafo-ideal"]//div[@class="job-list-content"]//h4//a'),
                "url": URLS["GrupoSaga"]
            },
            {
                "crawler": generic.Generic(
                    '//div[contains(@class,"p-panel")]//a[@data-tag="displayJobTitle"]'),
                "url": URLS["HospitalEdmVasc"]
            },
            {
                "crawler": generic.Generic(trab_conosco_locator),
                "url": URLS["Hyundai"]
            },
            {
                "crawler": generic.Generic(
                    '//div[contains(@id,"jobs-cards-wrapper")]//a'),
                "url": URLS["IBM"]
            },
            {
                "crawler": generic.Generic(trab_conosco_locator),
                "url": URLS["IcatuSeguros"]
            },
            {
                "crawler": generic.Generic(trab_conosco_locator),
                "url": URLS["LibertySeguros"]
            },
            {
                "crawler": generic.Generic(
                    '//div[contains(@class,"spf-common-search-item-header")]//a'),
                "url": URLS["Logicalis"]
            },
            {
                "crawler": generic.Generic(kenoby_locator),
                "url": URLS["Jumpadtail"]
            },
            {
                "crawler": generic.Generic('//a[contains(@class, "ui-tabs-anchor")]'),
                "url": URLS["FeComercioDf"]
            },
            {
                "crawler": generic.Generic('//a[contains(@class,"navbar-brand")]'),
                "url": URLS["Agiel"]
            },
            {
                "crawler": generic.Generic('//a[contains(@class,"navbar-brand")]'),
                "url": URLS["EmployerEstagios"]
            },
            {
                "crawler": generic.Generic('//div[@class="informacoes-header"]//a'),
                "url": URLS["StagEstagios"]
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": URLS["MercSaoluiz"]
            },
            {
                "crawler": generic.Generic('//div[contains(@class,"multiline-data-container")]//span//a'),
                "url": URLS["Oracle"]
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": URLS["Riachuelo"]
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": URLS["Santander"]
            },
            {
                "crawler": generic.Generic('//nav[contains(@class,"menu-footer")]//a[text()="Trabalhe Conosco"]'),
                "url": URLS["Senac"]
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": URLS["SlcAgricola"]
            },
            {
                "crawler": generic.Generic(kenoby_locator),
                "url": URLS["Suzano"]
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": URLS["UberlandiaRefrescos"]
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": URLS["Unidas"]
            },
            {
                "crawler": generic.Generic(gupy_locator),
                "url": URLS["UnimedFortaleza"]
            },
            {
                "crawler": generic.Generic(trab_conosco_locator),
                "url": URLS["UnimedRio"]
            },
            {
                "crawler": generic.Generic('//td//a[contains(@class,"joblist__link job__position")]'),
                "url": URLS["Volvo"]
            },
            {
                "crawler": generic.Generic(kenoby_locator),
                "url": URLS["Wiz"]
            },
            {
                "crawler": generic.Generic('//h2//a[contains(@class,"au-target")]'),
                "url": URLS["Microsoft"]
            },
            {
                "crawler": generic.Generic(hotel_hilton_locator),
                "url": URLS["HiltonHotel"]
            },
            {
                "crawler": generic.Generic(trab_conosco_locator),
                "url": URLS["Schmersal"]
            },
            {
                "crawler": generic.Generic('//div[contains(@class,"apply-button-container")]//a'),
                "url": URLS["Bistrol"]
            },
            {
                "crawler": generic.Generic(kenoby_locator),
                "url": URLS["ICherry"]
            },
            {
                "crawler": generic.Generic(kenoby_locator),
                "url": URLS["Mirum"]
            },
            {
                "crawler": generic.Generic('//ol[contains(@class,"m-layout")]//a'),
                "url": URLS["Dll"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["Ebanx"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["Invision"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["Harrys"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["DonorSchoose"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["Lift"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["TripAdvisor"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["WillowTree"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["Datto"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["Thumbtack"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["VaynerMedia"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["KeepTruckin"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["Checkr"]
            },
            {
                "crawler": generic.Generic(green_house_locator),
                "url": URLS["Nutrabolt"]
            },
            # {
            #     "crawler": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            
            # },
            # {
            #     "crawler": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            
            # },
            # {
            #     "crawler": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            
            # },
            # {
            #     "crawler": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            
            # },
            # Add new crawlers above
        ]
        return companies
