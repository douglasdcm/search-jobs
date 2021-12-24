
from tests.settings import DB_NAME
from pytest import fixture
from src.database.db_factory import DbFactory
from tests.helper import exec_command
from src.settings import NOTIF_TABLE, NOTIF_CAMPOS_DEF


@fixture
def setup_db():
    df = DbFactory("sqlite")
    db = df.get_db(DB_NAME)
    db.cria_tabela("positions", "url, description")
    db.cria_tabela(NOTIF_TABLE, NOTIF_CAMPOS_DEF)
    yield db
    df = DbFactory("sqlite")
    db = df.get_db()
    db.deleta_tabela("positions")
    db.deleta_tabela(NOTIF_TABLE)

@fixture(scope="session")
def setup_containers():
    exec_command("", "./tests/utils/start_containers.sh", "sh", sudo=False)
    yield
    exec_command("", "./tests/utils/stop_containers.sh", "sh", sudo=False)