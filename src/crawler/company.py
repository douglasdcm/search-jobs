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
                "locator": generic.Generic('//a[contains(@title,"Veja detalhes")]'),
                "url": "https://www.dqrtech.com.br/vagas/"
            },
            {
                "locator": generic.Generic(
                    '//a[contains(@class,"wp-block-cit-block-ciandt-link")]'),
                "url": "https://ciandt.com/us/en-us/careers/open-positions"
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": "https://vagascesar.gupy.io"
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": "https://jobs.kenoby.com/leroymerlin"
            },
            {
                "locator": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Sap"]
            },
            {
                "locator": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Mars"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["Sabin"]
            },
            {
                "locator": generic.Generic(
                    '//a[@class="link"]'),
                "url": URLS["Novarts"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Viacredi"]
            },
            {
                "locator": generic.Generic(
                    '//td[@data-title="Jobdescription"]/a'),
                "url": URLS["Roche"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["3Coracoes"]
            },
            {
                "locator": generic.Generic(
                    '//div[contains(@class,"search-results__jobinfo")]/a'),
                "url": URLS["3M"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Aeris"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Vivo"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Cielo"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Embraer"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Totvs"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["ViaVarejo"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Gupy"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["GupyTech"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Ambev"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Gpa"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["PicPay"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Randon"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Dasa"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Promob"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Altamogiana"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Vereda"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["PmWeb"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Sicredi"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Cocacola"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Assai"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["PetLove"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Cotesa"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["TakeBlip"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Oi"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Marisa"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Atento"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["Duratex"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["ShibataSupermercados"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["AguasAzuis"]
            },
            {
                "locator": generic.Generic(
                    gupy_locator),
                "url": URLS["RedeBrasil"]
            },
            {
                "locator": generic.Generic(
                    '//a[@class="left-link"]'),
                "url": URLS["AstraZeneca"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["BancoBV"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["CeA"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["Danone"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["Alelo"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["CVC"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["PagueMenos"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["Kenoby"]
            },
            {
                "locator": generic.Generic(
                    '//a[@class="text-dark"]'),
                "url": URLS["AmplificaDigital"]
            },
            {
                "locator": generic.Generic(
                    '//a[@class="text-dark"]'),
                "url": URLS["ExpertiseGp"]
            },
            {
                "locator": generic.Generic(
                    kenoby_locator),
                "url": URLS["ClearSale"]
            },
            {
                "locator": generic.Generic(
                    '//h3[@class="listSingleColumnItemTitle"]/a'),
                "url": URLS["Coats"]
            },
            {
                "locator": generic.Generic(trab_conosco_locator),
                "url": URLS["CopaEnergia"]
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": URLS["GrupoTrigo"]
            },
            {
                "locator": generic.Generic(
                    '//section[@id="search-results-list"]//a'),
                "url": URLS["Dell"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorAdm"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorBus"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorCor"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorCul"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorDes"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorDig"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorEng"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorExe"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorFin"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorFoo"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorLeg"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorOth"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorPro"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorRes"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorRoo"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorSal"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorSec"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorTal"]
            },
            {
                "locator": generic.Generic(arcor_locator),
                "url": URLS["AccorWel"]
            },
            {
                "locator": generic.Generic('//section[@class="box"]//h3//a'),
                "url": URLS["AllTests"]
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": URLS["Eurofarma"]
            },
            {
                "locator": generic.Generic(
                    '//div[@class="job-list paragrafo-ideal"]//div[@class="job-list-content"]//h4//a'),
                "url": URLS["GrupoSaga"]
            },
            {
                "locator": generic.Generic(
                    '//div[contains(@class,"p-panel")]//a[@data-tag="displayJobTitle"]'),
                "url": URLS["HospitalEdmVasc"]
            },
            {
                "locator": generic.Generic(trab_conosco_locator),
                "url": URLS["Hyundai"]
            },
            {
                "locator": generic.Generic(
                    '//div[contains(@id,"jobs-cards-wrapper")]//a'),
                "url": URLS["IBM"]
            },
            {
                "locator": generic.Generic(trab_conosco_locator),
                "url": URLS["IcatuSeguros"]
            },
            {
                "locator": generic.Generic(trab_conosco_locator),
                "url": URLS["LibertySeguros"]
            },
            {
                "locator": generic.Generic(
                    '//div[contains(@class,"spf-common-search-item-header")]//a'),
                "url": URLS["Logicalis"]
            },
            {
                "locator": generic.Generic(kenoby_locator),
                "url": URLS["Jumpadtail"]
            },
            {
                "locator": generic.Generic('//a[contains(@class, "ui-tabs-anchor")]'),
                "url": URLS["FeComercioDf"]
            },
            {
                "locator": generic.Generic('//a[contains(@class,"navbar-brand")]'),
                "url": URLS["Agiel"]
            },
            {
                "locator": generic.Generic('//a[contains(@class,"navbar-brand")]'),
                "url": URLS["EmployerEstagios"]
            },
            {
                "locator": generic.Generic('//div[@class="informacoes-header"]//a'),
                "url": URLS["StagEstagios"]
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": URLS["MercSaoluiz"]
            },
            {
                "locator": generic.Generic('//div[contains(@class,"multiline-data-container")]//span//a'),
                "url": URLS["Oracle"]
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": URLS["Riachuelo"]
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": URLS["Santander"]
            },
            {
                "locator": generic.Generic('//nav[contains(@class,"menu-footer")]//a[text()="Trabalhe Conosco"]'),
                "url": URLS["Senac"]
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": URLS["SlcAgricola"]
            },
            {
                "locator": generic.Generic(kenoby_locator),
                "url": URLS["Suzano"]
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": URLS["UberlandiaRefrescos"]
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": URLS["Unidas"]
            },
            {
                "locator": generic.Generic(gupy_locator),
                "url": URLS["UnimedFortaleza"]
            },
            {
                "locator": generic.Generic(trab_conosco_locator),
                "url": URLS["UnimedRio"]
            },
            {
                "locator": generic.Generic('//td//a[contains(@class,"joblist__link job__position")]'),
                "url": URLS["Volvo"]
            },
            {
                "locator": generic.Generic(kenoby_locator),
                "url": URLS["Wiz"]
            },
            {
                "locator": generic.Generic('//h2//a[contains(@class,"au-target")]'),
                "url": URLS["Microsoft"]
            },
            {
                "locator": generic.Generic(hotel_hilton_locator),
                "url": URLS["HiltonHotel"]
            },
            {
                "locator": generic.Generic(trab_conosco_locator),
                "url": URLS["Schmersal"]
            },
            {
                "locator": generic.Generic('//div[contains(@class,"apply-button-container")]//a'),
                "url": URLS["Bistrol"]
            },
            {
                "locator": generic.Generic(kenoby_locator),
                "url": URLS["ICherry"]
            },
            {
                "locator": generic.Generic(kenoby_locator),
                "url": URLS["Mirum"]
            },
            {
                "locator": generic.Generic('//ol[contains(@class,"m-layout")]//a'),
                "url": URLS["Dll"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["Ebanx"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["Invision"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["Harrys"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["DonorSchoose"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["Lift"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["TripAdvisor"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["WillowTree"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["Datto"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["Thumbtack"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["VaynerMedia"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["KeepTruckin"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["Checkr"]
            },
            {
                "locator": generic.Generic(green_house_locator),
                "url": URLS["Nutrabolt"]
            },
            # {
            #     "locator": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            
            # },
            # {
            #     "locator": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            
            # },
            # {
            #     "locator": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            
            # },
            # {
            #     "locator": generic.Generic(green_house_locator),
            #     "url": URLS["xxxx"],
            
            # },
            # Add new crawlers above
        ]
        return companies
