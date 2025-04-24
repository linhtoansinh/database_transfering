from backend.database import db
from backend.models.connector import Connector
from backend.repositories.base_repository import BaseRepository

class ConnectorRepository(BaseRepository):
    def __init__(self):
        super().__init__(collection_name="connectors", model=Connector)