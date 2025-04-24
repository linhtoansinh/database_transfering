from backend.database import db
from backend.models.source_connector import SourceConnector
from backend.repositories.base_repository import BaseRepository

class SourceRepository(BaseRepository):
    def __init__(self):
        super().__init__(collection_name="source_connectors", model=SourceConnector)