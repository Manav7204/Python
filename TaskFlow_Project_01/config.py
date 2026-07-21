import logging
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
LOG_FILE = os.getenv("LOG_FILE")
LOG_LEVEL = getattr(logging, os.getenv("LOG_LEVEL"))
LOG_FORMAT = os.getenv("LOG_FORMAT")

# Configuration Validation

# if not DATABASE_NAME:
#     raise ValueError("Missing required environment variable: DATABASE_NAME")
# if not LOG_FILE:
#     raise ValueError("Missing required environment variable: LOG_FILE")
# if not LOG_LEVEL:
#     raise ValueError("Missing required environment variable: LOG_LEVEL")
# if not LOG_FORMAT:
#     raise ValueError("Missing required environment variable: LOG_FORMAT")

required_variables = {
    "DATABASE_NAME" : DATABASE_NAME,
    "LOG_FILE" : LOG_FILE,
    "LOG_LEVEL" : LOG_LEVEL,
    "LOG_FORMAT" : LOG_FORMAT
}

for name, value in required_variables.items():
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")

def setup_logging():
    logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=LOG_FORMAT)
