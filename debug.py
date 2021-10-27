import logging
from src.settings import LOGS_FILE
logging.FileHandler(filename=LOGS_FILE, mode='w', encoding=None, delay=False)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOGS_FILE, level=logging.ERROR, datefmt='%Y-%m-%d %H:%M:%S')
