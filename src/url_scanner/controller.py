from src.url_scanner.fetcher import Fetcher
from src.url_scanner.classifier import Classifier


class Controller:
    def __init__(self, driver):
        self._driver = driver

    def run_fetcher(self, url):
        fetcher = Fetcher(self._driver)
        fetcher.download_htlm(url)
        urls = fetcher.extracts_all_links()
        fetcher.normalizes_items(urls)
        return fetcher.return_candidate_links(urls)

    def run_classifier(self, links):
        result = []
        for link in links:
            classifier = Classifier()
            classifier.receive_link(link)
            if classifier.is_link_of_carrer(link):
                result.append(classifier.return_best_links(link))
        return result

    def save_output(self, best_links):
        with open("url-scan.csv", "w") as f:
            pass

    def execute(self, urls):
        for url in urls:
            candidate_links = self.run_fetcher(url)
            best_links = self.run_classifier(candidate_links)
            self.save_output(best_links)
        return best_links
