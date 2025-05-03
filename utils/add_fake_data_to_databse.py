from tests.helper import populate_database_with_thecnical_jobs
from src.helper.helper import initialize_table
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
initialize_table()
populate_database_with_thecnical_jobs()
