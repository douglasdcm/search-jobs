class FakeDriver:

    def start(self, url="url"):
        pass

    def quit(self):
        pass

    def find_elements(self, by_type="by_type", locator="locator"):
        element = Fake_Element()
        return [element, element, element]

    def find_element(self, by_type="by_type", locator="locator"):
        return Fake_Element()

    def get(self, url="url"):
        pass

    def execute_script(self, script="script"):
        return True

class Fake_Element:

    def get_attribute(self, attribute="attribute"):
        return attribute

    def text(self):
        return "text_1"

class Fake_WebDriverWait:

    def __init__(self, driver="driver", timeout="timeout", poll_frequency="poll_frequency") -> None:
        pass

    def until(self, predicate="predicate"):
        return True