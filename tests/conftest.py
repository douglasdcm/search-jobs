
from tests.settings import DB_NAME
from pytest import fixture
from src.database.db_factory import DbFactory
from tests.helper import exec_command

@fixture
def setup_db():
    df = DbFactory("sqlite")
    db = df.get_db(DB_NAME)
    db.cria_tabela("positions", "url, description")
    yield db
    df = DbFactory("sqlite")
    db = df.get_db()
    db.deleta_tabela("positions")


@fixture(scope="session")
def setup_containers():
    pass
    print("\nprepare for test")
    exec_command("", "./tests/utils/make_test.sh", "sh", sudo=False)
    print("\nstart container")
    exec_command("", "./tests/utils/start_containers.sh", "sh", sudo=False)
    yield
    exec_command("", "./tests/utils/stop_containers.sh", "sh", sudo=False)
