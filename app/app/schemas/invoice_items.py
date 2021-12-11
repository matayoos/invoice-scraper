from pydantic import BaseModel


class InvoiceItemsBase(BaseModel):
    qty: int
    value: float


class InvoiceItemsCreate(InvoiceItemsBase):
    pass


class InvoiceItemsUpdate(InvoiceItemsBase):
    pass


class InvoiceItemsInDBStore(InvoiceItemsBase):
    id: int
    invoice_id: int
    item_id: int

    class Config:
        orm_mode = True


class InvoiceItems(InvoiceItemsInDBStore):
    pass


class InvoiceItemsInDB(InvoiceItemsInDBStore):
    pass
