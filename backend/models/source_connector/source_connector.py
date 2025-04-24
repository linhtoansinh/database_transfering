from pydantic import BaseModel

from backend.models.source_connector import MysqlSourceConfig


class SourceConnector(BaseModel):
    name: str
    config: MysqlSourceConfig
