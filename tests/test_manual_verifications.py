from logging import info
from src.helper.helper import data_pre_processing_portuguese
from pytest import mark
from tests.helper import populate_database_with_desired_jobs
from src.helper.helper import get_all_positions_from_database
from tests.settings import DATABASE_STRING


@mark.nonfunctional
class TestManualVerification:
    """Tests used for support to manual validation"""

    def test_populate_database_with_fake_data(self):
        terms = {
            "all": data_pre_processing_portuguese(
                "all cat dog cow rabbit carrot cucumber babana car block doll videogame fiat ford asia gurgel pedro heliodora camila marcos douglas"
            ),
            "animals": data_pre_processing_portuguese("cat dog cow rabbit"),
            "vegetables": data_pre_processing_portuguese("carrot cucumber babana"),
            "toys": data_pre_processing_portuguese("car block doll videogame"),
            "cars": data_pre_processing_portuguese("fiat ford asia gurgel"),
            "names": data_pre_processing_portuguese("pedro heliodora camila marcos douglas"),
        }
        positions = [
            {
                "url": "https://all.com",
                "description": terms["all"],
            },
            {
                "url": "https://animals.com",
                "description": terms["animals"],
            },
            {
                "url": "https://vegetables.com",
                "description": terms["vegetables"],
            },
            {
                "url": "https://toys.com",
                "description": terms["toys"],
            },
            {
                "url": "https://cars.com",
                "description": terms["cars"],
            },
            {
                "url": "https://names.com",
                "description": terms["names"],
            },
        ]
        populate_database_with_desired_jobs(positions)
        info("Maual test: ", get_all_positions_from_database(DATABASE_STRING))
