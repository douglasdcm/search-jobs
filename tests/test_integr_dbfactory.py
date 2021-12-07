from src.database.db_factory import DbFactory
from pytest import mark, raises


@mark.integration
class TestDbFactory:

    def test_dbfactory_for_sqlite_connects(self):
        dbf = DbFactory("sqlite")
        actual = dbf.get_db()
        assert actual is not None

    def test_dbfactory_for_postgres_raises_exception(self):
        dbf = DbFactory("postgres")
        with raises(Exception):
            dbf.get_db()