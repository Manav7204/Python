import logging

LOG_FILE = "logs/taskflow.log"
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


def setup_logging():
    logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=LOG_FORMAT)


DATABASE_NAME = "data/task.db"
