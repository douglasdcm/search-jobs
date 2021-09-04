from src.database import db, db_postgres
from psycopg2 import connect as postegres_conn
from sqlite3 import connect as sqlite_conn
from src.exceptions.exceptions import ErroBancoDados


class DbFactory:
    def __init__(self, db_type="postgres"):
        self.db_type = db_type

    def create_connnection(self,
                           database="postgres",
                           user="postgres",
                           password="postgres",
                           host="127.0.0.1",
                           port="5432"):

        if self.db_type == "postgres":
            return postegres_conn(database=database,
                                  user=user,
                                  password=password,
                                  host=host,
                                  port=port)
        elif self.db_type == "sqlite":
            return sqlite_conn(database)
        else:
            return False


    def make_db(self, conn):
        if self.db_type == "sqlite":
            return db.Database(conn)
        if self.db_type == "postgres":
            return db_postgres.Database(conn)
        else:
            raise ErroBancoDados()
