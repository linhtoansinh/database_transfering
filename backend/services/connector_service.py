from backend.enums.connector_actions import ConnectorAction
from backend.models.connector import Connector
from backend.repositories.connector_repository import ConnectorRepository
from backend.services.kafka_connect import KafkaConnect


class ConnectorService:
    def __init__(self):
        self.repository = ConnectorRepository()

    def create(self, connector: Connector):
        try:
            _id = self.repository.create(connector.model_dump())
            connector = self.repository.get(_id)
        except:
            raise

        try:
            KafkaConnect.post_kafka_connector(connector)
            return connector
        except:
            raise

    def delete(self, connector_name: str):
        try:
            KafkaConnect.delete_connector(connector_name=connector_name)
            self.repository.remove_by_filter({"name": connector_name})
        except:
            raise

    def execute_kafka_connector_action(self, action: ConnectorAction, connector_name: str):
        try:
            KafkaConnect.execute_connector_action(action=action, connector_name=connector_name)
        except:
            raise

    def upsert(self, connector: Connector):
        try:
            self.repository.upsert(connector=connector)
            KafkaConnect.put_kafka_connector(connector)
            return connector
        except:
            raise