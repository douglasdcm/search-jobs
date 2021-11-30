from tests.settings import DB_NAME
from pytest import fixture
from src.database.db_factory import DbFactory

@fixture
def setup_db():
    df = DbFactory("sqlite")
    db = df.get_db(DB_NAME)
    db.cria_tabela("positions", "url, description")
    yield db
    df = DbFactory("sqlite")
    db = df.get_db()
    db.deleta_tabela("positions")