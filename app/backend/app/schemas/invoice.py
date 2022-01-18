from datetime import datetime

from pydantic import BaseModel


class InvoiceBase(BaseModel):
    url: str
    date_time: datetime
    access_key: str
    auth_protocole: str
    nfce_number: str
    final_value: float
    discount: float


class InvoiceResponse(BaseModel):
    id: int
    url: str
    date_time: datetime
    final_value: float
    discount: float

    class Config:
        orm_mode = True


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceUpdate(InvoiceBase):
    pass


class InvoiceInDBBase(InvoiceBase):
    id: int

    class Config:
        orm_mode = True


class Invoice(InvoiceInDBBase):
    pass


class InvoiceInDB(InvoiceInDBBase):
    pass
