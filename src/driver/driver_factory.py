from src.driver.chrome import ChromeDriver


class DriverFactory:

    def get_driver(self):
        return ChromeDriver()
