from typing import Annotated, List

from pydantic import BeforeValidator, PlainSerializer


CommaSeparatedListType = Annotated[
    List[str],
    BeforeValidator(lambda x: [y.strip() for y in x.split(",") if y]),
    PlainSerializer(lambda x: ",".join(x)),
]