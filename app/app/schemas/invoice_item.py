from pydantic import BaseModel


class InvoiceItemBase(BaseModel):
    qty: int
    value: float


class InvoiceItemCreate(InvoiceItemBase):
    pass


class InvoiceItemUpdate(InvoiceItemBase):
    pass


class InvoiceItemInDBStore(InvoiceItemBase):
    id: int
    item_id: int
    invoice_id: int

    class Config:
        orm_mode = True


class InvoiceItem(InvoiceItemInDBStore):
    pass


class InvoiceItemInDB(InvoiceItemInDBStore):
    pass
