import os
from src.database import db, db_postgres
from psycopg2 import connect as postgres_conn
from sqlite3 import connect as sqlite_conn
from src.exceptions.exceptions import ErroBancoDados


class DbFactory:
    def __init__(self, db_type="postgres"):
        self.db_type = db_type

    def create_connnection(self,
                           database="postgres",
                           user="postgres",
                           password="postgresql",
                           host="postgres",
                           port="5432"):

        if os.environ.get("DATABASE_URL") is not None:  # for Heroku only
            return postgres_conn(os.environ.get("DATABASE_URL"))
        elif self.db_type == "postgres":
            return postgres_conn(database=database,
                                 user=user,
                                 password=password,
                                 host=host,
                                 port=port)
        elif self.db_type == "sqlite":
            return sqlite_conn(database)
        else:
            raise ErroBancoDados("It was not possibe to stablish the connection to database.")


    def make_db(self, conn):
        if self.db_type == "sqlite":
            return db.Database(conn)
        if self.db_type == "postgres":
            return db_postgres.Database(conn)
        else:
            raise ErroBancoDados("It was not possible to create the database object.")
