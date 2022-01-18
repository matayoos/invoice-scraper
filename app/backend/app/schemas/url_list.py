from typing import List
from pydantic.main import BaseModel

class UrlList(BaseModel):
    url: List

class UrlListResponse(BaseModel):
    invoice_list_total: int
    registered: int
    already_registered: list
    errors: list
