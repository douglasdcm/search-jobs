from src.helper.commands import (help_, install, sanity_check, clear, update, install_tables, subscribe, unsubscribe)
from tests.settings import DB_NAME, DB_TYPE, DRIVER_TYPE
from src.settings import LIMITE, NOTIF_CAMPOS, NOTIF_TABLE
from src.database.db_factory import DbFactory
from pytest import fixture
from src.crawler.generic import Generic
from os import getcwd
from pytest import mark, raises
from src.exceptions.exceptions import NotificationException


@mark.integration
class TestCommands:

    testdata = [
        ("semana", "semana"),
        ("dia", "dia"),
    ]

    @fixture
    def populate_db(self, setup_db):
        db = setup_db
        db.salva_registro("positions", "url, description", "'https://test_message_1.com', 'test_message_1'")
        db.salva_registro("positions", "url, description", "'https://test_message_2.com', 'test_message_2'")
        db.salva_registro("positions", "url, description", "'https://test_message_3.com', 'test_message_3'")
        return db

    @fixture
    def get_crawlers(self):
        return [{
                "company": Generic("//a"),
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
                "enabled": True
            }]

    def test_unsubscribe_raises_exception_for_non_existent_data(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        with raises(NotificationException):
            unsubscribe(db, "email_1")

    def test_unsubscribe_removes_single_data(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [(1, "email_1@email.com", "filter", "semana", 0)]
        subscribe(db, "email_1@email.com", "filter", "semana")
        actual = unsubscribe(db, "email_1@email.com")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual is True
        assert actual_table == expected

    def test_unsubscribe_removes_subset_of_data(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [
            (1, "email_1@email.com", "filter", "semana", 0),
            (2, "email_2@email.com", "filter", "semana", 1),
            (3, "email_3@email.com", "filter", "semana", 0)
        ]
        subscribe(db, "email_1@email.com", "filter", "semana")
        subscribe(db, "email_2@email.com", "filter", "semana")
        subscribe(db, "email_3@email.com", "filter", "semana")
        unsubscribe(db, "email_1@email.com")
        unsubscribe(db, "email_3@email.com")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual_table == expected

    def test_unsubscribe_removes_many_data(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [
            (1, "email_1@email.com", "filter", "semana", 0),
            (2, "email_2@email.com", "filter", "semana", 0),
            (3, "email_3@email.com", "filter", "semana", 0)
        ]
        subscribe(db, "email_1@email.com", "filter", "semana")
        subscribe(db, "email_2@email.com", "filter", "semana")
        subscribe(db, "email_3@email.com", "filter", "semana")
        unsubscribe(db, "email_1@email.com")
        unsubscribe(db, "email_2@email.com")
        unsubscribe(db, "email_3@email.com")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual_table == expected

    def test_subscribe_truncate_filter_if_len_bigger_than_limite(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        subscribe(
            db, "email_1@email.com",
            """
            aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa 
            aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa 
            aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa 
            aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa 
            aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa 
            bbbbbbbbbb
            """,
            "semana")
        actual_table = len(db.pega_todos_registros(NOTIF_TABLE, "filter")[0][0])
        assert actual_table < LIMITE

    def test_subscribe_raise_exception_if_invalid_filter(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        with raises(NotificationException):
            subscribe(db, "email_1@email.com", "123", "semana")

    def test_subscribe_raise_exception_if_email_not_patterned(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        with raises(NotificationException):
            subscribe(db, "email_.email.com", "filter", "semana")

    def test_subscribe_raise_exception_if_empty_filter(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        with raises(NotificationException):
            subscribe(db, "email_1@email.com", "", "semana")

    def test_subscribe_raise_exception_if_empty_email(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        with raises(NotificationException):
            subscribe(db, "", "filter", "semana")

    def test_subscribe_raise_exception_if_invalid_schedule(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        with raises(NotificationException):
            subscribe(db, "", "filter", "other")

    @mark.parametrize("schedule, expected", testdata)
    def test_subscribe_accepts_only_valid_schedule(self, setup_db, schedule, expected):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        subscribe(db, "email_1@email.com", "filter", schedule)
        actual_table = db.pega_todos_registros(NOTIF_TABLE, "schedule")[0][0]
        assert actual_table == expected

    def test_subscribe_update_schedule(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [
            (1, "email_1@email.com", "filter", "dia", 1),
        ]
        subscribe(db, "email_1@email.com", "filter", "semana")
        unsubscribe(db, "email_1@email.com")
        subscribe(db, "email_1@email.com", "filter", "dia")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual_table == expected

    def test_subscribe_update_filters(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [
            (1, "email_1@email.com", "test", "semana", 1),
        ]
        subscribe(db, "email_1@email.com", "filter", "semana")
        unsubscribe(db, "email_1@email.com")
        subscribe(db, "email_1@email.com", "test", "semana")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual_table == expected

    def test_subscribe_reactivate_all_filters_of_email(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [
            (1, "email_1@email.com", "filter", "semana", 1),
        ]
        subscribe(db, "email_1@email.com", "filter", "semana")
        unsubscribe(db, "email_1@email.com")
        subscribe(db, "email_1@email.com", "filter", "semana")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual_table == expected 

    def test_subscribe_saves_many_data(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [
            (1, "email_1@email.com", "filter", "semana", 1),
            (2, "email_2@email.com", "filter", "semana", 1),
            (3, "email_3@email.com", "filter", "semana", 1)
        ]
        subscribe(db, "email_1@email.com", "filter", "semana")
        subscribe(db, "email_2@email.com", "filter", "semana")
        subscribe(db, "email_3@email.com", "filter", "semana")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual_table == expected

    def test_subscrive_saves_just_one_filter_per_email(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [
            (1, "email_1@email.com", "filter", "semana", 1),
        ]
        subscribe(db, "email_1@email.com", "filter", "semana")
        subscribe(db, "email_1@email.com", "filter", "semana")
        subscribe(db, "email_1@email.com", "filter", "semana")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual_table == expected

    def test_subscribe_saves_data(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [(1, "email_1@email.com", "filter", "semana", 1)]
        actual = subscribe(db, "email_1@email.com", "filter", "semana")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual is True
        assert actual_table == expected

    def test_subscribe_reactivate_existing_data(self, setup_db):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        expected = [(1, "email_1@email.com", "filter", "semana", 1)]
        subscribe(db, "email_1@email.com", "filter", "semana")
        unsubscribe(db, "email_1@email.com")
        subscribe(db, "email_1@email.com", "filter", "semana")
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual_table == expected

    def test_install_tables_inserts_data(self, setup_db):
        values = "'email', 'filter', 'schedule', 1"
        expected = [(1, 'email', 'filter', 'schedule', 1)]
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        db.salva_registro(NOTIF_TABLE, NOTIF_CAMPOS, values)
        actual = db.pega_todos_registros(NOTIF_TABLE)
        assert actual == expected

    def test_install_tables_create_the_tables(self):
        actual = install_tables(DB_NAME, DB_TYPE["s"])
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        actual_table = db.pega_todos_registros(NOTIF_TABLE)
        assert actual is True
        assert actual_table == []

    def test_update_database_returns_true(self, get_crawlers):
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        assert update(db, DRIVER_TYPE, get_crawlers) is True

    def test_clear_remove_data_from_database(self, populate_db):
        expected = []
        db = populate_db
        dbf = DbFactory(DB_TYPE["s"])
        db = dbf.get_db(DB_NAME)
        clear(db)
        actual = db.pega_maior_id("positions")
        assert actual == expected

    def test_sanity_check_works(self, setup_db, get_crawlers):
        assert sanity_check(setup_db, DRIVER_TYPE, get_crawlers) is True

    def test_install_creates_database(self):
        assert install(DB_NAME, DB_TYPE["s"])

    def test_help_is_opened(self):
        actual = help_()
        assert "--initdb" in actual
        assert "--help" in actual
        assert "--sanity-check"

