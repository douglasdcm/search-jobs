import app
from src.helper.commands import compare, overwrite
from pytest import mark, fixture
from src.crawler.company import Company


@mark.functional
class TestEndToEnd:

    @fixture
    def setup(self):
        db_name = app.DB_NAME
        db_type = "postgres"
        install(db_name, db_type)
        df = DbFactory(db_type)
        db = df.get_db(db_name)
        clear(db)
        fields = "url, description"
        db.salva_registro("positions", fields, "'https://test.com', 'test'")
        db.salva_registro("positions", fields, "'https://rabbit.com', 'rabbit'")
        db.salva_registro("positions", fields, "'https://cat.com', 'cats dogs cows'")
        db.salva_registro("positions", fields, "'https://administrar.com', 'administraca'")
        db.salva_registro("positions", fields, "'https://andcondition.com', 'cat dog rabbit cow cucumber'")


    @mark.skip("to be validated")
    def test_find_content_in_a_fresh_container(self, setup, setup_containers):
        setup
        dbf = DbFactory(DB_TYPE["p"])
        db = dbf.get_db(DB_NAME)
        overwrite(db, Company().get_all())
        assert "dog" in compare("dog", db, "or")

    @mark.skip("not working")
    def test_doesnt_find_content_in_a_fresh_container(self, setup_containers):
        install(DB_NAME, DB_TYPE["p"])
        dbf = DbFactory(DB_TYPE["p"])
        db = dbf.get_db(DB_NAME)
        overwrite(db, Company().get_all())
        assert compare("blablabla", db, "or") is None
