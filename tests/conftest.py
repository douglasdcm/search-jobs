from logging import info
from pytest import fixture
from tests.helper import exec_command
from tests.helper import populate_database_with_thecnical_jobs
from caqui.easy.server import Server


@fixture(autouse=True, scope="session")
def setup_server():
    server = Server.get_instance()
    server.start()
    yield
    server.dispose()


@fixture
def setup_db():
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
