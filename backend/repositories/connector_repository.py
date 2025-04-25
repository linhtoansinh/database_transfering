from backend.database import db
from backend.models.connector import Connector
from backend.repositories.base_repository import BaseRepository

class ConnectorRepository(BaseRepository):
    def __init__(self):
        super().__init__(collection_name="connectors", model=Connector)

    def upsert(self, connector: Connector):
        try:
            self.collection.update_one(
                filter={"name": connector.name},
                update={"$set": connector.model_dump()},
                upsert=True
            )
            return connector
        except:
            raise