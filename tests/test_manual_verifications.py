from src.settings import DB_NAME, DB_TYPE
from src.helper.helper import data_pre_processing_portuguese
from src.database.db_factory import DbFactory
from src.helper.commands import install, clear
from pytest import mark


@mark.manual
class TestManaulVerification:
    """Tests used for support to manual validation"""

    def test_populate_database_with_fake_data(self):
        install(DB_NAME, DB_TYPE["s"])
        df = DbFactory(DB_TYPE["s"])
        db = df.get_db(DB_NAME)
        clear(db)
        fields = "url, description"
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
        db.salva_registro("positions", fields, "'https://all.com', '{}'".format(terms["all"]))
        db.salva_registro("positions", fields, "'https://animals.com', '{}'".format(terms["animals"]))
        db.salva_registro("positions", fields, "'https://vegetables.com', '{}'".format(terms["vegetables"]))
        db.salva_registro("positions", fields, "'https://toys.com', '{}'".format(terms["toys"]))
        db.salva_registro("positions", fields, "'https://cars.com', '{}'".format(terms["cars"]))
        db.salva_registro("positions", fields, "'https://names.com', '{}'".format(terms["names"]))
        print(db.pega_todos_registros("positions"))

    def test_clear_database(self):
        install(DB_NAME, DB_TYPE["s"])
        df = DbFactory(DB_TYPE["s"])
        db = df.get_db(DB_TYPE["s"])
        clear(db)
