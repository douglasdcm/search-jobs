from src.helper.helper import read_file
from src.settings import ROOT_DIR


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

            companies.append(company)

        return companies
