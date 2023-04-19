from src.driver.chrome import ChromeDriver
from src.exceptions.exceptions import WebDriverError


class DriverFactory:

    def get_driver(self, driver_type="chrome"):
        if driver_type == "chrome":
            return ChromeDriver()
        else:
            raise WebDriverError("The driver type {} does exist.".format(driver_type))