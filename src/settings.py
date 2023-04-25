from os import getcwd

BASE_DIR = getcwd()
ROOT_DIR = BASE_DIR + "/src/"
RESOURCES_DIR = ROOT_DIR + "resources/"
DRIVER_DIR = RESOURCES_DIR + "chromedriver"
LOGS_FOLDER = "/webapp/logs/"

TIMEOUT = 120
TABLE_NAME = "positions"
LOGS_FILE = LOGS_FOLDER + "crawler.log"
DATABASE_STRING_DEFAULT = "postgresql://postgres:postgresql@postgres/postgres"

URLS = {
    "Dell": "https://carreiras.dell.com/search-jobs",
    "Sap": "https://jobs.sap.com/search/?q=&locationsearch=&locale=en_US",
    "Mars": "https://jobs.mars.com/search/?createNewAlert=false&q=&locationsearch=",
    "Sabin": "https://jobs.kenoby.com/sabin-site",
    "AccorCor": "https://careers.accor.com/global/en/c/corporate-social-responsibility-jobs",
    "AccorCul": "https://careers.accor.com/global/en/c/culinary-jobs",
    "AccorDes": "https://careers.accor.com/global/en/c/design-technical-services-jobs",
    "AccorDig": "https://careers.accor.com/global/en/c/digital-products-information-technology-data-analytics-jobs",
    "AccorEng": "https://careers.accor.com/global/en/c/engineering-maintenance-jobs",
    "AccorExe": "https://careers.accor.com/global/en/c/executive-hotel-management-jobs",
    "AccorFin": "https://careers.accor.com/global/en/c/finance-controlling-audit-accounting-business-analysis-jobs",
    "AccorFoo": "https://careers.accor.com/global/en/c/food-beverage-jobs",
    "AccorLeg": "https://careers.accor.com/global/en/c/legal-jobs",
    "AccorOth": "https://careers.accor.com/global/en/c/other-jobs",
    "AccorPro": "https://careers.accor.com/global/en/c/procurement-jobs",
    "AccorRes": "https://careers.accor.com/global/en/c/retail-jobs",
    "AccorRoo": "https://careers.accor.com/global/en/c/rooms-jobs",
    "AccorSal": "https://careers.accor.com/global/en/c/sales-marketing-customer-loyalty-communication-revenue-management-pricing-jobs",
    "AccorSec": "https://careers.accor.com/global/en/c/security-jobs",
    "AccorTal": "https://careers.accor.com/global/en/c/talent-culture-jobs",
    "AccorWel": "https://careers.accor.com/global/en/c/wellness-recreation-jobs",
    "Novarts": "https://www.novartis.com.br/carreiras/buscar-vagas#country=BR",
    # TODO Not used. Needs to click on 'Veja nossas vagas'
    "MercadoLivre": "https://mercadolivre.randstad.com.br/LP_MercadoLivre_V2/",
    "Viacredi": "https://viacredi.gupy.io/",
    "Roche": "https://www.roche.com/careers/jobs/jobsearch.htm?countryCodes=BR",
    # TODO Not used. Has a lot of positions, but requires a login
    "SescRs": "https://www.sesc-rs.com.br/trabalheconosco/vagas/",
    "3Coracoes": "https://jobs.kenoby.com/3coracoes",
    "3M": "https://3m.recsolu.com/job_boards/1/?q=&utm_source=CSSearchWidget&startrow=1&location=%2C+us",
    "Aeris": "https://aeris.gupy.io/",
    "Vivo": "https://vivo.gupy.io/",
    "Cielo": "https://cielo.gupy.io/",
    "Embraer": "https://embraer.gupy.io/",
    "Totvs": "https://totvs.gupy.io/",
    "ViaVarejo": "https://viavarejo.gupy.io/",
    "Gupy": "https://vempra.gupy.io/?utm_source=site&utm_medium=footer",
    "GupyTech": "https://tech-career.gupy.io/?utm_source=site&utm_medium=footer",
    "Ambev": "https://ambev.gupy.io/",
    "Gpa": "https://gpa.gupy.io/",
    "PicPay": "https://picpay.gupy.io/",
    "Randon": "https://randon.gupy.io/",
    "Dasa": "https://dasa.gupy.io/",
    "Promob": "https://promob.gupy.io/",
    "Altamogiana": "https://altamogiana.gupy.io/",
    "Vereda": "https://vereda.gupy.io/",
    "PmWeb": "https://pmweb.gupy.io/",
    "Sicredi": "https://sicredi.gupy.io/",
    "Cocacola": "https://cocacola.gupy.io/",
    "Assai": "https://assai.gupy.io/",
    "PetLove": "https://petlove.gupy.io/",
    "Cotesa": "https://cotesa.gupy.io/",
    "TakeBlip": "https://takeblip.gupy.io/",
    "Oi": "https://oi.gupy.io/",
    "Marisa": "https://marisa.gupy.io/",
    "Atento": "https://atento.gupy.io/",
    "Duratex": "https://duratex.gupy.io/",
    "ShibataSupermercados": "https://shibatasupermercados.gupy.io/",
    "AguasAzuis": "https://aguasazuis.gupy.io/",
    "RedeBrasil": "https://redebrasil.gupy.io/",
    # TODO Not used. There are many positions, but need to click the link
    "Algar": "https://www.portalsinergyrh.com.br/Portal/MeuPortal/MeuPortal?empresa=1490&master=1",
    "AstraZeneca": "https://careers.astrazeneca.com/location/brazil-country-jobs/7684/3469034/2",
    "BancoBV": "https://jobs.kenoby.com/bancobv",
    "CeA": "https://jobs.kenoby.com/cea",
    "Danone": "https://jobs.kenoby.com/danone",
    "Alelo": "https://jobs.kenoby.com/alelo",
    "CVC": "https://jobs.kenoby.com/cvc",
    "PagueMenos": "https://jobs.kenoby.com/paguemenos",
    "Kenoby": "https://jobs.kenoby.com/kenoby",
    "AmplificaDigital": "https://jobs.quickin.io/amplificadigital/jobs",
    "ExpertiseGp": "https://jobs.quickin.io/expertisegp/jobs",
    "ClearSale": "https://jobs.kenoby.com/clearsale/",
    "Coats": "https://rbcoats.avature.net/careers/SearchJobs/?3_47_3=898",
    "GrupoTrigo": "https://grupotrigo.gupy.io/",
    "AllTests": "http://4alltests.com.br/vagas",
    "Eurofarma": "https://eurofarma.gupy.io/",
    "GrupoSaga": "https://jobs.solides.com/gruposaga#",
    "HospitalEdmVasc": "https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco",
    "IBM": "https://www.ibm.com/br-pt/employment/",
    "IcatuSeguros": "https://trabalheconosco.vagas.com.br/icatuseguros",
    "LibertySeguros": "https://trabalheconosco.vagas.com.br/libertyseguros/oportunidades",
    "Logicalis": "https://talentconnection-jobs.sabacloud.com/Saba/Web_spf/NA1PRD0099/jobs-jobs/career/searchresult/",
    "Jumpadtail": "https://jobs.kenoby.com/jumpadtail",
    "FeComercioDf": "https://www.institutofecomerciodf.com.br/vagas/",
    "Agiel": "https://www.agiel.com.br/site/vagas/",
    "EmployerEstagios": "http://employerestagios.com.br/",
    "StagEstagios": "https://www.vagas.com.br/vagas-de-stag-estagios?",
    "MercSaoluiz": "https://vemprosmercadinhossaoluiz.gupy.io/",
    "Oracle": "https://oracle.taleo.net/careersection/2/jobsearch.ftl?f=LOCATION(362940031553)",
    "Riachuelo": "https://carreiras.riachuelo.com.br/",
    "Santander": "https://santander.wd3.myworkdayjobs.com/SantanderCareers/0/refreshFacet/318c8bb6f553100021d223d9780d30be",
    "Senac": "https://www.dn.senac.br/",
    "SlcAgricola": "https://slcagricola.gupy.io/",
    "Suzano": "https://jobs.kenoby.com/Suzano",
    "UberlandiaRefrescos": "https://uberlandiarefrescos.gupy.io/",
    "Unidas": "https://unidas.gupy.io/",
    "UnimedFortaleza": "https://unimedfortaleza.gupy.io/",
    "UnimedRio": "https://trabalheconosco.vagas.com.br/unimedrio/oportunidades?box_link=&division_id=50787&division_name=",
    "Volvo": "https://www.volvogroup.com/br/careers/job-openings.html#page=1&countries=Brazil",
    "Wiz": "https://jobs.kenoby.com/wiz",
    "Microsoft": "https://careers.microsoft.com/us/en/search-results?keywords=brazil&_ga=2.18086970.243575399.1540493310-1941477767.1529592176&rt=professional",
    "Schmersal": "https://trabalheconosco.vagas.com.br/schmersalbrasil",
    "Bistrol": "https://careers.bms.com/jobs?location=Brazil&woe=12&stretchUnit=MILES&stretch=0&sortBy=distance_from&page=1",
    "ICherry": "https://jobs.kenoby.com/i-cherry",
    "Mirum": "https://jobs.kenoby.com/mirum",
    "Dll": "https://www.workingatdllgroup.com/en/Vacancies?el=&co=Brazil&wf=",
    "Lift": "https://boards.greenhouse.io/lift",
    "TripAdvisor": "https://boards.greenhouse.io/tripadvisor",
    "WillowTree": "https://boards.greenhouse.io/willowtree",
    "Datto": "https://boards.greenhouse.io/Datto",
    "Thumbtack": "https://boards.greenhouse.io/Thumbtack",
    "VaynerMedia": "https://boards.greenhouse.io/VaynerMedia",
    "KeepTruckin": "https://boards.greenhouse.io/KeepTruckin",
    "Checkr": "https://boards.greenhouse.io/Checkr",
    "Nutrabolt": "https://boards.greenhouse.io/Nutrabolt",
}



# https://www.squarespace.com/about/careers
# https://www.jdpower.com/business/careers/jobs
# https://www.wayfair.com/careers/jobs

# https://www.messagebird.com/en/careers/
# https://careers.toasttab.com/
# https://www.verifone.com/en/careers
# https://www.nerdwallet.com/careers
# https://www.wise.jobs/


# https://careers.doordash.com/#open-positions
# https://www.lyft.com/careers

# https://www.apixio.com/join-apixio/
# https://seatgeek.com/jobs

# https://www.savatree.com/careers/
# https://www.stitchfix.com/careers/jobs
# https://www.pinterestcareers.com/job-search-results/
# https://www.mobilityware.com/all-jobs
# https://www.jwplayer.com/careers/job-openings
# https://careers.hellofresh.com/global/en
# https://evernote.com/careers/
# https://www.elixirr.com/careers/

# https://buzzfeed.com.br/about/jobs
# https://www.braze.com/company/careers
# https://www.appneta.com/about/careers/positions/

# https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/jobs?q=Frameio-All1
# https://www.talkdesk.com/careers/td?program=td&office=undefined&department=undefined&permalink=undefined




# https://www.ideo.com/jobs







