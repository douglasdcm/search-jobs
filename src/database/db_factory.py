from os import environ
from src.database import db, db_postgres
from psycopg2 import connect as postgres_conn
from sqlite3 import connect as sqlite_conn
from src.exceptions.exceptions import DatabaseError
from dotenv import load_dotenv
from os import getenv

load_dotenv()  # take environment variables from .env.


class DbFactory:
    pass
    # def __init__(self, db_type="postgres"):
    #     self.db_type = db_type

    # def get_db(self, database="postgres", user="postgres",
    #            password="postgresql", host="postgres", port="5432"):
    #     """Get the database
    #     Args:
    #         database (str): name of the database
    #     """
    #     try:
    #         conn = self._create_connnection(
    #             database=database,
    #             user=user,
    #             password=password,
    #             host=host,
    #             port=port)
    #         return self._make_db(conn)
    #     except Exception as error:
    #         raise DatabaseError(
    #             f"Could not create a connection to '{database}' database. {str(error)}")

    # def _create_connnection(
    #         self,
    #         database="postgres",
    #         user="postgres",
    #         password="postgresql",
    #         host="postgres",
    #         port="5432"):
    #     if environ.get("DATABASE_STRING") is not None:  # for remote database only
    #         return postgres_conn(environ.get("DATABASE_STRING"))
    #     elif self.db_type == "postgres":
    #         return postgres_conn(dbname=database,
    #                              user=user,
    #                              password=password,
    #                              host=host,
    #                              port=port)
    #     elif self.db_type == "sqlite":
    #         return sqlite_conn(database, check_same_thread=False)
    #     else:
    #         raise DatabaseError("It was not possibe to stablish the connection to database.")


    # def _make_db(self, conn):
    #     if self.db_type == "sqlite":
    #         return db.Database(conn)
    #     if self.db_type == "postgres":
    #         return db_postgres.Database(conn)
    #     else:
    #         raise DatabaseError("It was not possible to create the database object.")
