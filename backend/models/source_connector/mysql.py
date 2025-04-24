
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

from backend.enums.source_connectors import SourceConnector
from backend.validators.validators import CommaSeparatedListType

class MysqlSourceConfig(BaseModel):
    """Mysql source connector configuration"""

    connector: Literal[SourceConnector.mysql] = SourceConnector.mysql
    connector_class: Literal["io.debezium.connector.mysql.MySqlConnector"] = Field(
        default="io.debezium.connector.mysql.MySqlConnector",
        serialization_alias="connector.class")
    database_hostname: str = Field(serialization_alias="database.hostname")
    database_port: int = Field(serialization_alias="database.port")
    database_user: str = Field(serialization_alias="database.user")
    database_password: str = Field(serialization_alias="database.password")
    database_server_id: int = Field(serialization_alias="database.server.id")
    topic_prefix: str = Field(serialization_alias="topic.prefix")
    # database_include_list: str = Field(serialization_alias="database.include.list")
    table_include_list: str = Field(serialization_alias="table.include.list")
    schema_history_internal_kafka_bootstrap_servers: str = Field(serialization_alias="schema.history.internal.kafka.bootstrap.servers")
    schema_history_internal_kafka_topic: str = Field(serialization_alias="schema.history.internal.kafka.topic")
    

    model_config = ConfigDict(serialize_by_alias=True)
