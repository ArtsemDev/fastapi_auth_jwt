from pydantic import BaseModel
from ujson import dumps, loads


class Token(BaseModel):
    token_type: str
    access_token: str

    class Config:
        json_loads = loads
        json_dumps = dumps
