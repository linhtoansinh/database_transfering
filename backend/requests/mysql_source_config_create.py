
from pydantic import BaseModel, ConfigDict, Field

from backend.validators.validators import CommaSeparatedListType

class MysqlSourceConfigCreate(BaseModel):
    database_hostname: str = Field(validation_alias="database.hostname")
    database_port: int = Field(validation_alias="database.port")
    database_user: str = Field(validation_alias="database.user")
    database_password: str = Field(validation_alias="database.password")
    table_include_list: CommaSeparatedListType = Field(validation_alias="table.include.list")

    model_config = ConfigDict(validate_by_alias=True)
