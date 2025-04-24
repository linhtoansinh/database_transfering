from typing import Annotated
from pydantic import AfterValidator, BaseModel

from backend.requests.mysql_source_config_create import MysqlSourceConfigCreate


def removeSpace(val: str) -> str:
    return val.replace(" ", "-")

class SourceConnectorCreate(BaseModel):
    name: Annotated[str, AfterValidator(removeSpace)]
    config: MysqlSourceConfigCreate
