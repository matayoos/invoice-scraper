from datetime import datetime

from pydantic import BaseModel


class InvoiceBase(BaseModel):
    url: str
    date_time: datetime
    access_key: str
    series: str
    auth_protocole: str
    nfce_number: str
    final_value: float
    discount: float


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceUpdate(InvoiceBase):
    pass


class InvoiceInDBBase(InvoiceBase):
    id: int
    grocery_store_id: int

    class Config:
        orm_mode = True


class Invoice(InvoiceInDBBase):
    pass


class InvoiceInDB(InvoiceInDBBase):
    pass
