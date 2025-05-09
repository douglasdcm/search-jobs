from src.helper.helper import read_file
from src.constants import ROOT_DIR


class CompanyInstance:
    def __init__(self, body: dict):
        self._url = body.get("url")
        self._active = body.get("active")
        self._locator = body.get("locator")

    @property
    def url(self):
        return self._url

    @property
    def locator(self):
        return self._locator

    @property
    def active(self):
        return self._active


class Company:
    def get_all(self):
        """Return the list of enabled crawlers
        Returns:
            (list): list of tuples where the 1st item is the object of the crawler and se 2nd
                informs if it is enable (True). If enabled, the crawler will be executed by the
                server
        """
        companies = []
        content = read_file(ROOT_DIR + "/crawler/companies_data.csv")

        for row in content:
            columns = row.split(";")
            locator = columns[0]
            url = columns[1]
            active = columns[2].replace("\n", "")
            company = {"locator": locator, "url": url, "active": active}
            companies.append(CompanyInstance(company))

        return companies
