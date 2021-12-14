from os import getcwd

BASE_DIR = getcwd()
ROOT_DIR = BASE_DIR + "/src/"
RESOURCES_DIR = ROOT_DIR + "resources/"
DRIVER_DIR = RESOURCES_DIR + "chromedriver"
LOGS_FOLDER = BASE_DIR + "/logs/"

DEBUG = False
TIMEOUT = 30
DB_NAME = "crawlers"
DRIVER_TYPE = "chrome"
TABELA = "positions"
CAMPOS = "url, description"
CAMPOS_DIFINICAO = """url VARCHAR(255) NOT NULL, description VARCHAR(50000)"""
LOGS_FILE = LOGS_FOLDER + "crawler.log"
DB_TYPE = {"p": "sqlite", "s": "sqlite"}

URLS = {
    "Daitan": "https://careers-br.daitan.com/pt/vagas/",
    "Dqrtech": "https://www.dqrtech.com.br/vagas/",
    "Mms": "https://www.modularmining.com/pt-br/trabalhe-conosco/aberturas-de-emprego-atuais/",
    "Ciandt": "https://ciandt.com/us/en-us/careers/open-positions",
    "Cesar": "https://vagascesar.gupy.io",
    "LeroyMerlin": "https://jobs.kenoby.com/leroymerlin",
    "Dell": "https://carreiras.dell.com/search-jobs",
    "Sap": "https://jobs.sap.com/search/?q=&locationsearch=&locale=en_US",
    "Mars": "https://jobs.mars.com/search/?createNewAlert=false&q=&locationsearch=",
    "Sabin": "https://jobs.kenoby.com/sabin-site",
    "Accor": "https://careers.accor.com/global/en/opportunity",
    "AccorAdm": "https://careers.accor.com/global/en/c/administration-support-jobs",
    "AccorBus": "https://careers.accor.com/global/en/c/business-development-jobs",
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
    "CopaEnergia": "https://trabalheconosco.vagas.com.br/copa-energia/oportunidades",
    "GrupoTrigo": "https://grupotrigo.gupy.io/",
    "AllTests": "http://4alltests.com.br/vagas",
    "Eurofarma": "https://eurofarma.gupy.io/",
    "GrupoSaga": "https://jobs.solides.com/gruposaga#",
    "HospitalEdmVasc": "https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco",
    "Hyundai": "https://trabalheconosco.vagas.com.br/hyundai/oportunidades",
    "IBM": "https://www.ibm.com/br-pt/employment/",
    "IcatuSeguros": "https://trabalheconosco.vagas.com.br/icatuseguros",
    "LibertySeguros": "https://trabalheconosco.vagas.com.br/libertyseguros/oportunidades",
    "Logicalis": "https://talentconnection-jobs.sabacloud.com/Saba/Web_spf/NA1PRD0099/jobs-jobs/career/searchresult/",
}
