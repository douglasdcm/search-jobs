from pages.daitan.vagas import Vagas

class Daitan:

    def __init__(self, url, drive) -> None:
        self._url = url
        self._vagas = Vagas(drive)

    def get_link_by_browser(self):        
        links = []
        next_ = True
        while next_:
            elements = self._vagas.get_link_of_all_positons()
            for element in elements:
                links.append(element)
            next_ = self._vagas.check_next_page_available()
            if next_:
                self._vagas._scroll_to_next_button()
                self._vagas.go_to_next_page()
        return links

    def quit(self):
        self._driver.quit()


