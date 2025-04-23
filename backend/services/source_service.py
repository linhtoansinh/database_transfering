from backend.models.connector import Connector
from backend.repositories.base_repository import BaseRepository
from backend.repositories.source_repository import SourceRepository
from backend.services.kafka_connect import KafkaConnect


class SourceService:
    repository: BaseRepository

    def __init__(self):
        self.repository = SourceRepository()

    def create(self, connector: Connector):
        try:
            _id = self.repository.create(connector.model_dump())
            connector = self.repository.get(_id)
        except:
            raise

        try:
            # add kafka connection here
            # ...
            KafkaConnect.post_kafka_connector(connector)
            return connector
        except:
            raise