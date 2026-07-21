import logging
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
LOG_FILE = os.getenv("LOG_FILE")
LOG_LEVEL = getattr(logging, os.getenv("LOG_LEVEL"))
LOG_FORMAT = os.getenv("LOG_FORMAT")


def setup_logging():
    logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=LOG_FORMAT)
