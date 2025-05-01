from src.driver.chrome import Driver


class DriverFactory:

    def get_driver(self):
        return Driver()
