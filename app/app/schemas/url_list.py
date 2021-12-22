from typing import List
from pydantic.main import BaseModel

class UrlList(BaseModel):
    url: List
