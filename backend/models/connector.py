from typing import Dict, Optional, Union
from pydantic import BaseModel

class Connector(BaseModel):
    id: str | None = None
    name: str
    config: Dict[str | int, Union[str, int, bool, None]]
