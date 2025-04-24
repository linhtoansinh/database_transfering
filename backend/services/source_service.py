import os
import time
from backend.repositories.base_repository import BaseRepository
from backend.repositories.source_repository import SourceRepository
from backend.requests.source_connector_create import SourceConnectorCreate
from backend.services.kafka_connect import KafkaConnect


class SourceService:
    repository: BaseRepository

    def __init__(self):
        self.repository = SourceRepository()

    def create(self, connector: SourceConnectorCreate):
        try:
            config = connector.config.model_dump() | {
                "database_server_id": round(time.time()),
                "topic_prefix": connector.name,
                "schema_history_internal_kafka_bootstrap_servers": os.environ["KAFKA_SERVER"],
                "schema_history_internal_kafka_topic": "schemahistory." + connector.name
            }
            connector = connector.model_dump() | {
                "config": config
            }

            _id = self.repository.create(connector)
            connector = self.repository.get(_id)
        except:
            raise

        try:
            KafkaConnect.post_kafka_connector(connector)
            return connector
        except:
            raise