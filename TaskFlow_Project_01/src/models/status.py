import logging

logger = logging.getLogger(__name__)


class Status:
    def __init__(self, name:str):
        self.name = name
        
    def __str__(self):
        return self.name