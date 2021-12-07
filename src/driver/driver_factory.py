from src.driver.chrome import ChromeDriver
from src.exceptions.exceptions import InvalidDriverType

class DriverFactory:

    def get_driver(self, driver_type="chrome"):
        if driver_type == "chrome":
            return ChromeDriver()
        else:
            raise InvalidDriverType("The driver type {} does exist.".format(driver_type))