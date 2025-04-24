from enum import Enum

class SourceConnector(str, Enum):
    mongodb = "mongodb"
    mysql = "mysql"
    postgresql = "postgresql"
