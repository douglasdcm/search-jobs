from logging import info
from pytest import fixture
from src.helper.helper import initialize_table, Connection
from tests.helper import populate_database_with_thecnical_jobs, exec_command
from caqui.easy.server import Server
from tests.constants import TEST_DB_STRING


@fixture(autouse=True, scope="session")
def setup_server():
    server = Server.get_instance()
    server.start()
    yield
    server.dispose()


@fixture
def setup_db():
    Connection.set_database_string(TEST_DB_STRING)
    initialize_table()
    populate_database_with_thecnical_jobs()


@fixture(scope="session")
def setup_containers():
    info("\nPrepare for test")
    exec_command("", "./tests/utils/make_test.sh", "sh", sudo=False)
    info("\nStart container")
    exec_command("", "./tests/utils/stop_containers.sh", "sh", sudo=False)
    exec_command("", "./tests/utils/start_containers.sh", "sh", sudo=False)
    yield
    exec_command("", "./tests/utils/stop_containers.sh", "sh", sudo=False)
