import logging
from driver.chrome import ChromeDriver
from crawler.daitan import Daitan
from config.settings import LOGS_FILE, URLS, DATABASE, TABELA, CAMPOS
from exceptions.exceptions import ComandoInvalido
from database.db import Database
from sqlite3 import connect
from sys import argv
from similarity.similarity import Similarity

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOGS_FILE, level=logging.INFO,  datefmt='%Y-%m-%d %H:%M:%S')

def main(*args):
    for argumentos in args:
        if "-h" in argumentos or "--help" in argumentos:
            print("""
Commands:
  --install   delete the existing database, if any, and install it again
  --run       execute the crawlers
  --help      open the help documentation
  --compare   args: path (str)
                compare the file.txt with the content of the curriculum against the list of positions
                e.g. --compare /tmp/file.txt 
                    """)
            return
        if "--install" in argumentos:
            install()
        elif "--run" in argumentos:
            run()
        elif "--compare" in argumentos:
            compare()
        else:
            raise ComandoInvalido("Invalid command.\nTry main.py --help ")

def install():
    msg = "Creating database..."
    print(msg)
    logging.info(msg)
    db = Database(connect(DATABASE))
    db.deleta_tabela(TABELA)
    db.cria_tabela(TABELA, CAMPOS)
    msg = "Database created."
    print(msg)
    logging.info(msg)
    Database.fecha_conexao_existente()

def compare():
    print("Not implemented yet. Work in progress...")
    cv = """
    
    Seniority

    SR
    Allocation City

        Campinas-SP
        Recife-PE
        Home Office

    About the Position

    We seek experienced high-performing software quality engineers for positions involving quality assurance and test automation for a telecom system solution. 

    You will join a highly skilled team delivering a highly distributed private cloud platform supporting containerized applications in addition to supporting virtual machines and bare metal nodes.
    Responsibilities

        Create test plans and related infrastructure to validate features and fixes to the system solution and triage issues found using your Linux, networking, database data handling, and other skills;
        Execute manual and automated tests for several versions and setups;
        Monitor execution pass-rate and report test results;  
        Setup the solution E2E environment and manage tests for specific configurations;
        Review, analyze, and supplement requirement specifications, and ensure maximum test coverage;
        Prove scalability and performance of software products;
        Automate test plans using script languages to augment the automated test coverage;
        Investigate automated test execution failures to identify adjustments necessary to the setup or to report bugs found;
        Interact with Software Development team in order to complete ticket cycles;
        Analyze system and applications and propose test strategy;
        Participate in technical discussions with customers;
        Report/Monitor/Verify issues in defect tracking tool (JIRA);
        Continuously improve the automation, speed, quality, and ease of testing;
        Create Test Cases and execute manual tests;
        Work in a dynamic, collaborative, and transparent environment where talent is valued over a role title.

    Essential Skills

    What we need in every potential candidate.

        Strong analytical, troubleshooting, and attention to detail;
        A highly versatile professional, able to navigate a wide range of contexts and potentially technologies;
        Good communications skills and the ability to identify the client’s needs;
        Strong computer networking understanding on the application (HTTP/HTTPs/etc.) and transport (TCP/UDP/TLS/etc.) layers, and some understanding of the network layer (IP/IPSec/etc.);
        Strong Linux familiarity, knows how to use a terminal, understands the OS structure (file system, process, memory, etc.) and how to navigate through some other Linux aspects like an advanced user;
        Resourcefulness to navigate through complex environment configuration documents; 
        Experience installing and deploying systems and applications on Linux based hosts;
        Experience troubleshooting systems and applications on Linux based deployments, e.g. collecting and analyzing logs in a distributed architecture, ability to analyze failures or bottlenecks related to performance or resource usage;
        Experience creating, maintaining, and executing performance tests for backend systems (e.g. load, soak, spike, etc.);
        Able to communicate in English at a minimum according to the parameters of level B2 for understanding, speaking, and writing of the CEFR matrix.

    Highly Desirable Skills

    What we need to have for the project as a whole. A potential candidate will have three or more of the topics below well developed.

        Experience automating integration/system tests for backend systems;
        Experience automating performance tests for backend systems;
        Knowledge of creating scripts using automated testing tools and end-to-end test framework
        Docker / Containers;
        Cloud platform concepts;
        Database knowledge or experience
    
    """
    db = Database(connect(DATABASE))
    positions = db.pega_todos_registros(TABELA)
    s = Similarity()
    result = s.return_similarity_by_cossine(cv, positions)
    print(result)

def test_run():
    # export PATH="/home/dmorais/repo/training/crawler_of_positions/resources/chromedriver_linux64/:$PATH"

    url = URLS["daitan"]
    chrome = ChromeDriver() 
    driver = chrome.start(url)
    Daitan(url, driver).run()
    # Add new crawlers here...
    # E.g. MyCompany(url, driver).run()



