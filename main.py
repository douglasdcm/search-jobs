import requests
from bs4 import BeautifulSoup as bs
import selenium
from driver.chrome import ChromeDriver
from crawler.daitan import Daitan

try:
    timeout = 30
    url = "https://careers-br.daitan.com/pt/vagas/"
    chrome = ChromeDriver() 
    driver = chrome.start(url)
    daitan = Daitan(url, driver)
    links = daitan.get_link_by_browser()
    for link in links:
        page = requests.get(link)
        soup = bs(page.content, 'html.parser')
        result = soup.find_all('li')
        print("===========================")
        print(link)
        for item in result:
            print(item.get_text())
finally:
    chrome.quit()
