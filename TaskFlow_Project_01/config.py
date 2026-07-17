import logging

def setup_logging():
    logging.basicConfig(
        filename = "logs/taskflow.log",
        level = logging.DEBUG,
        format= "%(asctime)s - %(levelname)s - %(message)s"
    )