#!/usr/bin/python
from subprocess import PIPE, STDOUT, Popen, run, call
from src.helper.commands import install
from src.database.db_factory import DbFactory
from src.settings import DB_NAME, DB_TYPE


def exec_command(params, entry_point, domain="python", sudo=False):
    try:
        cmd = []
        if sudo is True:
            cmd.extend(["sudo"])
        cmd.extend([domain, entry_point])
        if isinstance(params, str):
            params = [params]
        cmd.extend(params)
        return run(cmd,
                   stdout=PIPE,
                   stderr=STDOUT,
                   encoding="utf-8").stdout.strip()
    except Exception:
        raise


def populate_database():
    install(DB_NAME, DB_TYPE["s"])
    df = DbFactory(DB_TYPE["s"])
    db = df.get_db(DB_NAME)
    db.salva_registro("positions", "url, description", "'https://test_message_1.com', 'test_message_1'")
    db.salva_registro("positions", "url, description", "'https://test_message_2.com', 'test_message_2'")
    db.salva_registro("positions", "url, description", "'https://test_message_3.com', 'test_message_3'")
