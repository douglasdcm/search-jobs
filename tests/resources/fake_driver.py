
class SwitchTo:

    def default_content(self):
        pass

    def frame(self, index=None):
        pass


class FakeDriver:

    switch_to = SwitchTo()

    def start(self, url="url"):
        return self

    def quit(self):
        pass

    def find_elements(self, by_type=None, locator=None):
        element = Fake_Element()
        return [element, element, element]

    def find_element(self, by_type=None, locator=None):
        return Fake_Element()

    def get(self, url="url"):
        pass

    def execute_script(self, script=None, element=None):
        return True


class Fake_Element:

    text = "text_1"

    def get_attribute(self, attribute=None):
        return attribute

    def click(self):
        pass


class Fake_WebDriverWait:

    def __init__(self, driver=None, timeout=None, poll_frequency=None):
        pass

    def until(self, predicate=None):
        return True
