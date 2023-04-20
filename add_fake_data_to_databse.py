from tests.helper import (
    populate_database_with_thecnical_jobs,
    initialize_table
)
from os import environ
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
initialize_table(environ.get("DATABASE_STRING"))
populate_database_with_thecnical_jobs()
